Mar 30, 2026

## Vlad / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Hello. Hello. Hello. Can you hear  
**Vladyslav Krut:** Yes, one sec. Yes,  
**Filippo Tosetto:** me?  
**Vladyslav Krut:** I clicked on Figma link just before we started talking and it froze.  
**Filippo Tosetto:** Hi. How are you doing?  
**Vladyslav Krut:** Uh, all good. All good. Thanks.  
**Filippo Tosetto:** Yeah, it's good. It's good. It's sunny here.  
**Vladyslav Krut:** You  
**Filippo Tosetto:** Spring is is uh is arrived. So it's everything is is much better when there is sun around. But that's my perception of things. I know there are a lot of people that are more interested in rain, but not me in rain and gray  
**Vladyslav Krut:** in what? Sorry. Oh.  
**Filippo Tosetto:** skies.  
**Vladyslav Krut:** Oh, hell no.  
**Filippo Tosetto:** Nice.  
**Vladyslav Krut:** move to Spain to to to live with Greece or something like  
**Filippo Tosetto:** Fair point.  
**Vladyslav Krut:** this.  
**Filippo Tosetto:** Fair point. So Vlad, how was your last week?  
**Vladyslav Krut:** Uh it was uh okay kind of expectedly confusing and slightly overwhelming.  
   
 

### 00:02:10

   
**Vladyslav Krut:** I now start admitting let's say a lot of aspects that I'm supposed to be taking care of and I'm even a little bit struggling with multitasking now because like you know this moment when you're like okay I finally got time I got to do nice things that I was wanting to do and then you have a meeting and now it turns out that I need to set up arcana for example for face AI for proper um dot environment files management because what we have now is not sustainable in any means like we we commit production keys. So like okay that's another thing in my to-do list.  
**Filippo Tosetto:** We can talk about that in a  
**Vladyslav Krut:** Yeah, I wanted to ask it.  
**Filippo Tosetto:** second.  
**Vladyslav Krut:** I like five minutes before this call, I added it to our notes uh doc so that not only I am aware of the question but you also have it somewhere documented. Yeah, we should talk about this one. Then I spent I don't remember what half of the day Thursday or Friday trying to set  
   
 

### 00:03:12

   
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** up periphery tool that's supposed to help me to clean up that code which didn't went well from the very beginning but then I managed to make it work for some reason. It seems like it was either pre-installed uh old version on my MacBook so like it existed the tool was available but it was consistently reporting no code whatsoever and like that's not true and I was debugging  
**Filippo Tosetto:** Okay. Okay.  
**Vladyslav Krut:** like what is this why it's happening apparently there were some kind of obscure dependencies that I was lacking but it was not reporting me it was failing silently and reporting zero exit code so I had to debug that And I made it work. And then I got a script, nice everything. I got a file of all the code. I tried to, you know, split the work to make AI do this for me because am I going to do this manually? I mean, no, of course not. Uh,  
**Filippo Tosetto:** No.  
**Vladyslav Krut:** but then I figured out that periphery is probably smart to identify the chains of the dead code, you know.  
   
 

### 00:04:22

   
**Filippo Tosetto:** Is it  
**Vladyslav Krut:** So there is a f file that's used only in a specific function only when specific parameter is passed and some so on and so forth. So this whole chain should be cut out as unused which is cool  
**Filippo Tosetto:** Is it working like that by the  
**Vladyslav Krut:** but then yes it's really smart in identifying  
**Filippo Tosetto:** way?  
**Vladyslav Krut:** that code but then AI is not smart enough to cut in the dead code  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** in that way. It's like okay I got to rework the algorithm because you know just splitting into bunches of like 10 or 20 unused pieces. No doesn't work because there's insane amount of dependencies and then tries to build and then it complete mess. So yeah this part I will completely redo. I didn't make any progress here other than making a periphery work at all which is yeah okay good thing next time I will not have to spend time on this and like stuff like that and then a few times like code magic thing okay let's see why uh symbol debug symbols are not working well I see why let's remove the job because we have a shared one oh no never mind it doesn't And then I was I had to intentionally catch myself uh like to lower my quality standards because like we are in a startup.  
   
 

