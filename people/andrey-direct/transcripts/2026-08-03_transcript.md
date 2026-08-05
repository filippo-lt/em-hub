# Transcript — Andrey 1:1, 3 August 2026

**Source:** Granola — "Andrey / Filippo - Weekly 1:1", 3 Aug 2026, 10:00 CEST
**Participants:** Filippo Tosetto, Andrei Marinov
**Speaker mapping:** `Me` = Filippo · `Them` = Andrey

*Auto-transcription. Several proper nouns are corrupted and are noted inline on first occurrence: "her mom" / "her man" / "her money" = **German/Herman** (iMote PO); "the vitamin" / "vitamin received" / "the video" / "bit partos" = **David Martos**; "ATOR" / "hater" / "actor" = **Heitor**; "Martino" / "matiano" = **Matellano**; "brace" / "praise" / "bra" / "braised" = **Braze**; "market kit" / "Martech kit" = **MartechKit**; "trace check" / "treschch" / "race check" = **TraceCheck**; "i mode" / "iMode" = **iMote**; "kilo"/"kimmy"/"quin" = **Kilo / Kimi / Qwen**; "5.4"/"opus"/"fable" = model names; "durban" = **Sergio Durbán**; "julian" = Julián; "Thiago" = web staff engineer.*

---

**Me:** Good morning.

**Them:** Hello.

**Me:** How are you?

**Them:** Bit frustrated — time logging and hours.

**Me:** I can imagine, I see what you are doing. What's happening that you are recalibrating the things?

**Them:** They said they won't pay me until I fix my hours.

**Me:** Okay.

**Them:** Which isn't something in the contract.

**Me:** Okay.

**Them:** So — but I didn't want to be that guy, escalate that sort of thing. So yeah.

**Me:** Your times were off.

**Them:** They would.

**Me:** Okay. But now they're fixed, okay.

**Them:** By 200 hours, yeah.

**Me:** Don't know how to help you here, I'm struggling with this as well. And I know that I'm not the only one.

**Them:** Well it wasn't that bad — they had that button before, when you click clock out and it says log the estimated hours, not your true hours. And they took it away, then they brought it back, and they took it away again like a couple weeks ago. That's contributing a lot to the hours being bad.

**Me:** Yeah. Yes, I think that Factorial is not the best tool and this logging hours is not great, but hey, that's what we have, it's for Spanish law unfortunately, that's what we need to do.

**Them:** Makes sense. It's very weird because I'm on this business-to-business contract, and when there's something in my favour I'm being told that I'm not an employee of the company so I can't get it — like I don't get my birthday off — but for this kind of thing it's Spanish law, track it, and I am an employee. So yeah, it's very frustrating.

**Me:** Which is also… yeah. But also I'm thinking, external developers do not have this. HR, HR, love them. Andrei, how was your weekend?

**Them:** At a birthday party, so that's interesting. Well, birthday parties like these days for kids tend to be very fun, not like my own back then — you get like a cartoon character as a person who manages the kids, and they have balloon parties where they get those balloons you pop, there's snow which is just fall, they shoot out of stuff. Seems very fun.

**Me:** Yeah, how was it. Okay, nice. My birthdays were not like this.

**Them:** I don't think I had birthdays with outside children until I was like 10, so.

**Me:** Okay, yeah, very weird. I live in front of a park right now and I literally see the park from here, and they book the tables in the park to do kids' birthdays and they literally bring everything, like you know, the inflatable castle and there are clowns, there are things. Is it okay, this is a bit too much, isn't it? Is it for the kids or is it for the parents as well? There's so many things. I don't know, I'm not a parent so I don't know all the ins and outs of these kind of things.

Right — I have to admit I'm very, very tired and I'm gonna be struggling today and this week in general. Good news for me is that a month… almost there, almost there. Yeah, it's gonna be a long week. But looking at how things are I think we are in a good position.

First question for you is: is **German** back?

**Them:** Well, it says he's back, but he's declined today's meeting and he didn't join. So if German is back in the woods and no one hears him — if German in the back…

