May 26, 2026

## Vlad / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Hello. Hello. Good afternoon.  
**Vladyslav Krut:** Hello. Good afternoon.  
**Filippo Tosetto:** How are  
**Vladyslav Krut:** Uh,  
**Filippo Tosetto:** you?  
**Vladyslav Krut:** I'm tired and somewhat confused  
**Filippo Tosetto:** Yes. Uh, okay. How about  
**Vladyslav Krut:** about the amount of context happening around primarily. So, Face A is really nice and doing good.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** Then I have AI design now and I'm trying my absolutely absolute best to like stay focused and try to figure out what people are doing when they need help, what is happening. It's genuinely not an easy task. Feels like all of them know what they're doing because they really rarely asking for help or like even at slightest sounds confused. So I'm like listening looking at the board. not really knowing what's happening to be completely honest just making a smart face and then one time Miguel and now Wras asked to help with CI configuration for Android and I'm like okay let me take a look and now I'm looking at Android play console CI setup how upper test works and why it's not been it's not sending automatically the production review upon tech being pushed to the review immediately and I'm like oh my god what is this how how is this supposed to work why it's not like yeah so I'm chatting with AI trying to make it you know explain stuff to me it's doing pretty good job but I'm still like a lot of stuff a lot of buzzing around a lot of distractions something like  
   
 

### 00:02:16

   
**Filippo Tosetto:** Yes. Yes. Yes. That's normal. Don't worry about it. It's uh you're going to get there over time. um AI design. In this specific moment, the guys are developing a particularly challenging and I'm quoting challenging feature because it's not challenging at all. But it's not a simple display the data in a UI screen. It requires a bit more thinking and that is why everyone is oh my god, oh my god, what am I gonna do? Because if you think about it, the majority of the features that we have in all our applications are literally take the API response, display it in a nice screen. That's it.  
**Vladyslav Krut:** Oh well. Yeah. More or  
**Filippo Tosetto:** So now that there is a little bit of technical complexity involved,  
**Vladyslav Krut:** less.  
**Filippo Tosetto:** everyone is going a bit but I'm okay. It's fine as expected. Um Vlad, uh let's get this sorted. Meaning that this quota system is out and then the team is going to go back to the usual flow where you are going to be needed very little.  
   
 

### 00:03:39

   
**Vladyslav Krut:** Well, I hope. Okay. So far, they're not asking me about the help with the quarter system. They're it's mostly about CI setup, but Android CI setup. And I'm like, is it working that differently on Android? I'm like, it was supposed to be the same.  
**Filippo Tosetto:** No, it's  
**Vladyslav Krut:** Well, upper test for example, it's like it's now not in runtime.  
**Filippo Tosetto:** not.  
**Vladyslav Krut:** All these checks are happening. it now it's now happening during signing like okay let's see why on CI it's signing the development or the QA builds with production certificates and like okay that's why like that's my question like why is that that's more important question than what's happening with upper test how much should I interfere here should I just you know patch it a little bit Or should I like do this how I see this properly? And I  
**Filippo Tosetto:** I haven't I haven't checked the message.  
**Vladyslav Krut:** am  
**Filippo Tosetto:** What is the message about? Uh we are facing an issue with app check on Android CI.  
   
 

### 00:04:47

   
**Filippo Tosetto:** Our CI uses release keys to sign development builds that our QA team is. Consequently, the Firebase Android library we utilize in our app pre app treats our C bills as release bills. What? To solve this, we need to separate keys to sign our C bills.  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** Achieve this, we must upload a new sign key store on CI and update the configuration accordingly.  
**Vladyslav Krut:** Yeah, that's my face.  
**Filippo Tosetto:** Huh.  
**Vladyslav Krut:** Yes, exactly like like you just did. AI. Well, I I I used a smart AI for this because I'm stupid in that area. So like, okay, it it has a plan. Should I just trust it and and hope that it's right, you know, to switch QA builds to development signing, generate all the well the the key store, I believe it's called,  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** and then to production as it is now. That sounds like a correct like long-term decision.  
**Filippo Tosetto:** development.  
**Vladyslav Krut:** Not sure what exactly can I break here to be completely honest.  
   
 

