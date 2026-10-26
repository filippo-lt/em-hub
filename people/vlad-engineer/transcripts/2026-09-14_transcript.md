# Transcript — Vlad / Filippo Weekly 1:1, 2026-09-14

**Source:** Granola (meeting id `ca934a9c-d355-42e9-9705-34238750facf`)
**Date:** 14 Sep 2026, 11:00 CEST | **Participants:** Filippo Tosetto ("Me"), Vladyslav Krut
**Note:** raw verbatim transcript, speaker diarisation from Granola. "Andrei"/"Andrej" = Andrey. "Market kit"/"Marketing kit" = MartechKit. "Kimitree" = Kimi. "Surf API"/"SERP API" = SerpAPI. "RSC" = the TraceCheck repo.

---

**Vlad:** Sounds good.

**Filippo:** How are you doing? No, it's fine. It's fine. It's part of the job. I'm not— you keep saying sounds horrible for this kind of things. What's the difference between this one and talking to an LLM?

**Vlad:** Well, if I would have more of a choice, I would probably not be talking to LLM either. You always can kill LLM, well, kill the chat and then restart with the smarter one.

**Filippo:** Yeah.

**Vlad:** Something you definitely cannot do with a person. Yeah.

**Filippo:** Yeah, there are techniques.

**Vlad:** Maybe you can, but probably only once.

**Filippo:** There are techniques for that as well. I like— not teasing you, but trying to dig a bit deeper about this.

**Vlad:** I see, I noticed you.

**Filippo:** Um, but because I'm very curious.

**Vlad:** Mm-hmm. Yeah.

**Filippo:** Because when I asked you a few months ago, what do you want to move into? you grow up kind of thing. As you said, engineering manager straight away without really any doubt. But then when I present, yeah.

**Vlad:** I say it's tough almost without doubt. And then you were like, think about it, and I thought about it, and I was like, okay, maybe.

**Filippo:** I thought you said engineering manager.

**Vlad:** The primary answer was a staff engineer.

**Filippo:** See, that, that is the cause of all this debate that keeps going on.

**Vlad:** And then you explained that, but I am good at some aspects of it, so maybe I should consider. I was like, okay, let me think about this. So I considered and I was like, you know, I see you maybe. It can be true one day. Still exploring.

**Filippo:** Okay.

**Vlad:** And then since that moment, you're continually showing me more and more areas of that work that I am like, oh no, that sounds terrible, probably I should stick to the technical position.

**Filippo:** Initial. But so your, let's call them soft skills because they are soft skills, are very good. And I think staff engineer without this kind of soft skills are not great.

**Vlad:** Mm-hmm.

**Filippo:** Staff engineer, beside the technical complexity of problems that you would need to solve, needs to be able to communicate to people this kind of, is it a problem or is it a solution? And you're good at explaining things to people. So that's good on your end. Keep doing that. Vlad, it's Monday. It's new challenges in front of us, but before we dig into that, do you have any points that you want to discuss with me?

**Vlad:** I will. Let me think real quick. Oh, well, one that I just want to let you know. AI design is taking this last week and this week a lot of time because of very obvious reasons. The progress is moving somewhere. Starting from tomorrow, I believe we should either tomorrow or when the closest sprint starts, we should start addressing all these issues.

**Filippo:** Okay, good.

**Vlad:** So I will expect more stuff to appear when it appears. Becomes clear that maybe these guys don't really know some of the details the previous team implemented. Especially with Robel. I believe he can manage it, but there will be questions.

**Filippo:** Yep.

**Vlad:** Well, there will be problems. I believe we are about to uncover bigger kind of forms. Which is probably normal, like it's expected. It's a very necessary cleanup now.

**Filippo:** The state of this app is that it's going to move to growth, right? Meaning that we launched it, we proved that it works, and now it's going to receive much more investment from a marketing perspective. So for me, the natural movement now is to get these things sorted as soon as possible. One thing is though, those major security holes that you identified. Other things like GDPR-related, yes.

**Vlad:** Why is this?

**Filippo:** The latest things. These are not engineering-related tasks. These are decisions from product. We can show them that this is the state of things, but it's not up to us to take those decisions.

**Vlad:** I agree. However, if given a certain level of freedom to dictate, how would we address some of the issues? I believe it may be in some cases better from our side to show initiative and show the solution we would prefer to implement. Than for expect from somebody from legal to come to us to dictate their vision that may be much more complicated. For example, the robot— no, it's— or

