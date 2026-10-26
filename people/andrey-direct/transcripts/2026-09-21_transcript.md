# Transcript — Andrey / Filippo Weekly 1:1 — 21 September 2026, 11:30 CEST

> **Source:** Granola (meeting id `91ecc318-bfa9-484b-a5f1-d3a5b16bda2b`) — Filippo's personal
> note-taking tool, not a company recording.
> **Cleaning:** Granola splits speech into fragments; consecutive fragments from the same speaker
> are merged. Obvious ASR errors normalised: "iMode/iMOD/Emote/IMO" → iMote, "Praise" → Braze,
> "Julian/Julen" → Julen (SRE), "Plymouth website" → iMote website, "$15.99" → 1599,
> "Market Kit" → MartechKit. Garbled fragments marked *[unclear]*. Otherwise verbatim.

---

**Andrey:** Um, Monday-ish.
**Filippo:** Yes.
**Andrey:** Love. Thanks. I'm a bit sick as well. Not that good.
**Filippo:** Okay, let me, let me close the window because it's freaking noise. Sorry.
**Andrey:** Do you hear something from me? I have my fan going. Is it audible?
**Filippo:** No, no, I can hear you fine. No worries.
**Andrey:** I hope— let me know just in case.
**Filippo:** What? Who? There was no noise at all on your end. It was more here. Because I have a park in front of my— of the window, and there are kids literally screaming constantly. So yeah.
**Andrey:** I'm used to that, can't scare me there.
**Filippo:** Yeah, I know, I know. You and your kids, you people having kids, and I can, yeah, I can understand. You get used to it a bit.
**Andrey:** Oh yeah, it's background noise.

**Filippo:** Andrei, how's everything going?
**Andrey:** Ah. It's going okay. Progressing things along, just got some reports from Alex on stuff, so kicked off fixing those. On iMote, we are just about done with the iMote integration. I know that you said that Victor has that done somewhere, but he doesn't have a PR open and I don't see where. My agent just did it, so—
**Filippo:** Okay, okay, one sec. So first of all, A/B test done, well done. Record timing. Herman is super happy. This is a problem. The fact that we managed to deliver this in less than a week. They're going to expect us to keep delivering at this level. And while you're around, it's okay. When you're going to not be around anymore, that's going to be a bit of a problem, but that's on us.
**Andrey:** I know a really easy way to fix that.
**Filippo:** Yeah, I know as well, I know as well, but it's out of my hand.
**Andrey:** Well, tell Herman, maybe he knows someone who knows someone.
**Filippo:** Hi. Um, hi. Yeah. Yeah, Andrei, I can't do anything about that. And Friday's conversation— was it Friday, Thursday last week?
**Andrey:** Yeah. Uh, Thursday.
**Filippo:** Whatever. Was about making this official in general. Um.
**Andrey:** Yeah. I'm just joking.
**Filippo:** Yeah.

