# Transcript — Andrey / Filippo Weekly 1:1 — 14 September 2026, 15:30 CEST

> **Source:** Granola — Filippo's personal note-taking tool, not a company recording.
> **Omitted:** a short exchange near the start in which Andrey mentioned his external job
> search is left out of this file as ordinary discretion, not because anything went wrong.

---

**Filippo:** Good morning. Good morning. Sure, it's definitely morning.
**Andrey:** Somewhere.
**Filippo:** Yeah, sure. How are you doing, Andrei?
**Andrey:** Yeah. I'm doing well, and you?
**Filippo:** Yeah, I'm okay. Pretty busy, I would say, but that's the job in general.
**Andrey:** Mm-hmm. Yeah.
**Filippo:** I'm trying to move things forward with TraceCheck and clean up a bit of the backlog for a lot of other things, but it's fine. There's some work to be done in general. What about you?
**Andrey:** Um, I got access to Kilo again, so I'm happy and work. Basically.
**Filippo:** I really hope they're going to find a way to solve this. Because you cannot block the full company in this way. Absolutely not. It's out on my end. Let's see. I know that they are working with finance and they're working with Kilo as well. So let's hope this is not gonna happen anytime soon ever again.

*[— short personal exchange omitted —]*

**Filippo:** Andrei, I need two major things from you this week.
**Andrey:** Yeah.
**Filippo:** The first thing is something that hopefully you can close today because Matellano is asking me every day pretty much. Firestore ruleset, can you update them?
**Andrey:** I've updated it on dev for iMote and we'll update with the production release of 2.6.4 for production. So does it have to be like immediate even though we don't do it early, or?
**Filippo:** Is it related to a release somehow? Do we need to do an app release?
**Andrey:** Not particularly, just I figured we do the regression with the whole thing.
**Filippo:** Okay. So let's do like this. For some weird reason, iMote is not a priority in this case because the security team didn't flag specifically iMote, but they flagged Screen Mirroring.
**Andrey:** There's not much there, yeah. Okay.
**Filippo:** So could you release to production Screen Mirroring rules?
**Andrey:** I can, yeah.
**Filippo:** That would be great, so we can close that. And then when you do the full production release in iMote, I agree, it's better to do a regression in that sense.
**Andrey:** Yep, okay. I'll do that now.
**Filippo:** Thank you. That would be absolutely great. So Matellano is happy and he can put another check mark in his spreadsheet.

**Filippo:** Couple of things that I wanted to share with you in general. I opened a ticket to SRE so that the whole triggering to deploy the website is ready. I don't know when they're gonna do it. Hopefully this week. I'm gonna try to push for it. How are you doing with the new changes for the website?
**Andrey:** I haven't implemented them — I was kind of waiting on us to do the setup for development, production, and then start iterating a bit more.
**Filippo:** Random question: considering that they provided us the full HTML, is this something that we can simply use as it is, or do you want to run it through an LLM to sort of export it in a better way?
**Andrey:** I would run it through an LLM just in case, for things like mobile support. And anything else that might be.
**Filippo:** Yeah. Because another point that I am expecting, even though no one thought about it, is that — great, we have a landing page. But if we don't put any tracking around this, what is the point of having it?
**Andrey:** Okay. Yeah.
**Filippo:** So tomorrow I'm going to ask Herman if they thought about this part and let's see where we are at.
**Andrey:** Screen Mirroring is deployed.
**Filippo:** Nice. Great. Thank you, Andrei. Thank you. Am I right in understanding that Herman is going to be moving away from iMote from this week?
**Andrey:** Yes, Friday is his last day.
**Filippo:** Okay, so we're gonna deal with David Martos directly. That's gonna be fun. It's gonna be very fun.
**Andrey:** Or like a month.
**Filippo:** Let's see how he's gonna plan things. Kind of a bit worried about that.

