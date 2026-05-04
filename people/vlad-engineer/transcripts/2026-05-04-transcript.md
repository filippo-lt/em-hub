May 4, 2026

## Vlad / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Hello, blood.  
**Vladyslav Krut:** Hi. Hi. How are you doing?  
**Filippo Tosetto:** I'm good. What about you?  
**Vladyslav Krut:** Also good. Monday very busy day, but I feel like I'm crushing it so far. And  
**Filippo Tosetto:** Yeah,  
**Vladyslav Krut:** you  
**Filippo Tosetto:** I have a I'm like I'm less busy than usual, which is good. Sunray's back, so it's taking something off my backs. But I'm very determined on what I want to accomplish this month. Not aggressive,  
**Vladyslav Krut:** Sounds good.  
**Filippo Tosetto:** determined.  
**Vladyslav Krut:** Say  
**Filippo Tosetto:** not aggressive. So, I'm not upset with anyone.  
**Vladyslav Krut:** again.  
**Filippo Tosetto:** I'm just determined to move things in certain directions. But hey, that's my job. How was your  
**Vladyslav Krut:** Pretty nice. Pretty nice.  
**Filippo Tosetto:** weekend?  
**Vladyslav Krut:** I was I feel like I was not really doing anything other than like trying to solve the to-do list like the infinite one.  
**Filippo Tosetto:** Yes, blood. That's that's something I cannot help you with. Unfortunately,  
**Vladyslav Krut:** I don't think anybody could honestly.  
   
 

### 00:01:46

   
**Vladyslav Krut:** I feel like I just learn to live with  
**Filippo Tosetto:** yeah,  
**Vladyslav Krut:** this.  
**Filippo Tosetto:** it's going to get worse. Don't  
**Vladyslav Krut:** Yeah,  
**Filippo Tosetto:** worry.  
**Vladyslav Krut:** I I have predict suspicion that it's not getting any better this  
**Filippo Tosetto:** You know what? It's going to come a moment in your life when you start to care less and less about specific things.  
**Vladyslav Krut:** time.  
**Filippo Tosetto:** So, your to-do list will shorten by default because you're crossing things even if you haven't done them. But that's a a grownup story. You're still  
**Vladyslav Krut:** Yeah,  
**Filippo Tosetto:** young.  
**Vladyslav Krut:** I feel like you know moving to different apartment or house will cross a lot of stuff from this list but add a lot of  
**Filippo Tosetto:** So between me and my wife I think in in the last 15 years we changed  
**Vladyslav Krut:** more  
**Filippo Tosetto:** around 20 25 uh different houses. Yes.  
**Vladyslav Krut:** half a year at one place on average.  
**Filippo Tosetto:** But in two people,  
**Vladyslav Krut:** Okay. Still that's quite a  
**Filippo Tosetto:** well, if you think about it, I spent nine years in London and in there I changed at least five different  
   
 

### 00:02:53

   
**Vladyslav Krut:** lot.  
**Filippo Tosetto:** apartments. She spent seven years in Berlin and seven years in Amsterdam where she moved three three times per place which means six other times. And then uh together uh we moved to at least three to four five different apartments. So yeah anyway  
**Vladyslav Krut:** I see. Okay.  
**Filippo Tosetto:** anyway yeah so blood let's talk  
**Vladyslav Krut:** Life.  
**Filippo Tosetto:** about progress is gone that  
**Vladyslav Krut:** Yes. Let's make some progress now.  
**Filippo Tosetto:** was my questions you're free what's your  
**Vladyslav Krut:** So what my plan the first thing I will do after I stop bothering with one with 1.2 I feel like all the tickets that are now not on query review I can finish probably by the end of day. Uh Anton is gone now and according to what he pushed before leaving before disconnecting I have a suspicion that he didn't know that he could chain pull requests. There were like three tickets.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** I'm like what? Like I had a suspicion at some point a few times that he didn't know how to use git but that's next level.  
   
 

### 00:04:22

   
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** Okay. So I have merged a lot of stuff already today.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** I updated the configuration of the G repository. So it now requires only one approval and I can get this one either from you or just from an CI. So if you are busy or anything you don't have to review. I will have to wait like 15 minutes for CI to run it and merge whatever I need. I will finally new all the certificates that were generated. I don't really know how, but it didn't allow testing on real devices without switching to automatic mode. And I was like, okay, I will nuke that.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** It should be like one common to regenerate probably,  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** but it will break all the existing Tesla bills. So, I will maybe do this after hours or something in the end of day.  
**Filippo Tosetto:** Just just talk to QA just to make sure they know this is happening.  
**Vladyslav Krut:** Yeah, something like this should be really easy fix for everything and then uh moving forward delivering what needs to be done instead of right chasing  
   
 

### 00:05:32

   
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** all the like pixel imperfections or this the actual conversation I'm having now with Alexi is that there are two types of pages that will be we need to add like new and trend on the on the catalog of different filters and effects and it should not be covering the the icon it says this badge. So I have to move it up a little bit but there is no example of how it should look in catalog in Figma that's attached to the ticket. So we were together looking for where is it? Yeah, that's how we work now. And I will try to make sure that we are not continue working this way. Like if it looks all right,  
**Filippo Tosetto:** stupid.  
**Vladyslav Krut:** we just push it with like I spent quite some time  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** today uh investigating the situation with gender picker and why two icons cannot be shown  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** properly. Anton figured out a workar around but only for iOS 26, not for iOS 18\. So what I was doing is I was actually like looking around the internet trying to find if somebody else has managed to do this.  
   
 

