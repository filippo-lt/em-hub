Feb 16, 2026

## Andrey / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Hello.  
**Andrei Marinov:** Hello.  
**Filippo Tosetto:** I'm good. What about you? How are you feeling?  
**Andrei Marinov:** I'm doing well. Can't complain.  
**Filippo Tosetto:** Can you walk?  
**Andrei Marinov:** Working.  
**Filippo Tosetto:** Can you run?  
**Andrei Marinov:** No. No. It will be the 8th of March when I can.  
**Filippo Tosetto:** Uh, wait. And Andre,  
**Andrei Marinov:** But I got the brace off so I You can hear  
**Filippo Tosetto:** sorry. I don't wait.  
**Andrei Marinov:** me.  
**Filippo Tosetto:** I um I don't know.  
**Andrei Marinov:** You can hear me.  
**Filippo Tosetto:** It's me or you. It's breaking. Let's try again.  
**Andrei Marinov:** What about now? Is it okay now?  
**Filippo Tosetto:** Nope. Yes. All good.  
**Andrei Marinov:** I'm moving.  
**Filippo Tosetto:** All good. All good.  
**Andrei Marinov:** Okay. Uh yeah, I was saying uh yeah, I won't be walking anytime soon. It will be another three weeks or so. But at least I got the brace off and I can like bend my knee 60° which is I can't hear you.  
   
 

### 00:06:36

   
**Andrei Marinov:** Oh, you're mute.  
**Filippo Tosetto:** Yes. Sorry,  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** that's me. That's my I was muted. No, is that's an achievement already. Bending the knee.  
**Andrei Marinov:** makes sitting at a desk easier.  
**Filippo Tosetto:** Okay. I don't I I really feel that there is some connection issues here today.  
**Andrei Marinov:** Uh,  
**Filippo Tosetto:** Maybe try switching off the the camera.  
**Andrei Marinov:** am I stuttering or something? Yeah.  
**Filippo Tosetto:** Maybe switch off the camera.  
**Andrei Marinov:** Let's see now.  
**Filippo Tosetto:** Let's try again. Okay.  
**Andrei Marinov:** Is it better?  
**Filippo Tosetto:** Yeah. Oh, yes. I can hear it perfectly.  
**Andrei Marinov:** That's weird. Yeah. Let me see if I Now,  
**Filippo Tosetto:** I don't know.  
**Andrei Marinov:** is it worse now?  
**Filippo Tosetto:** No, but sometimes it just breaks up the the the the audio.  
**Andrei Marinov:** Is it  
**Filippo Tosetto:** So,  
**Andrei Marinov:** weird?  
**Filippo Tosetto:** it's weird.  
**Andrei Marinov:** I don't know. Monday.  
**Filippo Tosetto:** AI taking over probably.  
**Andrei Marinov:** It always happens on Monday.  
   
 

### 00:07:26

   
**Filippo Tosetto:** Yes. Okay. Good news and bad news. No, I'm joking. I'm joking. I'm joking. Uh, it's uh the good news is that I've seen that you um you took over with the llinter in Limo iOS and that was pretty straightforward. Do you wanna can you can you walk me through the experience itself because it's something that I want to do as well on my apps.  
**Andrei Marinov:** Uh yes. So I had the guys working on that I think the initial weeks when they started working on the project. Uh and they were they actually went through and fixed almost all the issues like there were 10 issues or something like that left which were smaller ones. Uh I was looking at swiftlint and it had like 5,000 uh swift link issues but when I looked closely it was actually third party dependencies like the ones that we include directly or it wasn't actually also scanning properly in the the code base. It wasn't scanning at the IM mode code base. It was scanning one folder up and it has some fast name stuff in there.  
   
 

### 00:08:48

   
**Andrei Marinov:** So it was uh getting those as well and after tweaking those we were left with 10 issues which I fixed. I uh did the CI uh required thing where the swift l is not required and everything is working correctly. So it most of the work was actually done by by the guys.  
**Filippo Tosetto:** So nice. This is very good. So with this configuration that you set up in IM mode, if a swift link rule is broken somehow the the CI will crash and this  
**Andrei Marinov:** Yeah. And we saw that baby.  
**Filippo Tosetto:** is also retroactive that you fixed  
**Andrei Marinov:** Uh, what do you mean?  
**Filippo Tosetto:** all the warnings.  
**Andrei Marinov:** Uh, all of the warnings currently on the dev branch are fixed. Yes.  
**Filippo Tosetto:** This is very good. Very good. I'm super happy about this.  
**Andrei Marinov:** I didn't fix them just to be clear.  
**Filippo Tosetto:** I thought it was  
**Andrei Marinov:** Uh the guys fixed them the initial weeks uh when they started working.  
**Filippo Tosetto:** but  
**Andrei Marinov:** I mistakenly thought that there were a lot more because we weren't scanning the correct thing.  
   
 

