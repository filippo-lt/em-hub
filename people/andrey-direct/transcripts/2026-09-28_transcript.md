# Transcript — Andrey / Filippo Weekly 1:1 — 28 September 2026, 10:30 CEST

> **Source:** Granola (meeting id `d7733e7a-e12f-4f25-994a-1cf43cd2679f`), Filippo's personal
> note-taking tool, not a company recording.
> **Cleaning:** Granola splits speech into fragments; consecutive fragments from the same speaker
> are merged. Obvious ASR errors normalised: "iMode/iMOD/iMOT/iMond" → iMote, "trace check" →
> TraceCheck, "Martek" → Martech, "Quen/QWEN" → Qwen, "Andrej/Andrei" kept as spoken. Garbled
> fragments marked *[unclear]*. Otherwise verbatim.

---

**Filippo:** Hello, Andrei. Hello. Hello, hello.
**Andrey:** Hello, yes, I will be getting some water.
**Filippo:** Hello. How is it going?
**Andrey:** Okay. Nothing. Nothing major.
**Filippo:** Good weekend.
**Andrey:** Great for a Monday. Yeah.
**Filippo:** Yeah. Okay. Nice. Nice. Today we have one month left.
**Andrey:** Yes.
**Filippo:** I'm not happy about this, but there's not much I can do about it.
**Andrey:** Me either.
**Filippo:** I was thinking about it and it's just, yeah. Company's choices.
**Andrey:** Yeah.
**Filippo:** Um, well done with Spanish. Good one, thank you. And, uh, well done with iMote website. Nice. Thank you.
**Andrey:** Yep.
**Filippo:** So you are now officially a web developer.
**Andrey:** Yay.
**Filippo:** Yay! Yay! I have to be honest though. I'm actually enjoying a lot the TraceCheck thingy and the freedom that we have to play with this, with AI tools. It's fun. Come on, it's fun. It's fun. And I'm learning a lot as well.
**Andrey:** It is fun. Yeah. Yeah. Yep.

**Filippo:** Okay. I have 2 major streams that I want to talk to you about, but nothing actually, nothing that you don't know about.
**Andrey:** Yep.
**Filippo:** Let's go quickly through iMote. As I said on Friday, let's give ownership to Victor about the app, the iMote app.
**Andrey:** Yep.
**Filippo:** Again, it's mainly to understand, to see if he understands everything. And so he will have time to ask you questions pretty much.
**Andrey:** True.
**Filippo:** One thing though. Because I've seen that iMote has 1 million PRs opened.
**Andrey:** Uh, at the moment, or one?
**Filippo:** Yeah, it looks like right now.
**Andrey:** Uh, the 15 open PRs, yeah.
**Filippo:** Yeah.
**Andrey:** Want me to wrap them up or?
**Filippo:** Is it something that— yeah, I don't know, you tell me.
**Andrey:** Uh, they're mostly like, uh, crash fixes.
**Filippo:** But are those fixes?
**Andrey:** Yeah.
**Filippo:** So yeah, if you can clean them up. It's mainly to support iOS 27. Yeah, no rush, just go through them just to clean up a bit the repo and that's it.
**Andrey:** Yeah. Okay.
**Filippo:** To be fair, nothing more. Great. I have a question. Let's see. My plan will be for you to ship the TVs to Barcelona, to the office.
**Andrey:** Yep.
**Filippo:** I'm going to talk to office management to understand how, but I was wondering if you are close to releasing TV Foundation Kit, would it make sense for you to keep the TVs for a bit more?
**Andrey:** I would probably leave that off to Victor as it'll be something to support long term and I want him to be like in charge and owning that.
**Filippo:** And then ship. Okay. Okay. Yeah.
**Andrey:** That's why I'm hesitant to wrap it up now and then leave and then an issue comes up and—
**Filippo:** Perfect.
**Andrey:** It's like we have to roll back or anything like that. That's my hesitation, but I'm fine if you want me to, I can do that.
**Filippo:** No, no, I like your approach. I think it's the best one. So I will talk to office management and let you know regarding the shipping. Most likely we will arrange someone to come to your house to take the things.
**Andrey:** Perfect.
**Filippo:** But let me talk to them first.
**Andrey:** Yeah.
**Filippo:** Nice. Thank you. And that's it for iMote app.