**Filippo:** Um, yes and no. Let me explain. Why do the work twice?

**Vlad:** It's not necessarily going to be twice because in the current state of things, legal will for sure come and tell us, guys, that's unacceptable. Fix it, please. Here is how. Maybe here is how. Not sure if they will explain how. However, if we close the biggest holes on our own, maybe they will not ask us to polish things that are not necessarily deal-breaking. What do you think?

**Filippo:** I like productivity, but in this moment what I need is to inform the right people. Is it different steps? You identify the things, you documented them in a Jira ticket, which is— thank you so much for the process, really appreciate it, because I doubt anyone has done something like this in the company so far.

**Vlad:** Yeah.

**Filippo:** Second, no, I know, I know. That's a bigger conversation. Is. To inform product about it. Hey, this is what we identified. We are going to close the major holes that we have because of security reasons, but bear in mind that there are some legal implications for these other items. You, product, decide how to move forward. You want to talk to legal, talk to legal. If you want to bury it under the sand, you do whatever you want. But the engineering work has been done. We cannot take decisions on how this thing should be fixed beforehand. No, no. I'm not saying this. I kind of, I don't care. I'm just drawing responsibilities here.

**Vlad:** Noted.

**Filippo:** That's it. That's it.

**Vlad:** In fact, this is going to be one of the things I need to make it very clear for Miguel that after we're done with the rest of the security, with the obvious security engineering issues, it's up to him to decide what to do. Because the last update I sent to him on Friday, I believe, was let's wait for legal because they anyway are doing the job and they will maybe come for us.

**Filippo:** But legal.

**Vlad:** Oh, I see. Don't, don't initiate. But wait.

**Filippo:** Legal do not initiate anything. It's product that needs to talk to legal about this, and this decision must be in product's hand. Do you want to talk to legal about this? Thanks. Bear in mind that we are liable. GDPR reasons. What does it mean? It's up to you to do your own research about this. I'm not a product person, I'm an engineering person. I'm flagging this and I'm kind of doing part of your job here because you should tell me how you should— we should store the data, not the other way around. It's responsibilities. Okay. It's a slippery slope here. It doesn't mean that I'm going to throw Miguel under the bus, obviously. You mentioned this to him on Friday. I'm going to mention this to him tomorrow because we have a weekly one-to-one and I'm going to say, hey, Vlad has done this and this and that. What do you think? Do you want to talk to product? So I'm going to guide him through. Buddy.

**Vlad:** Okay.

**Filippo:** At the end, we cannot spend all this time fixing their problems. Issues.

**Vlad:** Sure. Makes sense. That makes sense.

**Filippo:** That's it. That's it. Also because I need you in other. Yes. More important areas.

**Vlad:** Also makes sense. Yep. Other than that, there is one more thing that I will need to address this week. This is about Firestore rules, but on Face AI. A week ago, you asked me to do this.

**Filippo:** Yes.

**Vlad:** Over the course of the current week, if I remember correctly, 15th to 22nd. So this is also on my to-do list.

**Filippo:** Yes.

**Vlad:** For very soon. And the same thing for Firestore, because apparently iOS and Android apps has patched the initialization hole that they had.

**Filippo:** Yes.

**Vlad:** They did it. Yeah.

**Filippo:** Yeah.

**Vlad:** So I will do this on dev maybe today. And in prod when they release.

**Filippo:** Thank you.

**Vlad:** A lot of stuff is happening.

**Filippo:** That's absolutely correct. Yes, I know. More things are gonna happen and I would like to try to help you to split time in a way that you feel comfortable with. So instead of having you to multitask too much, I would like you to say, okay, on the mornings I work on AI design, for instance, in the afternoon I will work on TraceCheck. It's gonna be something that we need to work on together depending on how you prefer to work yourself.

**Vlad:** Okay, I see. So for now, I believe that mornings I spend on meetings, I don't work on anything very specific, like 4 every day at least.

**Filippo:** Yes.

**Vlad:** And majority of the work on AI design— oh wait, hold on, I also have AI design with marketing kit. Um, do I have to start splitting my job like half and half and start working on TraceCheck already? Maybe is it fine if I, you know, spend this week finishing integration, everything Martech Kit related?

**Filippo:** Let me explain what am I expecting from you.

**Vlad:** And next week? Yes, tell me.