**Filippo:** What else? Regarding TraceCheck, I think the only thing that is missing for you to work on this week, besides Alex coming with fixes, get the Spanish out, get the landing page out, and for you, TraceCheck this week should be okay. Um, and I think you're pretty much there with everything.
**Andrey:** Yeah.
**Filippo:** Good. Very good. Why am I saying this? Because I need you to work on iMote website. I'm very interested to know if and how you're interacting with David Martos.
**Andrey:** I have not interacted with him at all.
**Filippo:** So who's running the dailies?
**Andrey:** There are no dailies at the moment.
**Filippo:** So we are not going to do dailies anymore.
**Andrey:** I don't know. I haven't talked to David. Basically, Herman canceled the dailies last week, because he was the organizer, and I guess David Martos doesn't want to have dailies. He did like post some things in the ML chat today about Braze, and that's about as far as I've talked with him.
**Filippo:** Oh man, this is gonna be a nightmare. I'm gonna have a ketchup *[catch-up]*.
**Andrey:** Only for like a month.
**Filippo:** Sorry?
**Andrey:** Only for like a month then.
**Filippo:** Free.
**Andrey:** Not as much for me.
**Filippo:** I'm gonna have a one-to-one with him tomorrow. I'm gonna start to sort out this part. So the fact that we remove dailies, for me, it's a problem.
**Andrey:** Yes. What? It might not be so much as he's removed them as much as he hasn't set them up yet. So.
**Filippo:** I'm gonna have a chat with him.
**Andrey:** Mm-hmm. And also dailies is probably a bit too much with Herman. We didn't really have enough content for dailies. So maybe like every other day or 2, 3 times a week.
**Filippo:** What kind of interaction did you have with Herman during these dailies?
**Andrey:** Be better. Oh. It's mostly looking at the board and the board isn't like updated a lot, so. Going through things over and over. There were more things on the Android side as well, but now that the other staff is working on Martech, there weren't a lot of things on Android as well. I've basically approved one PR for Android for like the past couple of weeks. So there's not a lot going on there as well. And yeah.
**Filippo:** No, because I agree with you. There is not much things to do in iMote.
**Andrey:** No.
**Filippo:** So it's not worth to keep 15 minutes every day there, if nothing is happening. Agree.
**Andrey:** Yep.
**Filippo:** But at the same time, there are requests and we need someone from product to handle those requests. It's not that magically engineering decide what to do and how to do it and magically we get all the information. Okay, I'm gonna have a conversation with David tomorrow and it's gonna be a nice conversation. Okay.

**Filippo:** Said that. iMote website. So the one that was vibecoded by David Martos.
**Andrey:** Yep.
**Filippo:** The problem is the following. I'm going to give you a bit of a rundown of the situation. Today we have in imot.app, we have marketing campaigns running.
**Andrey:** No.
**Filippo:** It's an auto-generated website with a single page where all the campaigns link to. If we set up the deployment Terraform through SRE, so the usual one that we have in TraceCheck where by pushing to dev, it will deploy to dev.imot.app, then, etc., into main, to the live website, we are gonna break all the campaigns. I talked to a few people and they actually opened a Jira ticket, that I noticed that your AI picked up.
**Andrey:** No.
**Filippo:** Long story short, we need to copy the existing website into the new one so that when we deploy, we don't break the existing marketing part.
**Andrey:** Okay.
**Filippo:** And then once they shift towards the new website, we can remove that part.
**Andrey:** Yeah. Makes sense.
**Filippo:** I think everything is in that ticket. So my question to you is, would you be able to get this? At least the dev part ready. By midweek.
**Andrey:** Sure. Yeah.
**Filippo:** Why am I asking that? Because the sooner we get this done, the sooner I can get SRE/Julen to create the full kind of pipeline for deployment. And then we get something done by Friday, basically.
**Andrey:** No. Okay.
**Filippo:** Mm-hmm. Do you know if we have everything that we need in that sense?
**Andrey:** I think so, but I imagine as we go through it, things might pop up. But I think so.
**Filippo:** Good. Because I'm okay.
**Andrey:** Nothing comes to mind that we don't have.
**Filippo:** Okay. You have a few things in review. Okay, okay, okay. I'm not expecting this to go as smooth as everyone thinks because product was driving this mainly, that's why.
**Andrey:** Mm-hmm.
**Filippo:** Yeah. But yeah, if you can get something ready in the repo, I'm going to push Julen to create the link and then we take it from there.
**Andrey:** Okay.
**Filippo:** Whenever you have something, can you ping me so I just talk to Julen?
**Andrey:** Yeah, and you're referencing 1583, I believe.
**Filippo:** I can't even tell you. 1583.
**Andrey:** One second, I'll send the link.
**Filippo:** Yeah.
**Andrey:** Okay.
**Filippo:** No, no, no, no, no, no, no, no, this is something completely new, never heard of it.
**Andrey:** Oh, okay.
**Filippo:** What is this about? A working page published on *[imot.app]*. No, no, no, no, this is not what we need. I'm talking about the website that's been shared with us. Built by Claude Design.
**Andrey:** Yeah.
**Filippo:** Let me see. Where is it? Herman shared that with us. Checking if it's attached somewhere. *[unclear]* Where is this thing? You know what? I think I have it locally. I'm gonna send it to you.
**Andrey:** Perfect.
**Filippo:** Yeah, here it is. Where are you, Andrei? Andrei, here you are. So this is the static website. Ah, fuck. Policy violation file removed. What the hell? Zip file, can't send it.
**Andrey:** Maybe rename it to something else.
**Filippo:** PDF.
**Andrey:** Yep.
**Filippo:** And then you need to rename it. Yes, PDF. Okay. Let's see.
**Andrey:** Nope.
**Filippo:** Yeah, yeah, this one.
**Andrey:** I will remove. Oh, okay. No, I get it now. So you do search HTML before?
**Filippo:** No, no, it's a .zip.
**Andrey:** Oh, that's it. Okay.
**Filippo:** It's a zip file. Because it's a full-blown website with a lot of static pages and a lot of things.
**Andrey:** Yeah. I think I have that. I think it's mostly implemented.
**Filippo:** So what we need to do is to put that live. But also add that static web page that we have today. And I think I created a Jira story for it that I need to find. Hmm.
**Andrey:** So what did you say that Julen needs from us in order to do the dev environment?
**Filippo:** This. So you need the static website plus what I mentioned in that ticket that I just shared with you.
**Andrey:** But why does he need that? Because that's where all of the endpoints are. The pages, or?
**Filippo:** Because otherwise we break the current marketing campaigns.
**Andrey:** Yeah, but this is on like the dev, we're not going to.
**Filippo:** So we need to— Oh, but that's just me wanting to be sure that whatever we put in— yeah, that's it. That's the reason.
**Andrey:** No problem. Okay.
**Filippo:** So getting— Actually, I can ask Julen to move forward knowing that you're working on it.
**Andrey:** It'll be easier to see it deployed.
**Filippo:** And on— Yeah.
**Andrey:** Then. True. My Firebase and Docker and whatnot stuff.
**Filippo:** Yeah. Let me talk to Julen to push this. Okay. Let me get that done. And I don't know if we need other things. Like any API key or anything that we don't have today. So the sooner you get this sorted, the quicker it's going to get sorted on all the other teams that we will need to ask for.
**Andrey:** Well, the quicker we can deploy it today, if we can share it around and people can see what's wrong.
**Filippo:** Um, okay, let me, let me get, let me get Julen to do this as soon as possible then.
**Andrey:** Yeah.