### 00:09:59

   
**Filippo Tosetto:** still  
**Andrei Marinov:** Uh so yeah they they did that in two weeks.  
**Filippo Tosetto:** it is very good. Very good. I'm very happy. I mean, this Okay. Okay. I'm I'm excited about this kind of things. They thought it was a way more painful process that would take way longer and also the setup and everything else, but it seems to me that it went pretty well. So, very happy about this. Nice. Thank you.  
**Andrei Marinov:** Yeah, I mean it seems quick now, but the guys were fixing them a lot during the first weeks. Uh, I mean, pretty much all they did the first couple of weeks was swift clean issues. So it might seem fast now, but it's not fast overall in absolute time.  
**Filippo Tosetto:** also because I'm going to ask you obviously to do the same for a uh AI design now. So I guess that's not going to be as easy.  
**Andrei Marinov:** I would say that I would wait for whatever team comes in from there because I can trust these guys to be able to do  
   
 

### 00:11:12

   
**Filippo Tosetto:** Okay, let's discuss about it in a second anyway. Um, okay. I'm very pleased with that. I'm also very pleased that Artam is back and it seems to me that the guy is also extremely proactive.  
**Andrei Marinov:** Trying Cancia.  
**Filippo Tosetto:** It's it's this is good. So, very happy very happy about this. Um, okay. Um now let's talk about something else because I want to share with you the road map and everything that is happening. H but first I want to give you a bit of the feedback that we received for IMOT. So I don't know if you know but last week um the road maps have been presented for all the apps and there were quite a few complaints uh from Diego uh regarding IMOD because looking at the road map that has been presented for IMOT uh it looks like the next eight weeks is all about design and UI work. Okay. Um that's not the case. Me and you know that. But the way the road map was uh uh presented was not uh great.  
   
 

### 00:12:28

   
**Filippo Tosetto:** Also because you know you know better than me because you have been flagging this for forever that uh Jira is dead pretty much. I have no other way to explain and show this than than say that Jira is pretty much dead for this project. Um, and so there were quite a few complaints and and on one end I'm very upset about it because I don't like this kind of uh uh things that reflects on on the team itself because it's yes it's on product but it's also on us to check this but on the other end I'm also uh somehow glad that now that is in the open we can push to get it fixed. If you see what I mean zoom.  
**Andrei Marinov:** Uh what are they looking for exactly in the in the road map?  
**Filippo Tosetto:** Yeah. You know what? I'm going to I'm going to show the screen so maybe uh you you understand what I mean. So um Okay. Why is it not sharing? Okay. Now it's sharing.  
   
 

### 00:13:34

   
**Filippo Tosetto:** So have you seen this file?  
**Andrei Marinov:** Yes.  
**Filippo Tosetto:** Okay. Perfect. So it's it's pretty straightforward. I'm going to pick uh one of the apps that I have where you you see a road map uh kind of from a product perspective like this part. The first part you can see that you know week by week you can see things happening and each one of these uh kind of uh rows they have an epic attached and um dates on when is supposed to be delivered. There's also some technical work here uh and uh also some uh operational work let's say. So for this specific app for the twist what I did was to add terms of technical work I added a couple of interesting points which are you know uh kind of uh AI judge uh which is a way to for us to check a lot of details regarding the the AI that uh the gen sorry the details regarding the AI tools that we are using. So in terms of costs, in terms of quality and all of that, um I created the epic and I kind of run a bit of high level estimate and then put it based on our idea when this should be happening.  
   
 

### 00:14:55

   
**Filippo Tosetto:** Same for credit system. I will explain this in in another meeting because you're going to need to do it in in AI design as well. and product came to me on the other end with this um epics and our job as engineering managers is to put down some high level estimates and then sitting down we also create a capacity planning. Okay. So based on all of this you have a road map. Technically this road map should be for three months in advance and uh this document is a live document that should be evolving over time. So this is the by the book the idea behind the specific uh document that has been shared last week with uh from it was David Matayano and Christian the CPO they shared it with um with uh Diego and presented all these kind of ideas. Now if you check you should have access to it but I'm happy to share it again. you should have access to it with because it's for everyone. So you should be able to see it.  
   
 

