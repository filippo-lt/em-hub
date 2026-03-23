Mar 17, 2026

## Andrey / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Andrey Marinov:** Hello.  
**Filippo Tosetto:** Hello.  
**Andrey Marinov:** Hello.  
**Filippo Tosetto:** Hello to you. How are you doing?  
**Andrey Marinov:** Busy, busy, busy. Everyone wants to do an estimation,  
**Filippo Tosetto:** Nice.  
**Andrey Marinov:** refinement, and a planning today on all three projects.  
**Filippo Tosetto:** That's uh what happens when uh these kind of things have never been done before and everyone wants to do it in the same day because now that's part  
**Andrey Marinov:** Yep.  
**Filippo Tosetto:** of the metrics for uh uh leads lead people uh like POS PMs uh us you so that's why everyone is super busy that oh we estimates for user stories everything u I'm not going to keep you uh too long  
**Andrey Marinov:** Yep.  
**Filippo Tosetto:** then because I know I know this kind of things is are annoying but um Andre tell me what's your feedback after the meeting on Friday for the AI transformation  
**Andrey Marinov:** Well, if it works out like they say, it's going to be like what they say really agent engineering and the next step of how software development is done, that sort of thing. But I feel like it's more likely that we become more of a white coded thing.  
   
 

### 00:09:03

   
**Andrey Marinov:** uh especially with uh I'm I'm not convinced that uh if I don't know Android that well and I just use skills and rules I'll be able to produce code that someone who knows Android very well and uses AI will be able to um so yeah I raised that concern then on the meeting but I also don't agree that some of the the weaker modules uh models and now today that we can't use the other ones ones. Uh, sure the other ones are a bit more snappy, but they're and they seem like smart, but they're not as smart. And in this space, uh, it doesn't really make a lot of sense to try and use the other models when smarter models will get you where you want to be. I also don't agree with the thing where you plan everything with one model and the other one just executes it. uh because when you plan it, you don't plan it to exactly to write absolutely this function and this parameter and whatn not so that the other code will just transcribe it and make sure it compiles.  
   
 

### 00:10:14

   
**Andrey Marinov:** Uh so yeah, I have some like doubts, but it's it's uh there's potential for for people to just be able to work at it and be able to um I don't know to succeed, especially with models that get smarter and smarter. So I imagine that by the end of the year, some of my concerns won't be valid at all. And yeah, let's see.  
**Filippo Tosetto:** Um, thanks for the feedback. I I agree with some of your points. I agree with some of your points and uh I what I've uh learned by doing this experimentation in the last couple of weeks is that we still don't know enough. That's my impression. uh and uh no one has the truth right now in in the hands. So everyone is has his own opinion based on his experience. So um as I said I I partially agree with some of your points.  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** Probably I may agree with others but I haven't faced them yet. So I I second what you say. Absolutely.  
   
 

### 00:11:29

   
**Filippo Tosetto:** Um,  
**Andrey Marinov:** I think that some people will really succeed with this approach and really be good at it and others won't be as good at at it and maybe people will think that it's their fault. But maybe they just don't follow or follow too closely the way that we've specified. I don't know if that makes a ton of sense, but uh since it's not that deterministic, it's hard to say that you're misusing AI in a certain way and it's your fault. But I do think that some projects will be very very successful in this approach.  
**Filippo Tosetto:** What do you think? What what could uh make fail some of the project or people?  
**Andrey Marinov:** uh the thing where they don't uh obsess as much over the the structure and recently I've been reading up and it's more like uh it really accelerates you now but uh the the payoff for that is that you accumulate a lot of debt later on like in six months it's it'll be way worse. So you got to basically either start over or drudge along in this mess that you've created.  
   
 