**Filippo:** There is the whole iMote web part. So what is blocking us to merge into prod?
**Andrey:** I'm not aware of anything at the moment. It's mostly like a product go-ahead sort of thing.
**Filippo:** Okay. I'm a bit worried. Not about the job that you did, that Martos doesn't have full control over this point. So—
**Andrey:** Okay.
**Filippo:** I'm gonna push him to do all the checks that he needs, to talk to Martech and make sure that everything that needs to be done is ready.
**Andrey:** Yeah.
**Filippo:** But until we have any information there, there's not much to do in iMote Web, to be honest. Ah, yeah, one question. On Thursday or Friday, I was receiving millions of messages from all the people involved in iMote remote regarding this web, and the girl Stefania, she was asking regarding putting a couple of T&Cs pages.
**Andrey:** Yeah, yep.
**Filippo:** Have you managed to put them in dev?
**Andrey:** A couple of blog pages.
**Filippo:** Yeah. Give me a second, let me find this because—
**Andrey:** Last time I talked to Stefania, she said, I don't know anything about this website.
**Filippo:** Yeah, exactly. That's exactly my point. It's like, guys, why?
**Andrey:** Don't bother me. So I don't know about that.
**Filippo:** Here you go. I think this ticket.
**Andrey:** Uh-huh. I click on requests. Hmm. No, I haven't done that.
**Filippo:** Yeah. Yeah, if you could get those done as well.
**Andrey:** Hmm.
**Filippo:** Shouldn't take long. And that's why we need someone to take care of, and get a Jira board with tickets, because right now it's a mess.
**Andrey:** Yeah.
**Filippo:** And we can't really move forward very well. I will try to push this to get sorted this soon. What else, just to close a bit the iMote part. So considering this is phase 0, I'm hoping we can merge to production this week.
**Andrey:** Yep.
**Filippo:** So this part should be done, but then there's the old phase 1 that will start, which is the web funnel, web-to-app funnel. Now I'm a bit hesitant because I know you can do it, no problem. But at the same time, I would like someone else to take care of it because if you're gonna leave, you know. It's not a static website. It's something that we require a bit more involvement. So I'm gonna try to get someone to do this part themselves, but I may ask you to jump in and help if needed.
**Andrey:** Yeah. No worries. I'm here another month.
**Filippo:** Thank you.
**Andrey:** Anything you need.
**Filippo:** Thank you. Thank you, Andrei. Really appreciate it. It's just to let you know that at the moment it's still a bit blurry. There is a chance that I'm gonna get a web developer from the web teams to work on iMote Web, but I need to do some talking with people first. If that is gonna happen, I'm gonna assign this task to this person. Otherwise, I'm gonna ask if you could help, but let's move forward one step at a time.
**Andrey:** No. Sure.
**Filippo:** Um, anything else on your end regarding iMote?
**Andrey:** No, not really.

**Filippo:** Okay. Perfect. So we can move to TraceCheck. Um, the big thing for next sprint starting tomorrow is going to be image lookup. I'm going to work on an epic. There should be already an epic. I'm going to just check that we have all the information there, but there are a few things that I'm gonna ask you, what do you think? So one thing is to write an email—
**Andrey:** Yeah.
**Filippo:** —and to call those providers and get the results. The other is to upload an image, which I think from a UX perspective is a bit more complex.
**Andrey:** Yeah.
**Filippo:** In your experience, considering that we don't have yet a design and probably we will not have a design for this until we ship it, if we give an AI agent a task like this, would it be able to create a decent user experience?
**Andrey:** Yeah, absolutely.
**Filippo:** Yeah.
**Andrey:** It won't be very fancy, but it'll work. And we have a lot of the design system in there, so it will take care of what's currently in there and use that.
**Filippo:** I don't know. Okay. Okay.
**Andrey:** Um, might look a bit vibed, but I think it'll blend in what we got.
**Filippo:** For me, it's okay, the vibe part, considering that on Thursday we're gonna have a designer joining the team.
**Andrey:** Great.
**Filippo:** And he will review the whole website and start to actually design the website in a better way. So until we have that, I'm okay to move forward. Great. Tomorrow I'll prepare all the epics and the user stories and everything else, and then you can take it from there. Image lookup. Anything else? Question? Probably. Is there a way, in your opinion, we can block non-face images from a client perspective?
**Andrey:** Non-face. If it was iOS, I would have said yes, but there should be a way. Yeah.
**Filippo:** Yeah. Because that could be an interesting, you know, time and resource saving.
**Andrey:** Yeah.
**Filippo:** Just block the users that take pictures of their feet instead of their faces and we should be okay.
**Andrey:** Yeah.
**Filippo:** But I don't know.
**Andrey:** There definitely should be something. *[unclear]*
**Filippo:** Okay. I'll let you do your magic in that. I'm doing less and less coding nowadays because I don't have the time. So I'll leave you the sprint to do your magic there. If you could manage to merge in the history part. You know, the alias part.
**Andrey:** No. *[likely "Yes/sure", unclear]*
**Filippo:** That would be great. It was though created when we only had phone numbers. Is it gonna work with the emails as well?
**Andrey:** Good question. I think so. I'll try it out.
**Filippo:** Try it out, you can merge it in today so we get rid of that PR and it should be done.
**Andrey:** Yeah.
**Filippo:** Nice. That's pretty much it. Anything on your end?
**Andrey:** Ah, nope. I've already started *[unclear: "typing to these"]*, so we're good to go. Packing the TVs, so they're good to go. That was like the big thing I got.
**Filippo:** You already started? Okay. Okay.
**Andrey:** Uh, nope, nothing else.