### 00:16:09

   
**Filippo Tosetto:** The problem here is that if we check IMO the situation is not that great. So compared to the previous app that I show showed you, this is what we see in IMO. And if we check at the actual initiatives, you have design one, phase one, design phase two, liquid glass, light team, light and dark theme. So there is a lot of UI work. We also know me and you that we actually have a lot of technical work to be done here. Okay? because you have you know the u the problem with uh the connections that is dropped and doesn't work for all the TVs and we need to raise that to a higher level. we need to increase the number of Android TV to be supported. Uh the fact that that the um epic that you created regarding dropping the AXC frameworks and that is work that requires a lot of time but it doesn't really reflect in product evolution. Okay. So the narrative is the following and I want to be pretty transparent with you.  
   
 

### 00:17:28

   
**Filippo Tosetto:** That's why I'm doing this full uh introduction is that we receive from product some initiatives to improve the product. We technically add other initiatives to improve the product from a technical perspective. Okay. But if this part is not filled, I don't care. I mean I care because obviously the app is not growing itself. But that's not on me and you to take care of this. Our job is to say, okay, uh this second support here, let me open the epic. Let me look at it. Let me estimate it. Okay, and then I'm going to put here some numbers. So that is what we care about. If Diego goes here and see that there are no initiatives here, well, that's not my problem. That's something that the PM and the PO should somehow be doing. What we need to be doing is to align on the fact that you know for a redesign is going to take two weeks instead of five as it was before this morning because this morning was five weeks for a redesign which for me is an insane amount of time because what happened was  
   
 

### 00:18:47

   
**Andrei Marinov:** And let's go  
**Filippo Tosetto:** that product to show there's a lot to do they increase my initial estimates to more and more time. So this liquid glass was kind of going to the end of April because the other initiatives way were way way longer. Anyway, so this was the whole um introduction. Doubts, questions, anything?  
**Andrei Marinov:** Uh, no. I think you explained it pretty well. Uh, I can see in the comparison why people might think it's lucky as far as features.  
**Filippo Tosetto:** I'm going to show you something else now that for me it's going to be very important and I want your help to work on which is capacity planning pretty simple high level obviously and we have two developers. Oops. And we just fill this with whatever we have to do. So, it's like Lego blocks kind of concept. Um, and this morning I was like taking all the the epics and putting the the actual estimates for the epics, how long they're going to take. And I'm finding myself that actually we have a lot of work to do.  
   
 

### 00:20:30

   
**Filippo Tosetto:** It's just a matter of being able to organize it properly especially now that we have uh art and back. So, I would like your help here to fill in the capacity plan for the foreseeable future with the epics that we have uh in Jira. Where is it? Here. This is Jira epics which are pretty much the one that already put there. Uh because by having visibility on you know these kind of things we can plan the future. So I would like to if you could help doing it I can somehow help doing it. If you need help I don't know. Um, I don't I'm still thinking if it's it's probably you that should help me do this because you have visibility on the app itself and on the fact that developers are busy doing things that I wouldn't know enough about. What do you  
**Andrei Marinov:** Uh,  
**Filippo Tosetto:** think?  
**Andrei Marinov:** sure. Yeah, I can do that. So, basically take all of these epics and uh spread them out over the timeline.  
   
 

### 00:22:01

   
**Filippo Tosetto:** Correct.  
**Andrei Marinov:** for a developer.  
**Filippo Tosetto:** base. Yes, obviously per per developer. Um the idea here obviously you can have you know I'm just playing around maybe they are both working on this connection improvements so it's totally fine to to do this uh but ideally you have the time to open the epic and see my highle estimates they may not make sense this highle estimate I'm was just me coming up with them if you think they are not correct please let me know we can work around Uh but this is the full circle that we need so we can plan better the road map here.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** to this ex this um document I will change it a bit so that these initiatives yes they are technical but if you think about the first two they are actually having a huge product impact it's not really only technical work so somehow I would like to move them up but I still need to think about it do not worry about this specific document that's up to me to to to move it around.  
   
 

