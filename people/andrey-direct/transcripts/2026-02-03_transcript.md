Feb 2, 2026

## Andrey / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Hello. Hello. Hello. Hello.  
**Andrei Marinov:** Hello.  
**Filippo Tosetto:** Uh, I didn't like this guy.  
**Andrei Marinov:** I didn't like this guy either.  
**Filippo Tosetto:** He was very  
**Andrei Marinov:** He didn't want it at all. It seems like he might be great,  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** but he his interview skills are lacking.  
**Filippo Tosetto:** I'm sorry, but I'm I I don't want to work with this  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** person.  
**Andrei Marinov:** Yeah. Even if he's  
**Filippo Tosetto:** I mean, independently of his skill set is f\*\*\*  
**Andrei Marinov:** great.  
**Filippo Tosetto:** no. No, I don't want to work with this guy. Um, also he has four weeks notice, which for us is a nogo. So, uh, let's hope this other guy is good. Fingers crossed.  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** Okay, Andre, let's talk about a few things.  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** I'm I'm gonna actually Why don't you start and tell me about the WWDC uh thingy that you've been on Friday?  
**Andrei Marinov:** Uh it was kind of like the the sessions if you watch the sessions from WWDC but it's the it's live the guy is talking to you.  
   
 

### 00:01:22

   
**Andrei Marinov:** Uh but it's a lot of the same content. uh a bit updated because they've made quite a bit of changes since they showed those. But uh it wasn't really anything concrete. It was more like here's how we feel the design should look like. Uh he went a bit into the concentricity uh of things. Uh there's this uh new APIs for doing concentricity. I don't know if you've looked at them where the UI should match uh the corner radius of the iPhone device.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** That's sort of thing.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** Um which we currently I don't think we do at all. But yeah,  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** overall it was like a a short decision session. Uh there wasn't any code or anything like that.  
**Filippo Tosetto:** Did Did you find it useful somehow?  
**Andrei Marinov:** Yeah, if you haven't watched the videos, it's quite useful to uh get behind the idea of liquid glass. And I don't think it's like anything groundbreaking,  
**Filippo Tosetto:** Okay,  
**Andrei Marinov:** but it's interesting to  
   
 

### 00:02:28

   
**Filippo Tosetto:** nice. Uh,  
**Andrei Marinov:** see.  
**Filippo Tosetto:** that is actually good. And Thursday this week, we are going to have another session which is more hands-on. I do not know exactly what to expect from that but they asked us to go with you know Xcode ready to go and the design if we have it. Uh so my view on this is  
**Andrei Marinov:** Yeah, we have the design at all. Mi said that he's working with the design team.  
**Filippo Tosetto:** that  
**Andrei Marinov:** So hopefully he pulls something through. I went into Xcode and updated a bunch of things to like support the Xcode liquid glass design, but it looks horrible. So it's not just enabling  
**Filippo Tosetto:** But that's good. I think that's already progress.  
**Andrei Marinov:** it.  
**Filippo Tosetto:** It's like guys this is what we have today. How can we reach this other level providing that the designs will arrive sometimes this week. So plus considering that we have two apps which is IMOT and AI  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** cleaner where uh Mano that they already implemented a bunch of stuff.  
   
 

### 00:03:36

   
**Filippo Tosetto:** So it's going to be 45 minutes per app. Consider probably a bit less because there's going to be a bit of chitchat before and after. There's going to be also me and Andre and uh and David Matayano. So yeah. Um but why is this happening? Let's roll back. So la last week I was in the office and Apple was there for one full  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** day and what they did was to um go family by family and give us advices on how to improve the current apps in terms of market and marketing and all of that. Um and these other weeks, these other sessions that we're doing is the same but from a technical perspective. How does this work? Usually big companies like Lite Tech uh when we when Apple is starting to to see big numbers coming through. They they want you to to start to use more and more of their frameworks obviously and  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** uh in exchange they boost a bit the apps and that is why it's  
   
 

