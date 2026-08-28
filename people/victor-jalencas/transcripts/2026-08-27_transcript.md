# Transcript — Victor / Filippo 1-on-1, 27 August 2026

> Source: Granola (meeting id `168dfd65-2f10-40bb-b9ad-32e6fbb27f48`), 27 Aug 2026 10:15 CEST.
> Speaker labels normalised: `Me` → Filippo, `Them` → Victor. Verbatim otherwise, including transcription errors ("blood" = Vlad, "iMode" = iMote, "is 27" = iOS 27, "brace"/"place" = Braze, "durban" = Durbán, "Vashaslav" = Viacheslav, "market kit"/"matic kit" = MartechKit).

---

**Filippo:** When I asked Vlad to join the project, I asked him to take a look to get acquainted and everything else. And he came back to me with a list of things and was like, okay, let me run an analysis myself because I trust everyone, but it's better to, you know, I had a bit of time, so I started to run an analysis. And I found out that what [Vlad] found were kind of nitpicking and more about the different ways of doing things. So it's like, thank you for your analysis, Vlad, but you know, it's fine how it is right now. But my analysis, what he found out were a few things that actually were actually bugs. And you mentioned the fact that you overlooked. I don't think that is the right word here. It's more that maybe you don't have enough experience inside this type of apps with the smart tech stack to understand and to know the specific details.

**Victor:** Absolutely no experience with this.

**Filippo:** So I wouldn't blame you for this. There is no blame here. It's more a fact that you don't have the full context to understand this. And look at this conversation with the market team. They don't seem to be the right team to give this context, probably because they don't have it themselves. They are just a mirror of Durbán pretty much.

**Victor:** Okay.

**Filippo:** So I just wanted to clear the water on this. I hope there is no hard feelings that you feel okay with these kind of things. I value the work you are doing. I value the input that [Vlad] is having and I think it can work all together in kind of symbiotic. That said, I still would like you to drive the technical part of this initiative. Is it iOS or Android? I'm more like managing things from a product perspective, trying to keep things together to push things forward to handle priorities. But the whole technical part I would like you to own it fully, if you don't mind.

**Victor:** Yeah, same with it.

**Filippo:** If [Vlad] comes with something that you think is not correct, please flag it. And release cadence and these kind of things. I would like you to own this kind of things.

**Victor:** Very well. I would also like to learn more about all of these marketing and attribution world. Until now, most of actually, yeah, most of the apps I worked on were free, and they were like compliments to an existing website or application so no one was worried about promoting the app. There was one free new map, but I only worked on features, not on this side of the world. And then there are big heavily used apps that I use that I work on where the Proton apps, which absolutely refused to have anything to do with marketing. So this is the first one in which, or these are the first ones in which I'm diving into all of these attribution. And until now, the more similar thing that I have been doing was observability, sending events for performance or diagnostic reasons. Which is.

**Filippo:** You pretty much, it is actually important. It is 50% of the job in my opinion. That part because marketing analyze also that kind of data. Having that knowledge that we have Amplitude, it's more than enough. And the missing part that I'm thinking you're having is the whole attribution part, which is an extremely hard and not exact science. As you can see from these discussions that we are having today. So I'm just speaking by for experience because I've been debugging and checking and knowing these kind of things for a while now. But there is no real answer here. It's a trade-off for everything. So yes, I agree. I'm going to try to help you to find a way to get this knowledge somehow. Because yeah, if you're working in this initiative, is it iOS Android Flutter or whatever, having at least the basic knowledge of the building blocks will help a lot. Also, and that's where I'm completely deficient. I have a great understanding of the iOS part, but Android, which is a different beast. I have zero knowledge. They don't have ATT for instance. How does it work attribution there? No idea. So we need to find a way for you to get this knowledge if we keep working on this initiative. Good. Clear the air on that sense. I'm feeling better now. I have two questions for you. And one is a proposal. What do you think if we start to work with release trains for the Martech SDK initiative? Would it make sense?