### 00:06:55

   
**Vladyslav Krut:** The answer is no. So I went to the Apple guidelines and like guys here is how this component should be used for the general speaker.  
**Filippo Tosetto:** please. Thank  
**Vladyslav Krut:** There is a component called picker.  
**Filippo Tosetto:** you.  
**Vladyslav Krut:** We should use that and if it's not compatible with our reset all button then let's change it on the design level. I'm not going to be reimplementing UI components from scratch.  
**Filippo Tosetto:** Thank  
**Vladyslav Krut:** That's not our priority 100%. So if it's bearable, the current side of the UI,  
**Filippo Tosetto:** you.  
**Vladyslav Krut:** let's just push it because the rest of the application is still not bearable. Come on, it's lagging, freezing, jittering animations, everything is bad. Let's focus on something that will bring more value.  
**Filippo Tosetto:** Thank you. This is part of my new new month resolution. Now serious uh we are spending way too much time in pointless points pointless  
**Vladyslav Krut:** Yes, that's  
**Filippo Tosetto:** things u and especially there is one very important  
**Vladyslav Krut:** wrong.  
**Filippo Tosetto:** po point here that you just brought up unconsciously engineering should stop apologizing and should stop bending the the the rules because someone in design or from product doesn't know how an iOS hack works.  
   
 

### 00:08:19

   
**Filippo Tosetto:** You just brought the  
**Vladyslav Krut:** Yeah. So what I'm doing I'm like leaving the comment leaving a link to Apple guidelines and taking Herardo.  
**Filippo Tosetto:** example  
**Vladyslav Krut:** So Herardo can either go and talk to designer and change the design and then we will consider if it's worth fixing or Herardo says okay let's push it and we skip we stop engineering at this point what I'm trying to do is that make sure that it's like functionable it looks okayish and then we move on we are not in the stage of the application development where we can allow to spend more time doing that sort  
**Filippo Tosetto:** I agree. I agree. Question. Is it because QA is pushing back a lot or is it why why are we spending so much time in this details?  
**Vladyslav Krut:** uh QAS are really good at spotting mistakes and at nitpicking. Um some of them uh some of these nitpicks make sense you know when we have overlapping text not completely clickable button stuff like that other times we can just call it done and move on so  
   
 

### 00:09:32

   
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** what I'm doing now I cannot say that a lot but sometimes I do like an educational type of job that guys This is how the component is supposed to work according to Apple. If it doesn't match the figure, I'm taking Herardo and asking if Herardo would like me to spend extra time on it. And usually Herardo doesn't want to. So that's the communication that is happening and seems pretty fine to me to be honest.  
**Filippo Tosetto:** Yes. Um in the future if you we receive a push back in one of these points please involve me as well. So very simple example.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** If for instance uh tomorrow you need to work on the tab bar navigation uh at the bottom of the screen and they want liquid glass but they want a custom way to do it. If they push back on this, involve me, please.  
**Vladyslav Krut:** Okay. Okay. It's going to look aggressive from my side, but I think that's  
**Filippo Tosetto:** I is obviously try  
**Vladyslav Krut:** okay.  
   
 

### 00:10:39

   
**Filippo Tosetto:** to  
**Vladyslav Krut:** Yeah. Like how I will think  
**Filippo Tosetto:** Hey, can do you mind if we filipo because uh I have strict deadlines uh and he wants me  
**Vladyslav Krut:** something.  
**Filippo Tosetto:** to to work in a specific I don't know. uh we have internal guidelines so from engineering so that we don't reinvent the wheel from scratch. We prefer to use native components. My point the conversation will be pretty simple for me. Demonstrate to me if this is going to bring business value. If not we keep it as it is. It's pretty simple and this is coming from above.  
**Vladyslav Krut:** Okay,  
**Filippo Tosetto:** We need to start to  
**Vladyslav Krut:** as Philippo mentioned recently, we should either have a business reason or move on and ignore imperfections.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** That's going to be my main idea.  
**Filippo Tosetto:** Uh we are seeing a lot a lot a lot of pressure from the top to deliver way way faster and what I'm seeing in face AI is that we are stuck since one  
**Vladyslav Krut:** Yes,  
   
 

### 00:11:42

   
**Filippo Tosetto:** month pretty much.  
**Vladyslav Krut:** it generally feels like probably one whole month.  
**Filippo Tosetto:** this is not not good obviously and then if I start to nitpick on the work of  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** product I can say see that there is no business value in 50% of the initiatives that we are pushing and this is going to change this month for me as I can elevate a bit more on my actual position so to check the business value for specific initiatives and block things that are not important or move them in a sort of backlog less important part and tackle more important things that will bring value to the user. For instance, the app is lagging, the screen is freezing, we have no loaders.  
**Vladyslav Krut:** Let's fix this part, please. It's like it it hurts my my whole soul when I testing something else, something  
**Filippo Tosetto:** So,  
**Vladyslav Krut:** unrelated.  
**Filippo Tosetto:** what do you think rough estimate 120? When do you think it's going to go live?  
**Vladyslav Krut:** I really want to believe that on Monday, next Monday because today I am planning to finish all the work from my side one two days I expect to for the tickets to go through QA PO maybe something needs to be fixed and uh send so send it for Apple review on Thursday Friday and usually they approved during the weekend at least last two versions were approved during the weekend.  
   
 

### 00:13:25

   
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** So I genuinely expect it to go live on  
**Filippo Tosetto:** Okay. Sounds good to me.  
**Vladyslav Krut:** Monday.  
**Filippo Tosetto:** I think we are very very late but it's doable. It's a good idea. Okay. Nice. Thank you.  
**Vladyslav Krut:** Want to highlight there is one thing that is still not clear for me. uh the issue that Maria and Alexi were raising already a few times that when you try to upload the image, it just shows you generic error and it doesn't do anything. So apparently there there were at least four bugs stuck in the same exact place. One of them were related to upper test and I believe it should be completely fixed by now. I was testing it. it should genuinely be done resolved completely. Uh one of them were really minor like random rendering mistake when it was not preserving state of the error that was also fixed and it's still happening and why it is still happening now. So far I have no idea.  
   
 

### 00:14:30

   
**Vladyslav Krut:** It's somewhat hard to debug. This time the issue is reproducible on iOS 26 which means that I can use a proper device to eliminate all the simul simulators problems and I will be trying to fix that but I don't really know how many bugs there are on this exact spot still and from what I see in logs on gen like in Xcode there are some network requests to Firebase that are not being decoded correctly. which may or may not affect what's happening. There are some images that are not being downloaded on time and are throwing uh time out interval whatever which is should not be like uh bothering us at all but it is possible that it's showing a generic error. there are really really a lot of places from where this generic error may come and to fix it I have to find the root cause so this one is like it's hard to estimate this one the rest will be obviously  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** fixed because there's like UI fixes and stuff analytics something that like you do work you  
   
 