### 00:04:51

   
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** mainly you know a  
**Andrei Marinov:** But they boost that adopt the latest uh from their ecosystem.  
**Filippo Tosetto:** bit so it's a it's a kind of um we do something for you in exchange of you doing something for us  
**Andrei Marinov:** So  
**Filippo Tosetto:** kind of situation they've been pushing a lot for foundation models, but like well do you do image generation? No. Well, then we don't care.  
**Andrei Marinov:** yeah, they're too weak.  
**Filippo Tosetto:** They know. They know. They they were not really pushing for this. They were more interested in, oh yeah, we can only do text at the moment. Do you have anything for text? And no, we don't, as far as I know. So that's it.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** So that's the story regarding um the Apple situation. But um this also brings up the Mikall uh discussion and IMO in general. I'm going to give you a lot of information right now. Uh but uh it's uh it's all connected.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** last week.  
   
 

### 00:05:59

   
**Filippo Tosetto:** Um, from my level up, we were all in Barcelona, which means all the engineering managers, uh, obviously Dar Mataniano, there were also the staff engineers there. So, Victor, Ector, and Sergio. And then there was the all the product part which means product uh PO lead, PM lead, all the PM and all the POS plus a few other people. So we're a lot of people.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** Why did we do that? because we did the QBRS which is a quarterly business review or something like that where every PM were was  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** presenting the previous quarter results and plans for the next quarter. So very interesting and you went from a very clear and uh um welldetailed plan and results from apps like eye cleaner to situation where you know the information were not that great and I'm not talking about about IMOT but other apps other families let's say um and then uh the the the family with IMOT and uh QR now uh which were presented by David uh what's the name David Nunes something like that anyway the PM which I met finally uh Diego our CEO of apps was very interested in the numbers of IMO and let me explain why because according to the PM only 35% of our apps app users are able to connect to TVs.  
   
 

### 00:07:57

   
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** Obviously, this raised a lot of questions. We're like, wait, what? We have an app that only 35% of people can use. So, this triggered a sort of um Domino's effect where and I don't know if you've noticed emails from um uh Diego on Friday or Thursday. Do you have access? Do you receive mau  
**Andrei Marinov:** I received some emails but uh which ones are you talking about in  
**Filippo Tosetto:** emails?  
**Andrei Marinov:** specifically? There was some things like AB test launches that TJO has been released. Uh I don't think you I get  
**Filippo Tosetto:** Let me show you this.  
**Andrei Marinov:** anything.  
**Filippo Tosetto:** Have you received this email?  
**Andrei Marinov:** Uh, what's the the subject?  
**Filippo Tosetto:** uh is recap on QBRS.  
**Andrei Marinov:** I think I did. Yeah.  
**Filippo Tosetto:** Okay. So if you notice here,  
**Andrei Marinov:** Yeah, I did.  
**Filippo Tosetto:** there's a a really interesting line here which says expanding connectivity on TVs in IM mode.  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** Okay, so um this is tightening together with all the discussion.  
   
 

### 00:09:21

   
**Filippo Tosetto:** So Diego is asking us to improve the current level of connectivity of the application because if 35% is just the number of users that can connect to the app that can use the app, it's not a good number and that means we can improve it. Now in the moment I heard that number which for me was totally  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** new kind of activated my spider senses and uh I started to talk with Mik. So I met Mikall face to face super nice guy and we sat down together and what we discovered is that that number is not correct.  
**Andrei Marinov:** Is it pure?  
**Filippo Tosetto:** It's it's more it's more and I need to align with Nikal but I'm going to share with  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** you. So the the data that was shared was this but we should look at in a different way which is this way. So you have the start connection from TV and the complete  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** connection and this is split by device type and as you can see the average is around  
   
 

### 00:10:42

   
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** 74%. Which is not 35%.  
**Andrei Marinov:** Yeah. That seems kind of low.  
**Filippo Tosetto:** 35% is like impossible. It doesn't make sense. So this is more uh likely but I will align a bit better with um Mikall about it. So a long story short for next quarter we need to push for improving the connectivity and the stability of the connection of IMOT iOS. That's the the long story.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** uh because now we have Diego and in general the business people that are looking at us expecting this and there is a chance that we may need to present some numbers in the next QBR which is going to be in April. So uh this is the first big chunk of work that we should start to uh put into place as soon as possible for iMote. Now on aside uh I sat down with Mikall as I said Mikall is a very nice guy is tuned on  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** this and I told Mikall there is one big problem here which is if someone opens the Jira board is seeing that we're doing nothing in this app.  
   
 