### 00:23:26

   
**Filippo Tosetto:** And that is the initial idea uh for um capacity planning and road map these kind of things. thoughts.  
**Andrei Marinov:** Uh yeah, we can make that happen. That makes sense. Today we have the road map.  
**Filippo Tosetto:** Do do you do you see do you  
**Andrei Marinov:** We want to plan out how to achieve that.  
**Filippo Tosetto:** see benefit in  
**Andrei Marinov:** Uh, it's not for the team like me, but apparently someone higher up can go in and see, oh, they should be working on this, and next week they'll be working on that. So, I imagine it's uh helpful for someone else.  
**Filippo Tosetto:** It's helpful for me to see how the app is progressing. It's helpful to hire apps to see okay we are spending money for hiring to developers. So at least we know they are working on something that is not redesigning the app for 3 months. You know that is the concept here and uh that is also going to be tied to to money because uh each app now has a economic objective. So each initiative that we're going to work on needs somehow to bring some results in terms of money.  
   
 

### 00:24:48

   
**Filippo Tosetto:** Is it about ret retaining users or gaining new users? For instance, the fact that we are going to support older uh Android devices in my head is okay, this is a way to get new users that today we don't have the connectivity issue that we are having today is about retaining users. So, it's it's way more higher up. I know. But I I I wanted you to to understand what's behind all of this as well.  
**Andrei Marinov:** Yeah, I feel like that makes sense.  
**Filippo Tosetto:** Sorry, I'm going to ask you also another thing regarding IMO which is this spreadsheet and uh let me try to see this to to to explain it why I came up with this uh idea. I feel that today we have especially me for me it's hard to see risks in advance for this application not because I don't trust you I trust you I know you're doing a good job because I can see that when we're talking about technical stuff you're you're doing your your what you're good at uh and also organizing the team and taking care of everything so it's not I need more eyes on your work it's I need more visibility on product today and I feel that today I don't have much control but neither have you because Mikall doesn't have control if you see my point here.  
   
 

### 00:26:51

   
**Filippo Tosetto:** Uh so um I I tried to think about the best way for me to have a snapshot every week of the status of this app. And that is why I was kind of I don't care about the deliverables per se. I don't care that the guys are going to work on liquid glass today. But I do care if there are some blockers here that you know uh Jira store is not ready you know these kind of things. So this is obviously I impact high probability and the source is product somehow. So, it's for me to have a clear picture of the risks tied to this app today. What do you think?  
**Andrei Marinov:** Okay. Uh yeah, I think uh like putting things down uh would be able to track week to week how things are going. So, makes sense to be able to just open a spreadsheet and know how the project project is  
**Filippo Tosetto:** Thank you. I I don't want you to spend more than 10 minutes on this possibly before the hour one to one next week so we can you know keep it alive and we can we can discuss it.  
   
 

### 00:28:26

   
**Filippo Tosetto:** If we think that the product is going the right direction, we can scrap this practice. But for now, I would like to have a a bit of eyes on this situation. That's it. Nice. Um, okay. Let's go here. Um, next. I'm not iOS. We covered everything. Yes. Okay. We  
**Andrei Marinov:** Uh before that another update. Uh so I went in today again and it seems we have another crash issue. Uh this one is specifically with high sense and it's coming uh from a third party framework called Coco MQTT and it's something I don't think it's something that we caused. It's more of a 26 issue on that framework. Uh, it is.  
**Filippo Tosetto:** And Andre,  
**Andrei Marinov:** Yeah, let me just spell it out  
**Filippo Tosetto:** you're breaking up a lot for me.  
**Andrei Marinov:** here.  
**Filippo Tosetto:** I'm I'm really don't understand.  
**Andrei Marinov:** Sorry, it's it's likely me and I think I know why,  
**Filippo Tosetto:** Sorry.  
**Andrei Marinov:** but one second.  
   
 

### 00:29:48

   
**Andrei Marinov:** I'll come back.  
**Filippo Tosetto:** Are you VIP coding IMOT as well? Yeah.  
**Andrei Marinov:** Is it better now? Is it better now?  
**Filippo Tosetto:** Yeah. Yeah.  
**Andrei Marinov:** Is it better now?  
**Filippo Tosetto:** Were you vibe coding I mode as well?  
**Andrei Marinov:** Okay. Uh, no. I I have an internet connection that goes into my monitor and it goes into my laptop and for I updated to 26.3 today and that does not seem to be working and my Wi-Fi is like two rooms away. So, that's probably what's causing the issue. Uh yeah, I switched to my phone but yeah the the framework is called uh co MQTT I past it here in the chat. Okay, you saw that uh basically I think it's uh an issue on iOS 26 for that particular framework because all our crashes are on 26 and uh with this release we enable 26 support. So I imagine that's why it is uh it is for the high sense TVs. Uh they use this particular uh OS called Vida OS.  
   
 