**Victor:** To clarify, you mean like having a weekly cadence or bi-weekly cadence?

**Filippo:** Bi-weekly cadence?

**Victor:** We can just thanks to release-please. We can just decide when to release and just automate it. So having like a formal schedule for it, it's no complication on top.

**Filippo:** So the technical part of this is pretty easy. As you said, it's just pressing a button and we can decide that on Wednesday we do. And every two Wednesday we do a release. That's totally fine. The part that I'm still struggling in my head is how do we make sure it works? Not the release, but how do we make sure that whatever we merge to main is actually working as we expect.

**Victor:** Well, that, that's an important question, no matter the cadence, no matter whether we stage or not.

**Filippo:** Yeah, exactly.

**Victor:** Yeah. The only thing that I can think of is testing, testing, testing. But not testing. Well, there's two ways to do this. One is to integrate with a sample app. And then we do the testing ourselves as automated as possible. And the other would be to have the app have like a test suite in which there's a fictitious app defined in Amplitude in all of these dashboards. And then we send scripted series of events to each one using the infrastructure of the kit. To simulate a real app, but without having to build a real app, just simulating interaction and different scenarios. Like the user buys immediately after approving ATT and so on. Maybe you, as an idea, they could live in a playground, an Xcode playground. So you just click play and all of these happens.

**Filippo:** Why not? I see what you mean. You can create an app with proper UI tests to simulate the flow in user. Can this be a real app?

**Victor:** Yes, the thing is with real apps, other, other stuff is happening in the app. So we lose a bit of control.

**Filippo:** But that's why that's exactly why I'm thinking real app. Because instead of testing in, you know, in a sandbox with that perfect word sandbox, having a real app, maybe we'll expose us to specific scenarios that we haven't thought about.

**Victor:** Yes, but then in our test, we need to also include the repo for the other app. Or what I would like is a self-contained thing that we can run from within the repo and just run a script or execute the coordinator coordinating class that just drive through all the scenarios.

**Filippo:** So step one would be this playground app just to make sure that the flow is actually what we expect according to the specifications. And then we move to a real app. Okay.

**Victor:** I mean. Yeah. We can do both and we have this sample app included. In the, in the repo format.

**Filippo:** Think it makes sense.

**Victor:** Also, it's, it's simpler to. To run the test because for when I did the update for iOS 27 and integrated in iMote, I had to stop pointing at the repo and point at my local copy. And that is, that is always a hassle. But if you have a local application project that always points at the local code, then it's, it's simpler.

**Filippo:** Yes, I've been through that in the past. I know exactly what you're talking about and the problems that come with it. Okay, I think we can consider this something that we should add afterwards tackling all the priorities that we have here. Okay, I like it. I like your idea. Cool. Second question, how can I use release-please for a website?

**Victor:** Can you use this for a website? Of the user in this website?

**Filippo:** I need to decide. Right now we are version by date. It's a website, so there is no real software kind of release system. It's more like date based.

**Victor:** But what do you want to accomplish? Push to the, I mean, deploy it or just tag the version of the code.

**Filippo:** Workflow today is we work [with] Git flow. With website, we work in dev branching out from dev and then we want to release to prod. We just merge to main and there is an automation that deploys to prod. I want to tag, create a release every time we do a release to prod.

**Victor:** In that case, I don't know if release-please is the right answer to your problem. So you want to tag every time you deploy.

**Filippo:** Okay. To production, yes.

**Victor:** But that should be the work. I mean, the responsibility of the deployment script.

**Filippo:** But as far as I understood, probably I'm understanding wrong this release[-please]. It also creates a nice and readable release note.

**Victor:** Oh, yeah. But there are other tools that do this. Yeah. Starting from, yeah, from the comments or from.

**Filippo:** Okay.

**Victor:** Yeah. And actually, I was thinking that your deploy script should tag the version before deploying even. So that if there's an error deploying and it has to roll back, at least you know what was attempted to deploy. And if it was me, the trigger for deploying would be the tagging. But [I'm] a bit of an idealist on this. So don't pay too much [attention].