### 00:12:18

   
**Filippo Tosetto:** So we cannot have very low numbers paying two developers and having this jer board because the the the message that is coming across is that you're not giving enough work to these people and we are not ready with product improvements to get this uh done as soon as possible. Mal kind of agreed with me and it was kind of yeah but you know this and that. My perception is that is not receiving enough um information from the PM.  
**Andrei Marinov:** Yeah, I'm on the product side.  
**Filippo Tosetto:** Yeah. So I was okay that's not a problem. I'm just going to put a monthly meeting between us, me, youre and the and Davidit uh the PM. So we align on the next things to do and I will be pretty pushy on that meeting. I just want to explain this because I feel that we have two well right now we don't have two but we are supposed to have two developers which we are paying a lot of money and we are not using them as expected.  
   
 

### 00:13:36

   
**Filippo Tosetto:** Question to you is my perception right?  
**Andrei Marinov:** Yep, that seems right to me.  
**Filippo Tosetto:** Okay. So I will push from a product perspective to have things done Jira board ready estimation done uh put more user stories more more more we need to use these people as much as possible but also we need to use these people in the right direction. So it's not about you know okay let's implement liquid gas. No we have a real problem which is connectivity. Let's put our forces there and fix this. So let's uh wrap up by saying how do you see this challenge going? Is there a chance that we can build in my head I have few uh points here. Is it going to be about dropping connect SDK and building our own solution? Is it how do you see this this moving forward?  
**Andrei Marinov:** Uh it's probably not due to the connect SDK. Uh seeing that the starting of the connection is mostly okay. Actually I don't know in that funnel whether we have something before that because obviously starting of the connection you you started every time.  
   
 

### 00:15:03

   
**Andrei Marinov:** Uh which was the the bar that was the lowest the 53% which which device was that?  
**Filippo Tosetto:** Uh let's go back.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Uh let me show  
**Andrei Marinov:** T.  
**Filippo Tosetto:** you this one. Ten  
**Andrei Marinov:** Yeah, it's the the Samsung TVs.  
**Filippo Tosetto:** Tyson.  
**Andrei Marinov:** Uh, that's a weird one because for Samsung we use WebRTC. Yeah, we'll definitely have to check what's up with that. That seem that's very low.  
**Filippo Tosetto:** So do you think that improving this connectivity is something that is actually feasible for this outcome?  
**Andrei Marinov:** Well, if it works one of two times, definitely. I mean, people were paying for this and it only works half the time. That doesn't doesn't seem right.  
**Filippo Tosetto:** Okay. Interesting. Because I tested the app the other day and works perfectly on my TV. It's a Samsung.  
**Andrei Marinov:** What kind of do you have?  
**Filippo Tosetto:** It's a Samsung.  
**Andrei Marinov:** Does he have Tyson like  
**Filippo Tosetto:** No idea. What's that? Is it an OS specifically?  
   
 

### 00:16:14

   
**Andrei Marinov:** Android clone?  
**Filippo Tosetto:** How can I check that?  
**Andrei Marinov:** It probably does, but I don't know. Somewhere in the the menus of your TV or  
**Filippo Tosetto:** And I should I should find Tyson somewhere written.  
**Andrei Marinov:** Yeah. Or if you Google your TV, I know that recently they updated their uh their like version of  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** it because they released TVs like last month.  
**Filippo Tosetto:** Mhm.  
**Andrei Marinov:** So yeah,  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** when when is that from three days ago? Okay.  
**Filippo Tosetto:** Let's refresh.  
**Andrei Marinov:** Is that like launch?  
**Filippo Tosetto:** Now, this is from 1 minute  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** ago.  
**Andrei Marinov:** But is that throughout last week, last month? Okay.  
**Filippo Tosetto:** Uh,  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** last 30 days.  
**Andrei Marinov:** Yeah, that's interesting to see.  
**Filippo Tosetto:** What we can do is to reduce this for a second to last seven days. And it goes down a bit actually. Interesting.  
**Andrei Marinov:** Yeah, we'll definitely start here. Look at uh the lowest one.  
   
 