### 00:31:02

   
**Andrei Marinov:** It's a Linux based one. Uh as to why we didn't cut it during release, I don't know. Uh this didn't happen to us. I happens about to about 10% of users from time to time. This is something that we prioritize and plan to fix with 2.3 which is going to go out probably this week uh as we wrap up the sprint. Uh and yeah, just so you'll be aware of what's going on.  
**Filippo Tosetto:** Thank you for the  
**Andrei Marinov:** It wasn't picking up steam on on Friday.  
**Filippo Tosetto:** update.  
**Andrei Marinov:** We did pick up stream steam only during the weekend because guess people watch more TV during the weekend and yeah that's rather unfortunate.  
**Filippo Tosetto:** How do we fix it?  
**Andrei Marinov:** Um, no idea yet. We're I'm having sir looking into it.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** I went on their GitHub issues page and it seems that they had this sort of issue uh like four years ago. Some people were complaining. So, uh they claim to have fixed it in a version, but I don't know.  
   
 

### 00:32:13

   
**Andrei Marinov:** There's nothing more recent recently about that. So, I guess we'll have to go in, take a look, see how we fix it.  
**Filippo Tosetto:** How come the  
**Andrei Marinov:** It might be that it's a running it on a different queue,  
**Filippo Tosetto:** purple?  
**Andrei Marinov:** on a background queue uh makes it crash from time to time. That's something that I saw.  
**Filippo Tosetto:** How can we probably prevent this kind of problems?  
**Andrei Marinov:** Uh we talked about that with Miho. There were some ideas like automated testing, but that doesn't really make sense with hardware because we can automate the TVs as well. So it's pretty much doing a lot of manual QA uh on a lot of different configurations and hope we catch it. Another thing we talked about is uh doing phased releases where we incrementally uh release the app so that we can catch these things sooner and not affect as many users. Uh so we'll definitely start implementing that but other than doing like manual QA I don't think that we have bunch of other options.  
**Filippo Tosetto:** So technically speaking this is not something we can prevent.  
   
 

### 00:33:34

   
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** we are on the latest version of the library as well.  
**Filippo Tosetto:** So  
**Andrei Marinov:** It was updated last March. Uh so it's old but not that old. So,  
**Filippo Tosetto:** but see this this is for me a big issue because we are dependent on all these libraries that are not really maintained. And I keep running in my ad, is there a way for us to make sure this works? Can we build our own libraries? Can we do something about this?  
**Andrei Marinov:** Oh, we can go into building out our libraries, but it's like a lot of work to support different protocols. Like you're probably familiar with MQTT. This is a library that implements that protocol. Uh it's quite a big one. I mean, it's not something that we can easily reproduce.  
**Filippo Tosetto:** Is it about so each one of these library do they implement a specific protocol or is it  
**Andrei Marinov:** Uh yeah,  
**Filippo Tosetto:** more  
**Andrei Marinov:** different libraries deal with different TVs because they deal work with different protocols.  
   
 

### 00:34:47

   
**Filippo Tosetto:** okay so it's not that we have two libraries implementing the same protocol we just use them because they connect to two TVs  
**Andrei Marinov:** Yeah. So for example, one of the TV works with WebRTC, so we have to support that. Another one works with TQTT, so we have to support that. And we use different libraries for the different TVs. That's  
**Filippo Tosetto:** H.  
**Andrei Marinov:** many of which are outdated as I can  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** Uh there might be another library that has a credit for rank.  
**Filippo Tosetto:** Okay, need to find a solution because otherwise we keep running the same issue over and over again. So, we were going to need one developer that keeps up to date with all the libraries and making sure they work pretty much, which that's going to be his job. And  
**Andrei Marinov:** Yeah, pretty much. Because for example, there is uh this library that's actually for metal or server. Maybe we can use that instead of I  
**Filippo Tosetto:** because tomorrow we're going to need to handle this guy as well.  
   
 