**Filippo:** What else? iMote-wise, Victor is going to deploy hopefully tomorrow a new version of the MartechKit and it contains Braze integration.
**Andrey:** I think Vlad wrote about it today. But that one doesn't have Braze.
**Filippo:** No, that one no — so we are gonna release that today for MartechKit, feel free to update, but in the next couple of days we're gonna release. So I'm really excited about that. I'm expecting it to be working fairly okay.
**Andrey:** Okay. Great. Yeah.
**Filippo:** And to close the round on iMote. We need to start to plan some sort of handover. From you to Victor. What do you think would be the most important things to transmit?
**Andrey:** Well, the hardest thing about the project is basically working with the TVs and how that's structured. So probably something around that.
**Filippo:** So a full session regarding TV Foundation Kit. But also a sort of way for you to show Victor how you actually debug with the TVs themselves.
**Andrey:** Yeah.
**Filippo:** Okay. I'm gonna take a note here because I think we should organise this. In the next few weeks. TV Foundation. Anything else that comes to mind?
**Andrey:** Um, no, not really.
**Filippo:** I know you have some automation regarding Jira opening tickets for Crashlytics.
**Andrey:** That's just plugged into — yeah, we need to change out the token, basically the JWT token.
**Filippo:** Because it is using yours, basically.
**Andrey:** Yeah.
**Filippo:** Okay, one second, let me take that. Anything else that comes to mind related to this?
**Andrey:** Hmm. No — he'll have access to the TVs. When should I ship them out? It'll be like in October.
**Filippo:** Later. You were working with the regression for TV Foundation Kit. Is that live?
**Andrey:** No, no, it's us. It's just back and forth fixing issues with the QA team.
**Filippo:** Any idea on when this can be?
**Andrey:** A bit tricky because it's like you send out the build and you find new things, so it's hard to pin down, but probably like a couple weeks. At most.
**Filippo:** Would be great if you can get this out before you leave. That's my idea.
**Andrey:** Yeah.
**Filippo:** Anything else on iMote-related stuff?
**Andrey:** No, nothing I can think of.
**Filippo:** You have releases planned?
**Andrey:** I will do 2.6.4 now. Fairly soon — I don't know, with Herman leaving and David coming up, how that's going to work exactly, but yeah, that's the idea. Basically, who decides when you release?
**Filippo:** That's up to them. Nothing up to us. I can see that for next sprint, there's Braze, trial ads, rebranding. So Marta sent me a message today regarding changing fonts for the new rebranding. How hard is that?
**Andrey:** Um, not sure. Probably not a lot.
**Filippo:** Because if we did the things right, it should take one line of code, but we didn't do the things from scratch, you know? Theoretically, it should be pretty straightforward.
**Andrey:** No, we haven't. No, it's not.
**Filippo:** Okay, shit. All right, thank God we have LLMs though. That should be quicker in that sense.
**Andrey:** Yeah, that will help. And make it better.
**Filippo:** Speaking of LLM, are you still using GPT-5? Any other?
**Andrey:** I'm using DeepSeek, the new one they released the other day on Thursday, seeing how it's working. Supposedly it's just about as smart as the others, but way cheaper. So yeah, we'll see.
**Filippo:** Okay, let me know. I'm curious. I'm slowly starting to use Kilo Code myself. And so far I'm not really happy with the results.
**Andrey:** Which one are you using?
**Filippo:** I'm trying a bit of GLM, a bit of Kimi. But Kimi I find very slow.
**Andrey:** If you're used to Fable, then—
**Filippo:** I'm used to Opus in general. I use Fable not that much, but Kimi is so slow, so damn slow. It's like, seriously?
**Andrey:** That's why I leave it working overnight. But it does consider a lot of things.
**Filippo:** Does it? Results are good?
**Andrey:** Yeah. So on Thursday I gave it the issue — we had some issue. I gave it both to Kimi and to DeepSeek, and DeepSeek was pretty quick but didn't really dig into things. Whereas Kimi worked until it figured it out. It was the Parapet issue that we had.
**Filippo:** Yeah.
**Andrey:** DeepSeek said there's an issue with Parapet, contact them and—
**Filippo:** Go and figure it out.
**Andrey:** Yeah.