### 00:12:44

   
**Andrey Marinov:** So uh planning for that I feel like it'll be uh and be very mindful of how you structure your code and be very on top of it even though you don't write it. That will be the crucial piece of this thing because now we'll start and suddenly everything will accelerate quite well and then in six months we might be up against the wall on some of the projects. But let's see.  
**Filippo Tosetto:** Um,  
**Andrey Marinov:** I might be wrong.  
**Filippo Tosetto:** who knows? Honestly, who knows?  
**Andrey Marinov:** I think that as new models come come up and they come up like every month,  
**Filippo Tosetto:** That's  
**Andrey Marinov:** they'll be able to better compensate for that. So,  
**Filippo Tosetto:** Yeah.  
**Andrey Marinov:** uh, like if we stay at this level, that's probably going to happen. But since they get better and better, uh, we might get away with it.  
**Filippo Tosetto:** I've done an experiment in this weekend. Um because my I need to understand the mindset the the the flows and everything as a manager even though I'm not going to be the one building the whole thing.  
   
 

### 00:13:51

   
**Filippo Tosetto:** So for me was it's pretty important to be hands-on at the moment to understand all of this and I started to to play a bit the V coding parts like build an app that does this and I realized that very very soon you you accumulate technical debt you don't understand whatever you're doing and the model started to hallucinate etc. So I found that creating a flow, a workflow, it's much more important than the code itself. Um, so I'm I'm starting to to work on that. And I think this should be we need to find a way to to codify the the good workflow so that the developers instead of focusing on telling the AI which class to touch, they are more focused on which features to develop and how those features technically should be developed. So I'm I'm I'm getting my head around this concept. I'm I'm playing around. I've done a a very stupid web app uh sort of capacity planning web app and uh I realized very soon that you know the first three four five features all good and then the model start to I wouldn't say hallucinate but it slows down and this things are not going as expected.  
   
 

### 00:15:27

   
**Filippo Tosetto:** So it I find it very very fascinating and very interesting. Uh and I agree with you. Um today there's a lot of talk about rewriting from scratch the apps that Brain buyer built for us. But who's checking the code that AI writes so that we don't end up in the same position in six months? Yeah, your point. Exactly your point. Um but I I still find it very interesting. It's um I think it's way forward to what uh we were doing and uh I'm excited that the company is providing us the tools and uh possibility to learn about this.  
**Andrey Marinov:** Yeah, I agree. But after today's cursor thing where we no longer have access to like the top tools, are they  
**Filippo Tosetto:** That's a very question. Good question. I don't know. I don't know. Um, I'm also I'm also considering what you said few weeks ago regarding a gentic coding with code or codeex versus using cursor and I start to see the difference that you explained to me and uh but it's a learning curve.  
   
 

### 00:17:02

   
**Filippo Tosetto:** I'm as I said I doubt in six months we will still have the same uh tools that we are using today because we have been evolving and learning this kind of things. Today is just you know there's a lot of chatting around until we start to get our hands dirty. I doubt we we have a a strong opinion on  
**Andrey Marinov:** Yeah, like for example, even like three months ago,  
**Filippo Tosetto:** things.  
**Andrey Marinov:** uh the models at the time, if you would go and tell it to add a file to an export project, they couldn't like find and edit the proper way in the whole XML project file, but the the horror and the hell that it is that file, they couldn't do it. So, you had to do it yourself. But like these days, they manage it just fine. So yeah, that's a an example of how they get better and better and I imagine in six months it'll be completely different. Currently they suck a lot at UI.  
**Filippo Tosetto:** Yes.  
**Andrey Marinov:** I've been trying different models to and to make them write good UI for me or UI that works.  
   
 

### 00:18:09

   
**Andrey Marinov:** They just can't. They fail at it.  
**Filippo Tosetto:** But do you do you have set up a feedback  
**Andrey Marinov:** Uh yeah, I have it where I have logs and they  
**Filippo Tosetto:** loop?  
**Andrey Marinov:** log out to OS log and I have uh on the simulator there's this uh axe tool, COI tool that goes through and basically clicks through elements on the the simulator and I try to get those uh three to work together so that when it executes it, it goes and sees what it's done. Uh but for whatever reason, it says like, "Yeah, that that looks fine to me. That's that's what you gave me. And it's not doesn't it doesn't work. More importantly, things like animations or interactions don't work as they should. But it gets you like 90% of the way there. I mean,  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** it creates everything. You can just glue it together and it works.  
**Filippo Tosetto:** But this is good feedback because your point regarding I do not know how to write Android. Well, 90% error is not 100%.  
   
 