### 00:05:49

   
**Vladyslav Krut:** We just need it to work. We don't need the setup to be perfectly. I don't have to debug why it's not working the way it intended and is there a problem in our shared lane. No, I don't need. So I was trying to figure out and test and had debug lay that I could run locally without pushing to CI because there's a Q and CI as well and I was like what stop just revert the commit it's okay we have like 10 more lines in our code magic file that's it I gota get used to this yeah like we don't need it to be perfect we just need to get the job done so yeah this  
**Filippo Tosetto:** Yep. Yep.  
**Vladyslav Krut:** is new for  
**Filippo Tosetto:** Yeah. You're getting used to it.  
**Vladyslav Krut:** Yeah, I think so.  
**Filippo Tosetto:** Cool.  
**Vladyslav Krut:** Some that I think I had something  
**Filippo Tosetto:** Anything else?  
**Vladyslav Krut:** else. I don't really remember. Maybe I have something in my notes from last week. Give me one sec.  
   
 

### 00:06:55

   
**Filippo Tosetto:** No, it's fine.  
**Vladyslav Krut:** Oh, also they were really really really like I loved the talk that Serio gave on Friday.  
**Filippo Tosetto:** Agree.  
**Vladyslav Krut:** I was like wow again like I feel like you know like your brain is expanding like obtaining a  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** superpower with information how the long conversation works and reminder that it's it's stateless. It's just a transformer.  
**Filippo Tosetto:** It for me it unlocked a lot that conversation to understand that small detail about context window. It unlocked a lot and they start to understand the bigger plan behind all of this and the fact that models are just substitutable one from the other as long as the infrastructure that we build is going to be solid. So the guard race that we build are going to be solid.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** Is it going to be clothed oppus or or codeex or any Chinese model? I don't care. It's working if you know what you're  
**Vladyslav Krut:** Yes. Yes.  
**Filippo Tosetto:** doing.  
**Vladyslav Krut:** Like this is the idea that if your infrastructure or workflow works only with opus then you have a problem like yeah that makes sense.  
   
 

### 00:08:13

   
**Filippo Tosetto:** Yeah. Yeah. But it is right that what if  
**Vladyslav Krut:** Sure.  
**Filippo Tosetto:** tomorrow um oppus is going to cost $50 per co? Can we build our business on that? Definitely not.  
**Vladyslav Krut:** True, true.  
**Filippo Tosetto:** Anyway,  
**Vladyslav Krut:** Well,  
**Filippo Tosetto:** this is bigger  
**Vladyslav Krut:** I I think that rather other models become smarter and cheaper because of  
**Filippo Tosetto:** discussion.  
**Vladyslav Krut:** what's happening in the world like hardware is getting stronger, faster, bigger, better. So, I kind of expect the quality to increase and the cost maybe to drop. But still, why would we use more resources if we can save here? And it also allow us to like uh prove future proof our solutions, design them better. Let's do this. Not that  
**Filippo Tosetto:** So that's a thing that keep insisting on which  
**Vladyslav Krut:** difficult.  
**Filippo Tosetto:** is if a commercial a famous commercial model cost me $10 per you know feature build let's say And on the other hand, you have a Chinese model which co give you 95% of the result but instead of $10 cost you 10 cents to do exactly the same work.  
   
 

### 00:09:42

   
**Vladyslav Krut:** Why  
**Filippo Tosetto:** We we need to think you know we need to think like a business. And there is also another thing that I really appreciate which is yeah  
**Vladyslav Krut:** space?  
**Filippo Tosetto:** oppus is easy because you use oppus you just say do this for me and you figure out what to do but what are you learning about the infrastructure behind it in the in this case probably very  
**Vladyslav Krut:** Yeah. I don't think so. But there there is a cool  
**Filippo Tosetto:** People  
**Vladyslav Krut:** thing. But I also feel like Opus can sometimes teach you things that you don't know how to do yet. While if you go for Kim or composer like just don't even attempt  
**Filippo Tosetto:** y  
**Vladyslav Krut:** go and learn it yourself first and then you can create an AI.  
**Filippo Tosetto:** I think that at the end of the experiment the idea is for each one of us to have a an understanding of the pros and cons of each model and you know to change the color  
**Vladyslav Krut:** Of  
**Filippo Tosetto:** of a label I don't need to use opposing you know  
   
 

### 00:10:49

   
**Vladyslav Krut:** course.  
**Filippo Tosetto:** that is the mindset that we should start to use let's see let's see so uh Vlad um you have three questions I'm going to answer them before jumping on the other points Let's start with the easy one. Soul slab. Do we use it for what? Soul slab is a a tool that we use for QAS. What what does it do? It's you send them an IPA uh uh of the app and uh they deploy it in a factory of devices. So you have different versions of the operating system and different screen sizes. And this is just needed for um QAS to test that our app works on different kind of devices and usually it's the last step. I doubt the QA check so slab every day honestly but that is the reason for using it. So to avoid having to trigger manually a build for source slab, what we do is every build that goes through the pipeline goes also to source lab.  
**Vladyslav Krut:** Okay, I see.  
**Filippo Tosetto:** Does it answer your  
   
 