**Me:** Okay. So you don't know. All right. Good or bad — speaking, I had… I started, last question to **David Martos** last week, because you know, you worked on a prototype, what are we gonna do with it? Am I just wasting your time and tokens, are we doing stuff? And turns out that Martos never received that prototype.

**Them:** I probably gave it to Fernando. That David Martos needs to have it.

**Me:** That's not on you obviously, this thing, but it shows me that—

**Them:** Literally the only time I heard from Fernando for like the whole two, three weeks.

**Me:** And Martos is a bit frustrated about this and — I do it, what do I want me to say, it's like, talk to Fernando. So that's that.

In September, you know, things are gonna happen and things start to take shape — obviously this is not official yet. But the reality is that they're gonna flatten out a bit this PO/PM situation and there's going to be only one person. Is it a PO, is it a PM, we don't know yet, and who this person is gonna be. Thing is, the conversation will be directly with the person in charge from product, so there's not going to be any more middlemen here. So this kind of situation will not happen anymore.

Still. I'm the person that thinks that we don't need to force features into this app if it doesn't need any new features. But I mean, work on stability sure, work on marketing stuff sure, but do we really need any more big things for iMote? Don't know. Don't think so. Anyway, conversation is gonna change in September so let's prepare for that.

**Them:** The connection rate improvement — and there were some other operating systems that we maybe want to support, like Amazon, their Fire TVs. They released a new Fire TV and they changed the operating system to be called something else, it's not ROS anymore, it's something. So that's something that we can do. Also there's maybe a way to control PlayStations as well, remote external mode. So there's things we can do, but like, yeah.

**Me:** Do we want to?

**Them:** I don't know. I just talked to the agent.

**Me:** Come up with this to us, so I'm just gonna wait. Let me see if German… I see German accepted the meeting that we have tomorrow, the roadmap meeting that we have tomorrow. So I'm expecting to have a conversation with him about the future of this app. Let's see.

Okay, there is another initiative on iMote that we are gonna kick off this week and it's about **Braze**. And I'm explaining this because you will hear about this, but as I'm not going to be around next week I want to give you a bit of a view on the situation.

Which is: Braze is a new third-party library, you know, one of those from the Martech department, and in apps it will allow us to target users with push notifications. They want to integrate it in iMote, which I'm not against. And there are two ways to do this. The first one is to integrate it directly — totally fine. And the easier way would be to use MartechKit to do it, but it's not yet implemented in MartechKit. So the question here is which one is going to come first — chicken or egg situation, kind of thing.

To give you visibility, because I've been studying a bit the SDK, it should be pretty straightforward in our situation, meaning: initialise the SDK, set a user ID — which probably is going to be the RevenueCat user ID as we do for Amplitude etc. — and then we need to send specific events to Braze. This is the flow.

There are things that need to be decided from Martech before we do anything, like which ID we're going to use for the user, to reconcile it then with Amplitude etc., and which events we're going to send. So if I'm not going to be around and people are going to come to you and say "hey, we need to integrate Braze" — say "sure, no problem, we can do it. You need to give me these two data points."

Just to let you know, because I know how things are going to come through, from Martech, from Zero, from Product, none of which probably understands fully this topic. What I'm going to do is I'm going to invite you to a conversation that we're going to have with Braze itself, the company, this week. So you are aware of the situation. But please do not do anything unless you have full information regarding this topic. That's it.

Cool, that's it for iMote unless you have any other topic related to this.

**Them:** No. So Braze is going to be only for iMote, or for TraceCheck as well?

**Me:** Going to come to TraceCheck as well, but in a different form.

**Them:** Later on, or within the next two weeks, or…?

**Me:** Andrei, after one year in this company you may understand that these kind of things should have been implemented yesterday, because everyone thinks it's super simple and no one thinks of the complexity of this. Then engineering comes, reads the documentation, thinks about the implementation, says "sure we can do it, it's a one-liner for us, but you need to give us all of this information before we can do it."

**Them:** [Are we] there yet?