**Filippo:** I'm expecting that the 30th, so that you start to deliver small features in TraceCheck. From the first 2 weeks of October and from the 31st of October to you to be completely independent. So you will be able to work independently and carry over the full development of TraceCheck. What does this mean? It's that you know about the project in terms of product. What does it do? On one end. That means all the edge cases. All the payment things that are the things that are more complex in this project right now. You have an idea of the roadmap. That's an easy win. But most importantly, you know how to move forward with development. And I believe that you need a bit of training somehow. To do that.

**Vlad:** Well, I will definitely have some. I don't know if somebody will organize this for me, if I do it, or if I do this for myself. I'm pretty used to learning stuff myself, of course.

**Filippo:** We—

**Vlad:** But some general tips like what language or framework are we using, what's the convenient software that we use for that.

**Filippo:** Yeah, I'm gonna talk about that in a second. So Vlad, this is how I see it. Priorities for me are the following. One. I'm expecting to have the security issues related to Firestore in both Face AI and AI Design. So the major holes. Fixed between this week and the next. So there are small things.

**Vlad:** Sure.

**Filippo:** Like the actual rules for Firestore, those are something that you can do very quickly in a few hours and it shouldn't take you a full week to do. So the sooner you get those done, the better would be for you.

**Vlad:** Yes.

**Filippo:** Then I am expecting you to start to learn about TraceCheck.

**Vlad:** Okay.

**Filippo:** I'm not expecting you to write any code this week on TraceCheck, but I want you to start to get involved on the mindset to start to think that, okay, this is no apps, this is web. You're going to start to talk to me and to Andrey to have started to have an overview. So for me, it's important that you start that by next week. At least have an idea about what is TraceCheck, what is InfoSearch. And a few things that we do from a developer perspective. Does that mean that you need to spend 50% of your week in that? No, but I will try for you to spend at least 1 to 2 hours every day. Is it because there is a meeting for you to attend, or is it because you are spending to learn, to understand? to read— there's a lot of documentation about it— to ask questions if it's the case. That is what I would like you to start to do this week.

**Vlad:** Okay.

**Filippo:** From next week, a bit more involvement. And going on until you are— for me, the perfect split would be not this week, not in September, more towards the second part, more towards October, 80% TraceCheck, 20% AI design.

**Vlad:** Okay. That makes sense and is very doable as soon as I start working on marketing everything related. Yes.

**Filippo:** Yep. But for me, the reason why I invited you to this daily standup is not because you will have something to say, but it's because you start to hear about things, the problems that we are facing. At which level, what are the priorities, how are we working? There are a lot of information to absorb. So even though you absorb them somehow in a, how do you say, not active, in a

**Vlad:** Passive pay, I don't know, like

**Filippo:** Yes, yeah, something like that, that would be great for me.

**Vlad:** That feels like it, yes.

**Filippo:** Yeah.

**Vlad:** Like passive language learning in the new country.

**Filippo:** Yeah. That's it. So that is the reasoning why I would like you to start to be involved in this.

**Vlad:** Okay, I see. Makes sense.

**Filippo:** Nice. Uh, said that. I know that there is Martech Kit to wrap up. So I'm not expecting you to— so for me, integration of Martech Kit in AI design, it's not a priority per se. It's something for you to learn about. It's sort of not to learn about, to start to work on. Once you close the martech chapter this week.

**Vlad:** One cycle. Okay.

**Filippo:** So for me, what you're doing, FaceAI, for instance, is part of closing the martech kit chapter because you're testing what you've just done.

**Vlad:** Okay. That makes sense. I really hope that I done it really well.

**Filippo:** So Vlad. It's not going to be hard stop saying, yeah, no, I'm going to remove the credential from martech kit. You can't touch the code anymore. Come on, we are flexible. But yeah, this is ideally what I would like you to start to wrap up, wrap up martech kit this week, you wrap up all the work around security for AI design. And Face AI, and for me, if you start integration next week, it's totally fine. So I understand that the time is limited, especially the fact that you are going to be on holiday. So the time is very limited here.

**Vlad:** Yeah. Okay. Yep. That sounds like a plan.

**Filippo:** Do you have questions?

**Vlad:** Yeah. It sounds like a lot of things to do, which is fine. Usually it's like one long thing to do. Now it's a lot of small things.

**Filippo:** Yeah, you're closing up something, you're starting something else.

**Vlad:** Yep.

**Filippo:** Right. Other points from you?

**Vlad:** Checking my notes. The recent request from Damian regarding the new parameter in the Martech Kit, is it something that is not urgent, something we are not planning to do soon? or is it something that I or Victor should prioritize also this week or next week?