### 00:06:05

   
**Filippo Tosetto:** Okay. What is the problem with why QA build is different?  
**Vladyslav Krut:** I mean it it's also different in FAI for example. So we assigning one set with development certificates and the other one with production and secrets are separate which is makes  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** sense.  
**Filippo Tosetto:** So why is it not working in the same way for Android?  
**Vladyslav Krut:** Oh I have no idea. It's my second week here.  
**Filippo Tosetto:** Okay, let's do this. Um, how long how long have you spent here doing this?  
**Vladyslav Krut:** like 15 minutes so far. Not long at  
**Filippo Tosetto:** Okay, so reach one hour and then stop and send me your findings  
**Vladyslav Krut:** all.  
**Filippo Tosetto:** and I will try to figure out a way to do this.  
**Vladyslav Krut:** So like should I try to fix it or like I mean  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** what  
**Filippo Tosetto:** So, what I I what I want from you is to try to fix it,  
**Vladyslav Krut:** Okay, I can do this.  
**Filippo Tosetto:** but I don't want you to spend more than one hour on this  
   
 

### 00:07:17

   
**Vladyslav Krut:** Sure.  
**Filippo Tosetto:** point.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** And so, if you reach one hour,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** obviously if you're almost there and you have more five minutes, go for it. But if you in one hour you're still lost, uh,  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** let me know and we are going to try to find another way to handle this.  
**Vladyslav Krut:** Agreed. Okay.  
**Filippo Tosetto:** Nice. Thank you. Yeah. Um, yeah. Okay, let's do like that. Blood, what else do you have for  
**Vladyslav Krut:** Uh, what else?  
**Filippo Tosetto:** me?  
**Vladyslav Krut:** I have a more here are the complaints, but I feel like you don't want to hear them and I don't want to  
**Filippo Tosetto:** for me. Erardo is dead.  
**Vladyslav Krut:** like delay next  
**Filippo Tosetto:** Doesn't exist anymore. What? What? What?  
**Vladyslav Krut:** release again. So today on the daily stand up, we heard was like,  
**Filippo Tosetto:** Why?  
**Vladyslav Krut:** "Oh, okay." So if nobody has any updates, let's just continue with our day.  
   
 

### 00:08:14

   
**Vladyslav Krut:** And I was like, we have a build to release with all the tasks done and regression completed. Should we release? And K was like, oh, I forgot about it. And then he added more tickets. And then I rejected four out of six, I believe, tickets, uh, because these were problems with specific filters. So this fire store configuration you will not find it because he  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** created a chat with me and Ruben. I can add you there as well.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** And this problems related to fire store configuration also means that the root cause was that the vendor that we used from on the back end stopped providing these features. So they should be removed from fire store. So, how can we know if that happens again? It's like Andrew is the only one who knows that, but he probably doesn't know until he goes and check why it's  
**Filippo Tosetto:** Guys,  
**Vladyslav Krut:** broken.  
**Filippo Tosetto:** the the the answer to this question is pretty simple. This is coming.  
   
 

### 00:09:27

   
**Filippo Tosetto:** This is product that needs to know about this.  
**Vladyslav Krut:** I agree.  
**Filippo Tosetto:** I can react but I cannot know things.  
**Vladyslav Krut:** Uh  
**Filippo Tosetto:** There's no osmosis that I I receive information from from the internet, you know.  
**Vladyslav Krut:** exactly.  
**Filippo Tosetto:** Okay, don't  
**Vladyslav Krut:** And then he added another task that I couldn't just like you know  
**Filippo Tosetto:** worry.  
**Vladyslav Krut:** reflect.  
**Filippo Tosetto:** This is just noise for me.  
**Vladyslav Krut:** See  
**Filippo Tosetto:** This is for me is just noise. uh please do not waste too much time on this kind of things regarding the fact that we're not releasing 1.2.1 for me this is a clear sign that this guy needs to go uh because we wasted your time QA's time to do a full regression test and a smoke test and now he doesn't want to release. Why? What is the reason?  
**Vladyslav Krut:** No smoke test just yet. We never got a bill for smoke test.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** The QA did regression created a set of bug reports and asked Herardo to review and  
   
 