**Filippo:** Okay. Uh, what else? Do you have anything on your end?
**Andrey:** Uh, no, not really.
**Filippo:** On the iMote topic. Victor released a new version of the MartechKit on Friday, 4.0, and they said that there is a PR ready somewhere, and you said there is no PR.
**Andrey:** I don't see anything from Victor unless he's merged it in.
**Filippo:** Okay, I'm gonna— okay.
**Andrey:** Let me check. I didn't check whether it's merged.
**Filippo:** I might be— no, he hasn't. Sure he hasn't. iMote PR, Victor, Andrei.
**Andrey:** No.
**Filippo:** I'm gonna push this to get done as soon as possible.
**Andrey:** I have a PR up for it, so I can just merge in my PR.
**Filippo:** Okay. As long as it's 4.0, the version of MartechKit, and you just need to add the Braze API keys.
**Andrey:** Yeah. Actually, one thing that David Martos said is that we need to set up push notifications.
**Filippo:** Yeah.
**Andrey:** But he said with certificates.
**Filippo:** Huh?
**Andrey:** Why certificates?
**Filippo:** Andrei. Whatever is coming from David Martos could be easily coming from an AI. So—
**Andrey:** It is coming from an AI. I can see that it's coming from an AI.
**Filippo:** So please do not trust anything that comes from— when it doesn't make sense technically, most likely it's coming from an AI and the person that wrote it doesn't understand.
**Andrey:** Yeah. Okay. I'll look into whether I have the right access to set up.
**Filippo:** But, but, but wait, wait, wait, because Victor actually tested this.
**Andrey:** Well, actually, we probably have a key in Bitwarden. Or Victor has set it up. That's perfect.
**Filippo:** Yeah. Sorry.
**Andrey:** Set it up for me.
**Filippo:** One second. One second. Let me do this live. Andrei. *[messaging Victor]* Victor. Hey, Victor. *[unclear]* Add a PR for iMote. *[unclear]* And let's see what it says. So that part will be solved. Okay. So for me, priorities for iMote: get Braze out of the way, but you're depending on Victor and anyone else. Get the website out of the way. I'm gonna try to get *[the website]* out of the way, but you're depending on Julen. If you can kickstart a PR or something meanwhile, I'm gonna push Julen to do that.
**Andrey:** There is a PR and it's been merged with the— oh, with what we just talked about, 1599. So the thing where you said that we should *[not]* break the tracking, the campaigns.
**Filippo:** Oh nice, it's already done.
**Andrey:** Yeah, so it's testing though, ideally on that. Off to Julen.
**Filippo:** Okay. Okay, great. Talk to Julen. Good.