**Me:** It's going to come for both iMote and TraceCheck, obviously different ways here, concept is the same: we need the information that Martech needs to give us. I'm going to invite you to the meeting that we're going to have with Braze tomorrow as well. So tomorrow we're going to have one for web and on Thursday we're going to have one for app. Just going to invite you to both, you can just sit there and listen or ask questions if you have any, but that's the thing.

After this, I will — actually this week I will push Martech to give us information, and once we have those we can start the integration. Without those we can go nowhere.

One of the things where web is probably better than app is that in web we just need to integrate the SDK, set a user ID, and that's it. All the rest will be inherited from Amplitude, because there is a direct integration between Amplitude and Braze, so all the data that they need from the user will come through Amplitude. But again, I need confirmation from Martech that this is exactly what they want. Without that we can't do anything. The usual situation.

Okay. This is the Braze thing.

Regarding TraceCheck — great work last week and the week before, I think we are in a very, very good position here, and I'm in the state where whenever Alex wants to release, we are pretty much good to go. Do you have any ticket assigned to you that still needs working?

**Them:** No. Things are coming through from time to time — like Maria has some questions today, that issue she posted, some UI things that we need to take care of that don't match the design exactly, that sort of thing.

**Me:** Sure.

**Them:** Yeah, there's some small stuff here and there, but no tickets.

**Me:** Is Jira updated?

**Them:** For me it is… actually no. The ones in progress, I need to move my tickets.

**Me:** So all this, code reviews, things here. Okay, yeah, I just picked up one small thing here, I have an agent doing the thing. But yeah, have a look at this, let's keep the board updated. But I'm gonna push for releasing this Wednesday. I would like to release it before going on holiday.

Other points here are the following. I am discussing with Alex because I want him to present a roadmap to us. I don't like working with moving targets, we need to start to plan in advance the efforts and what we want to do. So I'm going to push for this tomorrow, I'm going to have another meeting with him. He is new in the company so he is used to do everything by face, used to kind of big things by the day. I want him to start to be a bit more planning.

In my absence, what I'm going to push for is: fix bugs, guys. That's it. Because there's no worth in adding new features. Let's try to fix bugs, it's just going to be two weeks that I'm not around, please let's do this.

Andrei, if you have any issue from a technical perspective — because they are going to try to squeeze in things that you have no clue about — please talk to **Heitor** and/or **David Matellano**. You can talk to Matellano if you're a bit more confident with him. But please, let's not try to add more stuff before this thing gets released, or they are trying to do whatever they want to do. Also because I am not that confident in web, which I think you are the same, because web is a bit of a black box for us.

Good news: Heitor started to work on sourcing for a web developer.

**Them:** Nice.

**Me:** So the plan is to try to find someone by September, whether internal or external, let's see. And once this person joins, kind of stays with you a bit in this project, and then you go back 100% in apps if you want to — obviously if you still like web you can keep working on this. Let's see. This company has a lot of new things. So let's see how things are moving forward.

Okay. Let me see what else I want to talk about today. How are we going with tokens?

**Them:** Good thing the company has money, I guess. I've used about $2,000.

**Me:** Okay, in roughly three weeks?

**Them:** For the past month, starting on the 6th. It's now $2,000.

**Me:** Well, that makes $500 a week. For this project, which has been delivered in record time. I don't think — I mean, Matellano is okay, it's like, I just need to know that you know that you're spending this money, but considering the importance of the project there's no issue in this spending. Obviously if you were to do smaller things it would complain. But for now it's okay with this kind of thing.

How do you feel about Kilo and those models?

**Them:** It's not as good as the other, the frontier guys, but I don't know whether it's the harness or the model itself, because I've been monitoring online what people say and they consistently rank Kimi as one of the best. But yeah, I think it might be that it's the harness that's stopping it quite a bit, and maybe some of their scaling issues from time to time — because I basically can't work with sub-agents, because when they complete their work the main agent never finds out and it just sits there. And pretty much all the time it gets stuck in a position like that and I have to go in and restart it, because even if I type to it it doesn't really process what I type. That's something that I've passed back as feedback to the Kilo people through the video. But yeah, other than that it's holding its own, I think. As you've seen it's gotten some of the UI pretty good. And yeah, like this is one of the rankings out there and it's like fifth place right behind the big guys.