### 00:10:27

   
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** Herardo forgot that it's still part of his responsibilities. So when today I reminded him that there is a build that is waiting a decision he dragged five more task to the sprint.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** Four of them I reflected and one is still somewhat valid. Okay. Gender selector is not refreshing the home screen where you have all this sizes like promotional part. So I feel like that's kind of important. I will do  
**Filippo Tosetto:** I don't care about this s\*\*\*.  
**Vladyslav Krut:** this.  
**Filippo Tosetto:** I need you to go through that list that we came up last week and you fix those things. I'm very serious now. This is a massive waste of your time. Please do not work on that. I want you to finish what you start. Please do me a favor.  
**Vladyslav Krut:** Gladly. How do I communicate  
**Filippo Tosetto:** I will communicate to to Reuben in one hour about this point that you  
**Vladyslav Krut:** it?  
**Filippo Tosetto:** are you you are dragged into minor things that keep delaying you working on what we actually need after the conversation with Reuben because for me Reuben is the PO of this app.  
   
 

### 00:11:46

   
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** Now, after the conversation with Reuben, I'll handle everything else. I may come back to you and say, "Hey, Vlad, can you please fix that, but I want to talk to Reuben because that's his  
**Vladyslav Krut:** Sure.  
**Filippo Tosetto:** help.  
**Vladyslav Krut:** Sounds great to me. Reuben is aware. He is in the chat that Herado created. So he saw the tickets and me behaving like not my problem, not my problem. Not my problem. But one task still left.  
**Filippo Tosetto:** Um,  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** so how long would it take you to fix this render selector?  
**Vladyslav Krut:** Uh like maybe our small one.  
**Filippo Tosetto:** Okay,  
**Vladyslav Krut:** I I assume somebody just forgot to put a refresh or something.  
**Filippo Tosetto:** it's fine. just need to know the the the the life cycle so that if I come back to you because I discussed with Ruben at least I know that it's going to take you only that specific amount of time which is never that amount of time because we know that there's a lot of context switching UA yeah  
   
 

### 00:12:45

   
**Vladyslav Krut:** You may have to do regression again or so.  
**Filippo Tosetto:** yeah okay  
**Vladyslav Krut:** Let's just drag it to 1.2.2 and and call it a day and push  
**Filippo Tosetto:** I'm going to talk I'm going to uh uh run this through Reuben uh and explain the cost of you spending just one hour on that task.  
**Vladyslav Krut:** Makes sense to  
**Filippo Tosetto:** Thank you.  
**Vladyslav Krut:** me.  
**Filippo Tosetto:** Then uh I'm um sorry today I have only half an hour because I'm I'm merging Monday and Tuesday into  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** one and I I  
**Vladyslav Krut:** It really feels like you're doing two days of job in one. Yeah.  
**Filippo Tosetto:** I actually managed to squeeze in 15 minutes of lunch break. Yes.  
**Vladyslav Krut:** I kind of feel sorry for  
**Filippo Tosetto:** No, it's fine. Don't worry. No.  
**Vladyslav Krut:** you.  
**Filippo Tosetto:** Um the task that you have open regarding the image ID, how how is  
**Vladyslav Krut:** Yes. So here I had five open problems this morning.  
**Filippo Tosetto:** it  
**Vladyslav Krut:** It was mostly done like 90% done.  
   
 

### 00:13:53

   
**Vladyslav Krut:** I believe two still left and then a lot of testing and minor stuff fixing. uh the biggest problem that something that I will not be able to you know fix in an instant is that the way our data contract works now that we receiving some configuration from fire store and sending them to back end and mobile app is kind of responsible for integrity of the data that we receive from fire store and before it didn't really matter because we had like one endpoint and you send any kind of JSON phone and it maybe works sometimes it doesn't and that's why and that's one of the reasons why I installed old build today because I had to check configuration now I see why it will not be happening again uh but now we need to find all these problems with integrity and I believe there are only two ways we can do this one is me doing this and the other one QA doing this just basically going opening every filter catching an error because it throws an error. Now uh checking this error going to Andrew asking what are the acceptable fields because they're not documented on swagger maybe going to po asking to update firestorm because it's sending something else and yeah like that a lot of people involved back and forth and there is no source of truth that I can use at this point I do I did this for one filter only for gender And I'm not looking forward doing the rest  
   
 