### 00:19:20

   
**Filippo Tosetto:** So, if you don't know Android, how can you fix the last 10%.  
**Andrey Marinov:** Yeah, I don't know. I haven't written Android yet.  
**Filippo Tosetto:** But it's it's good.  
**Andrey Marinov:** So with AI2, so might be easier.  
**Filippo Tosetto:** It's good. I I Yeah. Who knows? Who knows? Okay. Um, how are you using these tools today?  
**Andrey Marinov:** Uh, like in what way?  
**Filippo Tosetto:** I mean, are you starting to to work with them? Are you starting to produce  
**Andrey Marinov:** Oh, yeah.  
**Filippo Tosetto:** code?  
**Andrey Marinov:** I've only worked like that since last September  
**Filippo Tosetto:** Yeah, but I mean I mean for for Litech and and the projects you're involved  
**Andrey Marinov:** basically. Also that as well.  
**Filippo Tosetto:** on.  
**Andrey Marinov:** Uh, so recently on my mode we implemented locks for uh trying we're trying to solve the connection issues.  
**Filippo Tosetto:** Yeah.  
**Andrey Marinov:** also implemented crashing logs. So it's know it's very easy to just plug in logs into whichever tool and they can uh usually find out what's wrong with what happened or uh try and recommend like uh ways to retry or try and save the the connection rate.  
   
 

### 00:20:32

   
**Andrey Marinov:** Uh but to your point actually I started working at the um common library for that would uh  
**Filippo Tosetto:** Nice.  
**Andrey Marinov:** replace connect kit and it's pretty much done.  
**Filippo Tosetto:** What do you mean? It's pretty much  
**Andrey Marinov:** Uh so yeah it's now called TV foundation kit.  
**Filippo Tosetto:** done.  
**Andrey Marinov:** Uh,  
**Filippo Tosetto:** Yes.  
**Andrey Marinov:** it's on the resetter and I integrated it into both IM mode and uh, screen ring as well. I tested out IM mode. I tested it out on my Tyson TV. It works great. And on my Apple TV, it also works there as well. And it gets rid of connect SDK of some open cast and Google cast SDKs and other stuff. And uh yeah, I'll probably send out a bill to Lexi. Let's see if he can tell whether there's a difference. So it took it like two days to write it out. Uh there's like this is the execution plan of what we decided on how to implement it. This is actually the execution plan.  
   
 

### 00:21:41

   
**Andrey Marinov:** It's not the plan plan. Uh there was another plan. I might have to uh get it in there as well. This is what it did and how it did it was out of scope at the moment like Android TV. I don't have that one so I didn't bother with it. Uh this actually replaces connect kit as it scans and connects to the devices but the actual uh control of the devices is still within what we had previously.  
**Filippo Tosetto:** Yep.  
**Andrey Marinov:** And uh there's some DNA stuff that we changed as well, but uh uh it could be better on some of these things. Uh so yeah, it took a couple of days to talk to it and to write it out. I feel like uh there's now tests for it, which is great. Uh I feel like it did a good job. It's a Swift 6\. guys all the sentable stuff that we need use actors liberally when we have to uh and I looking at the code I feel like it's written of pretty good code and yeah so when I went to test it out first off there was one crash which it immediately fixed and then there was two bugs that I noticed but we managed to fix those as well and yeah I was still trying out yesterday because wrote it in two days but took me a week  
   
 