### 00:12:08

   
**Vladyslav Krut:** Uh, does it deploy uh our IPA to all like to physical devices or  
**Filippo Tosetto:** question?  
**Vladyslav Krut:** to simulators? Like how QA interact with this one?  
**Filippo Tosetto:** Uh  
**Vladyslav Krut:** Like do they test manually click it manually or what happens after the successful deployment like how the the interface looks?  
**Filippo Tosetto:** I have no idea.  
**Vladyslav Krut:** Okay, maybe we'll ask Maria.  
**Filippo Tosetto:** Yeah. Yeah. Ask Maria. Um good. Parapet. Parapet. It's very important what it is, what what is it and um and the way forward. So parapet is just a code name for uh what we call quota system. So today pretty much half of our apps works work with quota and credits meaning that you as a as a user you subscribe to the application and you get to talking for image generation uh I don't know 10 uh free image generations per day. Um,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** and then you can also purchase uh tokens or credits to perform other actions within the app.  
   
 

### 00:13:22

   
**Filippo Tosetto:** Let's say that the standard image generation cost you kas and you have 10 20 per day if you're a subscriber. But then if you want to use some more pro features, you need to spend more credits or tokens and you can buy them through in a purchase. This is the concept behind the quota system.  
**Vladyslav Krut:** Makes sense.  
**Filippo Tosetto:** Um what is this parapet is the full infrastructure that can be deployed in every single app to do this business logic that just explained. So until two months ago every single app was reproducing this logic by themselves. So zero reusability with all the problems related to this.  
**Vladyslav Krut:** I  
**Filippo Tosetto:** And there are a few problems that are very interesting to solve.  
**Vladyslav Krut:** see.  
**Filippo Tosetto:** As you have seen, none of our apps have a login system, an authentication system.  
**Vladyslav Krut:** Oh yeah,  
**Filippo Tosetto:** How do you authenticate the user or how do you make secure API  
**Vladyslav Krut:** true.  
**Filippo Tosetto:** calls? So what we do is we use we built this system that uses revenue cat and the revenue cat ID uh that is assigned automatically to your device to authenticate a user and to perform any quota related work.  
   
 

### 00:14:53

   
**Filippo Tosetto:** Um I'm going to share my screen with you so you so at  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** least we have something tangible uh to look at. Uh let me find it. Okay, probably this is better. You can see my screen.  
**Vladyslav Krut:** Second.  
**Filippo Tosetto:** So here we have different applications you should have access to all of them and let's take face AI and then you have basic configuration of face AI the Apple team and then you have revenue cut stuff and then you have  
**Vladyslav Krut:** Hey.  
**Filippo Tosetto:** JWT which is used for talking to the back end because every app that uses a CO system need to have a back end which is a sort of middleware. I'll explain a second and then you have the Firebase configuration. Why do we need this app check the security part?  
**Vladyslav Krut:** Yeah, that was  
**Filippo Tosetto:** Yeah, the security part.  
**Vladyslav Krut:** Mhm.  
**Filippo Tosetto:** Uh and then once every application is configured you have two ways of using it. the quota limits. So the subscription and you can add different quotas per app and they say that a free user has 10 quota to use and the premium users has 20 and they reset daily or you can say weekly, monthly or a billing cycle.  
   
 

### 00:16:32

   
**Filippo Tosetto:** And these are just example here but you can say that you have different types. At the moment we have zero cases with different types. So let's leave it like this. So what's happening that the system recognize if a user makes a purchase to in the app because revenue cat has a a web hook system that sends a notification to parapet our back end and so it sees if a user and I'm going here to custom quote I just picked a random user if a user is consuming the quota usage limits. So as you can see this is revenue cat user ID when it was subscribed the app from which you will subscribe.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** Uh maybe let's try to pick a user that I need some user that has done some actions. Maybe I can pick from PCI. Okay. Anyway, this user just has quota and credits. Um the credits are the second interesting part which are configured based on inapp purchase. So what you see here is the inapp purchase ID that we have configured in the app store.  
   
 