### 00:36:16

   
**Filippo Tosetto:** Okay. And we're going to have not you directly but it's going to have this other app which is pretty much uh casting the the the casting functionality we have in IM mode but still we need to connect to all the TVs. So in my head more and more is coming up the idea that we need a shared solution for all this. Okay.  
**Andrei Marinov:** Yeah. Well, from a quick look, there's more libraries that implement MQTT. So, maybe we can look into them more recently.  
**Filippo Tosetto:** Okay. All right. Um, okay. Okay. I I'm I'm I'm running in my head what's the best uh course of action for Iote in general. Um, but it's not the right moment. Okay. Uh while we're talking about IMOD, I share with you a folder with uh some Android uh CVS. In my opinion, there's only one that is worth interviewing, probably two just for the sake of it. Uh if you can go through them quickly today and then share with me your thoughts and then I'm going to schedule the interviews as as usual.  
   
 

### 00:38:02

   
**Filippo Tosetto:** What I'm going to do this time though, as this is Android, I'm going to invite Mano, so it can ask specific technical questions which I think nor me or you are good enough to handle this. And we need someone that knows these things here. Okay. And that covers I'm not Android. Um AI design pretty brief situ check up here. So Dimitro should have joined today is having issues with the connection. So logging in for some reason no one in it is helping me for this. So this needs to to to pretty much wait until someone is uh is helping probably the usual password issue. Uh I have another question. How's the situation with Salman going down? Because we removed this access yesterday.  
**Andrei Marinov:** Yeah, he didn't know. The team didn't know.  
**Filippo Tosetto:** Good night.  
**Andrei Marinov:** Uh but the the PMS or the person on their side wasn't in today. So it was only the iOS and Android Dash and they also find out today that someone is no longer here.  
   
 

### 00:39:19

   
**Andrei Marinov:** But uh we told them that there's a new guy coming on and they were like okay. So, let's see how it  
**Filippo Tosetto:** This is a communication issue that needs to be handled by cichlum because they knew since one week it's not that they discovered this morning and we said that we would cut access to this guy at the end of the week which we did. So if they are having issues it's issues on their side not on ours. This is just for you to have visibility on the situation. That's  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** it.  
**Andrei Marinov:** I know that you sent that message over that maybe it's nothing. So yeah, it's up to them.  
**Filippo Tosetto:** Good. Um,  
**Andrei Marinov:** Of  
**Filippo Tosetto:** whenever Ditro will be in, would you be able to uh set up a sort of uh on boarding  
**Andrei Marinov:** course.  
**Filippo Tosetto:** for him from a tech?  
**Andrei Marinov:** Yes. I insist on it.  
**Filippo Tosetto:** Sorry.  
**Andrei Marinov:** I insist on it. Yeah.  
**Filippo Tosetto:** You you insist.  
   
 

### 00:40:32

   
**Andrei Marinov:** I insist on on making it. Yeah.  
**Filippo Tosetto:** Ah, okay.  
**Andrei Marinov:** In system  
**Filippo Tosetto:** Good. Thank you. Good. Uh, I will ping also Miguel because I feel that Miguel sometimes is lost. I want him to get on board of this. Okay. Uh you said llinter not yet. Better wait.  
**Andrei Marinov:** Yes.  
**Filippo Tosetto:** Okay. Uh let me Okay. Let me just remove it for now. Uh then same exercise as before but for AI design. So I was checking a bit the the road map uh eye level estimates etc. If you could just double check that makes sense what I put down here. Uh and for me we need to discuss but not today about this uh because it will need a bit of this guys and probably that. So we will need to probably move this here. But don't worry about this part yet because I will discuss with uh uh Sergio Weso which is the PM. Uh what I'm interested about is that he checked this let's say until midappril and it makes sense uh according to what you know that's happening in the product.  
   
 

### 00:42:08

   
**Filippo Tosetto:** To me personally, it feels that the mobile three weeks for each one of this feature, it's a lot of time and this one four weeks. If you could investigate on your site, that would be great.  
**Andrei Marinov:** I'll take it Uh do we do we care that are  
**Filippo Tosetto:** Nice. Thank you.  
**Andrei Marinov:** we when are we migrating the team because that won't be right. We can tell from louder. It's how you  
**Filippo Tosetto:** the team sorry the team will be migrated uh it is somehow in the road map so I'm okay whenever you know uh let me go back here again whenever the team migrates we can say okay you know team new team is coming here we're just going to move down everything by two weeks because of on boarding and everything else is going to be delayed you know this kind of things. Uh but for now, let's keep it like this so we can see what we can plan for the future. I opened up the positions, so I'm expecting procurement to start to work on giving us more uh um upto-date CVS for this two roles.  
   
 