**Filippo:** That's it for iMote. For TraceCheck: Spanish. Out. Do you miss anything there?
**Andrey:** Nope.
**Filippo:** Okay, nice.
**Andrey:** Actually, so we should probably just do the email lookup page, then fix whatever issue Alex is seeing right now.
**Filippo:** Yeah. Yeah. Yeah.
**Andrey:** Then do a production release, then merge in the Spanish.
**Filippo:** Sounds good to me. So if you can do this.
**Andrey:** Yeah.
**Filippo:** Totally. You don't need my intervention there. You can run a production release.
**Andrey:** No, no, just, uh, just letting you know what the schedule is like.
**Filippo:** No, I like it. I think it makes sense. So feel free to move forward with this.
**Andrey:** Cool.
**Filippo:** In the meanwhile, I have a couple of agents doing some technical debt stuff like removing SERP API, and— but those are not related to the product itself. It's more like maintenance, so don't worry if you see something happening, merge it in if you see it.
**Andrey:** Gotcha.
**Filippo:** That's it. Sorry. I will merge it in. Once they are ready. And if they go to production, for me it's fine.
**Andrey:** Oh. Okay.

**Filippo:** Nice. Hey Andrei, let me check my notes. That is done. Oh, TV Foundation Kit regression, what's the state?
**Andrey:** Not a lot of progress there. Busy on all the other things, but I can get back to it this week and ideally we can talk with David Martos to prioritize that.
**Filippo:** Yeah, okay, I'm gonna do it the same tomorrow. Thank you.

**Filippo:** So I need to ask you something else. Which models are you using nowadays?
**Andrey:** DeepSeek. 4.1.
**Filippo:** 4.1.
**Andrey:** Yeah, it's really cheap, fast, and good.
**Filippo:** Hmm. Which one am I using here?
**Andrey:** Flash.
**Filippo:** Are you using the Flash? I'm not. Okay, I'm gonna try the Flash.
**Andrey:** Yeah. It's their latest release. I even started using it privately, I mean, my own, my personal stuff. And I put in $20 in it and I got like 2 billion tokens out of it.
**Filippo:** Yeah. What?
**Andrey:** Yeah. It's really good because off-peak hours. Like ridiculously cheap. And off-peak hours for China is our workday, basically.
**Filippo:** Nice. Okay. Um, because you were not on the presentation on Friday, but basically that was the last round of presentation. Durbán. And you share with us a tool that you built so that you can connect KiloCode to whatever tool you want.
**Andrey:** Yeah. I talked to him. Yeah. We've been chatting off and on. We discussed that as well. And there's a new popular thing called Jeff *[sic]* now as well. I don't know if you've heard it.
**Filippo:** Yeah. What the hell is that?
**Andrey:** It's a classifier. Basically, it saves a lot on the thinking and the tokens and makes things quite fast, but it's not as— you can chat with it, it can generate code, but it can figure out how to do things for you.
**Filippo:** Okay.
**Andrey:** Like, for example, testing a website. Makes it really easy and fast and cheap.
**Filippo:** Okay.
**Andrey:** Uh, yeah. And makes it so that like LLMs don't have to think as much on things. So it's like, it's not a replacement for your LLMs. It's like something that makes them a lot faster and easier to use.
**Filippo:** And access to it is not there. As far as I understand.
**Andrey:** Uh, there's a waitlist. But it goes pretty quickly.
**Filippo:** No?
**Andrey:** Like a day. But also there's like open source alternative now. That's even better than Jeff. So.
**Filippo:** Okay.
**Andrey:** Yeah, there.
**Filippo:** That was fast.
**Andrey:** Yeah, they're clowning on because an OpenAI person, like founder, I believe, that left OpenAI, built this thing for like 2 years in the background stealthily, and they released it and like a week later, better, faster alternatives for open source. So people are like, yeah. Yeah. It's— moats are dead. Software engineering is dead. There's no point to do anything.
**Filippo:** Pretty much that's all. That's what I keep telling everyone.
**Andrey:** Yeah.
**Filippo:** Software engineering doesn't exist anymore.
**Andrey:** No.
**Filippo:** Yeah. It's, for me, especially in the last few weeks, I completely understood that the software engineer that we used to know doesn't exist anymore.
**Andrey:** No.
**Filippo:** And whoever doesn't move into that direction is not going to last for long.
**Andrey:** Yeah.
**Filippo:** And especially when I started to create this kind of routine running on a schedule. Like, you can easily create something that literally improves the codebase over time. And it's insane for me. It's something that— why do we need software engineers anymore to think and read the code?
**Andrey:** No. Okay, too.