**Me:** Yeah. Max and high, okay — oh, because they're also ranking the thinking effort itself.

**Them:** They rank them by different things, like which one's best for front end, best for like science, for math, for other things. But I'm not 100% sure on the different filters and functionality, I haven't played quite a bit here.

**Me:** Okay. What's the name — Arena?

**Them:** But just yesterday they released the Qwen model, so that would be interesting to look into as well. Not as good as Kimi. But their local model is apparently pretty good, something that you can run on your hardware.

**Me:** That thing is insane for me.

**Them:** So it ranks about here. So this is 5.4 — in March, in May this used to be the top model anywhere, and now there is a model you can run on your — pretty expensive but doable — hardware that's better than this.

**Me:** Yeah, yeah. The capabilities of these models. Okay, this is very interesting to me. I have a personal opinion between Fable and Opus. But I understand why people would put Fable as first.

**Them:** Opus has been doing quite a lot of things that probably shouldn't do, like very defensive, very edge-case-handling stuff that adds a lot of lines and a lot of effort and a lot of tokens too, but maybe you don't want [that]. Because typically you would ship the happy path, some of the edge cases, and there's issues, [they] pop in and you fix them and you add support for those issues — typically how development has been working in the past. But it just goes and thinks of everything that can go wrong, if there's like people trying to steal anything that can happen ever, and that's — that coding gets quite sloppy. So that's something against it.

**Me:** Thing is that I think GPT-5 is exactly like this — is extremely verbose, is extremely looking at all the minute edge cases, trying to cover every single detail. Sometimes it's like, dude, just do a new API endpoint, [you] don't need a freaking bank security system here. And it's interesting how these models are moving in that direction, which hey, it's great because security, because all of that, but sometimes it's too much.

Okay, interesting. Okay, Andrei, I want to show you something, I'm gonna share my screen, because in my battle in understanding things here I finally got a bit of Datadog ideas, the things that I understood. I had a chat with **Thiago** on Friday and he explained me finally what Datadog is and how it's supposed to be used.

So Datadog itself is nothing other than a way to collect logs from a web application. And these logs can be collected in two ways. Through a library that you install in your code, and this library sends logs to Datadog. Or an integration with Google Cloud Platform that allows Google Cloud to push logs into Datadog. And those are two different capabilities.

Why — because the first one, so Datadog itself sending logs to itself, allows us to check specific things on a hardware level as well: how many requests, specific errors, load balancing things, memory issues, response times and all of that. While the Google Cloud Platform version of it is simply collecting both front-end and back-end logs that allow you to do stats things or understanding specific behavioural problems that may arise. So "Maria's not able to cancel her subscription" — let's check the logs and see what our user is doing and why she's not able to cancel, and through this platform you will be able to do that.

**Them:** Through the Google Cloud Platform.

**Me:** Me too, me too. So Datadog is just another layer on top that allows you also to create dashboards, so you have at a glance the situation of your app.

As of this morning we have configured Datadog sending data to itself, and I have **Julián** working on getting Google Cloud Platform to send data to Datadog. Once both are done I will try to create dashboards for us to have a look at that can be useful. But meanwhile — and again this is just for you to understand — if you go to APM here, this is where you have all the logs happening in real time and you see all the issues that may arise. So you see the number of requests, for billing for instance, total time, response latency etc., all these kind of things, all the deployments that happen, traces, so which APIs are responding good or bad. This is a one-hour time frame, you can see errors — oh, there is an error, need to check this one — then you have the live debugger, you know, these kind of things. With AI you're going to be able to learn better about this kind of tools. Again this is mainly for your information, if in the future you will need to do some live debugging or understand some behaviours and you don't have any other ways to do it.

That's it, that's what Thiago explained to us. Speaking of Thiago — he is a staff engineer that works mainly on the web part of MAO, and what I'm planning to do is, when I'm back from holiday, try to involve him to give us a bit of advice on how to improve architecture and make this vibe-coded app into a kind of a better state. But nothing to be done by now.

That's it I would say. Anything on your end regarding TraceCheck?