**Filippo:** No, you're not an idealist. That is, that was my idea as well, but SRE decided that we had to go through this way to do things. But this is a new website that we built and I'm trying to define all these flows. So that's why I'm asking you this kind of questions and how to work.

**Victor:** The first version of our CI scripts for apps. The trigger to make a release or in this case a deployment. It was the tagging. So when tag is added, GitHub sends a webhook to, to Codemagic or whatever Cloud Run or whatever you're using. And then that's what starts the ball rolling.

**Filippo:** What is the difference between that and a simple merge to main?

**Victor:** So I think that you want to deploy on every, on every merge to main.

**Filippo:** It is already working like that.

**Victor:** Okay. So in a, but actually that will mean a tag for every commit in main. That's a bit non-informative. So if every commit is special, no commit is special.

**Filippo:** Right. Unless we are also merging to main documents and less that kind of things. But if there is a trigger, as you said, that every commit to main is actually deploying.

**Victor:** Yeah. Then the hash is, is your tag. If you want to know which one is deployed. Just have it use the hash of the commit.

**Filippo:** Okay. Okay. So it doesn't make sense.

**Victor:** [Not] as I said. But the automated release note generation. Yeah, there's, there's a handful of scripts out there also in Node, in Python, wherever you use.

**Filippo:** Yeah, I'm using Node. Yeah, I'm sure there is something. Okay. Okay. Nice. Thank you. We'll do that. It's interesting this whole web world that I'm entering. It's just so much different from apps. Somehow it's way easier. Because you can do a lot of automated testing, even UI testing nowadays are super powerful. You can run them in the CI without really compromising anything while on mobile we know. But on the other end, it's very, very. Dangerous somehow. It's very easy to deploy to production, but the rollback is quite complex.

**Victor:** Why should it, I mean, are you using something like containers or Docker or something like this? Then you can just save the last known good image and just replace it. No.

**Filippo:** I think it's more psychological. There is a process to release an app, which is we go through TestFlight. We need to test in there. We need to test in production. And then we press the button, go to the world. With web is just [merge to] main. Everyone is going to get access to it. That's the, I think it's more psychological than anything else in that sense.

**Victor:** Yeah, there's no ceremony.

**Filippo:** No, no, definitely not. Okay. I honestly have no more questions for you. Do you have anything.

**Victor:** Do you want to talk about, yeah, let's talk about Braze if you want.

**Filippo:** Sure. Yes, let me give you a bit of an explanation about Braze. [It] is a new library that we would like to use in both web and apps. What does it do? It collects data about the user through Amplitude in our case. So that we can target properly the users through marketing campaigns coming from push notifications in terms of apps or emails in terms of web. That is the gist of it in very, very few words. Then. What does it entail? There is an SDK. Which should go through the Martech SDK. Why? Because somehow is part of the set of tools that share the same ID. And there is an order on which it should be initialized. And if I'm not wrong, it should be one of the first to be initialized. And then whenever we get the original RevenueCat ID, we set it to the Braze user. And this is it in terms of MartechKit. That's the whole package. What does [it] entail in terms of apps though? Because this is the switch here is if you're using the MartechKit, you get Braze for free. But we want to remove from completely OneSignal. Some apps were still using OneSignal. So that is something that we need to remove from all the apps. Nothing we can control. Obviously, that's on the app side. There is a bunch of documentation regarding Braze, but we don't much care about. Why is that? Because Braze allows you to — Braze SDK allows you to send data to their servers. To collect user information regarding their behavior or anything, any properties related to the user. But as we are already using Amplitude, that that data will reach Braze's servers through Amplitude. So there is a connector to Amplitude. So whatever data we send to Amplitude will be then parsed by some Martech script and it will be sent to Braze servers. So nothing to be done there. And to be fair, that's it.

**Victor:** To add also a hook or a universal link for push notifications. I remember integrating Braze[, a] version[,] when I was in [a previous company]. And basically, as I said, I only worked on features. But what we needed to do was to send specific events that were considered interesting. And then allow for a pop-up or an alert to be shown or to be triggered by Braze under specific conditions.

