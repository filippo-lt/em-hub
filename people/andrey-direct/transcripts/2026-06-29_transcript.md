Jun 29, 2026

## Andrey / Filippo — Weekly 1:1 — Transcript

*Source: Granola (auto-generated). Speaker mapping: **Me = Filippo Tosetto**, **Them = Andrey Marinov**. First 1:1 since Andrey's return from holiday (off 19–29 June).*

---

**Them:** Hello.

**Me:** Good morning Andre. How is Greece.

**Them:** Pretty good.

**Me:** Like the rest of Europe is on fire pretty much. But at least you were close to the sea I guess.

**Them:** Oh, yeah. On the beach. And every day. Couldn't get the little one out of the cart because she only cried. So her mom and she only stayed in the room the whole time.

**Me:** How was it with the young one?

**Them:** She's very much crying and she's a little one. So you can't really put her further out in the sun or anything like that. That was kind of expected.

**Me:** You got a holiday and your wife didn't pretty much.

**Them:** I wouldn't say a holiday. There is this concept that when you have kids, you're not going on a holiday. You're going on a trip. There is a big difference.

**Me:** Fair point. Makes sense. Have you rested a little.

**Them:** Let's say so. Yeah.

**Me:** Well that's what I'm very much looking forward to very soon. And when I say very very soon, in six weeks.

**Them:** That's still quite far off.

**Me:** Yeah it's far off. Where I am the temperature is insane, last week reached 36-37 and even with AC you can't leave. At least you were close to the sea. Okay so Andrei. What happened while you were away? A few good things. For once Kilo code should be available for you so you can play with it.

**Them:** Check it out.

**Me:** I have mixed reviews so far.

**Them:** Mixed reviews. Okay.

**Me:** There is a clear misconception on what cheap models can do. But hey, they are cheap so what do you expect. I'm curious to hear your review in a week or so.

**Them:** Good news about the new model. The new open one, 5.2. Have they tried that out?

**Me:** I don't know because I don't have access to kilo code. If you have access, have a look. If that's the case you have a smart model, maybe not as smart as gpt 5.5 or opus 4.8 but good, that you can outsource at least the coding part. Let me know, I'm very curious.

**Them:** Same here. Actually I started looking into running it locally. You need like four graphics cards, at least half a terabyte of RAM. It adds up — about six to eight thousand euros. And then you run it with seven tokens a second.

**Me:** Seven tokens a second. It's nothing — roughly two-three words a second.

**Them:** If you run it 24/7. It's still cheaper to put that 8,000 into whichever frontier model subscription — you have a better payout.

**Me:** Speaking of frontier models, are we going to have in Europe those new models from open AI. For now we have 5.5 and opus 4.8.

**Them:** For now. Yeah, that's the other thing, they can take away your local geo any way. There is also cool stuff where you can jailbreak the model to find out what happened in certain places in China — it does know it, they just put in safeguards. You can bypass that. You get more freedom if it's local — it'll let you write a scraper or bot stuff a hosted model refuses.

**Me:** This is how they do model distilling, to steal models.

**Them:** No, that's another thing where they get the response and figure out the weights.

**Me:** How do you know these things.

**Them:** Online, looking at blogs and reading. As much as I don't like X, it's pretty much where everything is up to date.

**Me:** It is true. Everyone is on X anyway. Okay let me take a look at my notes. So Andrei, before I jump into the big topic which is obviously Truth Seeker, do you have any news on iMode?

**Them:** Yeah, before I went on vacation I implemented the functionality. There were comments and issues from Alexi while testing. I'll be taking care of those. We're looking to do a regression by end of the week. And on the Android side, Google came in with some warning — something regulatory. So that's the big thing, how to fix the trust manager library. There's a hotfix we need to push through. That'll be the focus. There is the Martech PR for iMov Android. I saw it implemented. We were wondering what to do about that.

**Me:** I created that chat with him and Victor. I just need him to go through it — literally a peer review.

**Them:** No, he asked whether that's priority, when do we merge it in, and I didn't know. I also have the same open on iMod iOS — a PR I have not merged because I don't know when we want to push it out. Granov said you'd look into it.

**Me:** Wait, you have a PR in iMod iOS regarding market kit? Can you share it with me? Who integrated that — you did? It's great, thank you.

**Them:** It's like three weeks ago. I didn't know when we want to release it, so it's been sitting.

**Me:** Whenever you guys are ready honestly. Let me give you an overview of the Market Kit situation. iOS is already released in a few apps and works, so whenever you have time, merge it back and release it — make sure everything works because we'll break marketing otherwise. We are actually releasing a hotfix today for Market Kit iOS, so before doing the merge I'll ping you when it's done so you can upgrade to 1.2. Regarding Market Android — iMode Android is the first app where we introduce that, so I'd want Slob to spend a bit more time making sure everything works, since Victor doesn't know Android. Then we merge and monitor the release. Martech is becoming a priority — we have a few things open on the Martech side and this library lets them handle everything; we just upgrade the SDK version. The more apps we have it integrated, the better. Am I right that you started the foundation kit integration as well?

**Them:** I remember asking Herman when we want to do that before my break. He said first we push out the tiered stuff, then we get to it. We have a PR but I need to do a lot of testing.