### 00:15:43

   
**Filippo Tosetto:** Easy.  
**Vladyslav Krut:** observe result you push to to progress it this one like oh  
**Filippo Tosetto:** Okay. Thanks, BL. Um, next point, still in face AI, we have the green light from upper management, meaning the CTO and the CPO to bend the rules from North Project. So that means no one is going to check metrics. That means we can remove user stories. That means we can start to work on epics.  
**Vladyslav Krut:** Okay. Okay. Good. Can continue with this and I will ask followup questions  
**Filippo Tosetto:** Yeah. Yeah. Yeah. So that also means it's not only about hey dig the user stories,  
**Vladyslav Krut:** after.  
**Filippo Tosetto:** let's work with epics. It's much more deep than that. Which means that if you feel that the existence of a meeting is not important anymore because of what a retrospective for instance every freaking week a retrospective it's  
**Vladyslav Krut:** Here  
**Filippo Tosetto:** insane. Let's please remove that.  
**Vladyslav Krut:** I kind of feel like retrospective is the meeting that's supposed to be useful and supposed to happen maybe not every week but every two weeks like every sprint because there are a lot of problems that's like that's a place where we address problems that's like the the only place for me to give for example Her hardor QA honest feedback regarding processes and work and whatever because I will not be doing this like on other meetings other than one at once but I don't have one with them.  
   
 

### 00:17:37

   
**Vladyslav Krut:** So I feel like the retrospective is probably the useful one. The rest not sure  
**Filippo Tosetto:** I said retrospective. You could use it and remove that.  
**Vladyslav Krut:** though.  
**Filippo Tosetto:** My my point here is please, we are not constrained by this framework anymore. Feel free to move things around at your free will.  
**Vladyslav Krut:** Awesome. Got  
**Filippo Tosetto:** Um,  
**Vladyslav Krut:** it.  
**Filippo Tosetto:** in all of this equation, you seem to be pretty switched on in this team. So, whatever decision you say you take, please think of QA as well.  
**Vladyslav Krut:** I do every time.  
**Filippo Tosetto:** And I'm going to explain this and this is going to reflect also on the next few points that I have. We need to stop complicating our lives because oh doesn't know how to do this. Oh but this is the process. Oh, but no, it's going to happen very soon that you are going to sit down with the PM in this app. They're going to discuss about improvements, new features, and that's it. Nothing else.  
   
 

### 00:18:57

   
**Filippo Tosetto:** You go on, you write the code, the AI write the code, 3 days after you come back with something implemented.  
**Vladyslav Krut:** Okay. With PM, not this P, right?  
**Filippo Tosetto:** I said PM because PO to me doesn't make sense to have two different people.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** I'm need engineering, you me to talk to people that take decisions in terms of product. As of today,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** the structure of the company, the PO is just a person that writes in Jira things that the PM decided. I don't need this person anymore. It's just complicating things.  
**Vladyslav Krut:** Okay. I I thought that PO is making decisions cuz that's cuz it's the owner. Okay. Thanks for explaining that makes sense. Okay.  
**Filippo Tosetto:** So,  
**Vladyslav Krut:** Continue.  
**Filippo Tosetto:** is it going to be a PO? Is it going to be a PM? I don't know. I don't care. I just need to elevate you to someone that that understand the business that you're working on AI.  
   
 

### 00:20:00

   
**Filippo Tosetto:** What are the competitors of these apps? Do you know what is the road map? What's the plan on making money with this app? Do you know these things?  
**Vladyslav Krut:** Well, surprisingly a few of them I know,  
**Filippo Tosetto:** But but the I mean I'm I'm obviously being provocative now,  
**Vladyslav Krut:** but it's still surprisingly like I was not expecting to be able to answer even one of  
**Filippo Tosetto:** but  
**Vladyslav Krut:** these.  
**Filippo Tosetto:** I I'm provoking you, but this is where you as a software engineer with this new role that we define should sit. Not going there. Yeah, but this pixel or explain to people that according to Apple guidelines, you cannot put two icons in the same row because it doesn't freaking work. And if it's a case to remove designers,  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** I'm going to do it. I need you to be free to not not in that sense completely remove the designers. Don't worry,  
**Vladyslav Krut:** That's scary. I don't want Thank  
**Filippo Tosetto:** but No, don't worry.  
   
 

### 00:21:06

   
**Filippo Tosetto:** Don't worry. But I need you to be free to improve the app and not spend  
**Vladyslav Krut:** you.  
**Filippo Tosetto:** time moving an icon by two pixel to the right. You know, that is waste of time for me. An app that today has if it's a lot 50 uh 50 in monthly recurring revenues, it's insane.  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** Speaking of, before we jump on the next topic, have I ever show you this? You know what this is?  
**Vladyslav Krut:** I don't think you showed me this. It looks familiar.  
**Filippo Tosetto:** So this is re revenue revenue cut.  
**Vladyslav Krut:** Okay, sure.  
**Filippo Tosetto:** This is all the apps in the portfolio and this is oops this is the monthly recurring revenue.  
**Vladyslav Krut:** Okay, that's what MR stands for. I see that's impressive  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** number.  
**Filippo Tosetto:** So you have apps like this one that does this number.  
**Vladyslav Krut:** Great.  
**Filippo Tosetto:** And then you have apps like this one that does this number.  
**Vladyslav Krut:** I know. To me, the two numbers to the left are more embarrassing than the one on the right column.  
   
 