**Filippo:** Yeah. For me, it's something that should be prioritized. But this starts to become more a Victor problem than yours. It depends. Let's put it like this. Is this something that's going to take you 1 hour? Please, if you could do it, that would be great. Is this something that needs some thinking and planning, etc.? Let's get Victor to do it next week.

**Vlad:** Okay, so far the solution that I see is that we replace our key provider with some kind of configuration provider, and in the absolutely same entity as this new parameter that RevenueCat expects and Damian needs to provide. That seems to be it. Before committing to this plan, I would also ask AI if this fix is going to be as simple as that, because it can go and read and check if anything can go wrong here. I hope not, but I would ask. Because I'm lazy, this type of work can do really fast.

**Filippo:** Yes. Yes. Yes. Again. You decide if you can squeeze it in or if it needs to be done by someone else.

**Vlad:** I will take a look at this issue more in depth after addressing and merging all the stuff related to the current open big pull request that I have.

**Filippo:** Perfect.

**Vlad:** Because I, in the same time, I work on others. So just, you know, to have my work being done regarding the same project in sequence, not in parallel.

**Filippo:** Regarding AI design. Please. Outsource to the externals as much as possible. We are paying these people to do their job, and security is part of their job.

**Vlad:** Yes, I will. Majority of the stuff will be done by them. The Firestore configuration will probably be done by myself, and I have 2 more tickets assigned to myself, but not because I am planning to do this, but because I was too busy trying to figure out what actually needs to be done and from whose sides. So I'll probably, when I get to them, I will split them into 2 or 3 tickets and assign them to externals as well. It's just a lot.

**Filippo:** Yeah, I can imagine, I can imagine.

**Vlad:** Right.

**Filippo:** Okay. Other points?

**Vlad:** No, I think that's it. I have still general open question about the technical stack of this. Tech stack. TraceCheck. But that's open question. I am not sure how urgent it's going to be.

**Filippo:** Um, let's kickstart that. Let's kickstart that by starting with what is expected from you. Because I think if you don't know this part, you're not going to go that far.

**Vlad:** I have really low chances to succeed here.

**Filippo:** So let me try to explain. What we are trying to do in this product project. So first of all, it's a web project. It's, the frontend is written in React, React.js. I don't know if you ever heard this, but it's a framework written in JavaScript that was created by Facebook at the time, but now is pretty spread over. It's using a sort of rendering engine. Very, very similar to how SwiftUI works. In fact, I think SwiftUI kind of got the gist.

**Vlad:** Yep.

**Filippo:** Of the rendering engine from React.

**Vlad:** When I was working on React Native, I was like, I have seen it somewhere.

**Filippo:** Yes.

**Vlad:** It felt like SwiftUI takes heavy inspiration but tries to fix the biggest problems they had in at least React Native. Not sure about React as a whole, but React Native, yes.

**Filippo:** Yes. And we use Node.js as backend. And as programming language, it's TypeScript. Why? Because it's type safe. As easy as that.

**Vlad:** Obviously, yes.

**Filippo:** Good. More technical details will come to you over time, but I want to go back to the initial part. So what are your responsibilities now that you know the basic of the technology? Suffice to note that we don't write code. So we have in place a full agentic way of working. And this is where for me it's going to be very interesting because by knowing you so far, I can see that you are embracing AI, but you still hold control over it. To work.

**Vlad:** But my part of committed AI-generated code in Cursor were 100%.

**Filippo:** Yes, I know.

**Vlad:** Not 99, not 100, but yeah, I keep it in control. Yes.

**Filippo:** I know. So how do we work? It's pretty linear, I would say. There is Alex, which is the product project director. That comes to us with ideas on what to build. We discuss these ideas. We are still defining the whole workflow because this project is something that is evolving by itself. So maybe Alex creates an epic, maybe we discuss in a meeting, maybe we, in general, we know what we want to build. But then what's happening is that or Alex or we, most likely we, are creating the user stories related to this epic. And this for me is becoming extremely important. Because these user stories will need to be human-readable. QA will need to read those user stories. If we write technical code or we let AI do their own, you know, wall of text, QA cannot work. And the responsibility that we have is to take product input. Converted in a workable fashion. And put it live. I don't say, I haven't said writing code in all of this yet. So our role is to align with product. Keep Jira board up to date. Because it's more useful to us than to product.

**Vlad:** Mm-hmm.