### 00:15:34

   
**Filippo Tosetto:** No, no, no, no, no, wait, wait. So, we have a back end with the APIs.  
**Vladyslav Krut:** manually.  
**Filippo Tosetto:** Each API has different set of um parameters that they accept. So, different JSON formats, correct?  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** And this is not reflected into the swagger.  
**Vladyslav Krut:** Nope. It's  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** not.  
**Filippo Tosetto:** If we manage to get that so the swagger ready, would you be able to fix the things on your end without going through five different  
**Vladyslav Krut:** Absolutely. Yes, I will well majority majority of them.  
**Filippo Tosetto:** people?  
**Vladyslav Krut:** I will then run AI to set up proper validation for each specific request. It will be possible because right now it's not. And uh then it still will be up to QA maybe to run every single build, every single filter, but we will have a specific error every time.  
**Filippo Tosetto:** Sounds good to  
**Vladyslav Krut:** So it will be absolutely clear what is not working and no sorry will be there will  
**Filippo Tosetto:** me.  
**Vladyslav Krut:** be only one reason why it may not work.  
   
 

### 00:16:32

   
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** It will save a lot of time.  
**Filippo Tosetto:** Okay. We must.  
**Vladyslav Krut:** I probably go to Andrew and ask him to to update all these text  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** fields to have like acceptable parameters you  
**Filippo Tosetto:** But we need this done  
**Vladyslav Krut:** know.  
**Filippo Tosetto:** ASAP because otherwise you're  
**Vladyslav Krut:** Yeah. Yeah, pretty much. Well,  
**Filippo Tosetto:** stuck.  
**Vladyslav Krut:** I still have some things to do and uh but not a lot because it's 90% done. I'm very content with what I'm seeing. I'm going to fixing minor things now. I'm like generally super content with how app is working now.  
**Filippo Tosetto:** Good.  
**Vladyslav Krut:** We will have everything properly as I see.  
**Filippo Tosetto:** Nice.  
**Vladyslav Krut:** I will then document it and have a chat with Reuben and Q at some point to officially document it.  
**Filippo Tosetto:** Okay, this is very good. I'm very glad to hear because and I'm opening  
**Vladyslav Krut:** Hello.  
**Filippo Tosetto:** this. This is our last shot to get this up running.  
   
 

### 00:17:38

   
**Filippo Tosetto:** We cannot delay this anymore.  
**Vladyslav Krut:** Any specific one or generally speaking full spreadsheet? Okay.  
**Filippo Tosetto:** generally speaking for this spreadsheet. So let's say that this is the last chance we have with product to get this app to work as expected because if we ask for this time which I'm fighting for that means we need to have everything as expected.  
**Vladyslav Krut:** Yeah, I think that's very much possible. I'm already seeing like major improvement pretty much every day I do something. Sadly,  
**Filippo Tosetto:** Good.  
**Vladyslav Krut:** AI spending costs are reflecting that, but it's actually a good thing. I'm doing insane amount of job in very short timelines now.  
**Filippo Tosetto:** It is good. I like that. Um, just to quickly go through this. Um, eye level estimates half weeks. So, this will be half a week when you have a one. Okay, this is confusing.  
**Vladyslav Krut:** Yes,  
**Filippo Tosetto:** So what I'm going to do is do like this if you don't mind. And so this going to be 0.5 0.5 one  
   
 

