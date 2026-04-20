# GitHub Repository Rules Collection Guide

## Purpose

This spreadsheet collects requirements for Terraform-managed GitHub repository configurations across different repository types.

## Repo Types Defined


| Type                 | Description                         | Examples                               |
| -------------------- | ----------------------------------- | -------------------------------------- |
| **Mobile Apps**      | Customer-facing mobile applications | iOS/Android apps in stores             |
| **Web Apps**         | Customer-facing web applications    | Web portals, customer dashboards       |
| **Internal Tools**   | Internal engineering/support tools  | Admin panels, CLI tools, scripts       |
| **Shared Libraries** | Reusable code packages              | npm packages, Swift packages, SDKs     |
| **Infrastructure**   | IaC and platform configurations     | Terraform, CloudFormation, K8s configs |


## How to Use This Spreadsheet

### Step 1: Review Each Category

Go through each section with your team:

- Repository Basics
- Branch Protection
- Access & Teams
- Actions & CI
- Security & Secrets
- Code Quality
- Notifications & Automation
- Merge Requirements
- Special Features
- Compliance & Audit
- Archival & Lifecycle
- **Required Workflows** (NEW - specific GitHub Actions to enforce)
- **Workflow Settings** (NEW - Actions configuration details)

### Step 2: Fill in Values

For each setting, fill in the appropriate value for your repo type:

- Use `TRUE`/`FALSE` for boolean settings
- Use descriptive values for team names (e.g., `Mobile-Devs`)
- Add notes in the "Description/Notes" column

### Step 3: Indicate Priority

Mark each setting as:

- **High**: Must be implemented
- **Medium**: Should be implemented
- **Low**: Nice to have

### Step 4: Submit to SRE

Once completed, share the spreadsheet with the SRE team for Terraform implementation.

## Key Terraform Resources to Reference

When SRE implements these, they'll likely use these Terraform resources:

```hcl
# Repository configuration
github_repository

# Branch protection
github_branch_protection

# Repository rulesets (newer alternative)
github_repository_ruleset

# Team access
github_team_repository

# Actions configuration
github_actions_repository_permissions

# Required workflows (org-level)
github_actions_organization_required_workflow

# Reusable workflows (referenced by individual repos)
# Stored in central repo, referenced via `uses: org/.github/.github/workflows/...`

# Workflow files provisioned via Terraform
github_repository_file

# Environment protection
github_repository_environment

# Security features
github_repository_dependabot_security_updates
```

## Common Settings Explained

### Branch Protection Must-Haves

- **Require PR Reviews**: Prevents direct pushes to protected branches
- **Required Status Checks**: Ensures CI passes before merge
- **Require Up-to-Date**: Prevents merge conflicts

### Actions Security

- **Allowed Actions**: Control which third-party actions can run
  - `All`: Any action from GitHub Marketplace
  - `Local Only`: Only actions in `org/repo/.github/workflows`
  - `Verified Only`: Only verified creator actions
- **Token Permissions**: Default `GITHUB_TOKEN` permissions
  - `Permissive`: Read/write to most resources
  - `Restricted`: Read-only by default

### Security Scanning

- **Secret Scanning**: Detects exposed secrets in code
- **Push Protection**: Blocks commits containing secrets
- **Dependabot**: Automated dependency updates

## Required Workflows Explained (NEW)

The spreadsheet now includes a section for **specific GitHub Actions** you want in every repo.

### Workflow Types


| Value             | Meaning                                                               | Terraform Implementation                  |
| ----------------- | --------------------------------------------------------------------- | ----------------------------------------- |
| **Required**      | Workflow must run on every PR (cannot be skipped)                     | GitHub Required Workflows or org rulesets |
| **Optional**      | Provided as reusable workflow, repos opt-in                           | Available in `org/.github` repo           |
| **TRUE/FALSE**    | Workflow file should exist (enforced via Terraform file provisioning) | `github_repository_file` resource         |
| **Specific path** | Exact workflow file path (e.g., `.github/workflows/ci.yml`)           | Document in SRE Notes                     |


### How to Document Your Required Workflows

For each workflow in the spreadsheet, specify:

1. **Workflow Name** - Descriptive name (e.g., "PR Checks", "Security Scanning")
2. **Value per Repo Type** - Required/Optional/TRUE/FALSE
3. **Source Location** - Where the workflow file lives (e.g., `org/required-workflows/.github/workflows/pr-checks.yml`)
4. **Triggers** - When it runs (`push`, `pull_request`, `schedule`, `workflow_call`)
5. **Required Status Check** - If it blocks merges (must match `Merge Requirements` section)

### Example Workflow Specifications