### 00:17:26

   
**Andrei Marinov:** Start iterating on that.  
**Filippo Tosetto:** Yeah,  
**Andrei Marinov:** Maybe add more logging into the app to see where it fails for users.  
**Filippo Tosetto:** I mean Rocku is the best one. Interesting.  
**Andrei Marinov:** That's interesting because with their update recently,  
**Filippo Tosetto:** Okay,  
**Andrei Marinov:** they kind of stopped us from being able to stream.  
**Filippo Tosetto:** that's why I'm saying that's interesting. But again, I need to check with ML that this data is actually what we are looking. I mean, it's it's what we care about. So, I want to align with him. Okay. All right. Okay. So, um plan for this quarter is uh sorry, there was another point that was um discussed during the QBR that I didn't like. Uh which for me was simply using the wrong words to describe what we are actually doing. So um the PM told the the old board that what we are doing in IM mode is refactoring. I think there's a huge distinction between refactoring a piece of code and do some technical improvements.  
   
 

### 00:18:52

   
**Andrei Marinov:** But we're only refactoring because we don't have things to  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** do.  
**Filippo Tosetto:** f\*\*\*\*\*\*. This is very bad. Okay. No worries.  
**Andrei Marinov:** Said tvOS support that was like the big thing past couple months.  
**Filippo Tosetto:** Andre, um, regarding tos, has anyone checked that this is okay with Apple?  
**Andrei Marinov:** I have no idea. I assume so.  
**Filippo Tosetto:** Okay. Because in the meeting with Apple, they were like, "Oh, yeah. Yeah, we're going to release the ts compatibility now. And the people there from Apple were like, "Huh, have you already submitted for review?" No. So there was kind of this question mark there. H let's see. Let's see. Hopefully hopefully it's okay.  
**Andrei Marinov:** All right, it's fine. They're They're not going to see it unless someone like flags it.  
**Filippo Tosetto:** Okay. Okay.  
**Andrei Marinov:** There's no way they're going to test that.  
**Filippo Tosetto:** Okay. All right. Uh so long story short, I want to uh sit down with um the three of you on Wednesday actually um and discuss on what we're going to release going to work on as soon as possible to improve the current Jira board to stop working on refactoring and start to producing very meaningful work Because the message that the board is receiving is  
   
 

### 00:20:31

   
**Filippo Tosetto:** that we are just oh you know we're just refactoring because we cannot improve we cannot add more features because we need to refactor.  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** That's not correct.  
**Andrei Marinov:** that's not right.  
**Filippo Tosetto:** Okay. Good.  
**Andrei Marinov:** It's the reverse actually. We're refactoring because we can don't know what features to  
**Filippo Tosetto:** Yeah. This is exactly what I told uh Mikah. I was like, dude, I'm okay with that, but we need product to push for things. It's not that we can I mean, yes, we can refactor forever, but this is not going to improve the app. Okay, let's close this discussion with something that I'm not really happy about, but um let's see. One of the late motive throughout the QBRS is that we need to be faster. We need to be faster delivering new features. We need to be faster with our tests. We need to be faster in general to do things. Obviously, as you know, um there's the beautiful um conception that now everyone can code, everyone can write a piece of software because AI allows us to do that.  
   
 

### 00:21:59

   
**Filippo Tosetto:** So just use cursor uh code whatever you want and in half an hour you have a beautiful app. As we know the story is not that simple. So Mataniano managed to shield us a bit from this situation but we still need to work on a sort of P. So let me explain. We have uh Christian which is the CPMO uh the chief product marketing officer. We have another head of martekch that they want POS to start to use cursor or whatever tool to develop UI features. I'm not seeing your face, but I can imagine your face right  
**Andrei Marinov:** No,  
**Filippo Tosetto:** now.  
**Andrei Marinov:** you're you're exactly what how how I mean  
**Filippo Tosetto:** Exactly. I I I know I know everything that you're thinking and we know that this is wrong. Somehow there is the wrong message. There is the wrong narrative behind this. But it doesn't matter. What we want to prove is that we are okay doing this and uh we are going to we need to own this as in engineering so we can shape it in the right way because if we don't own it someone else in the company is going to own it and this message that can do whatever is not going to go down well.  
   
 