**Me:** Okay. Sounds good. Anything else on iMode? Am I right that Herman goes on holiday for three weeks mid-July?

**Them:** Yes. Herman starts on the 13th of July, three weeks. And the 27th of July, Lexi starts, four weeks.

**Me:** So we're going to have iMode completely out of testing for a month — middle of July to end of August.

**Them:** Yeah.

**Me:** Well, August is a bit of a flat month anyway. Let's try to get something stable out and not touch anything else.

**Them:** Yeah. Also the seven-hour workday.

**Me:** Oh, starting tomorrow, Wednesday?

**Them:** Get an email, something like that.

**Me:** Nice, that's good. Okay let's talk about the big priority — Truth Seeker web. Good news. I'm going to share my screen. This is the doc website I created, a status file with everything done and still missing. I spent a lot of time coding last week which was fun, and I burned through a lot of tokens but didn't finish them all, which is interesting. Things completed: we now have a dev version live at dev.truthseeker.com — you should have access. Stripe and Parapet are fully integrated. A user can subscribe, has a limited quota, can buy tokens — all connected to Stripe and Parapet. You can change quota, see users, buy, refund subscriptions. Payment setup, card, subscription, premium granted, spend token and lookup — all done. I had to fix a couple of bugs in Parapet myself — I've never written any Go in my life, but now I do. There's one pending item: add-ons — the PDF download add-on and future one-offs. Today Parapet can't sell a one-off product granting a lifetime entitlement. I'm working on adding it — not a blocker for you, I have the conversation with Durban open.

**Them:** Okay.

**Me:** What needs doing this week — design. We finally have a design. When you have access to the Figma file, have a look; everything for the home screen is confirmed. All the data there is fake. If you can start implementing this, great. A couple of points: we only have phone today; we could enable email later, so for now hide those tabs behind a remote configuration flag. Second, all the copy — the site is English only for now, multilingual in the future. Is there a way to have this modifiable by product people? The easiest thing I thought is Firestore, but for product people that might be complex. I leave it up to you — English first, but if you think of a solution to make it multilingual, your call. Also, each module — hide them behind feature flags as well, remote config. And the home screen with the legal part: we need it to open a real Stripe account. I created one with my personal email and it works, but for the official one we need the home screen with the main functionality hidden, the paywall hidden, and a link to the terms of service. Then Stripe can approve us and I redo the wiring of Parapet and Stripe from scratch. If we get this done by end of this week, that'd be great.

**Them:** [acknowledges]

**Me:** Also — this is a website but we expect 90% of our user base to be mobile, so focus mainly on the mobile design, an infinite scroll. That's the home screen. This is a loader — flow already implemented, just needs a fake loader. On lookup: when a user looks up a phone, we only trigger the carrier search first (super cheap), show that, then they buy via the paywall and we unlock everything. There's a fake animation while we pretend to work. I want to confirm this tomorrow in the product sync. Then the full report page — today we don't have all this info. What Self-Aware suggested is doing loops: get the first round, rerun the APIs to get more. I need to look at the endpoints. We're not loading pictures yet, maybe we want to. Download report downloads the PDF — wiring done, needs to look better. There's a debug menu at the bottom right: you can place yourself in different countries, do mocks, and a provider-row view that shows the full JSON response live. On top you see premium / non-premium and credits left, all wired live to Parapet. Use the Stripe test card 4242 4242, future date, any code.

**Them:** So where do you press again?

**Me:** Bottom right. In terms of timeline we're in a really good position. This week we enter the UI and wiring part, the UX. I'm hoping it's much faster than the previous one since the technical logic is sorted — but I don't want to give too much hope.

**Them:** Where people come in slower?

**Me:** Yes. Two more points. I'm pushing product and legal for answers — the legal questions I had almost a month ago have no answer yet. And the current lookup APIs don't give us everything we want, so I may need to spend time researching other providers. This is a priority project, and as usual engineering is doing things and product is slow. Also, Oscar will join us on testing before becoming full part of the team — this week he's working with us technically, preparing Gherkin files with all test cases so we wire them and make sure everything works, bypassing Jira. You have access to everything?

**Them:** Yeah, I think so.

**Me:** Can I invite you?

**Them:** No no, I was joking.

**Me:** You have access to Parapet though.

**Them:** Thank you.

**Me:** That's the important part, so you can see things happening. I think that's it on Truth Seeker. Anything else on your end? We talked about iMode. Despite what Herman wants, I'd try to split your time 70% web Truth Seeker, 30% iMode. Do you think that makes sense, or do you have much more to do in iMode?

**Them:** No, no.

**Me:** Okay. In that case I think I'm done. Oh — I saw your agents doing something while you were off, opening Jira tickets.

**Them:** I had tokens to burn. There's tech debt to be resolved in iMode. I set it to work.

**Me:** Just go and burn some tokens. Nice, well done. I really like that automation by the way, the Crashlytics-to-Jira part.

**Them:** Yeah, we got a bunch of stuff. I have to look through.

**Me:** Thanks Andrei. Have a good day, have a great week, and let me know anything you need for Truth Seeker — maybe API keys I forgot to send. Just ping me.

**Them:** Thank you.

**Me:** Have a good day, bye bye.

---

*This transcript was computer generated (Granola) and may contain errors.*
