# Truth Seeker Web — Plan 1: Foundation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the `truthseeker-web` repo with Firebase Auth (email + Google + Apple SSO), Firestore + security rules, server-side session cookies, locale-aware routing, auth-guarded route groups, and a Cloud Run dev deployment pipeline — so subsequent plans (search engine, billing, UI) have a working scaffold to build on.

**Architecture:** Next.js 16 App Router on Cloud Run, single deployable. Firebase Admin SDK on the server (Firestore + Auth verification), Firebase JS SDK on the client (sign-in flows). Session cookie pattern: client signs in via Firebase JS SDK → exchanges ID token for an HTTP-only `__session` cookie via `/api/auth/session` → middleware + server components verify the cookie via Admin SDK. Locale routing via next-intl with `en` only, codebase i18n-ready.

**Tech Stack:** Next.js 16, React 19, TypeScript, Tailwind 4, shadcn/ui, Firebase (Auth + Firestore + Admin SDK), next-intl, Vitest, Playwright, pnpm, Cloud Run, Cloud Build, Terraform.

---

## Prerequisites (manual setup before starting)

These cannot be coded. Complete before Task 1:

1. **GCP project** for dev environment (e.g., `truthseeker-web-dev`). Note the project ID.
2. **Firebase project** linked to the GCP project. Enable Firestore (Native mode, `nam5` or `eur3` region) and Authentication.
3. **Firebase Auth providers enabled** in Firebase Console:
   - Email/Password
   - Google (uses Firebase's built-in OAuth client; no extra config)
   - Apple — requires an Apple Developer account; create a Service ID + Key, paste them into Firebase Console → Authentication → Sign-in method → Apple.
4. **Firebase service account JSON** downloaded for the Admin SDK (Firebase Console → Project Settings → Service Accounts → Generate new private key).
5. **`gcloud` CLI** installed and authenticated against the GCP project.
6. **Local clone of `qr-now-web-`** at `~/Apps/qr-now-web-` (reference scaffold; we copy from it).
7. **Node 20+** and **pnpm 9+** installed.

---

## File Structure (target end state of Plan 1)

```
truthseeker-web/
├── .env.example
├── .env.local                          ← gitignored, dev secrets
├── .gitignore
├── .nvmrc
├── package.json
├── pnpm-lock.yaml
├── tsconfig.json
├── next.config.ts
├── eslint.config.mjs
├── postcss.config.mjs
├── components.json                     ← shadcn config
├── vitest.config.ts
├── Dockerfile
├── cloudbuild.yaml
├── firestore.rules
├── firestore.indexes.json
├── firebase.json                       ← emulator config
├── README.md
├── messages/
│   └── en.json
├── public/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── dev.tfvars
│   └── README.md
├── src/
│   ├── middleware.ts
│   ├── i18n/
│   │   ├── config.ts
│   │   ├── request.ts                  ← next-intl server config
│   │   └── navigation.ts               ← next-intl client helpers
│   ├── lib/
│   │   ├── firebase/
│   │   │   ├── admin.ts                ← Admin SDK init + verifyIdToken
│   │   │   ├── admin.test.ts
│   │   │   ├── client.ts               ← JS SDK init + auth providers
│   │   │   └── auth-context.tsx        ← React provider for client auth
│   │   ├── auth/
│   │   │   ├── session-cookie.ts       ← cookie name + helpers
│   │   │   ├── session-cookie.test.ts
│   │   │   ├── server-session.ts       ← server-side session reader
│   │   │   └── server-session.test.ts
│   │   └── auth-guard.ts               ← RSC helper to require auth
│   ├── app/
│   │   ├── layout.tsx                  ← root (just <html><body>)
│   │   ├── (public)/
│   │   │   └── [locale]/
│   │   │       ├── layout.tsx
│   │   │       └── page.tsx            ← landing placeholder
│   │   ├── (auth)/
│   │   │   └── [locale]/
│   │   │       ├── layout.tsx
│   │   │       ├── login/page.tsx
│   │   │       └── signup/page.tsx
│   │   ├── (app)/
│   │   │   └── [locale]/
│   │   │       ├── layout.tsx          ← auth-guarded
│   │   │       └── page.tsx            ← /app placeholder
│   │   └── api/
│   │       └── auth/
│   │           └── session/route.ts    ← POST: id token → cookie; DELETE: clear
│   └── components/
│       └── ui/                         ← shadcn primitives (button, input, label, card)
└── tests/
    ├── firestore-rules.test.ts         ← runs against emulator
    └── setup.ts
```

**Design principle:** `lib/firebase/`, `lib/auth/`, and `lib/auth-guard.ts` are bounded. UI tree in `app/` is split into three route groups (`(public)`, `(auth)`, `(app)`) so layout + auth behavior is encoded at the layout layer, not in every page.

---

## Tasks

### Task 1: Bootstrap repo from qr-now-web- scaffold

**Files:**
- Create: `truthseeker-web/` (entire directory)
- Reference: `~/Apps/qr-now-web-/`

- [ ] **Step 1: Copy scaffold and clean git history**

Run:

```bash
cp -R ~/Apps/qr-now-web- ~/Apps/truthseeker-web
cd ~/Apps/truthseeker-web
rm -rf .git
git init
git checkout -b main
```

Expected: New directory at `~/Apps/truthseeker-web`, no git history.

- [ ] **Step 2: Rename in `package.json`**

Edit `package.json`. Change:

```json
{
  "name": "qr-now-web",
```

to:

```json
{
  "name": "truthseeker-web",
```

Also remove any QR-related scripts (e.g., entries that reference `qr` in their name); we'll prune QR code in Task 3.

- [ ] **Step 3: Remove copied marketing/non-essential assets**

Run:

```bash
rm -f pricing-proposal-en.pdf funnel-diagram.md refactor_plan.md ROADMAP.md DEPLOYMENT.md
rm -rf .obsidian .DS_Store
```

Expected: `ls` shows only the structural files (package.json, next.config.ts, src/, terraform/, etc.).

- [ ] **Step 4: Update `README.md`**

Replace contents with:

```markdown
# truthseeker-web

Truth Seeker Web — V1 MVP (People lookup).

See design doc: `../em-hub/new-projects/truth-seeker-web/2026-06-01-design.md`.

## Setup

```bash
pnpm install
cp .env.example .env.local
# Fill in .env.local — see comments in that file
pnpm dev
```

## Stack

Next.js 16 App Router · TypeScript · Tailwind · shadcn/ui · Firebase Auth + Firestore · Stripe (later) · Parapet (later) · Cloud Run.
```

- [ ] **Step 5: Initial commit**

```bash
git add -A
git commit -m "chore: bootstrap repo from qr-now-web- scaffold"
```

Expected: One commit on `main`.

---

### Task 2: Strip Supabase from the scaffold

**Files:**
- Modify: `package.json`
- Delete: any `src/**/supabase*.ts`, `src/lib/supabase/`, `src/app/api/auth/**` if present
- Modify: `.env.example`

- [ ] **Step 1: Remove Supabase deps**

Run:

```bash
pnpm remove @supabase/supabase-js @supabase/ssr @supabase/auth-helpers-nextjs 2>/dev/null || true
```

Then manually inspect `package.json` and remove any remaining `@supabase/*` entries.

- [ ] **Step 2: Delete Supabase code**

Run:

```bash
find src -type f \( -name 'supabase*' -o -path '*/supabase/*' \) -print
```

Delete every file the command lists. Also delete `src/app/api/auth/` entirely if it exists (we'll create our own Firebase-shaped one in Task 11).

```bash
find src -type f \( -name 'supabase*' -o -path '*/supabase/*' \) -delete
rm -rf src/lib/supabase
rm -rf src/app/api/auth
```

- [ ] **Step 3: Remove Supabase env vars from `.env.example`**

Open `.env.example`. Delete any lines matching `SUPABASE_*` or `NEXT_PUBLIC_SUPABASE_*`. We'll add Firebase vars in Task 4.

- [ ] **Step 4: Verify build still parses (will fail on missing imports — that's OK)**

```bash
pnpm install
pnpm tsc --noEmit 2>&1 | tee /tmp/tsc-after-supabase-strip.log
```

Expected: TS errors only about files that imported Supabase symbols. Make a note of which files those are — they're the next deletion list.

- [ ] **Step 5: Delete remaining files that imported Supabase**

For each broken file from `/tmp/tsc-after-supabase-strip.log`, decide:
- If it's a QR domain file (will be deleted in Task 3 anyway): leave it.
- If it's a layout/page that referenced Supabase auth: delete it (we'll rebuild layouts cleanly in Tasks 14–18).

Then:

```bash
pnpm tsc --noEmit
```

Expected: errors now limited to QR domain code (acceptable; Task 3 removes them).

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "chore: strip Supabase auth + dependencies"
```

---

### Task 3: Strip QR domain code

**Files:**
- Delete: any `src/app/**/qr/**`, `src/components/**/qr/**`, `src/lib/**/qr/**`
- Modify: any pages that referenced QR features

- [ ] **Step 1: Identify QR-related code**

```bash
grep -rln -i 'qr' src --include='*.ts' --include='*.tsx' | tee /tmp/qr-files.log
```

Review the list. Anything under `src/app/(qr)/`, `src/components/qr/`, `src/lib/qr/`, or files clearly named `qr-*` → delete.

- [ ] **Step 2: Delete QR code**

```bash
find src -type d \( -name 'qr' -o -name '*qr*' \) -print
```

For each directory the command lists, confirm it's QR-domain (not "query" or similar false-positive), then:

```bash
find src -type d \( -name 'qr' -o -name 'dynamic-qr' \) -exec rm -rf {} +
find src -type f \( -name 'qr-*' -o -name '*-qr.*' \) -delete
```

- [ ] **Step 3: Verify**

```bash
pnpm tsc --noEmit
```

Expected: zero errors (we may still have empty layout/page files; that's fine — they'll be replaced in Tasks 14–18).

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: remove QR domain code"
```

---

### Task 4: Install Firebase SDKs + define env contract

**Files:**
- Modify: `package.json`
- Modify: `.env.example`
- Create: `src/lib/firebase/.gitkeep`

- [ ] **Step 1: Install Firebase SDKs**

```bash
pnpm add firebase firebase-admin
pnpm add -D firebase-tools
```

Expected: `firebase` (JS SDK), `firebase-admin` (server), and `firebase-tools` (CLI for emulators/deploy) appear in `package.json`.

- [ ] **Step 2: Define `.env.example`**

Replace `.env.example` contents with:

```bash
# ============== Firebase — client (NEXT_PUBLIC_ exposed to browser) ==============
NEXT_PUBLIC_FIREBASE_API_KEY=
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=
NEXT_PUBLIC_FIREBASE_PROJECT_ID=
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=
NEXT_PUBLIC_FIREBASE_APP_ID=

# ============== Firebase — server (Admin SDK) ==============
# Service account JSON, base64-encoded. Generate via Firebase Console → Project Settings → Service Accounts → Generate new private key, then `base64 -i serviceAccount.json | pbcopy`.
FIREBASE_SERVICE_ACCOUNT_BASE64=

# ============== App ==============
NEXT_PUBLIC_APP_URL=http://localhost:3000

# ============== Emulators (dev only) ==============
# Set to "1" when running with pnpm dev:emulators
USE_FIREBASE_EMULATORS=0
```

- [ ] **Step 3: Add `.gitignore` entry for `.env.local`**

Verify `.env.local` is in `.gitignore`. If not, append:

```bash
echo ".env.local" >> .gitignore
```

- [ ] **Step 4: Create local `.env.local`**

```bash
cp .env.example .env.local
```

Then open `.env.local` and paste real values from your Firebase console (client config from Firebase Console → Project Settings → Your apps → SDK setup; service account base64 as described in the comment).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat: add Firebase SDKs and env contract"
```

---

### Task 5: Firebase Admin SDK module (TDD)

**Files:**
- Create: `src/lib/firebase/admin.ts`
- Test: `src/lib/firebase/admin.test.ts`
- Create: `vitest.config.ts` (if not already present in scaffold)

- [ ] **Step 1: Configure Vitest**

Check whether `vitest.config.ts` exists in the scaffold. If not, create it:

```ts
import { defineConfig } from 'vitest/config';
import path from 'node:path';

export default defineConfig({
  test: {
    environment: 'node',
    globals: true,
    setupFiles: ['./tests/setup.ts'],
  },
  resolve: {
    alias: { '@': path.resolve(__dirname, './src') },
  },
});
```

Also create `tests/setup.ts`:

```ts
import { vi } from 'vitest';

// Ensure tests run in a deterministic env
process.env.TZ = 'UTC';
```

Install Vitest if missing:

```bash
pnpm add -D vitest @vitest/ui
```

Add to `package.json` scripts:

```json
"test": "vitest run",
"test:watch": "vitest"
```

- [ ] **Step 2: Write the failing test**

Create `src/lib/firebase/admin.test.ts`:

```ts
import { describe, it, expect, beforeEach, vi } from 'vitest';

describe('lib/firebase/admin', () => {
  beforeEach(() => {
    vi.resetModules();
    delete process.env.FIREBASE_SERVICE_ACCOUNT_BASE64;
  });

  it('throws if FIREBASE_SERVICE_ACCOUNT_BASE64 is missing', async () => {
    await expect(import('./admin')).rejects.toThrow(
      /FIREBASE_SERVICE_ACCOUNT_BASE64/,
    );
  });

  it('initializes Admin SDK once and re-uses the app on subsequent imports', async () => {
    process.env.FIREBASE_SERVICE_ACCOUNT_BASE64 = Buffer.from(
      JSON.stringify({
        type: 'service_account',
        project_id: 'truthseeker-test',
        private_key_id: 'k',
        private_key:
          '-----BEGIN PRIVATE KEY-----\nFAKE\n-----END PRIVATE KEY-----\n',
        client_email: 'svc@truthseeker-test.iam.gserviceaccount.com',
      }),
    ).toString('base64');

    const mod1 = await import('./admin');
    const mod2 = await import('./admin');

    expect(mod1.adminApp).toBe(mod2.adminApp);
    expect(mod1.db).toBeDefined();
    expect(mod1.adminAuth).toBeDefined();
  });
});
```

- [ ] **Step 3: Run the test — expect failure**

```bash
pnpm test src/lib/firebase/admin.test.ts
```

Expected: FAIL with "Cannot find module './admin'".

- [ ] **Step 4: Write minimal implementation**

Create `src/lib/firebase/admin.ts`:

```ts
import 'server-only';
import { initializeApp, getApps, cert, type App } from 'firebase-admin/app';
import { getAuth } from 'firebase-admin/auth';
import { getFirestore } from 'firebase-admin/firestore';

function decodeServiceAccount(): Record<string, unknown> {
  const raw = process.env.FIREBASE_SERVICE_ACCOUNT_BASE64;
  if (!raw) {
    throw new Error(
      'FIREBASE_SERVICE_ACCOUNT_BASE64 is required for Firebase Admin SDK',
    );
  }
  const json = Buffer.from(raw, 'base64').toString('utf-8');
  return JSON.parse(json);
}

function initAdminApp(): App {
  const existing = getApps();
  if (existing.length > 0) return existing[0];

  const sa = decodeServiceAccount() as {
    project_id: string;
    private_key: string;
    client_email: string;
  };

  return initializeApp({
    credential: cert({
      projectId: sa.project_id,
      privateKey: sa.private_key,
      clientEmail: sa.client_email,
    }),
    projectId: sa.project_id,
  });
}

export const adminApp = initAdminApp();
export const adminAuth = getAuth(adminApp);
export const db = getFirestore(adminApp);

export async function verifyIdToken(idToken: string) {
  return adminAuth.verifyIdToken(idToken, true);
}
```

- [ ] **Step 5: Run the test — expect pass**

```bash
pnpm test src/lib/firebase/admin.test.ts
```

Expected: PASS (2/2).

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(firebase): admin SDK init with singleton + verifyIdToken"
```

---

### Task 6: Firebase JS SDK client + auth providers

**Files:**
- Create: `src/lib/firebase/client.ts`

- [ ] **Step 1: Create the client module**

Create `src/lib/firebase/client.ts`:

```ts
'use client';
import { initializeApp, getApps, type FirebaseApp } from 'firebase/app';
import {
  getAuth,
  GoogleAuthProvider,
  OAuthProvider,
  signInWithPopup,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut as fbSignOut,
  type User,
} from 'firebase/auth';
import { connectAuthEmulator } from 'firebase/auth';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

function getClientApp(): FirebaseApp {
  const existing = getApps();
  if (existing.length > 0) return existing[0];
  return initializeApp(firebaseConfig);
}

export const firebaseApp = getClientApp();
export const auth = getAuth(firebaseApp);

if (
  typeof window !== 'undefined' &&
  process.env.NEXT_PUBLIC_USE_FIREBASE_EMULATORS === '1' &&
  !(globalThis as { __authEmulatorConnected__?: boolean }).__authEmulatorConnected__
) {
  connectAuthEmulator(auth, 'http://localhost:9099', { disableWarnings: true });
  (globalThis as { __authEmulatorConnected__?: boolean }).__authEmulatorConnected__ = true;
}

export async function signInWithGoogle(): Promise<User> {
  const provider = new GoogleAuthProvider();
  const result = await signInWithPopup(auth, provider);
  return result.user;
}

export async function signInWithApple(): Promise<User> {
  const provider = new OAuthProvider('apple.com');
  provider.addScope('email');
  provider.addScope('name');
  const result = await signInWithPopup(auth, provider);
  return result.user;
}

export async function signInWithEmail(
  email: string,
  password: string,
): Promise<User> {
  const result = await signInWithEmailAndPassword(auth, email, password);
  return result.user;
}

export async function signUpWithEmail(
  email: string,
  password: string,
): Promise<User> {
  const result = await createUserWithEmailAndPassword(auth, email, password);
  return result.user;
}

export async function signOut(): Promise<void> {
  await fbSignOut(auth);
}
```

- [ ] **Step 2: Add the emulator env to `.env.example`**

Append to `.env.example`:

```bash
NEXT_PUBLIC_USE_FIREBASE_EMULATORS=0
```

- [ ] **Step 3: Type-check**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat(firebase): JS SDK client with Google/Apple/email providers"
```

---

### Task 7: Auth context provider for React

**Files:**
- Create: `src/lib/firebase/auth-context.tsx`

- [ ] **Step 1: Create the provider**

Create `src/lib/firebase/auth-context.tsx`:

```tsx
'use client';
import { createContext, useContext, useEffect, useState, type ReactNode } from 'react';
import { onIdTokenChanged, type User } from 'firebase/auth';
import { auth } from './client';

type AuthState = {
  user: User | null;
  loading: boolean;
};

const AuthContext = createContext<AuthState>({ user: null, loading: true });

export function AuthProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<AuthState>({ user: null, loading: true });

  useEffect(() => {
    const unsub = onIdTokenChanged(auth, (user) => {
      setState({ user, loading: false });
    });
    return () => unsub();
  }, []);

  return <AuthContext.Provider value={state}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthState {
  return useContext(AuthContext);
}
```

- [ ] **Step 2: Type-check**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "feat(firebase): React auth context + useAuth hook"
```

---

### Task 8: Firestore security rules + emulator setup

**Files:**
- Create: `firestore.rules`
- Create: `firestore.indexes.json`
- Create: `firebase.json`
- Test: `tests/firestore-rules.test.ts`

- [ ] **Step 1: Create `firestore.rules`**

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    function isSignedIn() {
      return request.auth != null;
    }

    function isOwner(uid) {
      return isSignedIn() && request.auth.uid == uid;
    }

    // Server-only fields the client must never write to its own user doc.
    function hasServerOnlyFieldChange(before, after) {
      let serverFields = ['stripeCustomerId', 'planStatus', 'planRenewsAt', 'lastEntitlementSync'];
      return serverFields.hasAny(after.diff(before).affectedKeys());
    }

    match /users/{uid} {
      allow read: if isOwner(uid);
      allow create: if isOwner(uid)
                    && !('stripeCustomerId' in request.resource.data)
                    && !('planStatus' in request.resource.data)
                    && !('planRenewsAt' in request.resource.data)
                    && !('lastEntitlementSync' in request.resource.data);
      allow update: if isOwner(uid)
                    && !hasServerOnlyFieldChange(resource.data, request.resource.data);
      allow delete: if false; // server-only

      match /searches/{searchId} {
        allow read: if isOwner(uid);
        allow write: if false; // server-only
      }
    }

    match /searchResults/{searchId} {
      allow read, write: if false; // server-only
    }

    match /stripeEvents/{id} {
      allow read, write: if false; // server-only
    }
  }
}
```

- [ ] **Step 2: Create `firestore.indexes.json`**

```json
{
  "indexes": [
    {
      "collectionGroup": "searches",
      "queryScope": "COLLECTION",
      "fields": [
        { "fieldPath": "createdAt", "order": "DESCENDING" }
      ]
    }
  ],
  "fieldOverrides": []
}
```

- [ ] **Step 3: Create `firebase.json` for emulator config**

```json
{
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  },
  "emulators": {
    "auth": { "port": 9099 },
    "firestore": { "port": 8080 },
    "ui": { "enabled": true, "port": 4000 },
    "singleProjectMode": true
  }
}
```

- [ ] **Step 4: Install rules testing lib + write the failing test**

```bash
pnpm add -D @firebase/rules-unit-testing
```

Create `tests/firestore-rules.test.ts`:

```ts
import {
  initializeTestEnvironment,
  type RulesTestEnvironment,
  assertSucceeds,
  assertFails,
} from '@firebase/rules-unit-testing';
import { setDoc, doc, getDoc, updateDoc } from 'firebase/firestore';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

let testEnv: RulesTestEnvironment;

beforeAll(async () => {
  testEnv = await initializeTestEnvironment({
    projectId: 'truthseeker-rules-test',
    firestore: {
      rules: fs.readFileSync(path.resolve(__dirname, '../firestore.rules'), 'utf8'),
      host: '127.0.0.1',
      port: 8080,
    },
  });
});

afterAll(async () => {
  await testEnv.cleanup();
});

beforeEach(async () => {
  await testEnv.clearFirestore();
});

describe('firestore.rules — users/{uid}', () => {
  it('owner can read their own user doc', async () => {
    const ctx = testEnv.authenticatedContext('alice');
    await assertSucceeds(getDoc(doc(ctx.firestore(), 'users/alice')));
  });

  it('other users cannot read', async () => {
    const ctx = testEnv.authenticatedContext('bob');
    await assertFails(getDoc(doc(ctx.firestore(), 'users/alice')));
  });

  it('owner can create their own user doc without server-only fields', async () => {
    const ctx = testEnv.authenticatedContext('alice');
    await assertSucceeds(
      setDoc(doc(ctx.firestore(), 'users/alice'), {
        email: 'alice@example.com',
        createdAt: new Date(),
      }),
    );
  });

  it('owner cannot write stripeCustomerId on create', async () => {
    const ctx = testEnv.authenticatedContext('alice');
    await assertFails(
      setDoc(doc(ctx.firestore(), 'users/alice'), {
        email: 'alice@example.com',
        stripeCustomerId: 'cus_123',
      }),
    );
  });

  it('owner cannot change planStatus on update', async () => {
    await testEnv.withSecurityRulesDisabled(async (ctx) => {
      await setDoc(doc(ctx.firestore(), 'users/alice'), {
        email: 'alice@example.com',
        planStatus: 'free',
      });
    });
    const ctx = testEnv.authenticatedContext('alice');
    await assertFails(
      updateDoc(doc(ctx.firestore(), 'users/alice'), { planStatus: 'pro' }),
    );
  });

  it('owner can update non-server fields', async () => {
    await testEnv.withSecurityRulesDisabled(async (ctx) => {
      await setDoc(doc(ctx.firestore(), 'users/alice'), {
        email: 'alice@example.com',
      });
    });
    const ctx = testEnv.authenticatedContext('alice');
    await assertSucceeds(
      updateDoc(doc(ctx.firestore(), 'users/alice'), { displayName: 'Alice' }),
    );
  });
});

describe('firestore.rules — users/{uid}/searches/{id}', () => {
  it('owner can read their own history', async () => {
    await testEnv.withSecurityRulesDisabled(async (ctx) => {
      await setDoc(doc(ctx.firestore(), 'users/alice/searches/s1'), {
        query: 'jane doe',
      });
    });
    const ctx = testEnv.authenticatedContext('alice');
    await assertSucceeds(getDoc(doc(ctx.firestore(), 'users/alice/searches/s1')));
  });

  it('client cannot write to history', async () => {
    const ctx = testEnv.authenticatedContext('alice');
    await assertFails(
      setDoc(doc(ctx.firestore(), 'users/alice/searches/s1'), {
        query: 'forbidden',
      }),
    );
  });
});

describe('firestore.rules — searchResults', () => {
  it('client cannot read searchResults', async () => {
    const ctx = testEnv.authenticatedContext('alice');
    await assertFails(getDoc(doc(ctx.firestore(), 'searchResults/r1')));
  });
});
```

- [ ] **Step 5: Run the emulator + test**

In one terminal:

```bash
pnpm exec firebase emulators:start --only firestore --project truthseeker-rules-test
```

In another terminal:

```bash
pnpm test tests/firestore-rules.test.ts
```

Expected: PASS (8/8).

- [ ] **Step 6: Add npm scripts**

In `package.json` scripts:

```json
"emulators": "firebase emulators:start --only auth,firestore --project demo-truthseeker",
"test:rules": "firebase emulators:exec --only firestore --project truthseeker-rules-test 'pnpm test tests/firestore-rules.test.ts'"
```

- [ ] **Step 7: Run the all-in-one script**

```bash
pnpm test:rules
```

Expected: emulator starts, tests pass, emulator shuts down.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(firestore): security rules + emulator config + rules tests"
```

---

### Task 9: Session cookie helpers (TDD)

**Files:**
- Create: `src/lib/auth/session-cookie.ts`
- Test: `src/lib/auth/session-cookie.test.ts`

- [ ] **Step 1: Write the failing test**

Create `src/lib/auth/session-cookie.test.ts`:

```ts
import { describe, it, expect } from 'vitest';
import {
  SESSION_COOKIE_NAME,
  SESSION_COOKIE_MAX_AGE_SECONDS,
  buildSessionCookieOptions,
} from './session-cookie';

describe('session-cookie', () => {
  it('uses __session as the cookie name (required by Firebase Hosting/Cloud Run)', () => {
    expect(SESSION_COOKIE_NAME).toBe('__session');
  });

  it('max age is 14 days in seconds', () => {
    expect(SESSION_COOKIE_MAX_AGE_SECONDS).toBe(14 * 24 * 60 * 60);
  });

  it('build options sets httpOnly, secure (in prod), sameSite=lax, path=/', () => {
    const prod = buildSessionCookieOptions({ env: 'production' });
    expect(prod.httpOnly).toBe(true);
    expect(prod.secure).toBe(true);
    expect(prod.sameSite).toBe('lax');
    expect(prod.path).toBe('/');
    expect(prod.maxAge).toBe(SESSION_COOKIE_MAX_AGE_SECONDS);

    const dev = buildSessionCookieOptions({ env: 'development' });
    expect(dev.secure).toBe(false);
  });
});
```

- [ ] **Step 2: Run test — expect failure**

```bash
pnpm test src/lib/auth/session-cookie.test.ts
```

Expected: FAIL with "Cannot find module './session-cookie'".

- [ ] **Step 3: Write the implementation**

Create `src/lib/auth/session-cookie.ts`:

```ts
export const SESSION_COOKIE_NAME = '__session';
export const SESSION_COOKIE_MAX_AGE_SECONDS = 14 * 24 * 60 * 60;

type Env = 'development' | 'test' | 'production';

export type CookieOptions = {
  httpOnly: true;
  secure: boolean;
  sameSite: 'lax';
  path: '/';
  maxAge: number;
};

export function buildSessionCookieOptions(opts: { env: Env }): CookieOptions {
  return {
    httpOnly: true,
    secure: opts.env === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: SESSION_COOKIE_MAX_AGE_SECONDS,
  };
}
```

- [ ] **Step 4: Run test — expect pass**

```bash
pnpm test src/lib/auth/session-cookie.test.ts
```

Expected: PASS (3/3).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(auth): session cookie name + options helper"
```

---

### Task 10: Server-side session reader (TDD)

**Files:**
- Create: `src/lib/auth/server-session.ts`
- Test: `src/lib/auth/server-session.test.ts`

- [ ] **Step 1: Write the failing test**

Create `src/lib/auth/server-session.test.ts`:

```ts
import { describe, it, expect, vi, beforeEach } from 'vitest';

vi.mock('@/lib/firebase/admin', () => ({
  adminAuth: {
    verifySessionCookie: vi.fn(),
  },
}));

import { adminAuth } from '@/lib/firebase/admin';
import { verifySessionCookie } from './server-session';

describe('server-session', () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });

  it('returns null when cookie is undefined', async () => {
    const res = await verifySessionCookie(undefined);
    expect(res).toBeNull();
    expect(adminAuth.verifySessionCookie).not.toHaveBeenCalled();
  });

  it('returns null when cookie is empty string', async () => {
    const res = await verifySessionCookie('');
    expect(res).toBeNull();
  });

  it('returns decoded claims when cookie is valid', async () => {
    (adminAuth.verifySessionCookie as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
      uid: 'alice',
      email: 'alice@example.com',
    });
    const res = await verifySessionCookie('valid-cookie');
    expect(res).toEqual({ uid: 'alice', email: 'alice@example.com' });
    expect(adminAuth.verifySessionCookie).toHaveBeenCalledWith('valid-cookie', true);
  });

  it('returns null when verification throws', async () => {
    (adminAuth.verifySessionCookie as ReturnType<typeof vi.fn>).mockRejectedValueOnce(
      new Error('expired'),
    );
    const res = await verifySessionCookie('bad-cookie');
    expect(res).toBeNull();
  });
});
```

- [ ] **Step 2: Run test — expect failure**

```bash
pnpm test src/lib/auth/server-session.test.ts
```

Expected: FAIL ("Cannot find module './server-session'").

- [ ] **Step 3: Implementation**

Create `src/lib/auth/server-session.ts`:

```ts
import 'server-only';
import { adminAuth } from '@/lib/firebase/admin';
import type { DecodedIdToken } from 'firebase-admin/auth';

export type SessionClaims = Pick<DecodedIdToken, 'uid' | 'email'> & Partial<DecodedIdToken>;

export async function verifySessionCookie(
  cookie: string | undefined,
): Promise<SessionClaims | null> {
  if (!cookie) return null;
  try {
    const claims = await adminAuth.verifySessionCookie(cookie, true);
    return claims;
  } catch {
    return null;
  }
}
```

- [ ] **Step 4: Run test — expect pass**

```bash
pnpm test src/lib/auth/server-session.test.ts
```

Expected: PASS (4/4).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(auth): server-side session cookie verifier"
```

---

### Task 11: `POST /api/auth/session` route (ID token → session cookie)

**Files:**
- Create: `src/app/api/auth/session/route.ts`

- [ ] **Step 1: Implement the route**

Create `src/app/api/auth/session/route.ts`:

```ts
import { NextResponse, type NextRequest } from 'next/server';
import { adminAuth } from '@/lib/firebase/admin';
import {
  SESSION_COOKIE_NAME,
  SESSION_COOKIE_MAX_AGE_SECONDS,
  buildSessionCookieOptions,
} from '@/lib/auth/session-cookie';

export const runtime = 'nodejs';

export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => null)) as { idToken?: string } | null;
  const idToken = body?.idToken;
  if (!idToken) {
    return NextResponse.json({ error: 'missing_id_token' }, { status: 400 });
  }

  let sessionCookie: string;
  try {
    sessionCookie = await adminAuth.createSessionCookie(idToken, {
      expiresIn: SESSION_COOKIE_MAX_AGE_SECONDS * 1000,
    });
  } catch {
    return NextResponse.json({ error: 'invalid_id_token' }, { status: 401 });
  }

  const env = (process.env.NODE_ENV ?? 'development') as
    | 'development'
    | 'test'
    | 'production';
  const options = buildSessionCookieOptions({ env });

  const res = NextResponse.json({ ok: true });
  res.cookies.set({
    name: SESSION_COOKIE_NAME,
    value: sessionCookie,
    ...options,
  });
  return res;
}

export async function DELETE() {
  const res = NextResponse.json({ ok: true });
  res.cookies.set({
    name: SESSION_COOKIE_NAME,
    value: '',
    httpOnly: true,
    path: '/',
    maxAge: 0,
  });
  return res;
}
```

- [ ] **Step 2: Type-check**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

- [ ] **Step 3: Smoke test against the running app (Firebase emulators + dev server)**

Terminal 1:

```bash
pnpm emulators
```

Terminal 2 (with `NEXT_PUBLIC_USE_FIREBASE_EMULATORS=1` in `.env.local`):

```bash
pnpm dev
```

Use the emulator UI at `http://localhost:4000` to create a test user, then in the Firefox/Chrome devtools console on `http://localhost:3000`:

```js
const { auth, signInWithEmailAndPassword } = await import('firebase/auth');
const m = await import('/_next/static/chunks/main-app.js'); // pulled by HMR; skip if errors
// Easier: sign in via the eventual UI in Task 17. This step is just to verify the API exists.
fetch('/api/auth/session', { method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({}) })
  .then(r => r.status); // expect 400
```

Expected: `400` for empty body. (Full happy-path verified in Task 17.)

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat(api): /api/auth/session — id token → session cookie + DELETE clears"
```

---

### Task 12: Server-side auth guard helper (TDD)

**Files:**
- Create: `src/lib/auth-guard.ts`
- Test: `src/lib/auth-guard.test.ts`

- [ ] **Step 1: Write the failing test**

Create `src/lib/auth-guard.test.ts`:

```ts
import { describe, it, expect, vi, beforeEach } from 'vitest';

vi.mock('next/headers', () => ({
  cookies: vi.fn(),
}));

vi.mock('next/navigation', () => ({
  redirect: vi.fn((url: string) => {
    throw new Error(`NEXT_REDIRECT:${url}`);
  }),
}));

vi.mock('./auth/server-session', () => ({
  verifySessionCookie: vi.fn(),
}));

import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { verifySessionCookie } from './auth/server-session';
import { requireUser } from './auth-guard';

describe('auth-guard', () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });

  it('returns claims when session is valid', async () => {
    (cookies as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
      get: () => ({ value: 'valid' }),
    });
    (verifySessionCookie as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
      uid: 'alice',
      email: 'alice@example.com',
    });

    const claims = await requireUser({ locale: 'en' });
    expect(claims.uid).toBe('alice');
    expect(redirect).not.toHaveBeenCalled();
  });

  it('redirects to /[locale]/login when cookie missing', async () => {
    (cookies as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
      get: () => undefined,
    });

    await expect(requireUser({ locale: 'en', returnTo: '/app/search' })).rejects.toThrow(
      'NEXT_REDIRECT:/en/login?returnTo=%2Fapp%2Fsearch',
    );
  });

  it('redirects when session is invalid', async () => {
    (cookies as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
      get: () => ({ value: 'expired' }),
    });
    (verifySessionCookie as ReturnType<typeof vi.fn>).mockResolvedValueOnce(null);

    await expect(requireUser({ locale: 'en' })).rejects.toThrow(
      /NEXT_REDIRECT:\/en\/login/,
    );
  });
});
```

- [ ] **Step 2: Run test — expect failure**

```bash
pnpm test src/lib/auth-guard.test.ts
```

Expected: FAIL ("Cannot find module './auth-guard'").

- [ ] **Step 3: Implementation**

Create `src/lib/auth-guard.ts`:

```ts
import 'server-only';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { verifySessionCookie, type SessionClaims } from './auth/server-session';
import { SESSION_COOKIE_NAME } from './auth/session-cookie';

export async function requireUser(opts: {
  locale: string;
  returnTo?: string;
}): Promise<SessionClaims> {
  const cookieStore = await cookies();
  const cookie = cookieStore.get(SESSION_COOKIE_NAME)?.value;
  const claims = await verifySessionCookie(cookie);

  if (!claims) {
    const params = new URLSearchParams();
    if (opts.returnTo) params.set('returnTo', opts.returnTo);
    const qs = params.toString();
    redirect(`/${opts.locale}/login${qs ? `?${qs}` : ''}`);
  }
  return claims;
}

export async function getUserOptional(): Promise<SessionClaims | null> {
  const cookieStore = await cookies();
  const cookie = cookieStore.get(SESSION_COOKIE_NAME)?.value;
  return verifySessionCookie(cookie);
}
```

- [ ] **Step 4: Run test — expect pass**

```bash
pnpm test src/lib/auth-guard.test.ts
```

Expected: PASS (3/3).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(auth): server-side requireUser + getUserOptional guard"
```

---

### Task 13: i18n config (next-intl, en-only)

**Files:**
- Create: `src/i18n/config.ts`
- Create: `src/i18n/request.ts`
- Create: `src/i18n/navigation.ts`
- Create: `messages/en.json`
- Modify: `next.config.ts`

- [ ] **Step 1: Install next-intl**

```bash
pnpm add next-intl
```

- [ ] **Step 2: Create config**

`src/i18n/config.ts`:

```ts
export const locales = ['en'] as const;
export const defaultLocale = 'en' as const;
export type Locale = (typeof locales)[number];

export function isValidLocale(value: string): value is Locale {
  return (locales as readonly string[]).includes(value);
}
```

- [ ] **Step 3: Server config**

`src/i18n/request.ts`:

```ts
import { getRequestConfig } from 'next-intl/server';
import { notFound } from 'next/navigation';
import { isValidLocale, defaultLocale } from './config';

export default getRequestConfig(async ({ requestLocale }) => {
  const locale = (await requestLocale) ?? defaultLocale;
  if (!isValidLocale(locale)) notFound();

  return {
    locale,
    messages: (await import(`../../messages/${locale}.json`)).default,
  };
});
```

- [ ] **Step 4: Client navigation helpers**

`src/i18n/navigation.ts`:

```ts
import { createNavigation } from 'next-intl/navigation';
import { locales, defaultLocale } from './config';

export const { Link, redirect, usePathname, useRouter, getPathname } = createNavigation({
  locales,
  defaultLocale,
  localePrefix: 'always',
});
```

- [ ] **Step 5: Empty messages catalog**

`messages/en.json`:

```json
{
  "common": {
    "appName": "Truth Seeker"
  },
  "auth": {
    "login": {
      "title": "Sign in",
      "emailLabel": "Email",
      "passwordLabel": "Password",
      "submit": "Sign in",
      "withGoogle": "Continue with Google",
      "withApple": "Continue with Apple",
      "noAccount": "Don't have an account?",
      "signUpLink": "Sign up"
    },
    "signup": {
      "title": "Create your account",
      "submit": "Sign up",
      "haveAccount": "Already have an account?",
      "loginLink": "Sign in"
    }
  },
  "landing": {
    "headline": "Find anyone, instantly"
  }
}
```

- [ ] **Step 6: Wire `next.config.ts`**

Replace `next.config.ts` with:

```ts
import type { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts');

const nextConfig: NextConfig = {
  output: 'standalone', // required for Cloud Run container build
  experimental: {
    typedRoutes: true,
  },
};

export default withNextIntl(nextConfig);
```

- [ ] **Step 7: Type-check**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(i18n): next-intl wiring with en-only locale"
```

---

### Task 14: Middleware (next-intl + auth redirects)

**Files:**
- Create: `src/middleware.ts`

- [ ] **Step 1: Implement middleware**

`src/middleware.ts`:

```ts
import createIntlMiddleware from 'next-intl/middleware';
import { NextResponse, type NextRequest } from 'next/server';
import { locales, defaultLocale } from '@/i18n/config';
import { SESSION_COOKIE_NAME } from '@/lib/auth/session-cookie';

const intlMiddleware = createIntlMiddleware({
  locales,
  defaultLocale,
  localePrefix: 'always',
});

// Paths under /[locale]/app/** require an authenticated session.
function requiresAuth(pathname: string): boolean {
  // Strip leading /[locale]/ prefix
  const stripped = pathname.replace(/^\/[a-z]{2}(?=\/|$)/, '');
  return stripped.startsWith('/app');
}

export function middleware(req: NextRequest) {
  const intlResponse = intlMiddleware(req);

  if (requiresAuth(req.nextUrl.pathname)) {
    const sessionCookie = req.cookies.get(SESSION_COOKIE_NAME);
    if (!sessionCookie?.value) {
      const url = req.nextUrl.clone();
      const locale = url.pathname.split('/')[1] || defaultLocale;
      const returnTo = url.pathname + url.search;
      url.pathname = `/${locale}/login`;
      url.search = `?returnTo=${encodeURIComponent(returnTo)}`;
      return NextResponse.redirect(url);
    }
  }

  return intlResponse;
}

export const config = {
  matcher: ['/((?!api|_next|_vercel|.*\\..*).*)'],
};
```

Note: middleware does not call Admin SDK (it can't run in Edge runtime); it only checks cookie *presence*. The actual cookie *validity* check happens server-side in RSCs via `requireUser` (Task 12).

- [ ] **Step 2: Type-check**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "feat(middleware): locale routing + cookie-presence auth gate for /app/*"
```

---

### Task 15: Root layout + public route group

**Files:**
- Modify/Create: `src/app/layout.tsx`
- Create: `src/app/(public)/[locale]/layout.tsx`
- Create: `src/app/(public)/[locale]/page.tsx`
- Create: `src/app/globals.css` (if not in scaffold)

- [ ] **Step 1: Verify existing root layout, replace with minimal**

`src/app/layout.tsx`:

```tsx
import './globals.css';
import type { ReactNode } from 'react';

export const metadata = {
  title: 'Truth Seeker',
  description: 'Find anyone, instantly.',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}
```

If `src/app/globals.css` already exists from the scaffold, leave it. Otherwise create with Tailwind directives:

```css
@import "tailwindcss";
```

- [ ] **Step 2: Public route group layout**

`src/app/(public)/[locale]/layout.tsx`:

```tsx
import { NextIntlClientProvider } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import type { ReactNode } from 'react';
import { isValidLocale } from '@/i18n/config';

export default async function PublicLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();
  setRequestLocale(locale);
  const messages = await getMessages();

  return (
    <NextIntlClientProvider messages={messages} locale={locale}>
      <main>{children}</main>
    </NextIntlClientProvider>
  );
}
```

- [ ] **Step 3: Landing placeholder**

`src/app/(public)/[locale]/page.tsx`:

```tsx
import { getTranslations } from 'next-intl/server';

export default async function LandingPage() {
  const t = await getTranslations('landing');
  return (
    <div>
      <h1>{t('headline')}</h1>
      <p>Truth Seeker Web — coming soon.</p>
    </div>
  );
}
```

- [ ] **Step 4: Run dev server, visit /en**

```bash
pnpm dev
```

Visit `http://localhost:3000/en`. Expect "Find anyone, instantly" heading.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(app): root + public route group layouts and landing placeholder"
```

---

### Task 16: Auth route group (login + signup pages)

**Files:**
- Create: `src/app/(auth)/[locale]/layout.tsx`
- Create: `src/app/(auth)/[locale]/login/page.tsx`
- Create: `src/app/(auth)/[locale]/signup/page.tsx`
- Create: `src/components/auth/AuthForm.tsx`

- [ ] **Step 1: Auth route group layout**

`src/app/(auth)/[locale]/layout.tsx`:

```tsx
import { NextIntlClientProvider } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import type { ReactNode } from 'react';
import { isValidLocale } from '@/i18n/config';
import { AuthProvider } from '@/lib/firebase/auth-context';

export default async function AuthLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();
  setRequestLocale(locale);
  const messages = await getMessages();

  return (
    <NextIntlClientProvider messages={messages} locale={locale}>
      <AuthProvider>
        <main style={{ maxWidth: 420, margin: '4rem auto', padding: '1rem' }}>
          {children}
        </main>
      </AuthProvider>
    </NextIntlClientProvider>
  );
}
```

- [ ] **Step 2: Shared auth form component**

`src/components/auth/AuthForm.tsx`:

```tsx
'use client';
import { useState, type FormEvent } from 'react';
import { useTranslations } from 'next-intl';
import {
  signInWithEmail,
  signUpWithEmail,
  signInWithGoogle,
  signInWithApple,
} from '@/lib/firebase/client';
import { useRouter } from '@/i18n/navigation';
import { useSearchParams } from 'next/navigation';

type Mode = 'login' | 'signup';

async function exchangeIdTokenForCookie(idToken: string) {
  const res = await fetch('/api/auth/session', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ idToken }),
  });
  if (!res.ok) throw new Error('session_exchange_failed');
}

export function AuthForm({ mode }: { mode: Mode }) {
  const t = useTranslations(`auth.${mode}`);
  const tShared = useTranslations('auth.login');
  const router = useRouter();
  const searchParams = useSearchParams();
  const returnTo = searchParams.get('returnTo') ?? '/app';

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function withAuth(work: () => Promise<{ getIdToken(): Promise<string> }>) {
    setError(null);
    setBusy(true);
    try {
      const user = await work();
      const idToken = await user.getIdToken();
      await exchangeIdTokenForCookie(idToken);
      // Hard navigate to ensure middleware re-evaluates the new cookie.
      window.location.href = returnTo;
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'unknown_error');
    } finally {
      setBusy(false);
    }
  }

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    await withAuth(() =>
      mode === 'login' ? signInWithEmail(email, password) : signUpWithEmail(email, password),
    );
  }

  return (
    <div>
      <h1 style={{ marginBottom: '1.5rem' }}>{t('title')}</h1>
      <form onSubmit={onSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
        <label>
          {tShared('emailLabel')}
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            autoComplete="email"
            disabled={busy}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </label>
        <label>
          {tShared('passwordLabel')}
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            autoComplete={mode === 'login' ? 'current-password' : 'new-password'}
            minLength={6}
            disabled={busy}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </label>
        <button type="submit" disabled={busy}>
          {t('submit')}
        </button>
      </form>

      <hr style={{ margin: '1.5rem 0' }} />

      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <button onClick={() => withAuth(() => signInWithGoogle())} disabled={busy}>
          {tShared('withGoogle')}
        </button>
        <button onClick={() => withAuth(() => signInWithApple())} disabled={busy}>
          {tShared('withApple')}
        </button>
      </div>

      {error && (
        <p style={{ color: 'crimson', marginTop: '1rem' }} role="alert">
          {error}
        </p>
      )}

      <p style={{ marginTop: '1.5rem' }}>
        {mode === 'login' ? (
          <>
            {t('noAccount')}{' '}
            <a onClick={() => router.push('/signup')} style={{ cursor: 'pointer' }}>
              {t('signUpLink')}
            </a>
          </>
        ) : (
          <>
            {t('haveAccount')}{' '}
            <a onClick={() => router.push('/login')} style={{ cursor: 'pointer' }}>
              {t('loginLink')}
            </a>
          </>
        )}
      </p>
    </div>
  );
}
```

- [ ] **Step 3: Login page**

`src/app/(auth)/[locale]/login/page.tsx`:

```tsx
import { AuthForm } from '@/components/auth/AuthForm';

export default function LoginPage() {
  return <AuthForm mode="login" />;
}
```

- [ ] **Step 4: Signup page**

`src/app/(auth)/[locale]/signup/page.tsx`:

```tsx
import { AuthForm } from '@/components/auth/AuthForm';

export default function SignupPage() {
  return <AuthForm mode="signup" />;
}
```

- [ ] **Step 5: Type-check + run**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

```bash
pnpm dev
```

Visit `http://localhost:3000/en/login` — expect the login form to render. (Real sign-in tested end-to-end in Task 18.)

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(auth): login + signup pages with email/Google/Apple"
```

---

### Task 17: App route group (auth-guarded) + first-login user-doc creation

**Files:**
- Create: `src/app/(app)/[locale]/layout.tsx`
- Create: `src/app/(app)/[locale]/page.tsx`
- Modify: `src/app/api/auth/session/route.ts` (add user-doc bootstrap)

- [ ] **Step 1: App route group layout**

`src/app/(app)/[locale]/layout.tsx`:

```tsx
import { NextIntlClientProvider } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import type { ReactNode } from 'react';
import { isValidLocale } from '@/i18n/config';
import { AuthProvider } from '@/lib/firebase/auth-context';
import { requireUser } from '@/lib/auth-guard';

export default async function AppLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isValidLocale(locale)) notFound();
  setRequestLocale(locale);
  await requireUser({ locale });

  const messages = await getMessages();

  return (
    <NextIntlClientProvider messages={messages} locale={locale}>
      <AuthProvider>
        <main style={{ padding: '2rem' }}>
          <nav style={{ marginBottom: '2rem' }}>
            <strong>Truth Seeker (app)</strong>
          </nav>
          {children}
        </main>
      </AuthProvider>
    </NextIntlClientProvider>
  );
}
```

- [ ] **Step 2: App home placeholder**

`src/app/(app)/[locale]/page.tsx`:

```tsx
import { getUserOptional } from '@/lib/auth-guard';

export default async function AppHome() {
  const user = await getUserOptional();
  return (
    <div>
      <h1>Welcome</h1>
      <p>Signed in as {user?.email ?? 'unknown'} (uid: {user?.uid ?? '—'})</p>
    </div>
  );
}
```

- [ ] **Step 3: Bootstrap user doc on session creation**

Modify `src/app/api/auth/session/route.ts` — update the `POST` handler so that after the session cookie is created, we ensure a `users/{uid}` doc exists. Replace the `POST` function body with:

```ts
export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => null)) as { idToken?: string } | null;
  const idToken = body?.idToken;
  if (!idToken) {
    return NextResponse.json({ error: 'missing_id_token' }, { status: 400 });
  }

  let decoded;
  try {
    decoded = await adminAuth.verifyIdToken(idToken, true);
  } catch {
    return NextResponse.json({ error: 'invalid_id_token' }, { status: 401 });
  }

  let sessionCookie: string;
  try {
    sessionCookie = await adminAuth.createSessionCookie(idToken, {
      expiresIn: SESSION_COOKIE_MAX_AGE_SECONDS * 1000,
    });
  } catch {
    return NextResponse.json({ error: 'session_creation_failed' }, { status: 401 });
  }

  // Idempotent user-doc bootstrap.
  const userRef = db.collection('users').doc(decoded.uid);
  const snap = await userRef.get();
  if (!snap.exists) {
    await userRef.set({
      email: decoded.email ?? null,
      displayName: decoded.name ?? null,
      photoURL: decoded.picture ?? null,
      createdAt: new Date(),
      lastSeenAt: new Date(),
      locale: 'en',
      preferences: { darkMode: false, emailNotifications: true },
    });
  } else {
    await userRef.update({ lastSeenAt: new Date() });
  }

  const env = (process.env.NODE_ENV ?? 'development') as
    | 'development'
    | 'test'
    | 'production';
  const options = buildSessionCookieOptions({ env });

  const res = NextResponse.json({ ok: true });
  res.cookies.set({
    name: SESSION_COOKIE_NAME,
    value: sessionCookie,
    ...options,
  });
  return res;
}
```

Also add `db` to the imports at the top:

```ts
import { adminAuth, db } from '@/lib/firebase/admin';
```

- [ ] **Step 4: Type-check**

```bash
pnpm tsc --noEmit
```

Expected: zero errors.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(app): auth-guarded app route group + user-doc bootstrap on session create"
```

---

### Task 18: End-to-end smoke test (manual, against emulators)

**Files:** none new.

- [ ] **Step 1: Start emulators**

Terminal 1:

```bash
pnpm emulators
```

- [ ] **Step 2: Start dev server**

Terminal 2 (with `NEXT_PUBLIC_USE_FIREBASE_EMULATORS=1` in `.env.local`):

```bash
pnpm dev
```

- [ ] **Step 3: Sign-up flow**

1. Visit `http://localhost:3000/en/signup`.
2. Enter `test@example.com` / `password123` → click Sign up.
3. Expect redirect to `/en/app` showing "Signed in as test@example.com".
4. In the emulator UI (`http://localhost:4000`):
   - Firestore tab: verify a `users/{uid}` doc was created.
   - Auth tab: verify the user exists.

- [ ] **Step 4: Sign-out and protected-route redirect**

1. Open devtools → Application → Cookies → delete `__session`.
2. Navigate to `http://localhost:3000/en/app`.
3. Expect redirect to `/en/login?returnTo=%2Fapp`.

- [ ] **Step 5: Sign-back-in returns to original path**

1. On the login screen, enter `test@example.com` / `password123` → Sign in.
2. Expect redirect to `/en/app` (the `returnTo`).
3. Verify `lastSeenAt` updated in Firestore emulator.

- [ ] **Step 6: Google + Apple SSO (deferred to prod-like env)**

These cannot be tested against the emulator (no real OAuth). Verify in Task 21's dev Cloud Run deploy.

- [ ] **Step 7: Commit a note**

```bash
git commit --allow-empty -m "test: manual smoke test of email signup/login passes against emulators"
```

---

### Task 19: Dockerfile + cloudbuild.yaml for dev Cloud Run

**Files:**
- Create: `Dockerfile`
- Create: `.dockerignore`
- Modify/Create: `cloudbuild.yaml`

- [ ] **Step 1: Dockerfile (multi-stage, Next.js standalone)**

```Dockerfile
# syntax=docker/dockerfile:1.7
FROM node:20-alpine AS deps
WORKDIR /app
RUN corepack enable
COPY package.json pnpm-lock.yaml ./
RUN pnpm fetch --frozen-lockfile

FROM node:20-alpine AS builder
WORKDIR /app
RUN corepack enable
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN pnpm install --offline --frozen-lockfile
RUN pnpm build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=8080
RUN addgroup -S nodejs -g 1001 && adduser -S nextjs -u 1001
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
USER nextjs
EXPOSE 8080
CMD ["node", "server.js"]
```

- [ ] **Step 2: `.dockerignore`**

```
node_modules
.next
.git
.env.local
.env.*.local
README.md
docs
tests
```

- [ ] **Step 3: `cloudbuild.yaml` (dev pipeline)**

Replace existing `cloudbuild.yaml` with:

```yaml
steps:
  - id: 'install'
    name: 'node:20'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        corepack enable
        pnpm install --frozen-lockfile

  - id: 'lint-and-test'
    name: 'node:20'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        corepack enable
        pnpm lint
        pnpm tsc --noEmit
        pnpm test

  - id: 'build-image'
    name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '-t'
      - '${_REGION}-docker.pkg.dev/$PROJECT_ID/${_REPO}/truthseeker-web:$SHORT_SHA'
      - '.'

  - id: 'push-image'
    name: 'gcr.io/cloud-builders/docker'
    args:
      - 'push'
      - '${_REGION}-docker.pkg.dev/$PROJECT_ID/${_REPO}/truthseeker-web:$SHORT_SHA'

  - id: 'deploy-dev'
    name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: 'gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'truthseeker-web-dev'
      - '--image=${_REGION}-docker.pkg.dev/$PROJECT_ID/${_REPO}/truthseeker-web:$SHORT_SHA'
      - '--region=${_REGION}'
      - '--platform=managed'
      - '--allow-unauthenticated'
      - '--set-env-vars=NODE_ENV=production'
      - '--set-secrets=FIREBASE_SERVICE_ACCOUNT_BASE64=firebase-service-account-base64:latest'
      - '--memory=512Mi'
      - '--cpu=1'
      - '--max-instances=5'

substitutions:
  _REGION: 'europe-west1'
  _REPO: 'truthseeker-web'

options:
  logging: CLOUD_LOGGING_ONLY
```

- [ ] **Step 4: Add lint script if missing**

In `package.json`:

```json
"lint": "next lint"
```

- [ ] **Step 5: Local docker build sanity check**

```bash
docker build -t truthseeker-web:local .
docker run --rm -p 8080:8080 \
  -e NEXT_PUBLIC_FIREBASE_API_KEY=$NEXT_PUBLIC_FIREBASE_API_KEY \
  -e FIREBASE_SERVICE_ACCOUNT_BASE64=$FIREBASE_SERVICE_ACCOUNT_BASE64 \
  truthseeker-web:local
```

Visit `http://localhost:8080/en` — expect landing page. Stop the container.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(infra): Dockerfile + Cloud Build pipeline for dev"
```

---

### Task 20: Terraform for dev environment

**Files:**
- Create: `terraform/main.tf`
- Create: `terraform/variables.tf`
- Create: `terraform/dev.tfvars`
- Create: `terraform/README.md`

- [ ] **Step 1: `terraform/main.tf`**

```hcl
terraform {
  required_version = ">= 1.6"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.30"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "truthseeker_web" {
  location      = var.region
  repository_id = "truthseeker-web"
  description   = "truthseeker-web container images"
  format        = "DOCKER"
}

resource "google_secret_manager_secret" "firebase_service_account_base64" {
  secret_id = "firebase-service-account-base64"
  replication {
    auto {}
  }
}

resource "google_cloud_run_v2_service" "truthseeker_web_dev" {
  name     = "truthseeker-web-dev"
  location = var.region

  template {
    containers {
      # Placeholder image; Cloud Build replaces this on each deploy.
      image = "gcr.io/cloudrun/hello"
      ports {
        container_port = 8080
      }
      resources {
        limits = {
          memory = "512Mi"
          cpu    = "1"
        }
      }
    }
    scaling {
      min_instance_count = 0
      max_instance_count = 5
    }
  }

  lifecycle {
    ignore_changes = [template[0].containers[0].image]
  }
}

resource "google_cloud_run_v2_service_iam_member" "public_invoker" {
  name     = google_cloud_run_v2_service.truthseeker_web_dev.name
  location = var.region
  role     = "roles/run.invoker"
  member   = "allUsers"
}
```

- [ ] **Step 2: `terraform/variables.tf`**

```hcl
variable "project_id" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  description = "GCP region for Cloud Run + Artifact Registry"
  default     = "europe-west1"
}
```

- [ ] **Step 3: `terraform/dev.tfvars`**

Replace `<PROJECT_ID>` with your actual GCP project ID:

```hcl
project_id = "<PROJECT_ID>"
region     = "europe-west1"
```

- [ ] **Step 4: `terraform/README.md`**

```markdown
# Terraform — truthseeker-web

## One-time setup

```bash
cd terraform
terraform init
terraform apply -var-file=dev.tfvars
```

After `apply`, populate the secret manually (cannot be put in Terraform):

```bash
gcloud secrets versions add firebase-service-account-base64 \
  --data-file=<(echo -n "$FIREBASE_SERVICE_ACCOUNT_BASE64")
```

Grant Cloud Build access to the secret:

```bash
PROJECT_ID=<PROJECT_ID>
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
gcloud secrets add-iam-policy-binding firebase-service-account-base64 \
  --member=serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com \
  --role=roles/secretmanager.secretAccessor
```
```

- [ ] **Step 5: Run terraform init + plan**

```bash
cd terraform
terraform init
terraform plan -var-file=dev.tfvars
```

Expected: plan shows 4 resources to create (artifact registry, secret, cloud run service, IAM binding).

- [ ] **Step 6: Apply**

```bash
terraform apply -var-file=dev.tfvars
```

Confirm `yes`. Expected: resources created.

- [ ] **Step 7: Populate the secret + grant access**

Follow the README's manual steps.

- [ ] **Step 8: Commit**

```bash
cd ..
git add -A
git commit -m "feat(infra): Terraform for dev Cloud Run + Artifact Registry + secret"
```

---

### Task 21: First Cloud Build deploy + production smoke test

**Files:** none new.

- [ ] **Step 1: Connect Cloud Build to the GitHub repo**

In GCP Console → Cloud Build → Triggers, create a new trigger:
- **Event:** Push to a branch
- **Repository:** the truthseeker-web GitHub repo (connect if not already)
- **Branch:** `^main$`
- **Configuration:** Cloud Build configuration file (yaml or json)
- **Location:** Repository — `/cloudbuild.yaml`

- [ ] **Step 2: Push main to GitHub**

```bash
gh repo create truthseeker-web --private --source=. --remote=origin --push
```

(Or push to a pre-created repo: `git remote add origin … && git push -u origin main`.)

Expected: Cloud Build trigger fires automatically.

- [ ] **Step 3: Watch the build**

```bash
gcloud builds list --limit=1
gcloud builds log $(gcloud builds list --limit=1 --format='value(id)')
```

Expected: build succeeds in 4–7 minutes. Final step (`deploy-dev`) outputs the Cloud Run URL.

- [ ] **Step 4: Smoke test the deployed URL**

```bash
URL=$(gcloud run services describe truthseeker-web-dev --region=europe-west1 --format='value(status.url)')
curl -s -o /dev/null -w '%{http_code}\n' "$URL/en"
```

Expected: `200`.

Open `$URL/en` in a browser → landing renders. Then `$URL/en/signup` → create a real account (real Firebase, not emulators).

- [ ] **Step 5: Verify Google + Apple SSO (real OAuth)**

In Firebase Console → Authentication → Settings → Authorized domains, add the Cloud Run hostname (something like `truthseeker-web-dev-xxx.europe-west1.run.app`).

Then on the deployed URL:
1. `/en/signup` → click "Continue with Google" → complete OAuth → redirected to `/en/app`.
2. Sign out (clear `__session` cookie via devtools), then `/en/login` → click "Continue with Apple" → complete OAuth → redirected to `/en/app`.

Verify Firestore (real project, not emulator) shows user docs created.

- [ ] **Step 6: Commit**

```bash
git commit --allow-empty -m "ops: dev Cloud Run deploy succeeded; Google + Apple SSO verified"
```

---

## Foundation done — exit criteria

At end of Plan 1, the codebase satisfies:

- [ ] `pnpm test` passes (Vitest unit tests + Firestore rules tests).
- [ ] `pnpm tsc --noEmit` passes with zero errors.
- [ ] `pnpm lint` passes.
- [ ] `pnpm dev` runs the app at `localhost:3000/en` with emulator-backed auth working end-to-end.
- [ ] Cloud Build pipeline deploys to dev Cloud Run on push to `main`, and the deployed URL serves `/en` (landing) and `/en/login` (auth form).
- [ ] Google + Apple SSO sign-in works on the deployed dev environment.
- [ ] `users/{uid}` Firestore docs are created on first sign-in.
- [ ] `/en/app/*` redirects to `/en/login?returnTo=...` when the session cookie is missing.
- [ ] Firestore security rules block all client writes outside their allowed surface (verified by Task 8 tests).

Next plan: **Plan 2 — Search engine + eval gate**, which will:
- Capture Python baselines from the existing `deepsearch-service`.
- Port the orchestrator to TS (Vercel AI SDK + Zod + Tavily REST + OpenRouter).
- Build the eval harness with the 14/18 launch threshold.
- Add `/api/search/people-list` and `/api/search/person-detail` routes (initially without quota checks; those land in Plan 3).