### 00:23:08

   
**Andrey Marinov:** to set up the IMO provisioning profiles and whatnot between meetings and so on. Uh so yesterday I was finally able to sit down and test it with my TV and my Apple TV and all worked great.  
**Filippo Tosetto:** I'm right.  
**Andrey Marinov:** I'm not a big user of IM mode,  
**Filippo Tosetto:** This is  
**Andrey Marinov:** but I'll give it to Alexi and I'll see whether uh he what he thinks whether he can tell the difference.  
**Filippo Tosetto:** But I wasn't I mean you just done  
**Andrey Marinov:** And I said it's done, but obviously I haven't tested it pretty much at all outside of my own testing.  
**Filippo Tosetto:** some  
**Andrey Marinov:** So that's like a big it's done.  
**Filippo Tosetto:** Yeah.  
**Andrey Marinov:** It's not really done, but it's a good  
**Filippo Tosetto:** But for me,  
**Andrey Marinov:** start.  
**Filippo Tosetto:** for me the connectivity SDK which you called what? How  
**Andrey Marinov:** TV foundation kit and the whole idea was to also be very interactable with screen mirroring as well.  
**Filippo Tosetto:** the  
**Andrey Marinov:** I haven't run at all screen mirroring. I don't know how screen mirroring works even.  
   
 

### 00:24:16

   
**Andrey Marinov:** So,  
**Filippo Tosetto:** but I mean I was planning for you to work on that for three weeks.  
**Andrey Marinov:** I still might have to because now this is the the tough part. Like 90% is done, but the other 10% is where it's the most difficult since I'll probably give it over to Alexi and he'll have issues to work on or true. And uh there's still some things that can be made better uh that are outlined here in the what's up next. Uh, as far as uh the Google cast and Q\&A and webOS, there's maybe the story right as well, that sort of thing.  
**Filippo Tosetto:** I'm uh you you left me speechless. Okay, let me get my head around. So this is the foundation uh library that will be used in both IM mode iOS and screen mirroring um to replace all the connectivity code and through this  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** sorry the plan is to move all the dependencies that we have today uh from all those third party um uh libraries inside this connectivity  
**Andrey Marinov:** Uh yeah,  
**Filippo Tosetto:** Um,  
   
 

### 00:25:41

   
**Andrey Marinov:** this basically gets rid of uh that's fingering. It still uses cockt file for it.  
**Filippo Tosetto:** yep.  
**Andrey Marinov:** Very annoying. Uh, but yeah, it get rid gets rid of some stuff like the connect SDK and the and the Google Cast SDK. I don't see that here for some reason.  
**Filippo Tosetto:** So you get rid of them in the app, but you actually use them in the So it's  
**Andrey Marinov:** No, no, no. Don't even use them there. Yeah,  
**Filippo Tosetto:** gone.  
**Andrey Marinov:** they're done.  
**Filippo Tosetto:** Wow. Okay, this is huge.  
**Andrey Marinov:** it uh you to look through them and see what they do and how they do it. This is the Google Cast that's no longer needed because it's integrated into this library and it technically did them. Here we have removal the connect. Oh, because it's Yeah, it was copied in manually. It's not in package. That's why it's not in the package resolved. Uh yeah, it was removed. This is the the library and it's removed from here as  
   
 

### 00:27:04

   
**Filippo Tosetto:** Okay, I need to get my head around this because I wasn't expecting this to be so sudden and so  
**Andrey Marinov:** well.  
**Filippo Tosetto:** well done. Um, could you submit the link to that repository first of all? And uh, what are the next steps for this?  
**Andrey Marinov:** testing. Lots and lots of testing.  
**Filippo Tosetto:** Okay, testing. Perfect. And in terms of new features, do you already have some ideas?  
**Andrey Marinov:** uh probably getting all the control of devices though that will probably be a separate uh package within uh TV foundation kit because at the moment like uh there's TV core discovery session uh that sort of  
**Filippo Tosetto:** Mhm.  
**Andrey Marinov:** thing more modular because for example if we introduce remote control it doesn't make sense for uh screen mirroring because it doesn't do But uh obviously I know does it uh so try and figure that part out and maybe uh I was trying to see I haven't done it yet but there's now on Android that whole that whole thing I wanted to see whether I can use this exact same library on Android and involve it from there.  
   
 