### 00:18:45

   
**Vladyslav Krut:** I don't mind.  
**Filippo Tosetto:** one.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** Okay. Okay. So, okay, that's a bit too much.  
**Vladyslav Krut:** It won't be that much. I'm pretty sure  
**Filippo Tosetto:** One, two, three, three, and something. Okay.  
**Vladyslav Krut:** some of the stuff will start start inter like interconnecting.  
**Filippo Tosetto:** CS Yes.  
**Vladyslav Krut:** Yeah,  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** Monday not Monday but feels like Monday it will be less. I'm sure it will be less.  
**Filippo Tosetto:** Um  
**Vladyslav Krut:** These are more like safe for me estimations.  
**Filippo Tosetto:** I'm not going to say anything to anyone. I'm going to keep it like this. But what they are going to come to me is can we uh can we do first one and then we move forward with stuff and then we do another one and then because just to show progress. So if you were to prioritize them in terms of okay, I can get this done and this done and we already solve x amount of problems and then I'm going to work on this one and then I'm going to work on this.  
   
 

### 00:20:20

   
**Filippo Tosetto:** So you see a bit of a a strategy behind this  
**Vladyslav Krut:** uh not sure if I understood the question but maybe I did. So I am completely fine. I believe this will be a good idea to be like no doing a feature doing one of these. Doing a feature doing one of this and my first priority would probably be going  
**Filippo Tosetto:** Exactly.  
**Vladyslav Krut:** for filter screen duplication line five ID2. Uh this is insanely big one and probably the most valuable one.  
**Filippo Tosetto:** Mhm.  
**Vladyslav Krut:** Well, one of the most valuable ones needs to be addressed ASAP. And yeah, this one would be the first. Uh then I would go for editor everything editor related because primarily in the editor we will have to add high resolution  
**Filippo Tosetto:** Sure.  
**Vladyslav Krut:** feature and it would just make sense to do this before high resolution feature. Also, if high resolution feature is our next priority, then maybe let's skip screen the duplication and go for edit architecture because it's connected.  
**Filippo Tosetto:** No,  
**Vladyslav Krut:** It makes sense.  
   
 

### 00:21:33

   
**Filippo Tosetto:** forget about the road map that you see today because that can change any  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** time because now that Reuben is there, we are going to work on a proper road map.  
**Vladyslav Krut:** Sounds awesome. Okay.  
**Filippo Tosetto:** What about this the splash  
**Vladyslav Krut:** It doesn't bother me,  
**Filippo Tosetto:** screen?  
**Vladyslav Krut:** but that's important for users. Me as a developer, like I I genuinely don't really  
**Filippo Tosetto:** But that's but but that's what I'm going to negotiate. Okay,  
**Vladyslav Krut:** care.  
**Filippo Tosetto:** we're gonna go one week for filter screen duplication and for free I'm going to throw this. So they are happy because they see oh look at the improvement. So it's so it's me  
**Vladyslav Krut:** Make sense? Yes.  
**Filippo Tosetto:** doing uh negotiating parts. Um so okay then we have the architecture. This guy is  
**Vladyslav Krut:** This guy is big.  
**Filippo Tosetto:** big.  
**Vladyslav Krut:** It will it's getting smaller with every other task handled in from this list because everywhere where I'm  
**Filippo Tosetto:** Sure. Do we keep  
   
 

### 00:22:43

   
**Vladyslav Krut:** going I'm doing it with proper concurrency immediately.  
**Filippo Tosetto:** it?  
**Vladyslav Krut:** Then I will just flip the switch to switch six and it's going to be knocking  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** around.  
**Filippo Tosetto:** So in the moment you redo the the filter screen duplication, the editor architecture that you already close a lot of these points.  
**Vladyslav Krut:** Yes, it's hard to estimate how much uh but yeah,  
**Filippo Tosetto:** Yeah. Yes.  
**Vladyslav Krut:** it will be massive progress and then probably management of the very first one user state subscription  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** quota will will reduce it even  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** lower.  
**Filippo Tosetto:** So I'm going to keep this as last.  
**Vladyslav Krut:** Yes, it's a good idea.  
**Filippo Tosetto:** Okay. So, I'm just going to play a bit here. So, this guy, this guy. I'm just going to do something like this. What do you think?  
**Vladyslav Krut:** That's looks very good to me.  
**Filippo Tosetto:** Okay. Okay. All  
**Vladyslav Krut:** It will also be helpful. I know that maybe not just yet,  
   
 