### 00:18:23

   
**Filippo Tosetto:** So there is a onetoone relationship between this product here,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** this product here, this one and what we have in the app store.  
**Vladyslav Krut:** And I assume revenue cat is also has one one the  
**Filippo Tosetto:** Correct?  
**Vladyslav Krut:** same.  
**Filippo Tosetto:** So whenever a user purchase some tokens, Revenue Cat say okay user you can purchase this token and revenue through a web hook talk to our back end and gives in this specific case 50 tokens to our user. So these are the configuration parts.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** You have quotas that are renewable. They are renewable while tokens are consumable and they are configured. The quotas are handled through subscriptions because they are renewable  
**Vladyslav Krut:** Sure.  
**Filippo Tosetto:** and the tokens are handled through inner purchase because they they are consumables.  
**Vladyslav Krut:** So user can get more if they want than they have daily even on premium  
**Filippo Tosetto:** Correct. Correct.  
**Vladyslav Krut:** usage.  
**Filippo Tosetto:** And then so this is what's happening between our app the app store revenue cat and this back end.  
   
 

### 00:19:44

   
**Filippo Tosetto:** Imagine it as a back end as a service a normal service.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** But then we need a third uh entity in this which is the back end of the application where we assign a cost per function. Give you a very simple example. Face AI has different filters and we can decide that you know we have a a set of premium filters with level one. they all cost one credit, but then you can have some super premium filters that cost five credits. So what's happening is is that the applications the application  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** send to our back end a request to perform an action which is no no that is  
**Vladyslav Krut:** With the price of that amount of tokens. No,  
**Filippo Tosetto:** handled by the back end. So the apps say the user say okay I want a feel a beard on  
**Vladyslav Krut:** make sense. Yeah.  
**Filippo Tosetto:** this picture. the app send a request saying hey uh back end I'm user XY Z from revenue cut can I do this action the back end calls parapet and say hey tell me how many credits are left for this user okay how many credits do we have left uh I you have five credits left okay I need to perform a beard operation which cost one.  
   
 

### 00:21:24

   
**Filippo Tosetto:** So okay, I'm going to perform the whole thing. I tell the app, okay, you can have this picture with a filter and the back end tell parapet hey parapet user XY Z used one credit  
**Vladyslav Krut:** Makes sense. Okay.  
**Filippo Tosetto:** and obviously you have the cases where the user complete doesn't have any more credits and so Paraveet doesn't even perform the action because it said hey user you don't have credits I'm not going to perform this action for And so what happened in the app is that we display a pay wall saying you hey  
**Vladyslav Krut:** Sure.  
**Filippo Tosetto:** you've completed you used all your credits buy more. By the way, you find all the information here how the quota system works and in here you have the integration guide for back end for iOS, Android, flatter and API references.  
**Vladyslav Krut:** Awesome.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** I  
**Filippo Tosetto:** Um,  
**Vladyslav Krut:** see.  
**Filippo Tosetto:** do you need to do anything today? Probably not.  
**Vladyslav Krut:** Probably not. The primarily reason I understood that I need access understanding of how it works is because on that day when you were off the only day uh QA engineers had a lot of troubles figuring out on where is the problem, what is the user, what is the identifier, how many credits, how do we test like nobody knows anything and I felt like it probably going to be my responsibility to you know guide them and to help them identify the problem  
   
 

### 00:23:13

   
**Vladyslav Krut:** but I had no idea how to I at that point I didn't even have access to parapet and also what like the the the thing that worried me let's say that Maria told that she asked amongst other QA engineers about their experience maybe some of them have experienced problems or solutions and can help because according to you. A lot of other apps are using paret already.  
**Filippo Tosetto:** Just  
**Vladyslav Krut:** Yeah. Well,  
**Filippo Tosetto:** one.  
**Vladyslav Krut:** um Maria also told something like that that nobody knows and nobody can help. So I also didn't know literally anything. So I felt like I should get used to to this tool. Probably it will be needed. At least the understanding is something that I need.  
**Filippo Tosetto:** Um,  
**Vladyslav Krut:** So al also one of the things like you told a few times I believe on our group calls  
**Filippo Tosetto:** okay.  
**Vladyslav Krut:** that parapet is definitely correct. So what do we see in the app? So there could not be an issue with parapet. So I was like is it true?  
   
 