### 00:22:40

   
**Vladyslav Krut:** It's not one single  
**Filippo Tosetto:** So when you keep working on the same ticket to move an icon from left to  
**Vladyslav Krut:** digit.  
**Filippo Tosetto:** right, I think about this and this and this while on the other end we have these numbers.  
**Vladyslav Krut:** That makes  
**Filippo Tosetto:** Okay? And that is why I would like you guys to be  
**Vladyslav Krut:** sense.  
**Filippo Tosetto:** more involved in the business itself that you're working on. Every app is a small business. You should be aware of why we are making the certain decisions and being able to push back and when I say push back is obviously in a nice way say hey probably this is not really important we should move forward because we are very late. So yeah,  
**Vladyslav Krut:** Yeah, that should at least you know pay pay my salary and the other guys who are working  
**Filippo Tosetto:** it's  
**Vladyslav Krut:** on this project at least.  
**Filippo Tosetto:** but you're joking about this but the the there are talks about  
**Vladyslav Krut:** I'm not  
**Filippo Tosetto:** these points because today what we're doing is we know how much money an app make and we know how much money we spend in advertisement.  
   
 

### 00:24:01

   
**Filippo Tosetto:** If the advertisement is lower than the money that you make, all good, you're growing. If it's the other way around, not good.  
**Vladyslav Krut:** Do you spend any money on an advertisement for FA now?  
**Filippo Tosetto:** No, not yet. After 1.2.0,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** we will. But the point is that there are other costs.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** How much do you cost to the company? How much the PO does it cost to the company? How much the beam cost to the company? How much does each pressing a button and generating an image cost to the company? So blood this is a conversation that I need to have at my level obviously not at yours but I think that knowing or having an idea of all these points could help you taking specific decisions in the future.  
**Vladyslav Krut:** Yes,  
**Filippo Tosetto:** So that is why I'm very determined to start to elevate a bit the conversation and not  
**Vladyslav Krut:** absolutely.  
**Filippo Tosetto:** moving tickets from right to left, left to right because one pixel is off.  
   
 

### 00:25:08

   
**Filippo Tosetto:** And that's why I'm very happy if you start to say, "Hey guys, probably having a synchronous poker planning with five, seven people sitting here to look at me pressing a button. It's probably not the best way to use our  
**Vladyslav Krut:** That's not going to happen anymore. I already had this conversation with Herardo.  
**Filippo Tosetto:** time.  
**Vladyslav Krut:** No, poker playing I believe will not be happening at all. I I don't see any single point to have this conversation before.  
**Filippo Tosetto:** But at the same time, I don't want you to waste your time in chasing answers. You need to be able to take your own decisions in if things allow it. Obviously, one thing is to decide to do some small detail to to take decisions on some small details. The other is to keep other people accountable for what they need to be doing.  
**Vladyslav Krut:** Yeah, this one is important. Not sure if I can do this on from my side, but at least I can highlight  
**Filippo Tosetto:** No, exactly.  
**Vladyslav Krut:** it.  
**Filippo Tosetto:** Exactly. The whole point of moving the conversation to epics is this because we elevate the conversation is not about small details.  
   
 

### 00:26:29

   
**Filippo Tosetto:** It's more about taking bigger decisions. But you need the answer that you seek. Otherwise, you cannot progress. Especially now that I'm going to introduce something bigger for  
**Vladyslav Krut:** Yeah, let's go.  
**Filippo Tosetto:** you.  
**Vladyslav Krut:** What's going to happen? How How do we work now?  
**Filippo Tosetto:** So, face AI deliver 1.2 and then I need you to start to seriously look into AI design.  
**Vladyslav Krut:** Yes, that's what we agreed last  
**Filippo Tosetto:** So AI design is in a much better shape than face  
**Vladyslav Krut:** week.  
**Filippo Tosetto:** AI at least that not from not from a code perspective. I can't say that because I don't really have a full understanding of it but definitely from a product perspective the direction is way more clear. We already have marketing spent in the app. The app is way more advanced.  
**Vladyslav Krut:** Just  
**Filippo Tosetto:** the features are better. The app is responsive for instance. Um the timeline is for  
**Vladyslav Krut:** heat.  
**Filippo Tosetto:** you to take over obviously the full mobile development for iOS.  
   
 

### 00:27:45

   
**Filippo Tosetto:** Let's see if Android is still an option for sure by the end of Q3.  
**Vladyslav Krut:** sounds very reasonable.  
**Filippo Tosetto:** So you will you will have two applications face AI AI design and you will control at least all the mobile platforms by the end of Q3. This this timeline is obviously a bit shaky meaning could  
**Vladyslav Krut:** Of  
**Filippo Tosetto:** be before could be after depending on what you face in all of this. cannot say hey lad oh no it's uh end of Q3 you haven't done  
**Vladyslav Krut:** course,  
**Filippo Tosetto:** this yes  
**Vladyslav Krut:** we will be discussing this plan probably like every  
**Filippo Tosetto:** because things are going to move but  
**Vladyslav Krut:** month.  
**Filippo Tosetto:** um I want to ask you how you would approach at least the iOS part and then I have a proposal for you from from your  
**Vladyslav Krut:** How would they approach at least as part of a design?  
**Filippo Tosetto:** learnings Sorry from your  
**Vladyslav Krut:** Sorry, say  
**Filippo Tosetto:** learnings that you had from face AI the approach that you had the beginning how you working  
**Vladyslav Krut:** again.  
   
 

### 00:29:05

   
**Filippo Tosetto:** now what's your take  
**Vladyslav Krut:** Uh so so far probably an important you know it was somewhat obvious but I have proven that everything is different on every project and the way we approach solving problems will be very different depends on the existing state the people we work with and well the tools we are using and the tasks itself. Why I'm saying this? Because for now uh from what I was doing on face AI uh last months or so not a lot of this job could be done let's say autonomously by AI in reality very little part of it could be done and from all the tickets that I see in front of me now on the board pretty much none of it could be handled by I in isolation It's every time engineer should be really carefully going seeing either explaining what needs to be done and how and then realistically because of the state of the code base. A cannot solve this problems UI layout could be solved if this like one autonomous isolated screen. If this is poorly connected 14 components across nine screens changing one of them breaks another.  
   
 