### 00:23:43

   
**Filippo Tosetto:** So I rather grab this and start to shape it as we want before it becomes a monster. Which brings up the last point where you are going to be involved which is the following. Uh Mataniano suggested that this experiment should run on one single app for a very limited amount of time. Okay. And this app needs to have a developer advisor because the developer advisor is the person that can assess if the code produced can be merged to production or not. You can stop me whenever you want.  
**Andrei Marinov:** I know what the app is. Is that it?  
**Filippo Tosetto:** So the app is IMOT and uh the  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** the idea that Mataniano has is the following. The developer advisor needs to help the PO to set up the environment and to set up cursor with rules so that the PO can write whatever it wants in the prompting part and it gets some results which means the developer advisor will also need to spend time explaining and teaching the PO. how you know Xcode works.  
   
 

### 00:25:16

   
**Filippo Tosetto:** How can I prove that whatever I'm building is actually running on a simulator at least?  
**Andrei Marinov:** Does Mi have a Mac  
**Filippo Tosetto:** Correct. That's something else. That's one step at a time. Let's first define the the scope and then we discuss about all the constraints around it. Um my idea is not my idea um Matiano's idea is that you Andre spend a maximum of two hours a week working on this PC helping ML to do the stuff which doesn't mean though this is the the fine line you can help with the setup you can help with explaining how to run the app in the simulator later, but you do not do the work. You see the difference?  
**Andrei Marinov:** Okay. So, I just hold his hand and tell him what to put in and then review  
**Filippo Tosetto:** No,  
**Andrei Marinov:** that.  
**Filippo Tosetto:** no, no, no, no. What you need to do and this is where for me this is very confusing not confusing but we need to sit down and define extremely well the scope of this is that so cursor you can put some uh cursor rules or I guess some skills I don't know how the tool evolved because it's a bit that I don't really touch it so that the person there when they write the prompt the the the tool cursor in this case will only  
   
 

### 00:26:56

   
**Filippo Tosetto:** touch UI stuff and doesn't break other things. Question is this  
**Andrei Marinov:** Uh, no. I mean,  
**Filippo Tosetto:** possible.  
**Andrei Marinov:** how can you write only UI stuff without like providing the data for the UI? Let's say that you fetch something from the network and you have to present it. You can't just write the UI part.  
**Filippo Tosetto:** So the idea here is to get a very very  
**Andrei Marinov:** You have  
**Filippo Tosetto:** very very simple use case which may not even be real like change the position of this button or this button is to become red.  
**Andrei Marinov:** Okay. Yeah,  
**Filippo Tosetto:** So very very stupid and  
**Andrei Marinov:** we can do that, I guess.  
**Filippo Tosetto:** simple because you're going to spend 99% of the time  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** to set up this the the the infrastructure to teach Mikall how to run project and to do all the the the the basic things before even starting to write a line of This is my impression. As I said, I'm not very happy about this. But if we create the right environment at least we can tell the correct narrative behind this which is POS will need the time invested to train a PO and to set up the tool to do some basic things can be probably you can reduce it to you know not even half even less if you Andreas sit down with Mikall and in two hours  
   
 

### 00:28:48

   
**Filippo Tosetto:** you create the feature that he wants to build because you have the the technical knowledge to do it. So I'm still trying to find the best way to handle this.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** What's your real  
**Andrei Marinov:** I mean,  
**Filippo Tosetto:** perception?  
**Andrei Marinov:** the the AI models currently suck for UI work quite a bit on iOS. Uh they're great for like web,  
**Filippo Tosetto:** Good.  
**Andrei Marinov:** but on iOS they're not that great.  
**Filippo Tosetto:** Good.  
**Andrei Marinov:** And uh cuz for example, if like Miho goes in and tells it to make this button be something or implement this design, it's most likely going to go to um it's going to start with Swift UI, but then might mix in UI kit in and then all of a sudden it's it's not looking goodwise. I  
**Filippo Tosetto:** For me, this is perfect.  
**Andrei Marinov:** think  
**Filippo Tosetto:** This is perfect. This is exactly what we need.  
**Andrei Marinov:** we do. We are. We do.  
**Filippo Tosetto:** What I'm how I'm framing this is that it's going to be a four weeks experiment.  
   
 