### 00:23:46

   
**Filippo Tosetto:** right.  
**Vladyslav Krut:** but depends on what will be like our timeline. If we can see Reuben's version of the road map, we can also prioritize and maybe change the order to be better connected with the features we are about to deliver. And it may have some sense to sneak some of these into the implementation of the road map items. It's most likely be  
**Filippo Tosetto:** I'm I'm going to I'm going to have an alignment with him today,  
**Vladyslav Krut:** possible.  
**Filippo Tosetto:** but I doubt he's going to have a road map ready most likely next week. So by next week I'm hoping that we already starting to work on something  
**Vladyslav Krut:** Okay, that sounds good. Uh I expect to get done with the image ID related  
**Filippo Tosetto:** here.  
**Vladyslav Krut:** communication rework maybe tomorrow. I was about to say today, but let's be realistic. There are concerns. Maybe tomorrow and so Wednesday or something, I will have a relatively free time to begin working on any other  
**Filippo Tosetto:** Okay. So,  
**Vladyslav Krut:** task.  
   
 

### 00:25:04

   
**Filippo Tosetto:** hey Andrew, are you talking? Um, will it be possible to update all the swagger for the filters API in face AI? We are having some issues on the mobile part and having the documentation dated would speed up the process big time. Cool. Created a chat. So that is sorted. Okay. Nice. Um, all good with Maria after the conversation of after the s\*\*\* show on Friday.  
**Vladyslav Krut:** freaky Friday and we didn't have any communication then so yeah no problems  
**Filippo Tosetto:** Okay. Okay. Good. Blood, I think on my end that's everything that I needed to know. I'm going to ask you if you need anything from me.  
**Vladyslav Krut:** Let me check. I have some nose. Some too much of them. No, no. All good from my side as well. Regarding face,  
**Filippo Tosetto:** Okay,  
**Vladyslav Krut:** everything is going well. ignoring her art.  
**Filippo Tosetto:** it's going.  
**Vladyslav Krut:** Pretty  
**Filippo Tosetto:** Please ignore Erdardo because uh this this is going to be his last week.  
   
 

### 00:26:34

   
**Vladyslav Krut:** good.  
**Filippo Tosetto:** He's not going to do anything and it's just complicated things for me. So, I'm going to push to get that ticket out of your way as soon as possible. And I want you to focus to deliver what you are working on today and then start to tackle that list straight away.  
**Vladyslav Krut:** Okay, that sounds good.  
**Filippo Tosetto:** I Good.  
**Vladyslav Krut:** I have a plan.  
**Filippo Tosetto:** Anything else?  
**Vladyslav Krut:** probably worth mentioning that once I'm done with this migrations that I'm doing right now, I will be anyway expecting some amount of bug reports from QA. So I will be coming to this task again that's I think that's  
**Filippo Tosetto:** Oh yeah.  
**Vladyslav Krut:** clear for everybody. You you cannot rewrite half of the application and not create any regressions. Just wanted to say it out loud.  
**Filippo Tosetto:** Yes. Uh I will communicate this to to Reuben as well. Uh but he knows how things are. Who knows?  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** Okay. Um, anything else on your  
**Vladyslav Krut:** No, I think that's it. So,  
**Filippo Tosetto:** end?  
**Vladyslav Krut:** we have a Andrew, you just asked and I need to spend an hour doing Android CI for AI design and  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** and working on Yeah,  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** all good. Plan for the big sounds more or less  
**Filippo Tosetto:** I will try to keep you out of any political conversation that is happening.  
**Vladyslav Krut:** clear.  
**Filippo Tosetto:** I want you to focus on the code, please. Let's do  
**Vladyslav Krut:** At the same time,  
**Filippo Tosetto:** that.  
**Vladyslav Krut:** if you need a technical guide to sound smart while talking about some of these, well, involve me.  
**Filippo Tosetto:** We'll do. Thank you. Thank you so much. Uh, could you answer Andrew because he just answered,  
**Vladyslav Krut:** I Yes.  
**Filippo Tosetto:** I'll let you go. Thank you so much.  
**Vladyslav Krut:** Thank you. Have a nice rest of your day.  
**Filippo Tosetto:** You too. Bye-bye.  
   
 

### Transcription ended after 00:28:42

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*