### 00:24:30

   
**Vladyslav Krut:** Is it not confirmed to be true?  
**Filippo Tosetto:** So,  
**Vladyslav Krut:** How how do we about the rel tool?  
**Filippo Tosetto:** so do you have experience with revenue cat?  
**Vladyslav Krut:** just a little like six years ago I was integrating a VPN client.  
**Filippo Tosetto:** Okay. Okay.  
**Vladyslav Krut:** So probably not  
**Filippo Tosetto:** No problem. That's not a problem. Um I think not today um because I really need to leave  
**Vladyslav Krut:** enough.  
**Filippo Tosetto:** at in time because I have another meeting. But probably tomorrow or the day after or sometime this week, I want to talk to you about Revenue Cat, how it works, how it interfaces with the app store and what kind of information parapet receives from revenue and why I say always that parapet is right because parapet is just receiving and displaying information from Revenue Cat. And Revenue Cat just receives and displays information from the app store and the app  
**Vladyslav Krut:** And I used to think revenue as being source of truth.  
**Filippo Tosetto:** store you  
**Vladyslav Krut:** I didn't have problems with it back  
   
 

### 00:25:42

   
**Filippo Tosetto:** know.  
**Vladyslav Krut:** then.  
**Filippo Tosetto:** So if there is something broken in parapet that means two things or the app is broken or the app store is broken. And there's nothing. If it's the the app store, the QA can't do any we can't do anything. If it's the app, which 99% of the case it's the app, it's something that we need to fix ourselves. And I can tell you that all this back and forward with QA regarding this topic is mainly due to the fact that sandbox users has a have a very short uh lifespan and after five minutes they expire. So QA cannot do a proper 360 test but blood and this is where you  
**Vladyslav Krut:** Makes sense. That makes sense.  
**Filippo Tosetto:** start to understand a bit more the dynamics as well of the team. I cannot solve all the problems and you should not solve all the problems. There are problems that needs to be solved by product people and after  
**Vladyslav Krut:** Okay, I hear you.  
**Filippo Tosetto:** I repeat two three times to a product person I'm not pointing fingers to a product person that hey you need to fix this on your end because otherwise we won't be able to release an app.  
   
 

### 00:27:06

   
**Filippo Tosetto:** I'm just I cannot solve this problem.  
**Vladyslav Krut:** U can you give me a hand on understanding what parts of the task  
**Filippo Tosetto:** Sure.  
**Vladyslav Krut:** are supposed to be solved by products and not by  
**Filippo Tosetto:** Um, very simple use story. If the user story doesn't contain enough information for a developer to develop a feature,  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** it needs to go back to product owners explaining, hey, I'm missing this case. Hey, what's happen when the user press this button? Hi, what happens if there is no user connection? Or hey, you're talking about redesigning the main screen. Where's the design? I'm uh talking from experience here,  
**Vladyslav Krut:** Yeah. Yeah.  
**Filippo Tosetto:** even the last  
**Vladyslav Krut:** Yeah. I recognize some of these conversations.  
**Filippo Tosetto:** case.  
**Vladyslav Krut:** I think  
**Filippo Tosetto:** So why am I keep bouncing and talking and talking say guys are we ready for releasing? Are we ready for releasing? Are we ready for releasing? Because this part is not up to the side.  
   
 

### 00:28:18

   
**Vladyslav Krut:** it's  
**Filippo Tosetto:** We engineering provide the working product and they decide when and what to release.  
**Vladyslav Krut:** okay. That part was not clear though. Okay.  
**Filippo Tosetto:** Yes, there is another important point which is QA is QA and they want everything 300% correct but in I need that people work that works with me use their brain. So I am aware that if you take your app and try to buy something but meanwhile the old internet of the world goes down and you put your telephone inside the microwave for some reason the user will not be able to complete the purchase. I'm aware that that is an edge case, but are we waiting? Are we trying to fix this edge case to release an app in the store, the version one of the app in the store with zero users today and probably five users after it's been released just to fix this use case. So I need people to think, you know,  
**Vladyslav Krut:** Makes sense.  
**Filippo Tosetto:** because I'm facing these kind of problems. It's like guys, let's try to be a bit more pragmatic here.  
   
 

### 00:29:46

   
**Filippo Tosetto:** Let's consider the amount of user that we have today and do we really need to fix a bug that is affecting no one or probably one person? You know, if this app was making five millions a month, well, in that case, maybe we can spend a bit more time in fixing all the small little details here and there. But  
**Vladyslav Krut:** I see primarily from QA I hear problem that they don't know how  
**Filippo Tosetto:** sorry,  
**Vladyslav Krut:** to test which sounds kind of important at this point to be  
**Filippo Tosetto:** why it is very important,  
**Vladyslav Krut:** honest  
**Filippo Tosetto:** but who where does the QA find information?  
**Vladyslav Krut:** from product of course.  
**Filippo Tosetto:** And I told several times, guys, I personally do not have the time to write the documentation for QA. You need to write it because if QA doesn't know how to test, that also means that developer doesn't know how to develop  
**Vladyslav Krut:** Okay. Then I have related question. How do you let's say uh make product team listen or do  
**Filippo Tosetto:** It's easy.  
   
 