**Filippo:** Out of this. We have a workflow. Has been there since the beginning of this project, which is new feature. We create the specification as a markdown file. We have a specific folder in the repository where the specification is, and in there you work as you prefer. I debate with AI, so I usually use a high-level, high-cost AI to do this kind of brainstorming. And the output of this is a Markdown document where I try to avoid to write code, but sometimes you need to mention something technical there. And what does it do is the full specification of what we're going to build. And this is for every— so the idea is every PR has a planning doc attached to it. And they are always committed together. After this, sometimes— but I think it's a bit clunky— you have a second agent that creates the implementation plan, which is purely technical.

**Vlad:** Okay, makes sense.

**Filippo:** If you like it, you can use it. If you don't, it's up to you. The important part here is that we use red-green development or TDD development, whatever you want to call it, write test first. Make them fail. And then write the code.

**Vlad:** Nice.

**Filippo:** Again, this is all AI-driven. We don't do anything. There is a workflow. You can create your own skills. I use some skills. I can share them with you. I think some of them are already in the repo. The point here is that we rarely look at the code. At the end of this flow, the test will run. The full end-to-end suite of tests will run on your machine or in the CI, and there's going to be a PR created. This PR will have the documentation, so the specification document, the tests, and the code.

**Vlad:** Okay.

**Filippo:** We have right now around 700 end-to-end tests running. For every PR. This is great compared to mobile because it touches everything. And at the beginning it was a bit, yeah, whatever, now it's a lifesaver. Especially when you start to have rogue agents going around and doing things for you that can be very, very annoying. So your job here is take a product requirement. Convert it into a workable artifact. User stories. Work with agents to create the specifications. Get the code in a PR, and then you have reviewers and everything else. So the usual flow.

**Vlad:** What do you do when you need to change the specification?

**Filippo:** You write them, just you have a markdown file, so

**Vlad:** I mean, sorry, not the specification Jira-wise, but specification the codebase related. So the feature, we request an update, so now we need to update— well, okay, yeah, that's what you called specification that is stored in the repository. How you after that run the workflow? So, okay. Agents are not— how do you make agents write tests in the proper way for the updated specification without breaking everything?

**Filippo:** Wait, are you talking about an update of a feature that was already released or while you're working? Okay, okay.

**Vlad:** Yes. Update of the already released feature for this one.

**Filippo:** So there is a history. There is a history with the specification. What I'm gonna share with you right now. I'm gonna share the screen. So there is a lot of documentation here. Okay, so this is the README. The repository. And here you will see where to start, developer onboarding. And here, if you open it, there's gonna be how to start your journey inside this project. So what to read next, system architecture. Collaboration rulebook. Product augmentation, decision index. This is the important one.

**Vlad:** Okay.

**Filippo:** And it's touching your question. So every decision is documented.

**Vlad:** I guess.

**Filippo:** Okay, so, so if something changes because a product is evolving, it is documented.

**Vlad:** Did you find a way to make the agents to update the specification and have some kind of log decision instead of patching what already exists with newer version. Because of which you have a huge mess in the end. So that's something I was struggling to do, that's why I'm asking.

**Filippo:** Um,

**Vlad:** So the AI really likes to keep a history of changes.

**Filippo:** It is. Yeah.

**Vlad:** which is like the full archaeology since day one of the project.

**Filippo:** Yeah.

**Vlad:** But that's not what we may want. What we want is to have up-to-date specification without the full history of changes. And it doesn't matter how explicitly must have to obligate it and so on. It's saved for AI. It will ignore this instruction for me at least.

**Filippo:** Yeah. So let me, let me explain this. Um, you need to drive there. Yeah. Let's make a very concrete example. So the application, what it does is that you input a phone number or an email. And the output will be a list of information associated to this. One or the other, okay? input. How do we do that? A pipeline of third-party providers that we call. For this, for gathering information. We have a— let me see, where is it? Um, I did— ooh. I think this is something wrong with this. Yeah. As you can see. It's not as easy as it seems. This, not this one. This one. So I'm talking about this pipeline. So phone number, we call Abstract Phone Intelligence to do something. We have a check on the region, and then we have other providers: People Data Lab, People, Linkario, Abstract Email, blah, blah, blah, blah, blah. We want to remove SERP API because we noticed that we don't need it. The information that are not gonna be, um, they are not provided, that are provided by RESTful API are not useful to us, and also it has a cost, both in terms of money and time to get the final result. So one of the tasks that we need to do this sprint that's going to start tomorrow is to remove SerpAPI. How would we would I approach this? It's a change in a feature, okay? Something an update or something that you said. So how would I do this. I'm going to say, let's prepare to implement a new feature. Here is the Jira ticket for it. And then I will probably write a small description saying we need to remove SERP API because of these and these reasons, okay? Let's prepare the specification document. Bear in mind that we also need to remove— we need to remove it from the code itself, but also update the architecture documentation. So in this case, I am mentioning what I need.