**Filippo:** Okay, good. So let's move to the big one, which is TraceCheck. What's the state there? Because I see you have plenty of PRs open. There's still tickets in review. What's the state?
**Andrey:** I'm going through some tickets on Thursday and today. Most of today. I wasn't able to have things run on it, but now I'm going through the tickets, resolving any issues, merge conflicts, things not building. And looking at the design iteration on some of the things, like for example on the 501. It made some changes, but the changes that it made have issues if you go in and look at them. So I'm trying to make it so that it doesn't have issues. And slowly but surely it's getting there. And there's the search not working for emails, currently on dev, that Maria reported — and basically turns out we were missing an implementation.
**Filippo:** What?
**Andrey:** What it said was that one of the PRs said that it will do the implementation in a later PR and then we never did it. So I'm not sure how that happened. I wasn't the one that— well, yeah, I don't know.
**Filippo:** But I tested it. I tested it. It was my PRs, I guess.
**Andrey:** Probably. It's 409.
**Filippo:** It's very weird. Okay.
**Andrey:** And the PR says that we need to implement this in a later PR.
**Filippo:** Okay. That's on me then.
**Andrey:** And it wasn't. So we do.
**Filippo:** Do you think you can close these tickets by tonight?
**Andrey:** Sure, yeah.
**Filippo:** If you cannot, let me know and I unleash some agents myself.
**Andrey:** Do I get to close things, merging things as an admin, or—
**Filippo:** Yeah, go for it. Go for it. You need to do it through the GitHub interface.
**Andrey:** I'll leave out the Braze and the aliases, right?
**Filippo:** Yeah, correct. So those two, leave them out. There is a draft PR that I'm going to talk to you about right now. All the rest is yours. Feel free to merge if you think it's good enough.
**Andrey:** Okay.
**Filippo:** And for me — UI stuff, for me and for Alex, UI stuff are low priority.
**Andrey:** Okay.
**Filippo:** The second priority thing — well, the first one you've already done, which was Screen Mirroring. The second priority thing is this pricing A/B test for TraceCheck. I've done some technical discovery and I talked to Thiago, which is a staff engineer in web. The idea is to use Amplitude — they have a web framework that we can use, and that carries metadata.
**Andrey:** Okay.
**Filippo:** So the plan is to get the CRO team, Vlad and his team, to put into the metadata of the variants that are configured in Amplitude Web Experiments, to use the Parapet product ID. So we are gonna create two products with the same kind of pricing — the only difference will be the duration of the product itself. And the A/B test will carry as metadata the product ID, so that Amplitude will dispatch, to whatever variant your user is in, the actual product ID that they need to use. The change is gonna be that the backend will still need to read the Parapet IDs of the products to make sure that we are retrieving the right ones, but then only uses the one that is carried by the Amplitude experiment variant. And this is, in my opinion, the most complex logic.
**Andrey:** Yeah.
**Filippo:** All the rest, it's mainly UI. So wherever we mention pricing, wherever we mention duration for the trial, whatever we mention — this kind of thing must be dynamic and driven by this variant that the Amplitude experiment sends us. That's it. I created a draft PR that doesn't contain any code — I created it to brainstorm with Claude pretty much. It contains the sort of plans and a few other documentation thingies. Feel free to use it or not. I'll leave it to you. I don't mind, honestly. You can close it and start your own, but it carries the sort of business logic that I was discussing with Claude about.
**Andrey:** Yeah.
**Filippo:** Tomorrow we're gonna kickstart a new sprint and you will find all the user stories there.
**Andrey:** Perfect.
**Filippo:** It is extremely important that we deliver this in production by Thursday. So that is why, whatever cosmetic thing you're finding with emails, I don't care.
**Andrey:** Okay — you said this Thursday, right?
**Filippo:** Yes, it's this Thursday. I don't think it's a big, big change because it's about making labels dynamic pretty much. So let me know. If you're going to start to work on this tomorrow, I'm hoping that by tomorrow evening you already have something that you can start to play with. If not, let me know and we can start to tame expectations. Let's put it like this. Mainly because this is coming from Herman, the big boss, and so we want to get this done in a decent way.
**Andrey:** Okay.
**Filippo:** What else? Not much. Things are moving. We are slowing down with the amount of things to do in TraceCheck — not because we don't have the capabilities to go faster, it's because we need to deliver things with good quality in general. And then what I am trying to do from next sprint on is to try to make production releases smaller, so we can iterate faster, because right now this email thing is a huge block and it's just taking too long, to be honest.
**Andrey:** Uh-huh.
**Filippo:** That's it. Anything else, Andrei, on your end?
**Andrey:** Nope, nothing comes to mind.

**Filippo:** Let me check my notes. Two points. Vlad — you've seen Vlad coming in this morning. He is gonna take your place when you leave. And I already started to talk to him regarding his onboarding plan. He has some other things to do to close with MartechKit and AI Design before moving to this project. So the next few weeks he's going to mainly read documentation. But my plan is to start to get him to do small features from the first week or so of October and try to get him completely up to speed and independent by the end of October, when you leave.
**Andrey:** Sounds good.
**Filippo:** So I may need to ask you in the future to have a couple of sessions with him regarding specific points, but I'll let you know. There is no rush right now. He is going to go on holiday at the end of this week for a few days, so it's going to be moving later on.
**Andrey:** Okay.
**Filippo:** That is the thing regarding org. We are trying to hire a proper full-stack engineer. And I can tell you that the hiring part is very hard because nowadays you can fake your CV perfectly. So we have no way to filter out bad candidates before the first interview step. And what we are receiving and actually interviewing is a lot of execs — like lead managers, CTOs — interviewing for hands-on coding roles. It's gonna take a while. Unless we are super lucky, which you never know.
**Andrey:** Yeah.
**Filippo:** That's it. Anything?
**Andrey:** No, nothing on my end as well.
**Filippo:** Andrei, have a great day. Let me know if I can help with coding or anything. If you have questions regarding this A/B test, if you need to discuss anything, let me know.
**Andrey:** Of course, yeah. Probably tomorrow, as we get the stories and whatnot.
**Filippo:** Yep. Have a great day.
**Andrey:** You too. Bye-bye.