### 00:31:08

   
**Vladyslav Krut:** better  
**Filippo Tosetto:** So I've just seen that uh Herardo shared list of stories.  
**Vladyslav Krut:** a list of stories and I feel like personal  
**Filippo Tosetto:** So that's it  
**Vladyslav Krut:** responsibility now to go and review them.  
**Filippo Tosetto:** is part of your job. Yes. to go and and review them because today we have Anton in a month's time we won't have Anon so you will be responsible for developing them open a user story and start to read it does it make sense for me it's already too small unless it's changing a single label I I don't have much information as I us to filter categories I want the multi selection tool icon to be updated to the last design specification. Okay,  
**Vladyslav Krut:** Well, if this is about  
**Filippo Tosetto:** so that the interface Okay,  
**Vladyslav Krut:** right  
**Filippo Tosetto:** we have the scenario here and then we have the design. We check the design and see if the design contain that  
**Vladyslav Krut:** now the brow  
**Filippo Tosetto:** information. Yeah. Uh don't want dev access.  
   
 

### 00:32:24

   
**Filippo Tosetto:** Uh sorry just stop sharing instead I wanted to share that uh  
**Vladyslav Krut:** Oh, good.  
**Filippo Tosetto:** I think that the mod select is this icon.  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** So we just need to add this icon. So yeah, that user story probably contains all the information.  
**Vladyslav Krut:** Personally,  
**Filippo Tosetto:** Uh, let's go  
**Vladyslav Krut:** I don't really know if this feature like multi select is exists now.  
**Filippo Tosetto:** to  
**Vladyslav Krut:** So, is it about the icon or is it about the logic to add multiple filters? Well, Anton probably knows because he developed this app.  
**Filippo Tosetto:** But this is very important to understand because what I read here, I want the multi selection tool icon to be updated to the list of designs. As a developer, this is the important part for me. For me, it's just about change the icon. Sounds good. Going to do that. And the QA will do the same because here the only information that we have is that one.  
**Vladyslav Krut:** given a category that supports multi selection. So I I assume that's only about icon.  
   
 

### 00:33:41

   
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** I assume there are tools that support multis section.  
**Filippo Tosetto:** filter cataly as a reason I want filter and reflect updated design again another design update and here's the specification hover or I like guys we are developing apps how do you define a hover state.  
**Vladyslav Krut:** Uh,  
**Filippo Tosetto:** Come  
**Vladyslav Krut:** I think there may be something wrong here.  
**Filippo Tosetto:** Exactly my point. Exactly my point. Spend half an hour, one hour, go through the user stories and simply ask questions to Herardo and say, "Hey, Rardo, uh, what does it mean overstate here?" For instance, just maybe maybe it makes sense. I don't know. I didn't read properly the whole thing.  
**Vladyslav Krut:** Yeah. Yeah. You can I will open design and stuff like  
**Filippo Tosetto:** But my point here,  
**Vladyslav Krut:** that.  
**Filippo Tosetto:** do not assume that what comes in a user story is correct and the people that wrote this user story has the full understanding of what should be written there. A there's also another big point here.  
   
 

### 00:35:20

   
**Filippo Tosetto:** Herardo just arrived. There may be a reason that he doesn't know because he just arrived. So maybe he's just trying to find his way around things. So, let's try to to be honest here.  
**Vladyslav Krut:** I like this part of the like management and like communication is pretty clear for me. I meant uh when I was asking the question I meant what happens if there is no  
**Filippo Tosetto:** Oh,  
**Vladyslav Krut:** improvement. So if we you know like stepping onto the same rake pretty  
**Filippo Tosetto:** sure. That's that's and that's where I  
**Vladyslav Krut:** much  
**Filippo Tosetto:** let's look one month in advance. Okay. You know the product, you start to develop features, you are updating Jira, you're doing your job as a software engineer and you have one big problem is that it's been a month that you keep going back to uh but things are not improving. Okay. And the easy thing to do is just to come to me just say, "Hey, Philippo, I've been talking to Erdardo, but it seems that user stories are not really updated.  
   
 