**Them:** [Nothing] comes to mind. Seems like we fixed Maria's issue.

**Me:** Is it, or was the—

**Them:** Oh no.

**Me:** No. That's not working. That could also be the fact that we keep changing things in terms of configuration — Parapet, with that, removing, changing. Parapet: if you have any issue in Parapet you can talk to **Durbán**. If Durbán doesn't respond because he's too busy, talk to Heitor — they're both working on the platform. So anything related to Parapet, feel free to ask them.

Okay, Andrei. Think that's it.

**Them:** Holiday?

**Me:** I'm going in the Alps. I'm gonna do two weeks hiking — well, I'm gonna stay two weeks in a hotel with spa and everything, I'm gonna go hiking and then come back to sauna and those kind of things, to relax as much as possible. I need green, I need not technology, I need chill, fresh air and this kind of things. Unfortunately my brain is working in a different way and [I] already built a website to find trails — already scraped all the data from all the local kind of sources of data and I literally built a full thing.

**Them:** [You could] ask ChatGPT, you can now go in and ask it to research things and then build your website so you can explore it with people. It didn't work?

**Me:** Yeah, I tried, I tried — not as good as I wanted, but yeah, I literally… that's what I did. You have all the trails here, you can zoom in, and if you pick a trail like this one you go in, you have a 3D map of the thing, you see the different kind of elevation gain just to see where is good or bad, and then a few kind of information here, and I'm adding a few other points just to make it complete. But yeah.

**Them:** Sounds [good].

**Me:** That's me not wanting technology around me during my holiday.

Okay, before we close I have a question for you. Which part of the engineering manager job do you think — so, why would you like to choose the engineering manager path, which part of it do you like, and which part of it do you think you would like to develop in the future?

**Them:** Well, when I joined as an advisor it was mostly in this path: managing a couple of different projects, working with people to get the project completed and implemented and out there, resolving any issues that at what point might pop up, that sort of thing. And I just feel like the engineering [manager] is the next step and the higher-level overview of that, where you work with people that work with the people. So I feel that's why — just like the natural progression for that.

**Me:** It is the natural progression, it is a bit more complex than that for sure. And why not going down the staff engineer path?

**Them:** It's more of, from what I've seen — I haven't worked as staff, and like you said, picking up something and developing it to the benefit of the company, like Parapet and the MartechKit, that sort of thing — and that's also interesting, but it's not as much as working with the people and the general product side of things, from what I've seen. I'm not sure whether that will be the case in the future or not, but yeah, I signed up for the iOS advisor as working [with] people, appeals I think more to me. And yeah, that hasn't changed.

**Me:** I think so. And this is to give you visibility: the advisor role is a step slightly below the natural progression into engineering management, for sure. The fact that staff engineer in this company works on this horizontal initiative is partially correct. And for instance Vlad now is involved in the MartechKit — he's being hired as, you know, as an advisor, because we need someone to be more hands-on with experience in apps in this specific initiative.

I feel that the staff engineer will give the direction, the technical direction of something. An advisor can — it's okay, it's interesting for me. Staff engineer is not only related to those kind of initiatives. [I] think an advisor or engineering manager must be on top of those initiatives as well. As in, right now I'm also taking care of the MartechKit as an engineering manager. I'm not coding, I'm not doing anything there, I'm just overseeing and trying to balance things in that direction.