### 00:30:43

   
**Vladyslav Krut:** So no engineering mindset is needed here. Probably approach it first with at least a little bit of refactoring to you know to make some of the behaviors obvious both for engineer and for AI before actually approaching this when we'll have new features on face AI it will somewhat depends like let's say we add new you know filters or functions or something will it be easy? No, it still will not be easy because we have nine different screens that are doing approximately the same feature. I will go and take an inspiration from one of them or from all of them at the same time. I don't know. It's once again for me up to engineer like to find the best of them, the most clean and to reuse this one or approach it in a refactoryish way and unify everything as it was supposed to be from the very beginning. Don't really know yet when we will be working on optimization and eliminating loss. Well, when we were debugging v via Xcode, it throws you dozens of main thread errors checks pretty much on every button press like and don't solve them.  
   
 

### 00:32:02

   
**Vladyslav Krut:** Anton for sure solve them. Can AI see these warnings and errors and notifications? No, it cannot. It will be up to me to go through every specific action that is lagging finding exact places that are not working correctly where we have synchronous I don't know image rendering on main thread and eliminate it I will not have business well it will but it not will do this without me what's going to happen on face on AI design I have no idea I will go and take a look on how Z is working and meet the team and see how their board and road map are looking and then probably go and how do you say f\*\*\* around and look around and try to figure out what type of technical effort will be needed to implement to to continue moving with this road map. Will it be easy? Will it be straightforward? Other tools or screens or components to be reused or everything needs to be, you know,  
**Filippo Tosetto:** All  
**Vladyslav Krut:** done from scratch? Well, if the app is responsive, that's already good sign.  
   
 

### 00:33:20

   
**Vladyslav Krut:** If it's making money, it also kind of, you know, says at least some quality bar.  
**Filippo Tosetto:** right, let's see. Let's see.  
**Vladyslav Krut:** So it is going to depend on a lot of  
**Filippo Tosetto:** Let's see. So,  
**Vladyslav Krut:** stuff.  
**Filippo Tosetto:** this is AI design. It's definitely better than Face AI. It is way better than Face  
**Vladyslav Krut:** True.  
**Filippo Tosetto:** AI.  
**Vladyslav Krut:** So will be a very typical standard normal  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** and somewhat old school on boarding when I go meet the team.  
**Filippo Tosetto:** Nope. No, let me explain what I'm thinking because for  
**Vladyslav Krut:** Nope.  
**Filippo Tosetto:** me while you work on on face AI and other projects, I'm working trying to help you guys to move faster and to remove the big technical debt that we are dealing with today, which is the code base. And we know that AI cannot go you cannot tell the AI go and refactor this because I want it in this architecture I want all the bugs fixed as you know you just described the reason so I've been thinking with  
   
 

### 00:34:48

   
**Vladyslav Krut:** No  
**Filippo Tosetto:** um with Serio Durban what's the best approach for this so approach number one redo the app from scratch we know that it doesn't work because it will somehow you won't be able to keep progressing. You need to stop the product for a month until you redo it from scratch. And then we have three weeks of back and forth with QA. And we know that this is going to it's a long process.  
**Vladyslav Krut:** Yes, the report itself will not be that difficult,  
**Filippo Tosetto:** So,  
**Vladyslav Krut:** but the months after it  
**Filippo Tosetto:** so if it was a new app from scratch,  
**Vladyslav Krut:** will.  
**Filippo Tosetto:** new product, nothing yet decided, I think it is the best approach because with the tools that we have at our disposal,  
**Vladyslav Krut:** Absolutely.  
**Filippo Tosetto:** we're going to be really fast. How can we find the best way to put together these two words? And for me there is this is a sort of pre-work to be done that you surfaced while starting to work on face AI and please stop me here if if I'm saying something wrong but my impression was that you didn't have all the context of the app not only talking about from a codebased perspective but in general what does this product do and not because you know you you you are lacking the capabilities to find this information for yourself.  
   
 

### 00:36:20

   
**Filippo Tosetto:** But it's a sort of knowledge that only a person that worked in this project for a long long time can acquire. You know all the ins and outs of the  
**Vladyslav Krut:** more or less I agree.  
**Filippo Tosetto:** app.  
**Vladyslav Krut:** Yes, like F is a pretty small project. It's it's not about long time, but yeah.  
**Filippo Tosetto:** There is a second point that we know being true which is AI reproduce patterns that they know. If I start to code a new feature in a codebase that is not good, it's trying to reproduce that.  
**Vladyslav Krut:** Here  
**Filippo Tosetto:** Even if I put all the rules and skills in the world around it, it doesn't work  
**Vladyslav Krut:** I can correct you. Um, no.  
**Filippo Tosetto:** perfect.  
**Vladyslav Krut:** If you specifically explained how the new feature should be done via explicitly in the prompt or via skills, it will follow the skills because I feel like it's looking for the information around for the things it doesn't know how to do. If you provide examples, code snippets, relationship, everything as you want it, it will follow these examples and and produce it how you want it.  
   
 

### 00:37:43

   
**Vladyslav Krut:** I have a somewhat strong belief in  
**Filippo Tosetto:** Yep.  
**Vladyslav Krut:** this.  
**Filippo Tosetto:** But there is one point that we keep surfacing here is that you cannot outsource to an agent to do this job for you. You need to be there to check that the code produce is according to your standards that it doesn't introduce bugs that it doesn't replicate the bad pattern.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** So you need a human being you in this case to check that the code produced is actually effective.  
**Vladyslav Krut:** Yes. Absolutely.  
**Filippo Tosetto:** We could we we can we cannot buy code today.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** It's wrong. We cannot do it. I mean we can but you know so talking to  
**Vladyslav Krut:** We should not be doing  
**Filippo Tosetto:** Sergio he started to work on a new project to man an existing project with a team and  
**Vladyslav Krut:** this.  
**Filippo Tosetto:** he didn't do any coding he he simply on boarded a developer an internal developer to work on a project and this developer didn't know anything about the project how did he approach this it's pretty much your your your current situation I'm asking you to start to work on AI design you have zero context you don't understand anything around this yet.  
   
 