### 00:30:07

   
**Filippo Tosetto:** The first week is about, you know, setting up things and getting Mikall on board on how to use Xcode to build and and this and then you Mikall will have two weeks to do his own things and he can ask you questions. You can sit down for a per coding where you can help him a bit. But the point here is that I'm not against this but I'm not pro this what we need to do to go there is with the expectation that this can go in both ways and the outcome needs to be uh binary is this going to is this PR going to be merged into production meaning the code produced is good meaning PO's can start to do this or no this PR cannot be merged into production because of all these reasons. So I'm not here to say we need to make this succeed but not here to say we need to make this fail.  
**Andrei Marinov:** it. Yeah.  
**Filippo Tosetto:** It's it's just a scientific approach here.  
**Andrei Marinov:** Y  
**Filippo Tosetto:** I don't want to you you know what I mean?  
   
 

### 00:31:25

   
**Filippo Tosetto:** It's more like you want to do it totally fine. Happy to help. This is the the constraints we want to implement because they they already started. Yeah. But because we could start to use uh uh we could do two different scenarios. One implement a totally new feature and the other one uh to do some debugging. Like yeah, you're asking a PO to do debugging. But so I'm I'm I'm trying to direct the energies towards one simple example which is change the color of this button.  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** Just saying right now.  
**Andrei Marinov:** I think it will work for that.  
**Filippo Tosetto:** But but but that's good because okay we can change the color of a button but when we need to move the button from the bottom to the top that doesn't work. So why doesn't it work?  
**Andrei Marinov:** I'm just wondering like which story is he going to pick up to to work with on this? I mean, we don't really have stories to change colors of buttons.  
**Filippo Tosetto:** I don't think it will pick something that is already in production.  
   
 

### 00:32:48

   
**Filippo Tosetto:** And bear in mind that I do not know if Mikall knows about this  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** yet  
**Andrei Marinov:** it's going to ask about that. And does this even have a Mac?  
**Filippo Tosetto:** because No, he doesn't have a Mac.  
**Andrei Marinov:** Oh, how's he going to manage that?  
**Filippo Tosetto:** Yeah. But but this is you know for me this is an experiment and we need to be very scientific about it. It's not about we engineers know better than you. We this thing doesn't work because we know better. is more guys this today we cannot do that for this and this and this and this reason and we need to go there with proof and that's why I'm I'm okay I'm relaxed I'm going to create a plan this week before agreeing with anything I want to run this plan through you first of all I want to align with Mika see if he's actually aware of what's happening and once we are okay with this maybe I'm going to share it with the rest of the people.  
   
 

### 00:34:08

   
**Andrei Marinov:** Yeah. Okay.  
**Filippo Tosetto:** So also and this is for me the most important part in all of this discussion. Andre will help Mikall set up the tools and teach him how to run an app in in Xcode. Andre will not do the work because if Andre does the work it will succeed and the the point here is not about the final result is about the process. Okay. Sorry for this uh very long explanation.  
**Andrei Marinov:** No, I got  
**Filippo Tosetto:** Um that's it regarding this point. Um, do you have do you think we can create a sandbox environment? Let's say that Mikall is going to get hold of a Mac. Do you think create is possible to create a sandbox environment for him to use cursor or what are the the problems that you foresee?  
**Andrei Marinov:** uh sandbox. Do you mean like uh setup rules so that he doesn't mess up anything more than he has to?  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** Uh not sure about that. I mean even if you set approves if you're very insistent the model will just do what you say.  
   
 

### 00:35:40

   
**Andrei Marinov:** Uh, so it's not like going to be 100% proof, but I'd be very interested to like set it up and see how far along he goes and what the result is. I'm not like super confident, but yeah.  
**Filippo Tosetto:** I'm not confident either, but I think it's a good it's an interesting experiment in my opinion and maybe the outcome is not what they are expecting, but something that we can use anyway.  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** Let's see. Let's see.  
**Andrei Marinov:** I'm just wondering which stories would be up for grabs for uh this sort of work cuz we rarely have a story that's that simple.  
**Filippo Tosetto:** That is a product problem. It's not our problem.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** Meaning that we set up the technical side. It's up to them to pick up something that is manageable for them. even if they need to, you know, start from scratch, come up with some stupid idea that is not going to be merged into production, but at least the code produces good. So,  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** okay, what I'm going to do now is I'm going to create a chat, me, you, Mikall, and Fernando, and maybe set up a call sometimes this week.  
   
 