### 00:28:30

   
**Andrey Marinov:** Go to from there, but I haven't got a run that yet. I don't even have Android  
**Filippo Tosetto:** Andre and Andre this is just so  
**Andrey Marinov:** installed.  
**Filippo Tosetto:** many great news compact into 20 minutes.  
**Andrey Marinov:** Um, there's a big caveat that I barely tested it. It worked when I tested it, but I can't say it's like 100% because I did see some bugs and a crash. So, might not not be perfect  
**Filippo Tosetto:** But I'm I'm happy. It's fine.  
**Andrey Marinov:** and  
**Filippo Tosetto:** It's normal. It took you two days. Come on. What do we expect?  
**Andrey Marinov:** and there's some things that I don't like when is it here? uh where for example it's trying to figure out what kind of a device it is. It's there's a lot of uh yeah is it does it contain Roku? Does it contain Vio? Does it contain Amazon?  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** But that's the same like uh that's the same connect kit. So I imagine that's the way to do it because how would you know  
   
 

### 00:29:40

   
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** otherwise?  
**Filippo Tosetto:** Okay. Uh, very good news. Uh, quick parenthesis hardware for you. Um, most likely tomorrow I'm going to tell you move forward with the buying the devices that you need yourself and then we're going to expenses. Give me one sec, one day because um, apparently there are some of those devices in the office already. So, they are already there. It's just a matter to see if they are the one that we need. In case they do,  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** I'm going to ship it to you. otherwise going to buy them. Uh, you know, as you as you share with me, small ones that are pretty cheap. Uh, also because we don't want to fill your house with 1,000 TVs, you know. Uh, but this will leave you the give you enough for uh doing some tests at least for this. Um, Andre,  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** this is very good. you you're kind of leaving me speechless because I have I was already thinking about oh road map let's write down what we are how long it's going to take etc but you literally just done everything obviously we need testing the integration in the other apps so it's totally fine by me um would this mean that all those connectivity issues that we are having in IMOD could be solved over time obviously through  
   
 

### 00:31:13

   
**Andrey Marinov:** Uh possibly. I don't know.  
**Filippo Tosetto:** This  
**Andrey Marinov:** I don't know what the the the reason behind them is, so I can't say for sure. Uh we've just started logging them and uh yeah, I I was looking at whether there's a way to verify the logs that you get against our current code and whether the the new code fixes it. Uh but no, no results so far.  
**Filippo Tosetto:** Okay, it's fine. It's fine. Um I I will I will try to get my head around this my head around this library and then maybe we can sit down sometimes this week to define what could go next and if you want to put some documentation around it and how to do some marketing around this because this is very important for engineering and say hey AI look two days done the work that we struggle to do for months and months. Um, the next question that is going to be asked to me is great. Can Andre handle by himself I mode iOS and screen mirroring as in the two apps?  
   
 

### 00:32:24

   
**Andrey Marinov:** and screen mirroring or with AI design or without AI  
**Filippo Tosetto:** Yes. without AI design  
**Andrey Marinov:** uh then probably yeah I mean we'll define handle  
**Filippo Tosetto:** meaning.  
**Andrey Marinov:** uh work through the road map and implement all the what was on the  
**Filippo Tosetto:** Yes.  
**Andrey Marinov:** road because for example the the UI stuff uh that's going to take longer  
**Filippo Tosetto:** Yes.  
**Andrey Marinov:** because like I said they really suck at UI u the  
**Filippo Tosetto:** Do you think do you think it's going to be easier,  
**Andrey Marinov:** Nice.  
**Filippo Tosetto:** cheaper, quicker to redo it the app from scratch or  
**Andrey Marinov:** Uh,  
**Filippo Tosetto:** not?  
**Andrey Marinov:** probably not. Probably better to take what's there and uplift it because  
**Filippo Tosetto:** Okay. Okay. I'm not I'm not asking you to commit to anything  
**Andrey Marinov:** it's it'll be more incremental to the users as well.  
**Filippo Tosetto:** now. I'm just uh touching base with you, understanding your view of things. Um great, very great. I now I need to think a lot about this.  
   
 