### 00:38:56

   
**Filippo Tosetto:** He wrote a full repository full of markdown files with not only the architecture but also all the feature the design docks the the everything that need to be Yeah. Especially this stakeholder questions and decisions. And here this is a very very long set of questions and answers on how things should be done from a product perspective and from a mark uh from a a technical perspective. Good.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** So let's abstract a bit. We need a place better if it's in markdown with the full specification of the project all the features. Okay. Where is the place today where we can get that info?  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** And for me that place are the test cases, the food aggression. Because if you think about it, it's about if I open screen X and press button Y, this thing should happen. What is all of this? If you can think about it, it's a girking file.  
**Vladyslav Krut:** Yes, it really  
**Filippo Tosetto:** So different steps here.  
**Vladyslav Krut:** is.  
   
 

### 00:40:41

   
**Filippo Tosetto:** Step number one, get all the knowledge, all the context, put it in a markdown repository, files, whatever, from a feature perspective, but also from a technical perspective, architecture, APIs, calls, third party tools that needs to be used, AB testing, these kind of things.  
**Vladyslav Krut:** Mhm.  
**Filippo Tosetto:** Step number two, ask an AI to take this ball of knowledge and compare it to the current state of the codebase and create a diff.  
**Vladyslav Krut:** Will AI manage to do this?  
**Filippo Tosetto:** If it's atomic enough. Yes.  
**Vladyslav Krut:** That's really cool. If Okay, let's assume it can. I I I doubt honestly that it would work for face.  
**Filippo Tosetto:** Let's  
**Vladyslav Krut:** Well, maybe we can just try. Okay, let's assume it  
**Filippo Tosetto:** let's assume we can step number three break  
**Vladyslav Krut:** can.  
**Filippo Tosetto:** everything meaning start the refactoring and there are two refactorings levels. There is an horizontal refactoring and a vertical one. The horizontal one is I need to rewrite the old networking layer. The vertical one is feature by feature.  
   
 

### 00:42:18

   
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** And so your job will be to use all these components that we created, these artifacts that we created, this documentation that we created for you to understand how the app should work and for you to guide the AI to refactor a piece of code. So that in six weeks, one month, two months, whatever, the application on the other side didn't stop development. But we slowly moved it into the new into a clean way that we have of working so that in a quarter you can go faster in developing new features.  
**Vladyslav Krut:** clarification need. Did you say that the refactoring is going to happen while the app is moving forward by two different engineers in different repositories or branches on the same  
**Filippo Tosetto:** No, no.  
**Vladyslav Krut:** like it's like basically two engineers working together.  
**Filippo Tosetto:** Yeah, there's you. You're going to refactor.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** And there's the current iOS developer working in AI design that keeps working the way it's working.  
**Vladyslav Krut:** Okay,  
**Filippo Tosetto:** So first of all, does this make sense to  
   
 

### 00:43:49

   
**Vladyslav Krut:** absolutely. That's that kind of feels similar to what we were doing in Face AI with  
**Filippo Tosetto:** you?  
**Vladyslav Krut:** Anton primarily working delivering tickets. cannot say he was doing new features but doing tickets that people have chosen and I was like taking one ticket and refactoring everything around it in like little cleaner island trying to not break anything but make everything reusable adaptable and like working properly very similar to how it was with me and Antonius  
**Filippo Tosetto:** For me the preliminary steps could be very helpful. But you have the full knowledge of this or how to work today.  
**Vladyslav Krut:** Preliminary  
**Filippo Tosetto:** So would this actually help or not?  
**Vladyslav Krut:** steps.  
**Filippo Tosetto:** The outcome of this would be you have the the famous feature Girkin files. Okay, done for you for free because we are going to find a way to get this which will allow you to refactor a feature knowing exactly what should happen after the refactoring which also will create unit tests and technically it shouldn't break the current situation of the app.  
   
 

### 00:45:18

   
**Vladyslav Krut:** I believe in that but only under condition that the current state of zap is not better. Once again using faci as an example it would not work like 100% the existing image adjust view AI would break the leg and the application in this one file primarily because AI tends to trust how you know the methods and properties are called and the way they're called here doesn't reflect what they're AI will not spot this problem. Well, it will if you ask it specifically for that. Otherwise, it will just look at the higher level from the classes that are pulling this make wrong decisions and proceed with incorrect implementation.  
**Filippo Tosetto:** If you guide that.  
**Vladyslav Krut:** Gir file brings Girken file brings a lot  
**Filippo Tosetto:** Yeah. Sorry. Go on.  
**Vladyslav Krut:** of value and will help obviously spot all the functional bugs. So if the feature is not working correctly, if it's calling wrong endpoints, incorrect screens are shown. Yes, of course, all of that will be spotted. Let's be honest, it probably has been spotted by developer or QA or PO at some stage.  
   
 

### 00:46:49

   
**Vladyslav Krut:** Well, I hope there are three human levels of defense for the feature not for the feature working completely. completely incorrectly before it hits production like you see my point right but all the smaller  
**Filippo Tosetto:** I do.  
**Vladyslav Krut:** things like okay UI consistently we don't talk AI cannot spot this QA maybe should not spot this developers usually don't care uh but the animation perform or not application  
**Filippo Tosetto:** Not for me.  
**Vladyslav Krut:** performance. That's a big one. AI will not spot the problem unless you tell it like what to look for and maybe where. So if you ask it look for the image rendering on the main thread, will it find something? I don't know. We can test. I I haven't tried it yet actually yet.  
**Filippo Tosetto:** So what am I expecting you to do? First of all, you need to start to be able to manage two projects. So you need to manage your time into projects.  
**Vladyslav Krut:** Yes, this is where I see a big generally  
**Filippo Tosetto:** H but for me it's easier than you think.  
   
 