**Filippo:** So you are talking about the UI part of the library. As of today, we have no requirements related to that. So I will leave it out for now unless in the future maybe we will receive this kind of requests. But for now our only work here both in mobile and in web is to initialize the SDK. And connect the user ID to it. So whoever handles data can analyze that data. That is it. Nothing more.

**Victor:** Nice. I understand that we were going to [put it in core] because it will be mandatory [for] all apps.

**Filippo:** This is something I'm not convinced. Let me explain why. Not all apps should be. What are the advantages of putting into core instead of having it as an external dependency?

**Victor:** It simplifies the dependency management. And also during the initial, well, during the initialization in which we do [the] cross attribution, we can count on it being there instead of having to prepare a hook so that the module which may be optionally linked has a chance to set the RevenueCat ID to Braze.

**Filippo:** What are the disadvantages?

**Victor:** [Dis]advantages. Well, if an app does not need or does not want Braze, it will be there. Always. So as a library and also if we do the initialization unconditionally, then we will send the RevenueCat [ID] to Braze. Even if it's not [needed].

**Filippo:** What if we put a condition based on the fact that the app inject the SDK ID for Braze?

**Victor:** I looked into that at the very beginning so that the library could find out what libraries, whether libraries were present and it's a mess. In terms of verifying and testing that.

**Filippo:** I'm not saying about — I'm okay if this goes in the core, but the initialization of it. So, okay, go to core meaning all the apps will get this library inside them. But the initialization of it will only happen if the ID is present. We don't crash the app if the ID is not present.

**Victor:** Okay, yeah, that will, that will work. Also another thing that could work, but would require some major changes as well is a feature of Swift 6 called SwiftPM traits.

**Filippo:** Yes. Talk to me about it.

**Victor:** Which essentially when you're declaring the dependencies on a library, for example, MartechKit, you can, you can enable and disable optional parts of it, but within a single module. So you say, okay, I want MartechKit with Braze on board with TikTok and with Facebook. And then within the code, you can just have conditional compilation, which is if this is enabled, then run this code. It's kind of a debug like a flag, like conditional compilation triggered by debug or something like this. But it's simple because you don't have to modify the project settings. You just in the, in the Package.swift or the list of dependencies, you add the aspects or the subset that you want. It's a bit like, like CocoaPods use it to define optional parts, but it's all a single module, a single library. The downside to it is that it requires Swift 6. And then by default Swift 6 enables strict concurrency, but you can tell it to still use the Swift 5 concurrency model, which is not strict. Eventually we need to ensure strict concurrency. But that's a longer development because when dealing with Objective-C libraries, most of this is the case are done in Objective-C for compatibility. Then you have a lot of Sendable compatibility to care about.

**Filippo:** I know, I know Victor. I know exactly what you're talking about.

**Victor:** I'm glad that [I don't have] to explain.

**Filippo:** No, I know, I know on my — I still remember that moment where we try to do that migrate into Swift 6 and strict concurrency. Okay, so it's not the time to do that. But I'm totally fine with getting Braze into core. And. Yeah.

**Victor:** This, if, if the key provider, it has an optional Braze ID if it's present, we use it. If not, we skip it.

**Filippo:** I think it should be pretty straightforward to move forward with this integration. Feel free to use iMote as testing ground. I can give you the Braze SDK IDs because I have access to the panel whenever you need them just ping me and I can provide that.

**Victor:** Okay.

**Filippo:** Okay, checking my. Topic. I take Braze. That's done. Android — Viacheslav — everything under control there. Do you need a bit more management power there?

**Victor:** I need to switch my attention to it. [I] actually have paid little attention this week. What exactly do you need from me in terms of to work on it? Because from what I see, a lot of the things that [Vlad] pointed as [problems] were born from lack of knowledge of how the lifecycle works, for example, or how it links, how do you declare, how do you link to libraries and so on. There was a lot of technical knowledge that I was missing. So apart from overseeing the business logic of it, of tracking and so on. I think he's more, he's more apt for doing some of the tasks than I would be. So I can, I can review that, for example, for the anonymous ID and so on that he understands how we work. But other than that.