**Them:** [It's] not just like you only work on that and never touch anything else.

**Me:** Which part of advisor do you like the most?

**Them:** Very existential I guess. Just working with the guys, setting the direction and the vision and working with people through the different projects, the problems that they might have and unblocking them in certain situations — like you've been doing a lot of that for me for example — and that sort of thing is something I enjoy. Getting the process to run smoothly and for the factory to work, to automate things, is something that I found is very — something that I enjoy a lot. And this sort of thing is automating the product pipeline. It's not like math, it's not one plus one is two, because there's people involved obviously, but getting it to a smooth process where things just keep happening, and for me to just go in and work on the things that don't really support the process — that's something that's interesting to me.

Where with like the staff engineer I feel like I already automated a lot of things into the day-to-day work of like developing a product by myself, so I feel like that's something that I can do with no problem. That's why it's not as appealing to me. I don't know if that makes sense.

**Me:** It does make sense. So if I remove myself from TraceCheck for instance, would you be able to do — well, in this moment, both jobs obviously. Yeah, because that's the hard — it's not hard — the subtle thing about engineering management is that you are not really attached to a technology per se, because you are abstract, you go higher level. So would you be able to do this job in TraceCheck?

**Them:** Like, in the past I probably would have said no, because you don't only have the technology in there, but through this project I feel like that doesn't matter as much now, and it's a big different skill now, how to manage that. So I feel like yes.

**Me:** But you're still more attracted to apps?

**Them:** Like I said, that's what I know. And like for example now with Maria, she says there's some still UI issues in there and all I can do is go to the agent and tell it "fix it please", where if I work on apps I know what to do and how to fix it, even if it's Android I know enough. And I might get it with web again but it'll take longer and not be as efficient. That's the thing that's stopping me. But yeah, like I said, working on this project I feel like websites also aren't that big an issue, because I could get 99% there with TraceCheck, and we know the design is not perfect — it's again almost there — and with some iteration I feel like we can get it exactly right because we did it in other parts of the website. So yeah, this has been a really eye-opening project, where that mantra of "you're just a developer now, you're not a specific-technology developer anymore"—

**Me:** Okay.

**Them:** I feel like that's coming along more and more, and for sure in like six months, definitely a year, that would be completely the case as things progress more and more.

**Me:** I agree, I agree. Still think we need — our personal need — to understand some high-level concepts: how a backend works, security concepts, how specific details of Martech libraries work and they interact with the rest of the website. But the sticky-footer part, that's sold.

**Them:** And so when you're asking whether I prefer apps — I do prefer it because I know more and I can do more there, but I also feel like web won't be an issue.

**Me:** Okay, interesting. Interesting for me, I like this way of thinking. Nice. And going back to the advisor role: which part do you hate the most?

**Them:** Specifically having to work with people who refuse to communicate. Getting them to communicate, and communicate effectively — and that was something that was really the worst, at some point.

**Me:** The hardest part of being a manager in general? To being able to get the information that you need out of people that don't know how to communicate?

**Them:** Yeah.

**Me:** That's hard. So you need to learn how to ask questions.

**Them:** And even though I like spell it out for them exactly what needs to happen, I then come back to them later and it's not that — completely different. So like, I tried and I gave up, and it was everything copy-pasted 10 times.

**Me:** That's a trap that they fall into as well. It's not easy. My advice to you is yes and no: if you're managing those people, do not do what you just said, because otherwise they would never learn. If it's a stakeholder that you have to work with — saying product for instance — do not do this thing, [because] you need to coach them to be able to get the information out of them in the future. If it's a one-off, go for it. That's my advice here.

Okay, this is very interesting to me, to see through your eyes this part of your job and how you like it and why you like it. Okay. I'm gonna keep asking you questions around this topic because I want to create sort of a way for the future for you to move towards. For me it's very interesting — you have all the skills to become a staff engineer and the skills to become an engineering manager. I see some pitfalls in both. And I'm gonna try to help you reach what you like the most, or not, or this way to choose another path. Let's see, let's see. But it's good to know, it's good to know.

Okay, Andrei — anything else for you this week?

**Them:** No, I don't think so.

**Me:** Just to close it up: gonna push to get TraceCheck live — it's already live, two things, it's already live, but I'm gonna try to get Alex to, you know, gonna push it officially for the company to know. I'm gonna also keep you in the loop for the Braze thing, but again we depend on Martech's decision, so do not do anything in that sense until Martech takes a decision. For me I still have a question mark around Braze: if we want to wait for MartechKit to integrate it, or if you should move forward with iMote integrated there. Or if you want to integrate it yourself into the MartechKit and then integrate it into iMote. But that's another conversation, let's see how this week evolves and then we'll catch up throughout the week.

Thank you so much, have a good week, speak soon, bye bye.

**Them:** Yeah, bye.