### 00:48:05

   
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** Let me explain my thinking but I may be absolutely wrong here. First one is by you being a solo software engineer in Face AI, you're going to dictate some rules to help you move things forward and remove redundant process. For instance, time wasted for a lot of things.  
**Vladyslav Krut:** Of course.  
**Filippo Tosetto:** Second, if you can deliver the same at least at the same speed as we are delivering today, even if you're managing two projects, for me that's good enough for now.  
**Vladyslav Krut:** That sounds like huge win for me because the application is still not on the stage where AI can deliver.  
**Filippo Tosetto:** Yes, I  
**Vladyslav Krut:** It's still me not writing code but specifically that I would write.  
**Filippo Tosetto:** know.  
**Vladyslav Krut:** So yeah, keeping the same performance is already win. Genuinely I expect a temporary slowdown in speed until the moment when codebase is in a little bit better shape when AI can do work better or what also will help better understanding of what of what needs to be done because amending code is not where AI shines.  
   
 

### 00:49:26

   
**Vladyslav Krut:** Creating code yes it does it faster. So I do expect a slowdown temporary and then gaining speed. Yes, that how I believe it will  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** go.  
**Filippo Tosetto:** So, the idea for me is for you to spend this week to close face AI the 1.2. Get it out of the way as soon as possible, please. But also I'm really expecting you to explore a bit the AI design codebase and meanwhile I'm going to  
**Vladyslav Krut:** I should have plenty of time for this.  
**Filippo Tosetto:** move forward this idea of the experiment that I have in mind regarding refactoring if it could work.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** So I am working with Alex on the idea of getting all the data from X-ray all the test cases and trying to create these clear files. If we can get this done, which I'm sure that we can,  
**Vladyslav Krut:** Yeah, of  
**Filippo Tosetto:** I think this should help you a  
**Vladyslav Krut:** course.  
**Filippo Tosetto:** bit.  
**Vladyslav Krut:** Well, at least I will be able to explain to me what's happening everywhere for sure.  
   
 

### 00:50:47

   
**Vladyslav Krut:** That's yes or yes. Yes.  
**Filippo Tosetto:** Um, what I would like to have if it's timely possible by next Monday to have a at least for the iOS code base is to have a status report sort of, hey, this is bad. This is as bad as the CI. No, this is not as bad. It's just a lot of uh mud code that needs to be cleaned up. I don't know. Sort of an analysis from you.  
**Vladyslav Krut:** Okay,  
**Filippo Tosetto:** And next week I will start to introduce you to the  
**Vladyslav Krut:** now  
**Filippo Tosetto:** team.  
**Vladyslav Krut:** also make sense.  
**Filippo Tosetto:** Not this week. I don't want you to spend time this week with the  
**Vladyslav Krut:** Yeah, then next thing makes sense.  
**Filippo Tosetto:** team.  
**Vladyslav Krut:** This will like probably get me a little bit of time to get 1.2 out of the way and a little bit  
**Filippo Tosetto:** So yeah, that is um that is the plan.  
**Vladyslav Krut:** here.  
**Filippo Tosetto:** What do you  
**Vladyslav Krut:** I think that's completely doable. Yes, sounds reasonable.  
   
 

### 00:51:48

   
**Filippo Tosetto:** think?  
**Vladyslav Krut:** I plan to today and tomorrow finish majority of the coding part. Then I expect some kind of communication maybe a little bit back and forth with QA and PO to actually polish and release 1.2 send it to review. I should have time to take a look at to face AI or AI  
**Filippo Tosetto:** They are  
**Vladyslav Krut:** design and give some kind of status report.  
**Filippo Tosetto:** design  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** great blood. Anything else you need from me?  
**Vladyslav Krut:** Are you familiar with amplitude like how clo uh I have a  
**Filippo Tosetto:** Brilliant.  
**Vladyslav Krut:** question regarding our organization here uh how face AI fits the this structure I'm not I'm not really familiar with this so let me explain what I'm experiencing here it looks to me like have a I believe it's called space right or organization where we have all our apps.  
**Filippo Tosetto:** Organization is the organization. Projects are single apps.  
**Vladyslav Krut:** Okay. So we have projects other than symbols but we also have whatever is called  
**Filippo Tosetto:** So space is folder.  
   
 

### 00:53:14

   
**Vladyslav Krut:** spaceship.  
**Filippo Tosetto:** Think about it as a folder that we create and decide what to put inside. Usually this is handled by product people, product managers usually. So uh I'm I'm I'm I'm going to start from scratch. So when you open amplitude, you reach this screen.  
**Vladyslav Krut:** One sec. One sec. One sec.  
**Filippo Tosetto:** You go here.  
**Vladyslav Krut:** One sec.  
**Filippo Tosetto:** Yep. Can you see?  
**Vladyslav Krut:** Yes, I see.  
**Filippo Tosetto:** You go here.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** You can see all the spaces that we already  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** have.  
**Vladyslav Krut:** Here is probably where I may not have enough accesses if I Oh,  
**Filippo Tosetto:** But you should at least see this  
**Vladyslav Krut:** no. No. Never mind. I I see.  
**Filippo Tosetto:** one.  
**Vladyslav Krut:** I see. Okay. No, never mind. I see it.  
**Filippo Tosetto:** Okay. You open it and here you have other folders. Usually what I do is to look at dashboards because someone some someone smart created this dashboard for us can open it and the data start to appear here and here you see different boards based on whatever reasoning that there are inside here to check the data.  
   
 

### 00:54:36

   
**Filippo Tosetto:** So basic APIs like screen on boarding and inapp purchase obviously with the little users that we have these boards don't really mean a lot uh retention by country on different days uh breakdown on users by country these kind of things but this also can be behavioral if you can create a chart for it.  
**Vladyslav Krut:** Okay. So here is let me now share my screen because I have a suspicion that  
**Filippo Tosetto:** Sure.  
**Vladyslav Krut:** something doesn't really configure is not really configured correctly.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** So here is a am I sharing? Yes.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** So this is a dashboard right. I'm in the face AI on the dashboard. It doesn't show me exactly what is happening here. But if I press onto view, it throws me somewhere else away from Face AI and I'm not on PI anymore.  
**Filippo Tosetto:** Sorry. Can you go Can you open spaces?  
**Vladyslav Krut:** Yes, in spaces I have this joint space.  
**Filippo Tosetto:** All All spaces. Yeah. Go to all spaces.  
   
 