**Filippo:** So I have a question for you.
**Andrey:** Yes, of course. Always.
**Filippo:** Today we built a website. And we are pretty confident that 95%, 99% of cases are working fine unless we find some small bugs. And this is due to the fact that one, we start from scratch, and 2, we put down an insane amount of tests that are covering pretty much every scenario. How would you replicate this workflow on an existing codebase for apps?
**Andrey:** Same thing, lots of end-to-end tests to make sure. Actually, instead of like telling you, I don't know if you saw Shopify a couple of weeks ago decided that they won't do their apps in React Native anymore and will just use native.
**Filippo:** Yeah. Yeah.
**Andrey:** The article that got shared around was about how they do that, but there was another article that goes into how they did that. And it's basically that they build a couple of custom tools to do a lot of testing. And there was even, they shared around some videos of how they do the testing. And it's like the simulator and the LLM goes in lightning fast to click through all of the available ways of using the app, but basically, yeah, you write down what the app should do, and the LLM goes in and tests the hell out of it to make sure that everything looks and behaves properly. So in that way, you need a lot of tokens.
**Filippo:** Sure, you do.
**Andrey:** But they're getting cheaper and cheaper.
**Filippo:** That's my point. If DeepSeek with $20, you get 2 billion— 2 or 20?
**Andrey:** Uh, 2 billion too.
**Filippo:** 2 billion tokens. $20 for a company, $20 is nothing.
**Andrey:** Okay. Yeah.
**Filippo:** Okay. Okay. This is interesting.
**Andrey:** Here's the website, the exact way they did it.
**Filippo:** Oh, I'm gonna read that. Because I want to set up a few things.
**Andrey:** And if you look at the people on Twitter that wrote this article, they have a lot more going on there. On how and what to do.
**Filippo:** Nice. Oh. Okay. Good to know. Nice. Thank you. Um, Victor is almost there with the PR. Okay.
**Andrey:** All that, yeah.

**Filippo:** Andrei. Anything else?
**Andrey:** Nope.
**Filippo:** Cool. I'll leave it to you, the deployment for TraceCheck. For the landing page, the fix and the Spanish part. Um, yeah, I don't think TraceCheck needs anything else this week. Regarding iMote, I'm gonna push Julen today, and then let's see when we can get that done.
**Andrey:** Sounds good.
**Filippo:** And I'm gonna talk to David Martos and let you know about how that part goes. Because you still need to be around for another month and a bit more. Yeah. All right, gonna jump on an interview.
**Andrey:** Okay. Yeah. Okay.
**Filippo:** Andrei. Have a good one.
**Andrey:** Good luck. Bye-bye.
**Filippo:** Bye, thank you, bye.