### 00:36:27

   
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** Seems that you don't need to do anything else. It's not about you going to escalate to Arardo to do these kind of things. It's like you're doing your job as software engineer. You talk to first of all, you need to talk to Ardo, say, "Hey, I'm missing this information." But if it doesn't come back with the information that you need after several times, you can come to me and I'll solve the  
**Vladyslav Krut:** Okay, makes sense.  
**Filippo Tosetto:** problem.  
**Vladyslav Krut:** Primarily asking because you told me on Friday I believe that you or or Thursday that you used a whip. So it's supposed to be better now. So I was not sure whether it's going to be in the months of time my responsibility to use a we or this is  
**Filippo Tosetto:** No,  
**Vladyslav Krut:** still your part of responsibilities and I just raise if I  
**Filippo Tosetto:** no, no, no, no. Do not worry. I will never ask you to do so.  
**Vladyslav Krut:** see  
**Filippo Tosetto:** Um, it's something that I can do.  
   
 

### 00:37:21

   
**Filippo Tosetto:** Also, my position allow me to do it. And I use strong words, but please come on. You can achieve the same results without being aggressive.  
**Vladyslav Krut:** I just checking I also don't really know what did you mean by saying a you know I I  
**Filippo Tosetto:** this  
**Vladyslav Krut:** never asked you never told me so just learning all good I'm not assuming that's why I'm  
**Filippo Tosetto:** the in my career I learned that  
**Vladyslav Krut:** asking  
**Filippo Tosetto:** simple communication solves 99% of the problems. There is 1% of the problems where you need to escalate but most of the time it's just hey I'm missing this information or hey I'm what does it mean this sentence and they will update it works like that usually blood uh we have very little time  
**Vladyslav Krut:** Okay, sounds good.  
**Filippo Tosetto:** I want to spend two minutes on arcana uh yeah great beautiful I need you to start to produce features. Arcana can come later.  
**Vladyslav Krut:** Okay, just like that. Postponing this part.  
**Filippo Tosetto:** Um maybe I'm going to ask you to work on it in two three weeks time, but today I need you to start to produce meaningful results.  
   
 

### 00:38:40

   
**Filippo Tosetto:** Uh because the otherwise we will spend the rest of the month doing setups.  
**Vladyslav Krut:** Yeah. And I I kind of tired of this stuff. I want to do something  
**Filippo Tosetto:** Exactly. So that's exactly my points.  
**Vladyslav Krut:** useful.  
**Filippo Tosetto:** Arana, great. Yeah, sure. No problem. Later, please. Is the app working today? Are we perfect? Uh, that's that's my point on Arcana, which brings me to the last point that I wanted to talk to you about, which is do you have a plan for the next five weeks?  
**Vladyslav Krut:** Well, not detailed but I have as we discussed a set of tasks that needs to starting like as the first point absolutely is removing all the periphery findings all  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** the dead code to not confuse AI just makes sense and then switching to covering view models services repositories with unit tests and in parallel updating uh all the findings problems UI problems I primarily mean on the affected screens like adding a dark team support for example fixing broken animations for all the for everything pretty much things like that step by step one by one probably one pull request at a time and  
   
 

### 00:40:02

   
**Filippo Tosetto:** Do you have a rough timeline for this?  
**Vladyslav Krut:** Uh so regarding uh periphery I want really to say that this like one or two days job but but there are a lot there are like 500 findings by periphery and as I said like my first attempt with CI didn't go well so I need to refine it so yeah maybe it's like two days I expect no like  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** maybe maybe the most complex complex cases I can just do manually and it will be faster than explaining how to do this for some of them like this.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** Uh then oh and then together with unit tests covering the features with uh user story plus girkin file to have it documented. Not sure how exactly the order will go because unit test not always correlate one to one with girken feature this part I will have to improvise I don't really have a defined plan on this part the timeline for covering all of them  
**Filippo Tosetto:** That's okay. It's okay.  
**Vladyslav Krut:** with tests I don't know yet what I can do if we would like to timelines is I can uh count let's say you know just a row number of view models and services pretty much entities that I would like to describe with unit tests and give a rough estimate based on the amount of files.  
   
 