**Vlad:** Yes.

**Filippo:** So the old thing will go on, create a massive— I'm trying to keep it small, but it's not that small. The obvious problem is with AI is the amount of things they write anyway. At the end, we have a specification in there. Your job is to read this. And understand this. And see, wait. We don't update— we have this mentioned in the documentation, but it's not really updated according to this specification. Let me manually add a point, a to-do in the to-do list of the spec, say update the documentation. Or I can also prompt AI to do it itself, update the specification document, saying that we need to update the documentation. So it is you driving. That's important thing.

**Vlad:** So in the end, in the list of decisions, for example, will you have documented decision? discard SerpAPI? Because in that example, honestly, there should be no mentions of SerpAPI at all in the codebase anymore because it's not valuable anymore as an input. But if you keep it as log decision, I will continue read it and load it into the context every single time.

**Filippo:** Yeah. Yeah. So the fact that we have the plans— no, sorry. Where is it? Yeah. The plans? Oh, because Arak had some. The fact that we have plans. There is a history log here.

**Vlad:** And here. Why are you keeping it?

**Filippo:** I'm not keeping it. I mean, I'm keeping it. Because I need to know if something has already been done. Or why something was done in the past. Because in terms of if you find a bug, you need to understand where this bug was introduced, for instance. So for historical reason, we need to have a sort of log of everything that's been done. So these are the last few things that are open. But then in the archive you have a lot of other plans. These are all the features that have been tackled so far. It's up to your AI or how you drive the AI to load only the things that you need. And this is why for me it's very, very important to keep the documentation part of this website extremely clear. With links.

**Vlad:** Oh well, if it's working so far.

**Filippo:** It is working so far. So something that I introduced recently is a glossary. Why? To speak a common language with AI, TraceCheck. Seeker. What is a lookup? So in this way, when I talk about lookup, I write a prompt talking about lookup, the AI knows that I'm talking about this specific concept. There is no ambiguity around this. When I talk about report, search results, provider, so I know they are common knowledge. But if you think as a human being, you have a glossary regarding a project in your head. So we need to find a smart way to create a context for the AI, because when you have a small repository, it's easy. The information that the context needs to hold is not that big. When you start to have a repository like this one with so many information, with a lot of code, you need a way to find shortcuts or to get the AI to be able to find their own information in a smart way.

**Vlad:** Yep.

**Filippo:** It's not easy. It's not easy. Because there's a lot of drifting. And this is something that I'm working on on-site. Drifting means the AI start to do a lot of things by themselves, so we need a sort of routine. That doesn't code. Doesn't write code. And keep in check that we don't have slop in terms of code. Also keep the documentation up to date.

**Vlad:** I'm very curious to see this pipeline workflow.

**Filippo:** So, yeah. This was a status dashboard of the V1 that is now released. And this helped a lot. It is very interesting for me to work in this way. Is it working 100% correctly? No, but it is working. What is not working correctly? It stops working correctly in the moment you let it go. You don't check anymore. And what we noticed with Andrey is that we go through the full cycle. We get a PR ready. But we need to test it manually.

**Vlad:** Oh really?

**Filippo:** We need to do a manual test. Because yeah. You need to do this. There are things that AI may have misplaced. Most of the times it's fine. But there are cases where you totally see that it's not the AI hallucinating, it's that the specifications were not correct.

**Vlad:** Well, yeah, I see that can happen.

**Filippo:** Yes. Um, we were talking about the role definitions and then I started to drift into the agentic coding part. Align with product. Get the specification. So the repository is your responsibility. So yours as in engineering responsibility. We need to keep it up to date. We need to keep the code working. One of the responsibilities that we put on our shoulders, and I didn't say yours, is ours, is to improve the workflow, the way we work.

**Vlad:** What part of it do you want to improve?

**Filippo:** Everything. For me, everything. Literally everything. If you see that using Jira is a waste of time, just saying, just to give you a strong example. If you come with a proposition on how to improve that, let's do it. Anyone dictating? we should work. Because this is a web project. Web projects are a world on their own.