### 00:33:34

   
**Filippo Tosetto:** Um let's say that this um Foundation TV uh uh library is working and um would you be able to simply take over from um RTM the development of IMOT you just say okay Artm thank you that's it bit of um let's say u knowledge sharing and and you will be able to work alone on that and same for screen  
**Andrey Marinov:** So, I should be able to  
**Filippo Tosetto:** mirroring  
**Andrey Marinov:** I don't know anything about the app so I can comment there but probably.  
**Filippo Tosetto:** and I'm leaving aside Android for a reason because obviously this is all to be proved first. Okay, this is very good news.  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** I may calm down the excitement for now. Um, so let's go back to the the usual way of working. Let's say I have you met  
**Andrey Marinov:** Yes. He came along today. Yesterday. Which I mode? He came yesterday for the Android eye mode and today for the normal one, the iOS one. Yes, I  
**Filippo Tosetto:** Good news is that we're going to merge the two because there is no reason to keep them separated obviously.  
   
 

### 00:35:13

   
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** Any first impression? Anything or is just they just arrived present?  
**Andrey Marinov:** So far so good. Nothing nothing major.  
**Filippo Tosetto:** Okay. He's a nice guy. I'm already working with him in face AI. um is very detailed and thorough but from a technical perspective he will need a bit of guidance because probably doesn't understand all the things but he's always very receptive and when you ask him to do something or help on something he's very on top of things. So that's my impression when it was working only on launches. Obviously in growth there's a different story there. So let's see that's it. But um yeah I'm confident uh I know we receive a bit of a bump in term in terms of processes at least maybe there are no new features to develop or not big features to develop but at least in terms of you know road map and everything else should be uh man should be on top of things. So very good. Um, how is the on boarding going with the new guys instead?  
   
 

### 00:36:31

   
**Andrey Marinov:** Uh, so far so good with uh IMO Androids. It took a really long time to get him access. I started confusing people. So, I'm not even sure whether he has it already or not because it was someone told me today, but that was in the morning and I've already forgotten. Uh, but I'll double check on that and uh I'll see whether we can bring it up if he doesn't have it because I submitted the tickets at the same time. DIA design guys got it like the next day and definitely did not have it on Friday. I'll have to double check. Uh, but yeah, the the Android guy uh pretty pretty good. The AI design guys both are disappointed  
**Filippo Tosetto:** Oh,  
**Andrey Marinov:** maybe because yeah uh I talked to them on whenever  
**Filippo Tosetto:** really?  
**Andrey Marinov:** they joined Tuesday was it or whatever and I really told them  
**Filippo Tosetto:** Yeah.  
**Andrey Marinov:** that they should uh take these first couple of days and look through the code base and uh let me know what they think um should be changed all the tech deck stuff that we usually do And uh like the Android guy said, I mean, we're really busy now with the new stories and trying to look into them.  
   
 

### 00:37:48

   
**Filippo Tosetto:** Wow.  
**Andrey Marinov:** So, I'll get back to you on that. And the the iOS guy like gave me five bullet points like really trivial. Uh nothing major. And I was like,  
**Filippo Tosetto:** It is  
**Andrey Marinov:** okay. And then at planning today,  
**Filippo Tosetto:** not  
**Andrey Marinov:** the the Android guy was I mean said, "We don't know the code base. how do you expect us to work on this or estimate it? We should get familiar with the code base. And I'm like, "Yeah, I gave you guys a task to like go through the code base and try to identify weak  
**Filippo Tosetto:** Foreign  
**Andrey Marinov:** points." And then we solidified that into a ticket for the sprint so that they can like have something to track against because like we talked on the tech alignment, we wanted to start with garden design but they were like we we don't know which pieces we can just reuse and and how to make it work and how they like work together. So yeah, they officially now have like a task to go through the code base and produce at least for me.  
   
 