### 00:41:34

   
**Vladyslav Krut:** That's it.  
**Filippo Tosetto:** Okay, let me reverse the question. Would you be able to start to take user stories, new user stories, sorry, and produce feature from the second week of April? Third week, sorry, third week of April. After the 10th All  
**Vladyslav Krut:** I I would say from the next Tuesday. So it's going to be probably first because why I want to completely remove the dead code and  
**Filippo Tosetto:** right.  
**Vladyslav Krut:** then I can parallel my work and spend let's say half of the day delivering new features and half of the day uh for unit tests refining girin plus stuff the the only thing that I want to put up front to solve first is a dead code because  
**Filippo Tosetto:** Genius. Perfect.  
**Vladyslav Krut:** it confuses a that's  
**Filippo Tosetto:** Yeah. Yeah. Makes sense. Sounds great to me. Um on parallel, I'm reworking that workflow uh for plans, specifications, implement etc. And I've refined it in a very good state now. So that the plan part is producing a markdown file with the plan itself.  
   
 

### 00:42:54

   
**Filippo Tosetto:** So and what it does is explain from a technical perspective.  
**Vladyslav Krut:** Nice.  
**Filippo Tosetto:** Oh, I need to create a new model file for this feature. I need to uh update this view model to do that.  
**Vladyslav Krut:** Give it like  
**Filippo Tosetto:** This it then is then the specs  
**Vladyslav Krut:** this.  
**Filippo Tosetto:** are created which are the Girkin file and those are more human readable and they are more about use cases and then these two files are fed to the implementation agent. top new context window and this guy doesn't need to do any code scan because he receives already what he needs to  
**Vladyslav Krut:** This is very  
**Filippo Tosetto:** do and then once it's completed this gets handed  
**Vladyslav Krut:** important.  
**Filippo Tosetto:** over to the test agent that does everything on the testing side I'm refining this I'm I'm okay with 80% of the cases but it's going  
**Vladyslav Krut:** Okay, I see. I'm at this point not sure how not how good is of an  
**Filippo Tosetto:** there.  
**Vladyslav Krut:** idea to make the first step think about coding. Not sure but let's see if it works great.  
   
 

### 00:44:12

   
**Vladyslav Krut:** If it doesn't uh we will discuss or you will refine or whatever or I will  
**Filippo Tosetto:** But I'm I'm working more from an higher level and more like abstract.  
**Vladyslav Krut:** refine.  
**Filippo Tosetto:** I need your eyes and ears and hands to say no this is total b\*\*\*\*\*\*\* this doesn't work we need to do something different and this is the new way to do things until you can start to develop feature we won't be able to have that knowledge that's why I'm like okay okay yeah uh arana later  
**Vladyslav Krut:** Okay. Yeah.  
**Filippo Tosetto:** that's  
**Vladyslav Krut:** It was wasn't clear from for me when Andre asked me to do this. So like, okay, we postpone it. Make it like it. Yeah. Okay. Makes sense. Arana postpone.  
**Filippo Tosetto:** Cool.  
**Vladyslav Krut:** Really nice. CI should now be working. Debug symbols handle reported that doesn't work again.  
**Filippo Tosetto:** Thank  
**Vladyslav Krut:** So yeah, I really hope get not later than the beginning of the next week to to  
**Filippo Tosetto:** you.  
   
 

### 00:45:18

   
**Filippo Tosetto:** Um, whatever you're doing,  
**Vladyslav Krut:** features.  
**Filippo Tosetto:** think about AI design where you need to redo pretty much the same things that you are redoing.  
**Vladyslav Krut:** Sorry, didn't get it.  
**Filippo Tosetto:** AI design is the next topic that you're going to start to work on in May.  
**Vladyslav Krut:** Oh, okay. Okay.  
**Filippo Tosetto:** And and so whatever you're doing today,  
**Vladyslav Krut:** Now,  
**Filippo Tosetto:** you will need to reproduce the same approach later on. So try to think in a reproducible  
**Vladyslav Krut:** makes sense.  
**Filippo Tosetto:** way.  
**Vladyslav Krut:** I I forgot the name of the app, so I was like thinking about more like Figma design. Okay, makes sense.  
**Filippo Tosetto:** Um if you think that No, no. Do do the thing. Do do your things. Um, good. Anything that you need for me to unlock  
**Vladyslav Krut:** No, I don't think so.  
**Filippo Tosetto:** you.  
**Vladyslav Krut:** All should be clear. Decently well planned. If anything, I will let you know later in chat.  
**Filippo Tosetto:** Nice, Vlad. Thank you so much. Sorry, I need to jump on another  
**Vladyslav Krut:** All good. All good.  
**Filippo Tosetto:** meeting.  
**Vladyslav Krut:** You You do your work. I try to do mine.  
**Filippo Tosetto:** Nice.  
   
 

### Transcription ended after 00:46:43

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*