### 00:43:37

   
**Filippo Tosetto:** they won't be as complex as someone for iMote because this is more lightweight uh front end but I still feel that we should find someone decent because this project needs a a huge kick because there's also very much interest from a business perspective in this project. You're just waiting for it to start you know ramping up properly.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Nice. One last thing I wanted to talk to you about and it's more like uh I need a little help from you to com complete this document.  
**Andrei Marinov:** Yeah, we talked about it last week,  
**Filippo Tosetto:** Um no worries.  
**Andrei Marinov:** but I wasn't sure whether I should do it straight away  
**Filippo Tosetto:** I I I've done it. I've done most of it. So the good thing is that um with the north project so from next month probably next month or the one after this will be filled automatically so nothing to be done on your side this I will take care of filling because yeah it's I have access to forward so for me it's easy what I need help from you is this part uh I Can you please call me?  
   
 

### 00:45:07

   
**Filippo Tosetto:** I need your help into evaluating Artam and Sergey. Actually,  
**Andrei Marinov:** I can do  
**Filippo Tosetto:** I will need your help also for these two guys. Uh because I have an idea, but uh so we can do it right now quickly if you want.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Um so ARTM communication  
**Andrei Marinov:** Uh what's the is there like a what's the grading  
**Filippo Tosetto:** collaboration  
**Andrei Marinov:** here? Is there like five is perfect and no one is perfect Okay, let's put in  
**Filippo Tosetto:** for me. So for me five is the highest because it shows productivity, good communicator and that's it. So do not worry about put a to to give me a five if you think it's a five. That's  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** it.  
**Andrei Marinov:** On the next one, Armagana five. Uh, circus.  
**Filippo Tosetto:** Okay. Interesting.  
**Andrei Marinov:** What to study tail?  
**Filippo Tosetto:** Does it come to the standups?  
**Andrei Marinov:** What do we measure  
**Filippo Tosetto:** Uh does it flag a missing information in Jira? Is it uh present?  
   
 

### 00:46:45

   
**Filippo Tosetto:** Is it you know disappearing from uh from the two in the afternoon without reason? So is it is he a person that you know comply to all the processes?  
**Andrei Marinov:** I'll go five for Arm again and four for sometimes he's not that responsive.  
**Filippo Tosetto:** Okay. And if you would score in general. So we have issues here for forward and for user stories, but we know that these are not related to their performance per se, but they're related to the fact that they don't have work assigned to them, which we are going to change by the way. So if you would give yourself a a sort of final score for these guys, are they top? Are they average? Below average, critical.  
**Andrei Marinov:** Oh yeah, I would say maybe top score item and average.  
**Filippo Tosetto:** Sounds good to me.  
**Andrei Marinov:** You know, if there was a one between top and average, I'll probably put Like he did the above average.  
**Filippo Tosetto:** Average is not bad. Average is not bad. Don't worry. Um so in fact for me this this guy is a bit average.  
   
 

### 00:48:15

   
**Filippo Tosetto:** Um okay while we are doing this exercise should we go through also the uh AI design guys.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Okay. Salman very  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** low.  
**Andrei Marinov:** Should we go with him or not? Uh on engagement and productivity. Uh it's like two for southern and three  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** And for color process and professionalism like one uh for a marriage probably like a  
**Filippo Tosetto:** Interesting. And you agree with me? They are below average.  
**Andrei Marinov:** Yeah, I have some doubts that it might even be critical.  
**Filippo Tosetto:** Well, I cannot put critical because the app is going to the store. They are producing code. And if I look at this, they are top performers because they are doing a lot of git commits, but also they are closing an insane amount of story points, which that also shows  
**Andrei Marinov:** Uh that's hours that's like story points in AI  
**Filippo Tosetto:** that but I like this. This for me is very interesting because it shows how broken our system is because we have four apps here and they are all with different metrics.  
   
 