### 00:55:53

   
**Filippo Tosetto:** Be all Yeah.  
**Vladyslav Krut:** Yeah, in all spaces. Okay, I have quite a lot of them  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** here.  
**Filippo Tosetto:** You can search for face AI for instance. Yeah. Go to dashboard.  
**Vladyslav Krut:** It's where I was. Yes.  
**Filippo Tosetto:** What the hell?  
**Vladyslav Krut:** Okay, then it not was not me who is doing something wrong. Maybe I need do you know who I can contact about this?  
**Filippo Tosetto:** I'll I'll put you in a chat with um with the right people is the people from  
**Vladyslav Krut:** Okay, thank you. I was doing one task rel to analytics and I was supposed to test somehow that I did the job  
**Filippo Tosetto:** market.  
**Vladyslav Krut:** correctly and I couldn't.  
**Filippo Tosetto:** So quick trick that I have for checking events. So if you're developing if you want to check an event in the left hand side there is some live events which is the up  
**Vladyslav Krut:** I users not live  
**Filippo Tosetto:** up yes here this  
**Vladyslav Krut:** events.  
**Filippo Tosetto:** is uh so on top you see no no on top there's a filter under underneath create  
   
 

### 00:57:05

   
**Vladyslav Krut:** Uh say again where underneath  
**Filippo Tosetto:** underneath create on top top top  
**Vladyslav Krut:** create. Okay.  
**Filippo Tosetto:** left there's apps AC and okay now you need to  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** search for oh you don't have access to face AI  
**Vladyslav Krut:** Yeah, that's how I figured out that something is not working correctly for me.  
**Filippo Tosetto:** okay so I'm I'm going to share I'm we're going to solve this  
**Vladyslav Krut:** I have it here.  
**Filippo Tosetto:** problem but I want to show you how you can easily um do some debugging. So if you press the live events, you see all the events live for a specific app. In here, you can choose the app place AI, you have stage and uh live. I want to choose stage because it's for sure more alive than the other apps. And here you see all the users that we have at the moment. And you can activate the live events. As you can see, every user is identified by a user ID. Okay? And so if you press any of these events the which are happening in  
   
 

### 00:58:06

   
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** Spain, you will have all the list of events happening for that specific users in the past and right now. If you want to see user properties, you have two ways. You have the user properties on your left here. User properties,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** library, iOS, etc. where you can see more like  
**Vladyslav Krut:** Yeah. Yeah. So, total library photo.  
**Filippo Tosetto:** subscriptions.  
**Vladyslav Krut:** That's the one I added and it's working. Nice.  
**Filippo Tosetto:** Yes. But also every event has some properties and you can see them on the right. So this event property is the session ID which is this one. the screen main and and here you can see all of that and obviously you can see more the 11 one that you were looking for. So I'm going to um to ask Martek to give you more permission regarding uh all the boards and so you can do all the debugging by yourself. But if you need any help in finding a way to use amplitude, let me know because I can help you because I spent a lot of time in the the last five years checking data in  
   
 

### 00:59:29

   
**Vladyslav Krut:** Well,  
**Filippo Tosetto:** amplitude.  
**Vladyslav Krut:** I have a feeling that I was doing everything right, but I didn't have access.  
**Filippo Tosetto:** So that's it.  
**Vladyslav Krut:** Yeah, that was my only question.  
**Filippo Tosetto:** Any other questions?  
**Vladyslav Krut:** No, that was the only one. Oh, no, one more. One more. So, the high level plan is very clear. I'm working on faci trying to deliver it make it good. Start working on AI design. Spend some time like shadowing the engineer and doing some refactoring if needed. What about Android? Is it still on the board? Is it still in our plans or we are like under discussion exploring whether it will be feasible or not? Where are we?  
**Filippo Tosetto:** It's still a in the plans, but first I need to be able to demonstrate, we need to be able to demonstrate that you can actually work with AI without going too deep in the code base in iOS,  
**Vladyslav Krut:** Sure  
**Filippo Tosetto:** which is your area of expertise.  
**Vladyslav Krut:** because if I cannot I have little chances this is  
   
 

### 01:00:35

   
**Filippo Tosetto:** How can you do it in Android?  
**Vladyslav Krut:** Android well I still will probably succeed but it's going to be it's going to be taking more time and we are trying to save  
**Filippo Tosetto:** For me that is definitely end of Q2 starting to look Q3 second half for you two. Infree, you're going to start to explore the idea of Android once you catch it. Both face AIOS and uh um AI design iOS things that you are comfortable  
**Vladyslav Krut:** Okay, makes sense. Yeah.  
**Filippo Tosetto:** saying, hey, I'm good. New feature bum. Develop next next codebase is in good shape. Processes are in good shape. Hence why having that place with all the context and knowledge of an app is going to help you on Android as well because it's going to be easier if it's centralized.  
**Vladyslav Krut:** Maybe the very last one.  
**Filippo Tosetto:** Lad, I'm off  
**Vladyslav Krut:** When do we start this initiative with Epics?  
**Filippo Tosetto:** yesterday uh as soon as  
**Vladyslav Krut:** Got it. Okay, let's stay in touch then.  
**Filippo Tosetto:** possible. Uh, tomorrow we're going to have the space. No, on Wednesday I'm going to make it more obvious to Eardo to push for this. No more user stories, but I want epics with all the information there.  
**Vladyslav Krut:** Okay, makes sense.  
**Filippo Tosetto:** I already pushed back a few epics, by the way.  
**Vladyslav Krut:** Thanks. I appreciate it. I didn't see, but nice to know.  
**Filippo Tosetto:** Yes. Right, Vlad. Have a great day. Let me know if you need anything else.  
**Vladyslav Krut:** Thanks. You too. Sure you.  
**Filippo Tosetto:** Bye-bye.  
**Vladyslav Krut:** Bye.  
   
 

### Transcription ended after 01:02:35

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*