**Vlad:** Okay.

**Filippo:** You are not really convinced about all of this until you start to get your hands dirty.

**Vlad:** I'm not, I like, what do you mean? Because I was trying to build a reliable way of working with AI so I do not have to look into the code. And I am, well, I'm not there. Like 95 maybe percent of the code that AI writes for me, I will not need to ask to request or to change or to anything. But 5% of the mistake is a huge percent of mistake if that's my responsibility. It means that I will ship the feature and every, I don't know, 1 out of 20 PRs will introduce a bug. That's a lot of bugs on my side.

**Filippo:** Great. Okay.

**Vlad:** So

**Filippo:** How do I make sure that that 5% doesn't exist anymore or it goes down to 0.5%?

**Vlad:** That's a very good question. That's what I was looking for. So far I got, well, this far.

**Filippo:** All the bugs that we found so far. They were related to unspecified use cases. That we didn't know about.

**Vlad:** Yes. I usually find underspecified use cases while reviewing the code. Because I'm very, very much trained to see problems in the code. So, okay. Maybe in like we have payment states, different ones. So we have this case, this case, this case, and then in Swift we have default. I'm like, hold on. What's default? What did we not list? So I go and check what did we not list, and that's exactly what was underspecified, what I was not aware of.

**Filippo:** Perfect.

**Vlad:** Product issues. the code, usually when I work in iOS, at least.

**Filippo:** So today you have 2 gates. 3 gates. Um, sorry, let me find— now these are snapshots. Services code test. Uh, where is it?

**Vlad:** If anything, yes, I'm not convinced, but I will go and try. Of course I will. I'm not convinced. I'm skeptical about it. But also you have showed the results. So it's working. It's already making money.

**Filippo:** I'm gonna try to find something for you. Here it is. Okay. Go back here. Oh, come on. Okay. Think about it in this way. You have 3 gates. Gate number 1 is you. Discussing with your AI if you want, or discussing with me, or discussing with Maria, or discussing with product regarding a new feature. You want to add a new lookup flow, and instead of looking for emails or phone numbers, we're going to look for names. Perfect. This is a feature. So you start to define it. What do you want? User can input something. Where does he input? Well, we are just going to use the same UI that we have for the other things. But what are the use cases here? Is it name? Is it just name? Or name and surname? What if I misspell something? Is there any— so you start to think about this. Then you think about the output. In the end, what you're going to have is in your head, you have a model that you can convert into a user story that Maria can use to test this. Perfect. Step number 1. This is the first gate. Second gate. Discuss with your LLM a good model. Is it Opus, for instance, or Kimi regarding the specifications? And it's up to you how you define the rules here. Make the AI smart. For instance, I have a skill to ask me questions until we exhaust all the possible venues for a specific feature. And if the feature is too big, we can split it. What's the output here is a document explaining with words the things, right? So you read that. And you think about, probably here we want this, we want that. Perfect. You are checked this second gate. What is the third gate? Something in between code and a document, and this is the famous Gherkin file that we have in here. Have everything that you need in terms of pseudocode. Scenario: buying the monthly subscription grants premium access. Given my subscriber state starts as none with no premium access, when I purchase something, blah, blah, blah. And here you have all the cases generated for you. And your job here is to review this. This is where all the cases come.

**Vlad:** Okay, so you also, we as engineers also review this, okay?

**Filippo:** What's gonna happen when you say, good, I like this? No need to move forward. Sorry, let's move forward. This will kickstart the generation of tests. And then the test will generate the code. Okay. So you don't know. You don't know all the ins and outs of the language or the frameworks. Because you don't have 5 years of experience on the topic. So you need to find ways for you to analyze all of this. What's the last step? Code generated, PR created. You sometimes you need to do a manual test. That's it.

**Vlad:** Well, do you test all the cases in your Gherkin file or only the success pass or?

**Filippo:** Everything. Every single thing.

**Vlad:** Okay. Okay. Okay. Okay.

**Filippo:** You will see when you start to explore the repository, the amount of gherkin files and how big those gherkin files are. Because this is where you make sure that you don't introduce regression, or you try to, and you try to cover all the possible scenarios. What's happening is that every time we find a bug, a new test is created.

**Vlad:** Makes sense. So from what I can estimate now, it's going to be like 60% of the time manual testing, manual QA, and the rest is talking to people and talking to LLM.

**Filippo:** He's mostly talking to LLM.

