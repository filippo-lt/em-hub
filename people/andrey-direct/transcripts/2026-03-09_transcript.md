```markdown
Mar 9, 2026

## Andrey / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Hello.  
**Andrei Marinov:** Hello. How's it going?  
**Filippo Tosetto:** I'm good. What about you?  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** Yes.  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** Are you Are you walking all good?  
**Andrei Marinov:** I started yesterday and it's very tiring for some reason.  
**Filippo Tosetto:** Yes. It's um I I remember that time it was like training your brain again to do something you need to think about. Yeah. It's  
**Andrei Marinov:** I mean,  
**Filippo Tosetto:** it's  
**Andrei Marinov:** I don't think it's that far because uh I can like limp around, but uh for whatever reason, at the end of the day, I'm really tired. Yesterday, I slept for almost nine hours.  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** I haven't done that in years and years, and I'm still tired.  
**Filippo Tosetto:** Whoa. Okay. Wow. All right. And how's your wife doing?  
**Andrei Marinov:** Uh she's okay. Uh she actually is now on her uh sort of sick leave before  
**Filippo Tosetto:** Actually,  
**Andrei Marinov:** maternity. So uh she just started today actually and she's figuring out what to do with her time and life until then.  
   
 

### 00:01:33

   
**Filippo Tosetto:** she she can help. There's plenty to do for her if she wants.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** But when is when is she due?  
**Andrei Marinov:** And the paper at some point.  
**Filippo Tosetto:** End of April. Okay. Okay.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** So, you still have around six weeks. Nice. Okay. Okay.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Nice. Andre, how are you doing after our conversation the other week? Yes. Last week.  
**Andrei Marinov:** I'm doing okay.  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** That's yeah nothing nothing major.  
**Filippo Tosetto:** Okay. Nice.  
**Andrei Marinov:** Why?  
**Filippo Tosetto:** Um, let's go down to business because the first part is easy and then I want to talk about the second part. Uh, new team starting tomorrow. Um I'm assuming you're going to be the one doing the technical on boarding for uh IMO Android. I don't know how much you can explain in terms of architecture but at least you know CI/CD PR reviews the usual s\*\*\*  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** and uh same for AI design maybe there you will have a bit more to say especially what to expect from them considering the current state of the codebase.  
   
 

### 00:03:02

   
**Filippo Tosetto:** Um this is very important. The company is going full bersc on AI tools and there are now in the contracts with Anada and actually every provider they must provide cursor to all the developers and please push them to use it.  
**Andrei Marinov:** I love  
**Filippo Tosetto:** Uh I'm I'm seeing very interesting results from  
**Andrei Marinov:** you.  
**Filippo Tosetto:** this. Uh meaning that I have too many PRs now for the two projects that I have. It's freaking insane the situation which is good. Which is good.  
**Andrei Marinov:** How many do you get a day?  
**Filippo Tosetto:** Uh only this morning I think it was four or five for one  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** project.  
**Andrei Marinov:** For for only for the morning or for like the whole day?  
**Filippo Tosetto:** Uh just for the morning.  
**Andrei Marinov:** Okay. And how many usually in a  
**Filippo Tosetto:** Uh uh one  
**Andrei Marinov:** day?  
**Filippo Tosetto:** one two sorry one per platform.  
**Andrei Marinov:** Four.  
**Filippo Tosetto:** One per platform. Yes.  
**Andrei Marinov:** project.  
**Filippo Tosetto:** Uh but um I'm not counting the Chinese 57 blocks because they already started to use AI since beginning of January.  
   
 

### 00:04:22

   
**Filippo Tosetto:** And uh we can see two and a two months after  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** The number of user stories delivered, the number of commits and the quality of the code is pretty much increased  
**Andrei Marinov:** Nice.  
**Filippo Tosetto:** by multiply by three. Yes, it's very nice. Not what where we want to go yet. We want to go far, but three 3x is already good comparing to what we had today.  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** Um, do you see any issues with the plan that Miguel presented today?  
**Andrei Marinov:** Uh you know it's like uh mostly small stuff to get them up to speed so that uh they can get familiar with the code and yeah start working on  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** it.  
**Filippo Tosetto:** Uh my suggestion for you is please tell them to use AI tools to remodel the code first thing. Don't worry about you know the full process things. Just go  
**Andrei Marinov:** Yeah. And I started getting some technical stuff so that we can do the same thing like on my mode with the epics and technical dep related epics.  
   
 

### 00:05:43

   
**Filippo Tosetto:** Perfect. Very nice. Um, Dimitro, how is it  
**Andrei Marinov:** Uh so far no change since last time  
**Filippo Tosetto:** going?  
**Andrei Marinov:** when we talked. Uh it was there was an interesting PR today as well but I don't know I'm still early to tell whether it's it's like good or not from what I see. So, here his PR from today. Uh, there's some prompt templates from Ginger. I'm not never heard of this stuff. Uh, but apparently some of the stuff that he's put in there is not a correct syntax error, which should fail immediately, which is I don't know. I I have no idea. I've commented all of this stuff for him and uh we'll talk it through with him. Uh but it's interesting to I mean it's weird because it it's just AI says that this will fail. Uh and supposedly he's been testing this. So maybe not. Let's see. Uh some other stuff. this thing again. This means it custom prompt and with this in here it means just print print the literal uh semicolon.  
   
 

### 00:07:10

   
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** I forgot the name of what that was called but it will just print this thing uh which is  
**Filippo Tosetto:** Yeah. Yeah. Yeah. Yeah.  
**Andrei Marinov:** again weird but I don't know. Um again some sort of a strange formatting here. Maybe he's copied it from some place, but this will break things.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** Uh, this is like a meditation error again. Some uh typos, which means that he's at least typing it himself. I don't know. Again, a typo here and a typo here. Uh, he doesn't know how to spend spell and hands. And yeah, this is like some tests were going to get uh ignored if it's not the deploy environment. Apparently, there's a better way to do it. Uh some things that are hardcoded to true, which sort of doesn't address things later on, which is not great. Uh this is not a big one. Uh so yeah that sort of thing that where there's like some small things that I don't know maybe if you run the what you're working on and uh those kind of things will pop up.  
   
 

### 00:08:32

   
**Filippo Tosetto:** But do you think this is related to the fact that this guy is mainly AI trained instead of be trained as well?  
**Andrei Marinov:** Oh, this is the eye part the  
**Filippo Tosetto:** Oh, okay.  
**Andrei Marinov:** ginger stuff. This is the and it's everything it's related to prompting. So the Python  
**Filippo Tosetto:** brainstorm moment with you. I have a very good uh  
**Andrei Marinov:** So the cycle  
**Filippo Tosetto:** yeah I have a very good uh back end/AI engineer working with me in face AI but he's from a different company. If I ask him to come here and have a look at this PRS, what do you think?  
**Andrei Marinov:** I still think that it's a bit early. Um,  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** only need another week or two to if these sort of things keep happening, I'll definitely bring it up. But, uh, yeah, you asked. I show  
**Filippo Tosetto:** No, no, but please.  
**Andrei Marinov:** you.  
**Filippo Tosetto:** Good. Um, keep me informed. I'm expecting this guy to start to produce something a bit more meaty very  
   
 

### 00:10:12

   
**Andrei Marinov:** Uh so the the garden design is up to that now and he's implementing it.  
**Filippo Tosetto:** soon.  
**Andrei Marinov:** So that's where the the true test is.  
**Filippo Tosetto:** That error mapping thing. Is it done?  
**Andrei Marinov:** Ah, yeah,  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** it is.  
**Filippo Tosetto:** has been deployed and spine.  
**Andrei Marinov:** Uh, it's not been deployed, but it's in testing.  
**Filippo Tosetto:** Why is that?  
**Andrei Marinov:** Uh, this spring we wrapped it up and, uh, we're just about now  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** releasing.  
**Filippo Tosetto:** Okay. No,  
**Andrei Marinov:** I mean,  
**Filippo Tosetto:** it sounds good.  
**Andrei Marinov:** deployed as far as deployed on the stage environment, it is. Yeah.  
**Filippo Tosetto:** Ah, okay. That that's that's for me that's uh that's good enough.  
**Andrei Marinov:** It's not deployed in the app overall.  
**Filippo Tosetto:** Yeah. Yeah. Yeah. But the important thing is that you're testing they are testing that that things are moving forward.  
**Andrei Marinov:** Uh yeah, so the external QA came to go ahead today and Maria was just testing now and uh she had a lot of comments but it's it was mostly about the nor  
   
 

### 00:11:15

   
**Filippo Tosetto:** Yeah. Yeah. Yeah.  
**Andrei Marinov:** framework.  
**Filippo Tosetto:** She does that. It's a She's She's fighting. That's another story.  
**Andrei Marinov:** No.  
**Filippo Tosetto:** That's another story. Okay. But so what I understand is that Dimmitro, this is the third week. Third or fourth?  
**Andrei Marinov:** It is. Yes. Third. And he was out like 3 days, four days. He was  
**Filippo Tosetto:** Okay. Okay.  
**Andrei Marinov:** sick.  
**Filippo Tosetto:** Third week. Some code is being tested right now. It started to work on a meaningful feature. Okay. I was a bit more worried. No, I think it's it's it's  
**Andrei Marinov:** So far so good.  
**Filippo Tosetto:** good.  
**Andrei Marinov:** Just like these sort of things that I uh pointed out a couple of times and I'll keep looking at them. Uh see if anything else like that pops up and whether it's something that consistently happens or if he's just new new to the cold base and still getting orientated sort of thing.  
   
 

### 00:12:09

   
**Filippo Tosetto:** This is good for me. Okay. Nice. Um, tomorrow devs will come um I'm expecting this app in a couple of I say three weeks to start to ramp up the the the delivery speed. Obviously um for some reason the company  
**Andrei Marinov:** No.  
**Filippo Tosetto:** is betting a lot on this app mainly because competitors are making a lot of money. So, we're just waiting to be able to deploy deploy enough marketing money in this app once it's in a good state pretty much.  
**Andrei Marinov:** Go.  
**Filippo Tosetto:** But I think it's it's going to be okay. Cool. Uh, anything else regarding AI design on your side?  
**Andrei Marinov:** Um, no.  
**Filippo Tosetto:** Okay. Uh, quick word on what happened on Friday. Well, you were aware that CClum would have been gone. Um,  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** the only person that stayed from Cloum is the QA because we think he's a very very good DQA and what we're trying to do is to hire him through another way. U but this is just to keep you informed of the movements.  
   
 

### 00:13:27

   
**Filippo Tosetto:** There was a moment of panic on Friday when they told him he would have been gone as well and we don't want that. We want him to work with us because he's a really good guy. So that that that's been solved. Nice. Good. Uh let's talk about IMOD and in general about RO shifting and everything else. Uh sometimes this week you will receive an invitation from um don't know who's going to send this to you but it's basically about explaining the transition that we are going to plan to do towards a more AIcentric uh approach.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** They will give you the full picture. I'm not going to give you the full picture now because they're going to be better. But the idea here is to get uh developer advisors to be using AI to code features.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** Um yeah that's the the the role shifting that I'm talking about here which means that we are planning to possibly remove externals if we see that this is working and through the AI uh tools you will be able to develop all the features without the need of anyone external.  
   
 

### 00:15:05

   
**Filippo Tosetto:** Is this going to work? We hope so. We run some uh some tests and it seems to be okay. Is this yet well defined? Not. We will be working to define all of this. I'm not going to explain all the phases of this plan, all the ins and outs. I want you to discover this uh through the presentation that they're going to give us. Um but there is something that we can start to do on our  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** side and your side as well. Uh and this is part of a bigger plan that I have in had uh which is um today we have IMOD and screen mirroring. You know this and they share a big part of their core which is the connectivity part. Imote is change channel on a TV. Screen mirror is I send stuff from my phone to the TV. They both need to connect to uh a TV. So last week I explained that I wanted to somehow build a library so that it can be shared between the two.  
   
 

### 00:16:24

   
**Filippo Tosetto:** Um and I want um Sergei to build it. Do you see it? How do you see this? First of  
**Andrei Marinov:** I think we thought that that's the way to go to share more code between the apps because they do  
**Filippo Tosetto:** all,  
**Andrei Marinov:** uh just uh I don't know how that will fit within the row shifting as well as someone else building it.  
**Filippo Tosetto:** let's play a game then. What would you do?  
**Andrei Marinov:** Uh probably  
**Filippo Tosetto:** I give you I give you a constraint. I give you a constraint. You need to use cursor.  
**Andrei Marinov:** yeah okay I'll  
**Filippo Tosetto:** There is no way around it.  
**Andrei Marinov:** probably start with uh using cursor to implement that library for both apps uh get what's similar what's not similar uh whether it's feasible at all I don't know for example what screenary does at the moment supposedly does the same thing is the same library but maybe they do it they already have separate needs that uh maybe can be met by one library. So first validate that and then from then on start to design and implement that library that's feasible to to work for both apps so that it can uh supersede it in both apps but I  
   
 

### 00:17:59

   
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** I don't see how like one person would be writing the app the the library and then in the other app will like doing things but maybe wait for that library or that's  
**Filippo Tosetto:** Okay,  
**Andrei Marinov:** going  
**Filippo Tosetto:** you can do this. We can do this. Do you want to be the one building the library? And we get um siri to fix bugs in the app  
**Andrei Marinov:** okay.  
**Filippo Tosetto:** because screaming it's a it's full of bugs.  
**Andrei Marinov:** It's okay.  
**Filippo Tosetto:** Uh and uh so on one end we have Artm that keeps moving forward with the little that we have to do in IMO. On the other end we have um Siri you know starting to look into the app  
**Andrei Marinov:** Actually,  
**Filippo Tosetto:** itself and fixing any problems and you do the library.  
**Andrei Marinov:** the big concern there is the hardware because I think that circuit does have a lot of hardware and I don't have anything. So,  
**Filippo Tosetto:** Um, this is something I need to clarify with to see if we can send you anything of any order at the moment.  
   
 

### 00:19:19

   
**Filippo Tosetto:** But, uh, meanwhile, can we use the externals for that?  
**Andrei Marinov:** We can yeah but it will be a slow sort of process because you develop something and you can't test it out. You ship it to someone and they have to it doesn't work and they  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** say yeah it doesn't work in this place and they get back get it back to you. So I guess in that sense it does make cursor hey to uh to start off on  
**Filippo Tosetto:** Um, why don't  
**Andrei Marinov:** that.  
**Filippo Tosetto:** I still would like you to to be involved in this and hardware is a minor problem for me and something I will iron out very soon like tomorrow I will have an Sir,  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** do you have a list of devices in your head?  
**Andrei Marinov:** No, I'll have to look it  
**Filippo Tosetto:** Okay. Okay.  
**Andrei Marinov:** up.  
**Filippo Tosetto:** Um, yeah, let's start to look into the that direction. But Andre, if you want to build this, if you feel okay to build this, I can't wait for you to start.  
   
 

### 00:20:42

   
**Filippo Tosetto:** any other problem that we have today,  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** let's solve it. I would like you to very much start with this because uh if you can create this library uh or at least start to define it meanwhile while we are on the hardware issue you know define the interface find doing this kind of things for me that will be very very beneficial and is proving that we are moving forward towards this plan of uh AI adoption. So please if you can start define it and by next week have at least I mean amazing will be if you already started to write the code itself but if you at least have you know a repository with an interface  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** something and coming up with with you know kickstarting this project that would be absolutely great for me.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** What is your  
**Andrei Marinov:** I don't know how much that will take and how much time I'll have  
**Filippo Tosetto:** workload?  
**Andrei Marinov:** for it, but I imagine the next couple of weeks are going to be busier than usual with all of the on boarding for the new people answering questions, uh, showing them things, that sort of thing.  
   
 

### 00:22:09

   
**Andrei Marinov:** Uh, so yeah, that's something else to consider.  
**Filippo Tosetto:** Uh okay, I would like to find the time for you to do this. So we have on boardings starting tomorrow for three for three developers. Um okay, you need to do the usual PR work that you're doing. uh automated. That's what I'm trying to do.  
**Andrei Marinov:** you know.  
**Filippo Tosetto:** And then um you know the usual ceremonies which I'm assuming they're taking a lot of time.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Okay. What do you think based on your priorities and your time mainly? What do you think you can deliver by the end of the week in terms of this library?  
**Andrei Marinov:** uh I guess the the plan for it whether it how much first start off with looking into what's been implemented in screening and uh see where in my that uh intersects and how feasible it is and then what we can do uh to support different TVs with it because uh sort of a general high level plan I imagine.  
**Filippo Tosetto:** Sounds good.  
   
 

### 00:23:50

   
**Filippo Tosetto:** Which meanwhile will give me the time to sort out the hardware issue and and so once you have a high level plan I sort out the hardware issue all the on boardings will be done pretty much from next week you can kickstart the whole process. If if it can be done obviously. Nice. I like it. I really much like this. Um good. Why do you think sorry roll back the plan is also for you in the future to start to work on the apps themselves. What do you think is better for you to build this library instead of working on the apps?  
**Andrei Marinov:** uh that that's like discovering and connecting to TVs. That's the meat of the app. Uh that's what mostly it does. So working on the app itself. Uh that's more well like migrating to liquid glass that sort of thing currently. So I can do that as well. But I feel like it would be more beneficial to start  
**Filippo Tosetto:** Yes.  
   
 

### 00:25:23

   
**Filippo Tosetto:** No, no,  
**Andrei Marinov:** there.  
**Filippo Tosetto:** I agree. I was just curious to to hear your reasoning. Um, yeah, I agree with you. Okay, nice. Um, anything else on your side?  
**Andrei Marinov:** Uh no, nothing comes  
**Filippo Tosetto:** Let me check my my  
**Andrei Marinov:** up.  
**Filippo Tosetto:** notes. Okay. Okay. Okay. Okay. It's weird that we already covered everything.  
**Andrei Marinov:** We cut an hour.  
**Filippo Tosetto:** By the way, I brought your questions to uh Sergio. Where is it?  
**Andrei Marinov:** Which ones?  
**Filippo Tosetto:** Uh the questions regarding AI and he he gave me some interesting answers regarding it.  
**Andrei Marinov:** Okay. From your cursor constraints,  
**Filippo Tosetto:** Uh no,  
**Andrei Marinov:** I don't think that they were very  
**Filippo Tosetto:** there is no no it's it doesn't agree with you in a few points  
**Andrei Marinov:** beneficial.  
**Filippo Tosetto:** but I I let you ask the questions when this presentation is going to happen because uh not because it's it's good for me that it's not  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** about convincing you.  
   
 

### 00:27:08

   
**Filippo Tosetto:** is about you understanding the reasoning behind this. And the the long story short here is yeah maybe you are right but what we are trying to do here is to build all the skills and rules and those can be moved to a new tool tomorrow if that's the case and your concern about tokens it's not a concern trust me use them use there. Uh there is a big concern in the company because people are not  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** using enough tokens to use them.  
**Andrei Marinov:** Okay then.  
**Filippo Tosetto:** All right. Uh okay, Andre, I think there's nothing else on my site. Uh unless you have anything you want to share.  
**Andrei Marinov:** Oh, no. Nothing comes the  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** way.  
**Filippo Tosetto:** Um there is some movement on the product side of things. I already mentioned something to you the other day.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Um I don't know how is the mood in the in the meetings in the in the team itself if something is in the air. No. Okay.  
   
 

### 00:28:30

   
**Andrei Marinov:** No.  
**Filippo Tosetto:** Okay. Let's see. There is um this is going to happen most likely throughout this week.  
**Andrei Marinov:** Are  
**Filippo Tosetto:** and from next week you're going to have a new PO and if he's the PO they are talking about is  
**Andrei Marinov:** you  
**Filippo Tosetto:** is working with me already and I think he's a nice guy and um there is also a plan to bring IMO Android to uh growth merge the teams because it's pointless to keep two separated someone is even  
**Andrei Marinov:** No  
**Filippo Tosetto:** mentioning the fact that probably adding screen mirroring as well it's a good idea I don't know regarding this because they are two different apps.  
**Andrei Marinov:** heat.  
**Filippo Tosetto:** Um you are not the developer advisor for screaming and I need to think about this because strategically it may make sense but for now I want to keep the scope as defined as it is today. So I don't want to uh give you more stuff to do. Let's see it. Let's see how it's going to move forward.  
**Andrei Marinov:** Yeah, okay.  
   
 

### Transcription ended after 00:30:01

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*
```