```yaml
# Example: Security Scanning (Required)
Source: org/required-workflows/.github/workflows/security-scan.yml
Enforcement: Required (runs on all PRs, cannot be disabled)
Triggers: pull_request
Required Check: security/scan
Applies to: All repo types

# Example: Deploy Pipeline (Type-specific)
Source: org/.github/.github/workflows/deploy.yml
Enforcement: Reusable workflow (repos reference it)
Triggers: workflow_call
Required Check: N/A (optional)
Applies to: Infrastructure repos only

# Example: Performance Tests (Customer-facing only)
Source: Terraform-managed file in each repo
Enforcement: TRUE (file must exist, content from template)
Triggers: pull_request
Required Check: perf/regression
Applies to: Mobile Apps, Web Apps
```

### Central Workflow Repository Structure

SRE should create a central repository (e.g., `your-org/.github` or `your-org/required-workflows`):

```
org/.github/
├── .github/
│   └── workflows/
│       ├── reusable-ci.yml           # Reusable workflow template
│       ├── reusable-security.yml     # Reusable security scan
│       └── required-pr-checks.yml    # Required org workflow
├── workflow-templates/               # Starter workflows
│   ├── mobile-ci.properties.json
│   └── mobile-ci.yml
└── templates/                        # Terraform templates
    ├── mobile-workflows/
    ├── web-workflows/
    └── library-workflows/
```

### Connecting to Required Status Checks

The `Required CI Checks (list)` setting in the **Merge Requirements** section must match the workflow names in this section:

```
Required Workflows: PR Checks (Required)
↓
Workflow publishes status: "ci/test", "ci/lint", "ci/build"
↓
Merge Requirements: Required CI Checks = "ci/test ci/lint ci/build"
```

### Common Workflows to Consider


| Workflow                   | Purpose                              | Recommended For          |
| -------------------------- | ------------------------------------ | ------------------------ |
| **PR Checks**              | Test, lint, build on every PR        | All repos                |
| **Security Scanning**      | SAST, secret scanning                | Customer-facing repos    |
| **Dependency Check**       | Vulnerability scanning               | All repos                |
| **License Compliance**     | Verify dependency licenses           | Open source libraries    |
| **Code Quality Gate**      | SonarQube/code coverage              | Apps and libraries       |
| **Release Automation**     | Auto-create releases with changelogs | Published libraries/apps |
| **Deploy Pipeline**        | Deploy to environments               | Infrastructure repos     |
| **Stale Issue Management** | Auto-close old issues/PRs            | All repos                |
| **Performance Regression** | Performance benchmarks               | Customer-facing apps     |
| **Accessibility Scan**     | a11y testing                         | Web/Mobile apps          |


## Adding New Repo Types

If your organization needs additional repo types:

1. Add a new column to the spreadsheet
2. Define the characteristics in this guide
3. Fill in appropriate values for each setting
4. Examples: `Documentation`, `Experiment`, `Contractor-Project`

## Questions for Discussion

Before finalizing, consider:

1. **Should all repos have the same CODEOWNERS requirements?**
  - Apps: Likely yes (product ownership)
  - Libraries: Yes (maintainer accountability)
  - Internal tools: Maybe optional
2. **How strict should CI requirements be?**
  - Customer-facing: Strict (e2e tests required)
  - Internal: Flexible
3. **Who approves emergency hotfixes?**
  - Consider "break glass" procedures
4. **Should we enforce commit signing?**
  - High security environments: Yes
  - Most teams: Probably not (friction)
5. **Merge strategies?**
  - Squash: Clean history (recommended for most)
  - Merge: Preserve full history (libraries)
  - Rebase: Linear history (purist preference)

## SRE Handoff Checklist

Before sending to SRE:

- All columns filled for your repo types
- Priorities marked (High/Medium/Low)
- Team names verified (exist in GitHub org)
- Required status check names confirmed (match CI config)
- Reviewed by at least 2 EMs or Staff Engineers
- Document any exceptions or special cases in "SRE Notes" column
- **Workflow-specific items:**
  - Workflow source locations documented (which repo contains each workflow)
  - Required workflows vs reusable workflows clearly distinguished
  - Workflow trigger events specified (push/PR/schedule)
  - Required status check names match workflow job names
  - Any workflow inputs/secrets documented
  - Central workflow repository name decided (e.g., `org/.github`)

## Post-Implementation Verification

After SRE implements the Terraform:

- Create test PR to verify branch protection rules
- Verify team access levels in GitHub UI
- Check Actions permissions are applied
- Confirm security features are enabled
- Test CODEOWNERS enforcement
- **Workflow verification:**
  - Required workflows appear on PRs automatically
  - Reusable workflows can be called from repo workflows
  - Workflow status checks appear in branch protection
  - Workflow files exist in repos where specified
  - Workflow permissions are correctly configured
- Document any deviations from the spec