**Filippo:** Okay, well, I'm gonna use the next 10 minutes to bounce some ideas with you then, because as you may know, TraceCheck is just one website of a kind of more vast family of websites.
**Andrey:** Family.
**Filippo:** What do they have in common, these websites? They have the lookup, and also the middleware between the website and Parapet. So what I was thinking was to create shared services. So you have these shared services, and then you have the websites, each one with their backends, and those websites talk directly to these shared services. My question that I'm trying to find an answer to right now, but I can easily ask around: would it make sense to create multiple Firebase projects?
**Andrey:** Ah, for each project? Or—
**Filippo:** One for the shared services and one for each website.
**Andrey:** I think so, yeah. Yes. Otherwise, the alternative would be to have one Firebase account with all of them in there, which probably isn't *[unclear]*.
**Filippo:** Yeah. It's gonna be a mess.
**Andrey:** Yeah. I don't know if you can, like, filter through stuff in there. You could add different domains to one gcloud, so— again, if it was apps, I would have gone different databases. That's probably something too *[unclear]*.
**Filippo:** I'm thinking about maintenance. Because today, if we find a bug or there's a new feature, you only have one place. And that's it. If you start to have multiple places—
**Andrey:** Oh, it definitely makes sense to like split them off in its own service, I think. One service to handle them all.
**Filippo:** Yeah. Okay. That's going to be a nightmare also for Julian and his team. I need to talk to him.
**Andrey:** Yeah. Sucks for him.
**Filippo:** Okay. So this is the only thing that I'm doing myself at the moment, and mainly because this is something that needs to be carried over to whoever is going to be your substitute in the future. And I'd rather have the idea fixed in my head on how this is going, but I may ask you to review a few things once I have the clear thing in my head.
**Andrey:** Absolutely. Yeah.
**Filippo:** Okay, nice.
**Andrey:** No, thank you.
**Filippo:** Thank you. Have you tried *[unclear: "Jeff"]*? Have you tried *[unclear: "Jeff"]*?
**Andrey:** No, not *[that]*, not yet. I'm starting a bit to convince myself to get like a local LLM going, uh, like 2 3090s NVIDIA, and try out some things that way. I have another like Mac here that I'm running the small Qwen model. It's very slow. I've handed it off a project and it's been working for like just 100 hours, but it's probably more than that with configuration and whatnot. And it died a couple of times on me, but it's like it's going crazy here doing things. It would be very interesting to see what happens. But yeah, it's like a niche. It's slow here, but if I have 2 3090s, I can even run the bigger one. I sent you a screenshot last week, didn't I, about best value for money?
**Filippo:** Yeah.
**Andrey:** And you can technically run the Qwen Next one. That's better than GPT-6 Luna. You can run it locally really fast on 2 3090s and some RAM. So yeah, that's kind of itching me, it's just about as good as DeepSeek Flash according to that chart. Which is the Trust Me Bro benchmarks.
**Filippo:** Okay. Yeah. But, um, why not one of those new Mac Studios?
**Andrey:** Very expensive. I mean, it's like €11,000. Where one 3090 is like €800 and I need 2, and 8-year-old hardware for like €500 and €200 here and there. So it will come out at around like €1,500, which is far from €11,000.
**Filippo:** Yes. Yes. And what are you going to do with these LLMs locally?
**Andrey:** Ah, apply for jobs.
**Filippo:** Really?
**Andrey:** Yeah. Have them on the loop. Scanning the internet. Uploading my CV everywhere. And these days they now have like an AI interview part. And you can have your AI do the AI interview part.
**Filippo:** What? How's it going?
**Andrey:** Yeah, it's like gaming the system. Like the company says, oh, we don't want to deal with all these candidates, so we'll do an AI interview. They'll figure it out. And on the other hand, you say, I don't want to deal with all these companies. I'll have my AI do the interview. They talk to each other and then pass on to the next round.
**Filippo:** Do the same. Do you have any leads so far?
**Andrey:** Uh, yeah, a couple.
**Filippo:** Okay, good. If you need any reference, no worries.
**Andrey:** Much appreciated.
**Filippo:** Really happy to do that. Absolutely. Okay. Okay. Andrei, I have nothing else.
**Andrey:** Me either.
**Filippo:** I'll let you go.
**Andrey:** Thank you.
**Filippo:** Have a good one.
**Andrey:** Talk soon. Bye-bye.
**Filippo:** Bye.