### 00:37:06

   
**Filippo Tosetto:** Um my plan is to come up with some technical constraint. So a well-written plan for this technical constraint. Share with you and discuss this with the other two and see where we are at.  
**Andrei Marinov:** Sounds  
**Filippo Tosetto:** Nice. Okay.  
**Andrei Marinov:** good.  
**Filippo Tosetto:** Um a couple of words on IMO Android. I already explained before but I just want to reiterate a bit. Um, Cichlum is walking on thin ice with us and most likely they're going to be they're going to be brainwired if you know what I mean.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Uh, so the situation with IMO Android is that they keep wanting to release an app that has some major bugs. So let alone the technological issues that we have, the app has some major bugs that Oscar is flagging. Their internal QA is totally useless. But sooner or later, most likely this week, we will be able to approve this app and put it in the store. What's going to happen afterwards? I am fighting very hard for this app to be merged with the iOS part.  
   
 

### 00:38:30

   
**Filippo Tosetto:** Why? Because otherwise it's just going to duplicate work for everyone because Yeah.  
**Andrei Marinov:** It would be nice if Mikaw is on it as well. Yeah.  
**Filippo Tosetto:** So the only person that will differ between the two teams will be the PO because there's going to be I'm planning to share the external QA as well because I know that the guy is very good and he will have access to the devices. The Android developer will come from Anadada and uh Rafa from procurement is getting uh gathering um CBS for us to to check the the internal QA is Oscar which is internal. You are going to be in both projects. So literally the only person that is not going to be uh the only um uh skill set level that is not going to be the same is just going to be the PO which for me is a massive waste because you're going to spend time double the dailies double the sprint review and all of that. So I'm fighting for it but there is a chance that this app is going to be split between growth and launches.  
   
 

### 00:39:41

   
**Filippo Tosetto:** I find it stupid. It doesn't matter said that. Let's see how it goes. Just wanted to make you aware of the situation.  
**Andrei Marinov:** Okay.  
**Filippo Tosetto:** Okay. Um, screen mirroring, you don't worry about that. It's not going to be with you. It's most likely going to be with the uh new a new dev advisor that I'm hiring. But just speaking between me and you, what I'm seeing is that the apps IMO and Screamering are sharing a lot of functionalities.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** So what about creating a a package that we can share between the two? just throwing this out there because at least the discoverability  
**Andrei Marinov:** Yeah, that makes sense.  
**Filippo Tosetto:** part it's going to be for both. Uh so I don't know uh this is something that came up like literally today. So this is an idea that maybe we can discuss in the future finally.  
**Andrei Marinov:** Yep. Maybe even maybe even do like a cotlin multiplatform thing  
**Filippo Tosetto:** Sorry.  
**Andrei Marinov:** and have it in Android as well  
   
 

### 00:41:03

   
**Filippo Tosetto:** Would that  
**Andrei Marinov:** probably.  
**Filippo Tosetto:** work?  
**Andrei Marinov:** I don't know. I was thinking about it today but needs some experimentation.  
**Filippo Tosetto:** But isn't it going down to the hardware? So you would need to anyway to wrap the OS specific API  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** calls but  
**Andrei Marinov:** possibly it was a thought. Yeah.  
**Filippo Tosetto:** we need a good Android developer then.  
**Andrei Marinov:** Yep.  
**Filippo Tosetto:** Okay. But you just gave me some very interesting bullets I can use. What kind of functionality would we need beside discoverability? the  
**Andrei Marinov:** I the whole web RTC and um what was it  
**Filippo Tosetto:** waste.  
**Andrei Marinov:** called? HTTP ERC I believe it was for one of the platforms that sort of thing to be wrapped up.  
**Filippo Tosetto:** What's your  
**Andrei Marinov:** Okay. So, H ECP and HTTPS smart  
**Filippo Tosetto:** SoPS? Yes.  
**Andrei Marinov:** cast.  
**Filippo Tosetto:** Okay. But what's your view on building our own discoverability um  
**Andrei Marinov:** Uh well,  
**Filippo Tosetto:** framework?  
**Andrei Marinov:** if it's the other one is abandoned, we'll pretty much have to do it.  
   
 

