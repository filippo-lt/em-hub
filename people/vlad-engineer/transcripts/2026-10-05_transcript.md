# Transcript — Vlad / Filippo Weekly 1:1, 2026-10-05

**Source:** [Granola](https://notes.granola.ai/d/434e24ba-e915-4048-be67-87ac5f985e7a) · 11:00 CEST · F = Filippo, V = Vlad

**Filippo:** Good morning.

**Vlad:** Good morning. Yeah, camera is here. How are you doing?

**Filippo:** I'm okay, what about you?

**Vlad:** I'm also okay.

**Filippo:** Okay, okay, we are all okay.

**Vlad:** Another Monday. Yeah, that's fine.

**Filippo:** Hey, yeah, it's another Monday. How is your flu? Last week you were a bit, uh, you said at the beginning of the week you were not feeling that great.

**Vlad:** Yes, exactly. By Thursday I was already fine.

**Filippo:** Okay.

**Vlad:** I just booked it off.

**Filippo:** Okay. That's good. Nice. How was your weekend?

**Vlad:** Uh, pretty interesting. I had some activities. I went dancing again. There were, well, not really little dancing-related events here in Valencia, like 40 or something people. This doesn't happen every weekend for me at least.

**Filippo:** Nice.

**Vlad:** It was very interesting to see and meet a lot of different people. That I met before in the different context. It's funny how people have different personalities, you know, for when they're just chilling out, spending time with friends, or versus when they're coming to like some kind of other designated social activity.

**Filippo:** Yeah. Yeah. Yeah, that.

**Vlad:** I also have different personality, I know, but it's always fun to discover new sides of personality of people who you already, like, you think you know, but obviously you don't, you know, only one part.

**Filippo:** Yes. Yes. Yeah, that's especially— no, I guess you're not talking about people from work. But especially seeing the difference between people at work and people outside of work, that they are completely different sometimes.

**Vlad:** Oh, that's true. That's always like that.

**Filippo:** Yeah, I am very different from me at work and me outside of work. Vlad, um, I don't know if you noticed, but I just sent you a quick Slack message— Slack, sorry, chat message. No idea why we don't use Slack in this company, but that's another story. Why is that? Because I noticed that we usually, when we start to talk, we spend a lot of time because we go into the details and sometimes It's not that I forget to give you priorities, but maybe they are confused. In our talks, right? So I prefer to put down in writing the 3 main things for this week. That's it.

**Vlad:** Okay, makes sense. Is it like it lists in this exact priority or that's

**Filippo:** Yes. Prioritized list in order of priority.

**Vlad:** Yeah. Okay. Noted. So I will stop working on Marta Kit for iDesign for now. Unblock Alexei because we had, we were supposed to be doing related work. And focus on trace check. Makes sense. Okay, that's very clear. Like it.

**Filippo:** So Yeah, I think it will clear the air and then we can start to talk about your points. I have a few other points that I want to talk about, but at least we have that in writing and we know what we need to do. Cool. So Vlad, I'll leave the room to you if you have anything for me.

**Vlad:** I'm not sure if I have a lot. Well, a lot of work related to AI design, like actually a lot of work. If the goal was some time ago to be spending about 20% of my time, it's not like that. I'm spending 50-50 now. From today it will change a little bit because I will focus on suppression list for emails and phone numbers on trace check and only once that's done I will switch back to the AI design whatever day it may be. I hope it's soon.

**Filippo:** What? What is requiring so much of your time in AI design?

**Vlad:** Last 2 weeks it was all the security fixes. Like a lot of work, even just people are highlighting some issues. I'm like, okay, let me take a deeper look. Rewriting tickets, simplifying the tickets, descopying some of them because AI findings, as they may sound, professional after a deeper look and engineering influence. So it appears that some of them are just bullshit.

**Filippo:** Yeah.

**Vlad:** Splitting some of the tickets, creating new extra ones because apparently there are dependencies that were not found during the original round of creation.

**Filippo:** Yeah.

**Vlad:** So yeah, I added a lot more tickets than what was created on day 1. And majority of the, all the new ones required actually my time and effort and expertise to, okay, let's take a deeper look. Let's figure out if that's correct.

**Filippo:** Okay.

**Vlad:** This part. And the second part is SmartTicket integration.

**Filippo:** Yeah.

**Vlad:** The generally speaking code base on the AI design is messy. Very messy. And yep, I got AI do some work for me. But the sheer amount of obviously breaking changes It introduces just to adapt AI design is insane, and it actually requires a review of like one by one. Okay, did we lose the integration? Did we lose this integration? Is this ever firing? Yeah, I believe that majority of the work that I was doing now manually reviewing before and after and finding proper way to fix is actually supposed to be handled by MartaKit in some future. Because there are much more work related to identifiers, identification between different Third-party vendors. AI design has more. Somehow.

**Filippo:** How, what, like what?

**Vlad:** Let me open it and find. Too many projects at the same time. So what we had here, we had a relation between TikTok And AppsFlyer. Not sure why, but it was there. So I'm supposed to preserve that. It sets, generally speaking, AI design sets Device ID as well as another connector, but the RevenueCat ID. Not sure which exactly. Who uses it? But if it was set this way, I probably cannot skip it. Then I got feedback from Martech team and they pointed me to the PM that I still did not contact about the events because I'm too busy with a lot of other stuff.

**Filippo:** Regarding PM, please do not contact Sergio Hueso for this. Contact Miguel and ask Miguel to review those events. That's his job.

**Vlad:** Okay.

**Filippo:** One thing that I would like to understand here, and this is more like a way for us to discuss. I'm not 100% sure. This integration point that you are mentioning are supposed to be there. So in your opinion, is there a way for us to investigate if this was a requirement coming from MarkTech or A rogue AI agent just doing things.

**Vlad:** Obviously there is a way. But yeah, it just requires talking to a whole bunch of different people again, this time not generally speaking about the list of events we have, but very specifically. Considering the format of the case, I doubt that that was a rogue agent. Somebody requested that.

**Filippo:** Okay. Okay.

**Vlad:** I am pretty sure, I am not sure if this request is still standing after many, after much time, or it may not necessarily be needed anymore.

**Filippo:** Okay.

**Vlad:** But that's not a big or not a complicated situation to keep. The complicated part is more like It's now the setup for A-Design, like the startup, is now working by sheer luck and a bunch of random delays. So we initialize this service, then we wait 0.3 seconds to start up another one, then we have 10 seconds timeout until one of them returns, and then we start the third one. Like dependency injection not detected, owner of all these calls not detected, error handling not detected. Yeah. That's like coding issues and even Opus is like, oh, I don't know what's happening here.

**Filippo:** Damn. This is bad. This kind of task should take This integration, I mean, shouldn't take this long to be done. But obviously, if you start from scratch, it's probably a 2-hour job. If you have to do all your little exploration that you're doing, it's obviously going to take more time. I understand. I now understand the reason behind this. Okay.

**Vlad:** Yes, and then I will ask once I'm done, well, I have a set of commits, I need to check if I didn't lose anything and AI is Partially helpful here. You know, every new agent tells that previous one was wrong when I asked it to review it. This sounds correct. So I like, okay, I will figure it out myself again.

**Filippo:** Sounds like a bunch of developers.

**Vlad:** Yes, yes, yes, exactly. So I will ask Alexei to review it.

**Filippo:** Okay.

**Vlad:** Manually because he has the context. He knows which of these requirements, well, some of these requirements were actually requested.

**Filippo:** Okay.

**Vlad:** Yeah.

**Filippo:** Okay.

**Vlad:** That's what I'm supposed to do, but now I am supposed to do this closer to the end of the week. I will not be working on this today.

**Filippo:** Um, for me, AI design-wise, the important thing here is to delegate the security work to the developers. What are the steps that we need to take to get there? Probably you need to review all the tickets as you are doing.

**Vlad:** Yes, and split some of them that require different people. So we have one ticket for one person, what Miguel basically asked.

**Filippo:** I'm wondering. Isn't this something that someone can help you with?

**Vlad:** Oh, absolutely. I'm pretty sure. Well, I'm not sure if Miguel can do this. I believe Miguel should be able to do this.

**Filippo:** To understand what's frontend backend.

**Vlad:** He seems to be willing to understand what's happening. What are these tickets? About.

**Filippo:** Is he the right person to do this?

**Vlad:** Maybe not. This should be somebody from engineering. So. Prob— like, I, in the companies where I worked before, I used to think that any of the engineers on the engineering team can read through the requirement. If it's already defined pretty well to figure out if another ticket for, let's say, if this is iOS guy reviewing another the same ticket for Android needs to be done or not. Or if backend engineer checks it, okay, something new should be sent, they can also figure out that somebody have to be sending this work. All of them should be able to do that.

**Filippo:** That is exactly. We are paying this guy.

**Vlad:** ViewZ.

**Filippo:** We are paying these guys a lot of money and they are senior. The work that you are doing seems to me babysitting.

**Vlad:** It also feels to me like babysitting.

**Filippo:** Okay, so Why did we reach this point? Is it because we never asked them to do it or is it because Miguel is pushing for you to do it?

**Vlad:** 2 points, but different ones. Well, the Miguel asking me to do this. Yes, Miguel doesn't trust him. This part. Some would make sense. Miguel is not sure. I understand that. Maybe not respect it, but understand it. But also these guys are asking me questions. Clarifications regarding the tickets that they should absolutely be able to do themselves. Some, a few times I tried, you know, be like, and what do you think? Like just returning it to the sender and they came up with the correct answers after doing some kind of investigation. Which I, okay, so they can get answers. But I just don't want to be doing this all day.

**Filippo:** I don't think your time is valuable spent like this doing babysitting work. We are paying these people to do it themselves. I'm okay if they come to you with some questions. Some. But by skimming through all those tickets, security tickets, 80% of those are literally One-liners that everyone can understand. So Why should you spend 2 days this week going through each one of them and writing the acceptance criteria and say, Alexei, you do this, Mitro, you do that? Let's, hmm. But this is my view of things from where I'm sitting. So you maybe have a better context.

**Vlad:** No, that's a pretty accurate description of what's happening. What, well, it would be nice to put some owner onto these tickets.

**Filippo:** Good.

**Vlad:** And by the structure we have in this team, I am the owner.

**Filippo:** No, you're not. No, you're not. Vlad, you are the person that oversees the engineering team, but you are not part of the team. You're making sure that things are moving smoothly. But you're not babysitting. Developers. If we had hired junior or mid-level developers, I would totally say to you, please help them figure out these things. But we hire senior people exactly for this reason. You need to make sure that whatever comes out of their coding is correct and we're not gonna, you know, break anything. But we have the tickets, they just need to read them. And act on that. Yeah, maybe some of the tickets are AI slop. Totally agree because I use the AI to generate them. I don't need you to do the job, the work.

**Vlad:** So who should be the owner?

**Filippo:** Oh, I'm gonna write in that chat that we just had with Miguel saying, Miguel, ask the developers to pick, split that list into 3 parts, one for Dimitro, one for Maleksi, and one for what's the name?

**Vlad:** Voilà.

**Filippo:** And they act on them. That's it, guys. I'm sorry, but you are much more valuable in another project right now. So If you leave this project, what's going to happen? Nothing is going to move because Vladka is not around to assign me a ticket.

**Vlad:** That's very reasonable to me. Maybe we should also, we should ask developers to write this acceptance criteria and then they can send me to review.

**Filippo:** Sorry. Great. Agree.

**Vlad:** Reviewing acceptance criteria much better than writing it from, from my side in the first place.

**Filippo:** I would like For you to elevate. Your work. And if you are in the trenches doing the babysitting work, you will never be able to actually do meaningful work. For me,

**Vlad:** That makes sense.

**Filippo:** For me, your time is better spent understanding the whole Martech Kit integration because that is the point where we make money. And I personally trust you a lot. Not an external developer to do this job. I could ask you to delegate to an external developer, but what is going to be the result?

**Vlad:** Good. Should we make them work on integration then? Okay, maybe too risky. Here we have a lot of money involved. Okay.

**Filippo:** Am I saying something wrong? You are there in the team.

**Vlad:** No, you're not saying anything wrong. I do agree with that. At some point I somewhat forgot that I'm here supposed to be an advisor and not necessarily tech lead, for example. That makes sense. I believe these guys should be able to read through the tickets, update the ticket if it's necessary, and ask questions they cannot have answers themselves. But they tend to ask for clarification before doing their own investigation, which is not good for— not a good picture for senior engineers, of course.

**Filippo:** Your instinct of asking, what do you think is the perfect way of dealing with this kind of situation? And this is, you know, you elevating yourself.

**Vlad:** Yep, that makes sense. Like none of them wants to work with Jira. I mean, like refining the tickets. That's another, actually, that's another point that I was struggling last time. I asked guys to review the tickets that were assigned to them. So I can do refinement if necessary. They say that they did, all looks good until they started working on it. Looks like no refinement were done originally when I asked for it.

**Filippo:** I'm not happy about this.

**Vlad:** Me too.

**Filippo:** Where is the blame. Meaning, is it them not taking responsibility? Is it product not giving them the responsibility and treating them like babies? Where do you think is this?

**Vlad:** That's a good question. I will be thinking out loud now. I don't have a strict answer.

**Filippo:** Please, please, we are doing that.

**Vlad:** Okay, so, uh, Developers. are feeling very convenient and very comfortable in the position when somebody have to babysit them. That's like, is Viponize incompetent about that? Not necessarily, but close. From the product side, I do not really see an issue here. Product have little trust in developers. Therefore, is coming to somebody who he can trust, to myself, with questions and concerns, which is probably correct thing from his side. Yeah, I believe developers could get better at this. This is what I would expect. But like, I also understand this major, major difference between people who, between developers who are working on the product. As a product team and they developed something that they will have to maintain and something that gives them possibility to grow against outsourced developers. And we all understand that outsourced developers have little to no motivation to progress because their company doesn't pretty much let them to do this. So there is no incentive to go above what they're doing right now. So they just don't.

**Filippo:** Your reasoning is perfect, and I agree. 100%. On it, there is one small detail that you're not considering all of this.

**Vlad:** Enlightened me.

**Filippo:** What is the difference between These developers. And Someone with a very good AI.

**Vlad:** I did not understand the question.

**Filippo:** What if I take that Epic with all those white, white book tickets for security. And I ask Fable to You know, go through each of them, dispatch an agent. And open a PR for each ticket. What is the difference between this and the work that this team is doing? I'm creating extremes here, but

**Vlad:** I see. I understood now. I don't think You will have big difference. I am pretty sure. Alexei and Volo, both mobile developers, are using AI for everything. And they are not good at this.

**Filippo:** Sure. That's my problem.

**Vlad:** They just prompt, maybe send the link to the ticket.

**Filippo:** Okay.

**Vlad:** Maybe they review or test manually after the fix and push it to PR. From the state of the code I see, I don't review it, I just scroll past it, I see that they are not thorough about what they push. Kilo is making a lot of findings as an AI review. And they often have to go and fix what Kilo found.

**Filippo:** I don't need developers like this anymore. I'm sorry. If you, Vlad, have— let's start this conversation 25 minutes ago. You come, you start to talk, and you say, hey, I'm spending a lot of time reviewing these tickets. For security. I'm like, okay, I need to go through each one of them, making sure that they make sense, and then create acceptance criteria. Let's stop here. Let's say that you do this. If you take this refinement that you're doing and I tell you, Vlad, here is $1,000, burn them in tokens.

**Vlad:** Well, that still will require some attention for me from my side to test it manually. Of course, it will be time waste, but yeah, it will be pretty easy. Fable is very much capable of doing majority of the work that these guys are doing.

**Filippo:** Perfect. So I don't need humans anymore. I'm, I'm again, I'm going to an extreme here. But if we remove that part as well of the thinking of, okay, I can write myself an acceptance criteria for this one-liner, if we remove that step, I don't need a team.

**Vlad:** Yes, that sounds about right.

**Filippo:** Okay.

**Vlad:** You need A backend engineer though. This dude is good. Like he's arguing about everything, majority of the tickets that I created and he was right in all of them.

**Filippo:** I know. I know.

**Vlad:** Engineering from his side is very impressive. From mobile side, I'm not impressed.

**Filippo:** Okay. Sorry for this debate. But that is what I wanted to reach today with you. It's like you are already doing

**Vlad:** No, fine.

**Filippo:** A great job into triaging all of this. But we are going too far. And not because you are It's something that you like. It's something that you found yourself in doing.

**Vlad:** Well, There is clearly part of the blame on me because, yeah, I could probably not be doing this. I just never considered delegating further.

**Filippo:** We cleared the air, Vlad. What I'm going to do is I'm going to write in that chat with Miguel saying Vlad is busy with something else. We need the team to triage all these tickets. I don't know how, I don't know when they need to do it. And by Wednesday, we need to have each ticket assigned. We need to have questions, if any. We need to have acceptance criteria. That's it. Because I really need you to focus on something more important.

**Vlad:** So let's see if we can make these guys just work. Better.

**Filippo:** I can make them work.

**Vlad:** That work, you mean you can make them work or you can do— okay, yes, okay, yeah, let's try.

**Filippo:** Yes. Because there is a small fallacy in your reasoning on external developers not wanting, not having any push to grow.

**Vlad:** Incentive. Yep.

**Filippo:** But there is another point here, which is We use external developers because we can add more or remove some from a team if they are not performing. If I can replace them with a few thousand tokens, it's way cheaper than hiring them. Trust me.

**Vlad:** Of course.

**Filippo:** So they need to prove themselves to be better than an AI agent.

**Vlad:** Well, that's tricky because they're doing testing manually. There's something that we, like, we can attempt to replace it, but AI is not there yet to judge the correctness.

**Filippo:** Great. I agree. I agree. I agree with you.

**Vlad:** So let's just put more responsibility on them.

**Filippo:** So Yes.

**Vlad:** They are using AI. All the APRs are created by Cursor in the very bottom. It says explicitly, nobody hides that.

**Filippo:** Perfect. Perfect. Perfect. Okay. Does it make sense?

**Vlad:** Yeah, absolutely.

**Filippo:** Nice. Okay, Vlad, sorry to jump straight into this point, but I think if I can replace, if I can free up your time more, I think it's worth investing.

**Vlad:** That's a good one. I like it. Absolutely. I also like this approach to a solution. I don't like what I was doing last 2 weeks in AI design. Like I was doing because I thought that I have to and there is like the only way. You're thinking a bit outside of the box. Yeah, sure. Let's do this. Let's make them responsible for delivery. I will review the acceptance criteria.

**Filippo:** Sure, sure.

**Vlad:** We leave notes like we have. Somebody needs to do this and I am an advisor for that. Sounds good.

**Filippo:** If you find other points, In your week. Where you think you could remove or move responsibility to someone else. Let's discuss about it or even act alone around this.

**Vlad:** Noted. Okay. I will try to be, to not just keep an awareness of where my time goes, but also why my time goes there.

**Filippo:** Correct. Great, thank you. Do you have other points?

**Vlad:** Maybe.

**Filippo:** Okay.

**Vlad:** Can we make also somebody to review what's happening with all the analytics events and providers who is not me?

**Filippo:** Uh, yes. Product owner. Depends. Wait, let's try to split this into different areas. What kind of problem are you trying to solve?

**Vlad:** The fact that Martech Kit as an SDK provides tools to send analytics events to Specifically AppsFlyer and Amplitude. And when migrating to Martech Kit, I need to figure out what to do with existing analytics layer in the application.

**Filippo:** Yeah. Yep. Yep.

**Vlad:** That has 4 analytics providers. Not just 2. And some of the events I feel like non-canonical but should be. So somebody have to review this manually. Yes, review this, decide. Can we drop any of the analytics providers? Is anybody using them? And then once we have a clarity on what events goes where, Implement this. Using the tools that we have.

**Filippo:** You said you asked this question to Martech. They came back with an answer which makes sense to me.

**Vlad:** Yeah, it's not bad. Yeah.

**Filippo:** So as far as understood, what they are saying is amplitude carries product-related events. We send only these 4 events to AppsFlyer. Anything else doesn't exist. In terms of events providers. In terms of dictionary of events or list of events, whatever you want to call it, Product is responsible. So if I were you, I take literally Cloud, give me the list of events we are sending. Here it is, the list. Take the list. Paste it to Miguel, review this, tell me what to keep, what to remove.

**Vlad:** Miguel doesn't know. I opened the question to Martech Kit because Miguel told that he doesn't know.

**Filippo:** Perfect. Perfect. We are going to remove all of them. We only keep the one from Artikit. And this is very clear to me because I discussed with Sanchez about this. If they don't know what this is used for, we don't save it because it's costing the company so much money, you have no idea. We are talking about millions every year to Amplitude because we have random events just sent because one day maybe we will need this.

**Vlad:** The thing is, Martech team. Knows. What majority of these events are for? Miguel does.

**Filippo:** Let's split it into group of events.

**Vlad:** Yes.

**Filippo:** The events in the MarTech Kit which are related to monetization, those must be used correctly, and you already have inside them in MarTech Kit.

**Vlad:** Yes.

**Filippo:** So if you find in the codebase something that is that one or some kind of version of it because it was written badly, Let's replace that and use the correct one.

**Vlad:** That's obvious. Yes.

**Filippo:** If you find any random event because Blue button tapped event. If product cannot give you a reason for that event, we will remove it.

**Vlad:** A question.

**Filippo:** Sure.

**Vlad:** Does Martech team Only works with canonical events.

**Filippo:** Yeah. They do.

**Vlad:** Only with canonical. So all the custom app events, they are not for Martech team at all.

**Filippo:** They do. Correct. They are for the product team.

**Vlad:** I didn't know that.

**Filippo:** Yeah.

**Vlad:** I thought that Martech team may also specify what apps may need as an app event. Okay, that changes a little bit.

**Filippo:** See it like this.

**Vlad:** Things around.

**Filippo:** So we have a place where we throw a lot of events and these events are in 2 major categories, could be 3, 2 major categories. The big one is where we make money. So we need to know if a user goes through the onboarding, if the user sees the paywall, if the user closes the paywall, and these are the canonical events that Martek is talking about.

**Vlad:** Yes.

**Filippo:** Then you have another set of events that product people add to the app to check if a feature is used, which makes sense because they are feature-related. I'm launching a new feature, a blue button. Versus a red button, I want to check if the user tapped that. I need a product event related to that, and that is something that product owns. It's not engineering, it's not marketing. Maybe, and I say maybe, one day engineering needs a couple of events themselves because, you know, we need to check why a specific error happens and we track it in Amplitude. Totally fine, that is on us.

**Vlad:** Okay. All of that. I don't have to do. Alexei is perfectly capable of getting the list of events, taking a look at the Martech kit What canonical events are.

**Filippo:** Yeah.

**Vlad:** Comparing the 2.

**Filippo:** Yeah.

**Vlad:** And deciding what needs to be patched because it's not following canonical format and what just doesn't fit any of the holes and reporting this. So Miguel makes the decision about each and every single one of them.

**Filippo:** It is. Correct.

**Vlad:** And the rule. I don't have to be doing any of that. However. There is one hole in all this process. When I open the ticket to the Martech team, They told me to keep all 4 events for AppsFlyer that we send now.

**Filippo:** Yes.

**Vlad:** In the kit, in the SDK, we have only one. Which means that the idea that Martech team works with all the canonical events is already not completely true. There are more events that are needed to Martech team that are not in the iOS SDK.

**Filippo:** Could you do me a favor and Or you write yourself a question. In a chat or you open a ticket in the, in the Martech board, the same one that we used. That you used. Because if you find this and these other events need to be tracked in the Martech Kit, we simply move this to a ticket into the Martech Kit and someone, Victor, will act on it.

**Vlad:** Okay.

**Filippo:** Because this is not something related to AI design, it's related to all the apps.

**Vlad:** Sure, I already have a ticket open. I can do this there.

**Filippo:** That will make sense to me. Okay, nice.

**Vlad:** But we asked for a question. Are there not AppsFlyer, but maybe Amplitude events that Martech team works with? That are not in the SDK?

**Filippo:** No, because they created a repository. Specifically for Amplitude. With the list. Of canonical events, they will check. And this is a smart way because what we do with the Martech Kit is that we, when we create a new build, we have a script that goes fetch that list of events and create the enumeration for us to use. So that every single app has all the same strings for each event.

**Vlad:** Okay, I see. I understand. I don't trust this answer enough, but okay, let's do it this way. Let's do it this way.

**Filippo:** The reality of things is what I just told you. Then we need to also try to play by the game, which is instead of remove everything, Create the list of events for you or Oleksii, I don't care. Honestly. And get this in front of Miguel saying, hey Miguel, these 10 events are Martech related. What about these other 20? Should we keep them? Or can you provide an explanation for them? This is how I would behave.

**Vlad:** Yes, I think the Google spreadsheet isn't coming.

**Filippo:** Yes.

**Vlad:** Should we do the same from Android side in parallel?

**Filippo:** Yes.

**Vlad:** I feel like we should.

**Filippo:** Absolutely.

**Vlad:** Initialize this process before I get to integration of the Martech pack to Android. Save me some time down the line.

**Filippo:** Yes. Yes. Yes, Vlad. This is the kind of work That you have to do. Not reviewing freaking tickets that a developer can do.

**Vlad:** Okay, that makes sense. It feels much more enjoyable than the other part I was working on last 2 weeks.

**Filippo:** Yeah. More questions, more points.

**Vlad:** Regarding AI design, I believe that's it.

**Filippo:** Perfect.

**Vlad:** I think, yeah, I don't have anything else in my mind.

**Filippo:** Regarding TraceCheck.

**Vlad:** Regarding TraceCheck. Since Friday. I discarded all the work that I was doing and I restarted following the instructions of our conversation. And I was surprised on how different it goes. I tried the model that you suggested, the DeepSeek V4 Flash.

**Filippo:** DeepSeek, yeah. Yeah.

**Vlad:** By the way, there are like 4 of them. Different V4s on Kilo. I found the one that looks better. And I am concerned now. But Eve, Asks much less questions.

**Filippo:** Mm-hmm.

**Vlad:** It does more work. It costs less.

**Filippo:** Mm-hmm.

**Vlad:** Is it missing something important? Hey, welcome.

**Filippo:** There's only one way.

**Vlad:** Complicated and difficult questions. Now it just asked me, do I want the key of the document in Firestore be an email or a phone number or hash of it? SHA-256.

**Filippo:** An hash. The answer is hash, by the way.

**Vlad:** Yeah, I also figured that out. Take. Okay, that's it. However, after that, it proceeded to do the coding end-to-end without stopping for my review at any point. So It pretty much finished working a few minutes before we started this meeting, so I will have to go and review now and maybe rework some parts, not sure. But this feels like much more progress. I also feel like my competency is not going to grow this way. Maybe it will when I read everything because I did not have a chance. Agent just did it start to finish.

**Filippo:** What I see. First of all, has the conversation on Friday helped?

**Vlad:** Yes, of course. Well, Yes, obviously.

**Filippo:** Perfect.

**Vlad:** Yes.

**Filippo:** Vlad, the reality of this is 2 ways. I want you to be part of this team for a bit of time. Because we are working in a way That is not yet seen in apps. So I want you to grasp the way we are working here, and I'm not saying what we are doing is 100% correct. But we are starting to see results and we are starting to see that trusting too much AI or going too fast is we are losing control. But find a good balance there is actually helping a lot.

**Vlad:** Yes, and once we find it, I believe we can translate this information to apps.

**Filippo:** And That is exactly what I would like you to go as a process. I'm not expecting this to happen today, tomorrow, or this month, but in a few iterations in your head to build this process. So The job here is, yes, to deliver features, but to question and to understand the process behind this.

**Vlad:** I will get there. I absolutely will. Maybe not from the first go.

**Filippo:** No, but that's fine. Try to find a balance between, you know, trying to deliver on time, but also question why and how. The in-between. I don't need an Adea developer that takes a ticket and just outsources it to Claude or Course or whatever they are using and create a PR. I don't need that. I need you to think about, hey, okay, 2 different models, completely different results. Why has this taken so little questions? But is this going to work or not? Ask yourself these questions.

**Vlad:** I will. Yes.

**Filippo:** Personal experience. Opus 5.1, still not 5.5, against DeepSeek. Same task. Same results. DeepSeek. Is slower. But is less verbose. Opus is faster, but so much information dumping that you don't really need.

**Vlad:** Yes, my experience tells about the same. Yes.

**Filippo:** But in terms of correctness of the final task, unless you're working on something super complex, they are pretty much the same.

**Vlad:** Impressive. Okay. Well, I will continue working with DeepSeek. I want to try this more. I really like the style of communication of it. Very short and direct and straight to the point without bloat.

**Filippo:** What I noticed And again, this is my experience in general, and everything is changing so fast that, you know, We reached a point where these frontier models are very, they have very little difference one from the other in terms of output. The harness that you build around them. Does majority of the work, how you ask them the questions, what kind of process you built around it, your review process as well. That is gonna help define the final result much better than using one frontier model versus the other.

**Vlad:** Yes, that makes sense, of course.

**Filippo:** Funny enough, today, I have the same results between Fable and Opus, same results. The difference is just the speed. Fable is way faster. And less verbose. But I have the same results.

**Vlad:** Sounds like it's not worth it.

**Filippo:** Depends. Obviously, I'm not saving lives here. I'm just building some shit websites or applications.

**Vlad:** Probably your task is simple for both of them.

**Filippo:** Yeah.

**Vlad:** To discover gift.

**Filippo:** Could be. Could be. Is good. Vlad, I'm checking my notes. Anything else on your end?

**Vlad:** Yes, I have a question regarding the harness that you have in the web race stack.

**Filippo:** Yep. Traceback, trace check.

**Vlad:** TraceCheck repo is called differently. What of these skills you are invoking manually when you work?

**Filippo:** I do.

**Vlad:** Do you do any manual minority, like explicitly?

**Filippo:** I do call manually the deploy to production.

**Vlad:** Okay.

**Filippo:** I do call manually the sync dev. So sometimes agents create branches, work trees, et cetera. When I pull the sync to dev, it cleans up a bit the whole situation.

**Vlad:** It rebases on— yeah, I already used that.

**Filippo:** And And that is actually about it, I would say.

**Vlad:** Oh, okay.

**Filippo:** Give me a second. File Explorer. Oh, well, the Jira writing part is actually Something that I use often. Because it's quite useful.

**Vlad:** It calls it itself from what I noticed.

**Filippo:** Calls itself.

**Vlad:** Yeah, like AI figures out that if it involves Jira, it should call it. So it used it a lot for me, but I never had to ask for it explicitly.

**Filippo:** Yeah. Then Archive plan, it's used by an automatic thing that I have. Diagnose bugs, never use. Docs review is used automatically. Drift fix, drift review, use automatically. Grill me, green me. Grill me, grilling. Handoff. Parallel review. Resolve merge conflict, ship PR. 2 tickets. Never use. They could potentially be removed. The web accessibility and web SEO, they were used once to make sure the website would actually be accessible and SEO ready. But they are not used that much. That's it.

**Vlad:** Okay, got it. That's impressive. So I don't have to, you know, know in depth all of them or pretty much any of them if you manually call just 2 and sync dev for me was called also. By the agent itself. And it was like, oh, but the dev has new commits and the plan number is different. So let's rebase it. Sure, let's sync them. Deploy prod. Staying the pretty much only one to be called manually. Okay. That's your call.

**Filippo:** Feel free. To create a PR to remove some of them.

**Vlad:** No, I'm not trying to remove them. I was asking about like, is there anything I should be calling manually? Because otherwise agent may, you know, not do this or not hint me with it that we have a skill that it should use, but it doesn't.

**Filippo:** Yep. Yeah.

**Vlad:** What you are telling me that no. The skills that are there.

**Filippo:** Yeah.

**Vlad:** Are invoked when needed. I don't have to keep manual, like, track in my head of all the tools it uses in the process. It knows how, right?

**Filippo:** Yeah. Yeah. Nope. Okay, uh, And Uh, Okay. Oh, one thing. Whenever you can, but I keep reminding you. Holidays for Christmas.

**Vlad:** Yeah, I'm sorry, I was planning to do that. I got distracted about 14 times on the way to this. I will do this by the end of the week. I already have a note in my to-do list for that.

**Filippo:** Vlad, it's okay. I'm just reminding you.

**Vlad:** Okay, yeah, I will get in touch.

**Filippo:** That's it. So if next week, yeah, if not next week is not ready, I will remind you again.

**Vlad:** Okay.

**Filippo:** Um, okay, so just to quickly recap. Priority number 1, trace check. Not only delivering the task, please let's deliver those tasks if you can run. Wednesday, Thursday would be great so we can do a deployment and then learn the process, question the process around trace check.

**Vlad:** I will be doing it anyway, absolutely.

**Filippo:** AI design, I'm going to write in that chat with Miguel saying, Miguel, let's outsource this to the developers and Vlad will answer any questions, but I don't want you to spend your time doing that. It's not your job.

**Vlad:** Okay, will you explicitly mention both security audit and analytics related market integration or only the first one?

**Filippo:** Only the first one. I leave the martech-related questions to you. Feel free to use that chat that we have together. So I'm there and I can push towards that.

**Vlad:** Okay.

**Filippo:** Perfect. And last point is AI design, martech kit integration. That seems to me that it requires a bit of your time there because of all of this.

**Vlad:** Yeah. So it will be a little bit delayed. I will give green light to Alexei. Yep.

**Filippo:** Vlad, I think that is it. I need to go in an interview in 4 minutes. So if it's okay with you, I will close it here.

**Vlad:** Sounds good to me.

**Filippo:** Nice.

**Vlad:** Thanks for today. It was very useful.

**Filippo:** Likewise.

**Vlad:** Good luck with the interview.

**Filippo:** Thank you. Have a good one.

**Vlad:** You too. Bye.

**Filippo:** Bye-bye.