**Filippo:** Prioritize his findings — blockers, minor, close whatever doesn't make sense. That is for me the number one priority here. Making sure that whatever [he] produces somehow makes sense within the library itself and within our styles. Obviously your knowledge of Android is limited. We know that that's not a problem here. But also from a technical perspective I would like you to be the one that create the release. This shouldn't go through Viacheslav. So feel free to take over the PRs, merge them and create a release whenever we decide. And finally in there I can help you if you feel that he's lacking some information on the context. If you can provide them and I'm apt to provide them as well. What I'm going to try to do is to get him a bit more in our dailies because I need to see the progress happening because he's not really vocal about it. So I need to have a better understanding there.

**Victor:** I noticed that he released from a branch, like from a release branch, [not] from main, but that is [explained] because he didn't know about how we were, how we were intending to work. And regarding the dailies, when you said three per week, I was assuming on alternate days, not like in the middle of the week. But what do you think about doing Monday, Wednesday and Friday?

**Filippo:** On Friday.

**Victor:** Or even daily, real dailies, like daily? But I don't know your schedule also.

**Filippo:** That's my problem. For me I'm checking my calendar. For me. Really bad.

**Victor:** My calendar is open and I guess [Vlad's] as well because [he doesn't have] so many meetings. So feel free to create a week, a daily and then just attend the ones that you can.

**Filippo:** Yeah.

**Victor:** And the rest [Vlad] and I will do without you.

**Filippo:** I think it's a good idea. I'm going to set a daily daily. The whole week and then who can attend will be there and probably — but I'm still trying to get my head around this concept. I would like to set up also sort of sprint planning or something like that. Maybe use one of the dailies take it a bit longer every two weeks. To review the work and to set up the work for next sprint. I think it will be beneficial for everyone to understand what are the priorities and everything else. What do you think?

**Victor:** Yeah, it makes sense. So we move from the Kanban style thing to a sprint. Even if, well, if we have a list and actually it makes sense.

**Filippo:** That's where I want to go basically. And this will give predictability also to other stakeholders. If [someone] has come to me [asking] what are you doing? Hey, we have scheduled delivery. This is happening bam bam bam bam look at the Jira board look at our backlog and you know having this kind of cadence will help the other stakeholders as well. Okay dailies.

**Victor:** Actually. No, no, never mind. I always want to say we could even have it so that every merge commit bumps the [version] number. Automatically so that every merge is a release.

**Filippo:** It can create a bit of confusion. I'm thinking that developers that are using our library — giving predictability to also the developers will be very useful that they know that maybe they just bump the version once a month, but we do release every two weeks. And if they find bugs they know that it's going to be released very very soon.

**Victor:** Yeah. Makes sense.

**Filippo:** Let's try like this I'm going to set this up. Try to create a bit of a system there trying to — I don't think we can automate this but trying to put a bit of order in that sense.

**Victor:** But I'm afraid we will lose a bit of control.

**Filippo:** Correct. Correct. I agree. One thing that I would like though to happen is to set the release, the fixed version or release version in Jira for the tickets that we have. That I believe can help a lot mainly for traceability purposes.

**Victor:** [Is] that the [version] in which it will appear[?] Okay, but if we merge a breaking change, then the [version] number grows and then maybe 2.1 [becomes] 3 because we release 3 instead. How does that work in [that] case?

**Filippo:** [You] fill in release in Jira and you just bump. Okay I see your point I think about it. I think about it okay makes sense Victor I need to jump on another meeting and thank you so much for your time. I will bring up the Martech discussion in that conversation by the way because I want everyone involved to be present and know about this.

**Victor:** See you in an hour. Yeah. Okay. So yeah.

**Filippo:** Thank you bye bye.

**Victor:** Bye.