### 00:42:45

   
**Andrei Marinov:** But we can also maybe look into it and see if we can improve it a bit because it's open source. just fork it. And  
**Filippo Tosetto:** Oh yeah, that will make  
**Andrei Marinov:** we need to look at the code first obviously to see how bad it is or not not as  
**Filippo Tosetto:** sense.  
**Andrei Marinov:** bad because I believe it the whole thing is written in Rust and then it's like uh for each platform they do like a wrapper briefly from what  
**Filippo Tosetto:** It's written in rust.  
**Andrei Marinov:** I saw I think that was the case. Yeah.  
**Filippo Tosetto:** Maybe you can create a wrapper first of all that can be shared. So we expose some API that can be shared but it can be used by different apps but then the core can be reritt in the core. We use connectivity connect SDK for the moment but then we slowly remove it by adding our own implementation over time.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** So the the apps are dependent on this common SDK that we build and then we have a team working only on the SDK.  
   
 

### 00:43:59

   
**Filippo Tosetto:** Interesting.  
**Andrei Marinov:** Yep,  
**Filippo Tosetto:** Interesting. This could be a very interesting project.  
**Andrei Marinov:** I  
**Filippo Tosetto:** Nice.  
**Andrei Marinov:** agree.  
**Filippo Tosetto:** Uh let's close this discussion with AI design.  
**Andrei Marinov:** The most fun part slowly making  
**Filippo Tosetto:** is it? No, it's it's okay.  
**Andrei Marinov:** progress  
**Filippo Tosetto:** Yeah, that's the slowly part that I don't like. Um well, we have seen tomorrow. We're going to have an interview. Uh this week we're going to have a few interviews with this uh people and  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** um let's see let's see my idea is to remove salmon  
**Andrei Marinov:** Yeah. Hopefully we find someone cuz he's uh he would say he's the one that's  
**Filippo Tosetto:** sorry  
**Andrei Marinov:** slowing things down the most.  
**Filippo Tosetto:** he is and I can tell you that now I'm working with in two different project that twist and face AI with two you know normal bean developers uh the Chinese guy and another one um and it's a pleasure to work with these people because they they explain things but they are also for sure faster in their solution so I'm not looking for a machine learning engineer here because for that we have face an AI lab doing this kind of things.  
   
 

### 00:45:36

   
**Filippo Tosetto:** I'm just looking for a smart backend developer that can use the information given by AI lab and can implement them. So there is no rocket science. Let's see tomorrow regarding this  
**Andrei Marinov:** No,  
**Filippo Tosetto:** interview. I think that's it. I'm thinking yes.  
**Andrei Marinov:** sounds good.  
**Filippo Tosetto:** Um, regarding the rest of the team for AI design, depending on the conversation with CClum, uh, we'll see. But for me, once we sorted out what we have in running right now, for me, those two guys are the next two to go because we cannot work with  
**Andrei Marinov:** Yeah. The version number it beat you as well.  
**Filippo Tosetto:** I'm very confused because these guys are advancing the application. So I cannot complain about their productivity.  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** So how can they be producing this work if they're not good enough?  
**Andrei Marinov:** a lot of it is AI generated. It's kind of like the uh we already know where Mihow Pipe coding things will take us because we see it with the SQL people.  
   
 

### 00:47:16

   
**Filippo Tosetto:** Well, it's not bad if you think about it, though. No, maybe. Okay. Okay. Um, all right. Uh, I'm going to talk to Matiana tomorrow about replacing these two guys as well. Uh, but most likely is going to disappear anyway. So, let's see.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** I talked most of the time. Sorry for that. I just wanted to give you a lot of context and a lot of status after my trip to Barcelona.  
**Andrei Marinov:** Yeah. No, that's good to catch up.  
**Filippo Tosetto:** Yeah. Anything on your side you want to  
**Andrei Marinov:** Uh, no,  
**Filippo Tosetto:** share?  
**Andrei Marinov:** not really. Nothing comes to mind. We covered all of the  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** stuff.  
**Filippo Tosetto:** Uh perfect. So just to let you know main focus for me for this quarter for now would be most likely IMOD uh you  
**Andrei Marinov:** Man.  
**Filippo Tosetto:** know improve connectivity uh do this PC with Mikal sit down with the product people to push for some product announcement instead of us just you know reviewing and refactoring code and especially changing the narrative where well we cannot do any  
   
 

### Transcription ended after 00:49:06

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*