### 00:38:59

   
**Andrey Marinov:** Uh so yeah, that was a bit disappointing. I was expecting like more more activity in that. Uh yeah, actually the multi guide does have G access GitHub access because he wanted some keys from me. I remember that. It's all good. Are you  
**Filippo Tosetto:** Okay. Yeah. Sorry. Okay. This is disappointing. Um, so we are not really moving forward that fast as expected.  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** Okay. Uh, it's fine. I'm going to find a way. Okay. Um I have one last question for you which is regarding AI design and the metro. How is your perception? Are you still with a doubt?  
**Andrey Marinov:** Uh still nothing from like last week. He took some time to reite the API into fast API and some other uh Python framework. Uh overall he did well the AI stuff and like some smaller issues uh but nothing major. So that's that's okay. again. still keep in my Oh,  
   
 

### 00:40:23

   
**Filippo Tosetto:** cuz it's a month that is in.  
**Andrey Marinov:** he he does work.  
**Filippo Tosetto:** Has it delivered something?  
**Andrey Marinov:** Yeah, I mean he's uh has quite a bit of PRs and he's like rewriting some of the stuff. He delivered the stuff and he's working through the garden design as well. So, he does deliver.  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** It's the how he delivers it.  
**Filippo Tosetto:** Okay. Okay. But this is good news. Uh so something is moving in that sense. It's just a matter of assigning to him the tasks. Okay. Let's hope that the mobile guys are a bit more responsive. I like to give people a benefit of the doubt is just one weekend. You're right. A bit of productivity wouldn't Yeah.  
**Andrey Marinov:** Let's see. Maybe starting  
**Filippo Tosetto:** Um just one one thing from you I need um  
**Andrey Marinov:** up  
**Filippo Tosetto:** which is the uh what is it? Performance reviews.  
**Andrey Marinov:** a few the  
**Filippo Tosetto:** I I will do it.  
   
 

### 00:41:28

   
**Andrey Marinov:** rest.  
**Filippo Tosetto:** No problem. Um but I need your help for this point. Communication, engagement, productivity for the metro.  
**Andrey Marinov:** Uh uh four I would say this one maybe  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** three and four  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** again.  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** Oh, I copied the upper row by  
**Filippo Tosetto:** Um in terms in terms  
**Andrey Marinov:** mistake.  
**Filippo Tosetto:** of general evaluation comment I  
**Andrey Marinov:** Not really. uh since I'm keeping a close eye on him due to like maybe some uh mishaps, some misses in the the code logic that were flagged that maybe should have been uh caught. But they were like if some error happens then don't lock that error at all or  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** we never know about it. that sort of thing cuz like the main stuff works but there's like could be more  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** complete the solution could be more complete or thought  
**Filippo Tosetto:** Would  
**Andrey Marinov:** out and it doesn't seem like he  
**Filippo Tosetto:** you?  
**Andrey Marinov:** AI and what I've  
   
 

### 00:43:06

   
**Filippo Tosetto:** Yeah.  
**Andrey Marinov:** seen  
**Filippo Tosetto:** So, this is going to change very soon because uh we are going to start to track how they use  
**Andrey Marinov:** yeah  
**Filippo Tosetto:** AI through cursors API.  
**Andrey Marinov:** are they going to are we going to give them licenses  
**Filippo Tosetto:** No, no.  
**Andrey Marinov:** or are they'll give us the stats  
**Filippo Tosetto:** They should get licenses for  
**Andrey Marinov:** then is going to give us the stats or are  
**Filippo Tosetto:** Yes.  
**Andrey Marinov:** people directly going to give us the  
**Filippo Tosetto:** This is this is something that I do not know and is not part  
**Andrey Marinov:** stats.  
**Filippo Tosetto:** of my tasks. Someone else will do it for us, but it's going to be very interesting.  
**Andrey Marinov:** This is very easily like gameable.  
**Filippo Tosetto:** But are there maybe there are some cursor API?  
**Andrey Marinov:** Like they give us an API key and we see their usage.  
**Filippo Tosetto:** I'm checking theation  
**Andrey Marinov:** And I saw today that we are on the legacy plan that gives you 500 requests and they have a new  
**Filippo Tosetto:** maybe.  
**Andrey Marinov:** plan that's not like that.  
   
 