**Vlad:** Okay.

**Filippo:** So we started with zero control, just AI do everything. We put AI to handle Jira as well. Wrong. Do it. What we are doing now is to strip AI from the process and start going back to human beings. Jira. I'm using Jira because it's a tool that we already have in the company. It's used in other projects. We can use Linear, we can use a piece of paper, I don't care, but we need a place where to track things because there are people in the team. And everyone needs to agree, Jira is the contract. I agree, you agree, Alex agrees, Maria agrees. Good. Oh, but I thought that this needs to be in the— There is a user story. Your job is to read the user story. If you don't agree with it, we can change it, but this needs to happen beforehand.

**Vlad:** That makes sense.

**Filippo:** It's going to be an interesting journey for you.

**Vlad:** Yes, very much.

**Filippo:** Um, what else? We can use more strong model for this project because this project is bringing good money. So you can use

**Vlad:** Okay. Does it mean that I need to be added to another organization in Kilo or whatever?

**Filippo:** Not yet, not yet, because we don't have other— so the plan is to create other organizations for agentic coding. So where the budget is higher and we control this kind of things. Today they are not created yet, so we're just gonna drain MAU's kind of credits as much as possible, pretty much.

**Vlad:** Okay.

**Filippo:** Vlad, that's the gist of it. Do you have questions?

**Vlad:** No, I don't think I have so far. Somewhere this week I will download the software, try to run tests, you know. Do this type of stuff. Read the README and the new developer guide. And after that, I will have much more questions probably. Do you guys share and track all the skills and rules you use for this agentic workflow in the repository itself, or you have your own delegated sets that are local?

**Filippo:** I do for them. No, I do for the majority of things. I do because I think they are valuable. Feel free to use them or not. I'm about to update them. For instance, how does it work to release to production? I created a massive skill for it because it's a manual process that today the trigger to deploy to production, to the production server, is when you merge a PR from dev to main, main needs to always be clean. And when you merge something to main, it will deploy to production. But that is not only it, because what I want to do is also to update Jira to make sure that all the tasks that are created in PRs that are going to be released to production, they're going to be marked as so. And then we created a sort of webhook, so it pastes to the general chat that we have. What's been happening? There are a lot of things. I have some Semaphore that tells me, hey, this is not deployed to production because there was an error. So I created these kind of skills related to this project. I'm happy to guide you through them once you start to get involved a bit more.

**Vlad:** Noted.

**Filippo:** Yes. For instance, I was working last week on something to avoid this drift. So I have, the idea is to run some sort of a routine every Monday morning to do a general check on the codebase and documentation, making sure everything is up to date. And if it's not up to date, it generates a GitHub issue. That another agent will pick up. And fix.

**Vlad:** Okay. I'm here, I'm just curious. Why another agent? Like, I also have to do it with another one, but why?

**Filippo:** Because I want a human being to check those issues. Agent 1 is a loop. That creates the Jira issue. If he finds something saying architecture documentation is wrong, blah, blah, blah. And you say, I want this, this, and this done. And then the second agent starts, reviews the things, and creates a PR related to it, and the human beings need to press the button.

**Vlad:** I see. What about the things that you do not agree as findings provided by AI? So if you just ignore it and you'll find them again next week? Do we change anything?

**Filippo:** I marked them. So I'm working on this workflow. My plan is you can use labels in Jira saying, in Jira issues say good to go, not good to go.

**Vlad:** Okay.

**Filippo:** Agent will pick up the good to go and close the not good to go. Creates a sort of memory saying these things can be ignored.

**Vlad:** Okay, nice.

**Filippo:** Vlad, I need to go.

**Vlad:** Sure.

**Filippo:** Welcome to the new world. You see why I would like you to start to get involved as soon as possible, because there's a lot.

**Vlad:** That's a lot. It's a lot and it's very different. It's not just language or engineering stack different.

**Filippo:** I believe it's super exciting and it's something that at least I personally like a lot.

**Vlad:** I will let you know as soon as I start. So far it looks scary, like you don't have control.

**Filippo:** Okay. Yeah. Uh, we are gonna take it week by week. But the important thing is for me to start to dip your toes into it.

**Vlad:** Okay.

**Filippo:** Vlad, I need to go to an interview.

**Vlad:** Okay, good luck. Thanks for all the context. Have a nice rest of your day.

**Filippo:** You too.

**Vlad:** Bye.

**Filippo:** Thank you. Bye.