### 00:50:03

   
**Filippo Tosetto:** You have IMO that has zero pretty much in Jira and story points. You have tattooist which is okay and I know the guys are top performers and then you have this is which doesn't make sense at all. It just doesn't make sense. Anyway,  
**Andrei Marinov:** When you look at it,  
**Filippo Tosetto:** sorry.  
**Andrei Marinov:** they have 11 tasks and 135 story points where on the tourist they have 63 task with  
**Filippo Tosetto:** Yes. Yes.  
**Andrei Marinov:** That's mostly because they overinflate their installations quite a bit sometimes and also because we use ours. We can't compare ourselves.  
**Filippo Tosetto:** Uh speaking of ours, how is it going with um North project in AI Time.  
**Andrei Marinov:** Uh so I've seen that media has started uh putting up a lot of meetings like retros and plannings and refinements with me. So uh that's pretty much all I've seen about the project so far.  
**Filippo Tosetto:** Okay. Okay. I guess it's more a matter of waiting for the new team uh to get the whole thing kicks kick starting but we need to make a move.  
   
 

### 00:51:29

   
**Filippo Tosetto:** So this is something that we don't need to push. It's up to them. So for us it's just we are user of this system and for once we don't have to take the reigns. So we'll see what's going to happen there. But you know this whole capacity planning road map and everything else is for giving a bit of shape to the current state of all our products and gives visibility to to me that I'm not in the project like you are and to say hey why are we taking you know uh three weeks for garden design. So this kind of things. So why are we taking four weeks for floor styles in the app? We don't need to do much. It's just a couple of views. So why are we planning for four weeks? So this is the exercise that is helping me to do this capacity plan. That's it. Andre the think that's it. Um actually couple of words on the PC. Um what happened that this guy David Sanchez decided to take over everything and pretty much um making the whole exercise uh pointless because we didn't have the time to put any constraints any guard rails and he decided to go off on a tangent and do whatever he wants and the result is that he's just copying and pasting AI I comments and letting the AI run as you can  
   
 

### 00:53:18

   
**Filippo Tosetto:** see pretty much rogue. Uh so I'm going to wrap up this in the next couple of days because it's it's just time wasted for you. It's not worth it. Uh but there was a big learning for me behind all of this which is a nontechnical person that uses AI to work on an existing app must have guard rails otherwise the work is totally useless. So we learned  
**Andrei Marinov:** Now,  
**Filippo Tosetto:** something.  
**Andrei Marinov:** I think it could work, but if we like don't care at all about the code quality. Uh like if we get uh what was the name the other works on um I'm blanking on what was the first two apps that I worked  
**Filippo Tosetto:** Oh,  
**Andrei Marinov:** on.  
**Filippo Tosetto:** Mirage. Mirage. Goya.  
**Andrei Marinov:** So if he takes up and starts working in there, I mean the call quality already is awesome. So he can't do much worse and if he goes crazy in there, start shipping features, then I think that's that's perfect because it's a project, you know, the quality is bad, you can't do much worse.  
   
 

### 00:54:36

   
**Andrei Marinov:** So yeah, I feel like that kind of a project would be perfect for this situation where at the end you don't really care about the quality of the  
**Filippo Tosetto:** But for me there is a problem here which is if we're doing this exercise to help speed up you know releasing UI features for instance in all our apps we cannot leave the POS doing that this by themselves. We need to set guard breaks. We need uh developer advisors time to check the PRs that they are not breaking the CI as we have seen. They're not using obsolete, you know, coding practices. Come on. We are using a sync weight everywhere in the app. Why are we going back to closures, you know, for for a sync  
**Andrei Marinov:** We're not but we want to start using it and the code base currently isn't good but  
**Filippo Tosetto:** work?  
**Andrei Marinov:** we want as we work on features to improve the code base where current is just following what's already there which is no  
**Filippo Tosetto:** But that's my point. That's my point.  
   
 

### 00:55:42

   
**Filippo Tosetto:** Have we set guard rails and rules? No. If we would have set those, would have it worked probably better. Anyway, don't don't worry. It's uh it was an exercise. It proved some. Okay. Um Andre, do you have any feedback? Anything uh to share? Want to share?  
**Andrei Marinov:** Uh just just got the fish guard uh play store account invitation.  
**Filippo Tosetto:** No worries. If you need any Yeah, I also asked uh access for Oscar. So, probably that will fix the problem. But please align with him and make sure that he can start to to test this up because technically we want to release this week if we can.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Nice. Thank you so much. Um, if you need anything, I'm around. Uh, let's keep a let's keep a close eye on IM mode. Uh, I really want to get product a bit more active in this app honestly because I feel that we need a bit of direction from them.  
   
 

### Transcription ended after 00:57:24

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*