### 00:44:19

   
**Andrey Marinov:** And so there will be a difference in how we use cursor versus how they use cursor.  
**Filippo Tosetto:** It's fine. As long as they are using it, I'm fine. But the fact that you're telling me that this guy is not using it, it's, you know, but it's okay. It's uh on your side. Please keep reporting these things to me and uh I will use the information as an aggregate for bigger discussions. Um overall Dimitro how would you say average below average top?  
**Andrey Marinov:** All  
**Filippo Tosetto:** Okay,  
**Andrey Marinov:** right.  
**Filippo Tosetto:** sounds good. Yeah, sounds good to me. Nice. Thank you for that. Uh, that was on my to-do list. I'm checking done. Oh, one last question. How was the Apple sessions?  
**Andrey Marinov:** Uh I had them in the background and didn't look a lot at them because I had meetings during all of that time.  
**Filippo Tosetto:** Okay.  
**Andrey Marinov:** Uh so cut some stuff but uh pretty much like uh the other thing complete with blast where they had a lot of uh a lot of D on the WWDC sessions some new things but their foundation models are very underwhelming and not worth it at all for now.  
   
 

### 00:45:54

   
**Filippo Tosetto:** Yes. Yes. For now.  
**Andrey Marinov:** Maybe next year.  
**Filippo Tosetto:** For now.  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** For now. That's it. I feel that with the speed of this field, if Appleles don't start to change the way they deliver software, they're going to be behind. They're already behind. It's going to be even more.  
**Andrey Marinov:** I don't know if you've tried them on your phone, but like when I try image playground, it takes so long and my phone gets so hot.  
**Filippo Tosetto:** I haven't tried myself.  
**Andrey Marinov:** The  
**Filippo Tosetto:** I haven't tried myself. But nice. Okay, Andre, thank you. This was a very useful, insightful 101\. Um so what's happening is that Mataniano is pushing a lot for this AI transformation and we want to establish a more shared c culture.  
**Andrey Marinov:** Yeah.  
**Filippo Tosetto:** So feel free to share all the questions, all the doubts. Feel free. We have the chat that I invite you to and that's the place where  
**Andrey Marinov:** I don't want to seem like a hater.  
   
 

### 00:47:05

   
**Andrey Marinov:** I mean, I I kind of surface that around you quite a bit, but uh I do believe that that's the future and that's how we work like two years from  
**Filippo Tosetto:** No,  
**Andrey Marinov:** now if we work. So, I fully believe in that. I've only been doing that since September and I think it's great.  
**Filippo Tosetto:** you and me both. I believe in this since a while. And uh what I also believe is that no one in this company has the the the truth. There are different ways to do things. And literally until three months ago, no one thought that this would be happening. Now it's happening. So it's a matter of discussing and sharing ideas and sharing. Hey, I tried this model. It's working good for this. I tried this workflow seems to be working good for developing new features. feel free to participate. Um, also because we don't want to get Sergio Durban to be the benevolent dictator in a good way because right now he's the one kicking off the old um the all in kind of initiative but he's not going to keep doing it for us. We need to be the one that push this kind of things. So if you have you know hey I found this uh swift UI uh rule that is very good for cursor should use it. Feel free to share whatever you think is good  
**Andrey Marinov:** Okay.  
**Filippo Tosetto:** and Andre thank you so much for uh the TV foundation library that was not expected. Um I want to come back to you with a proper plan on how we should move forward just also to you know set down to put down some dates on when you think this transition can happen this kind of things. So very well done. Give me a bit of time to get my head around this but for now very well done. I'm I'm just excited. Yeah. Yeah. It's going to be good. Thanks.  
   
 

### Transcription ended after 00:49:35

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*