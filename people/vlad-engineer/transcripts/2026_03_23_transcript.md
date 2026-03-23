Mar 23, 2026

## Vlad / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** You were a bit more in discovery phase, but tell me  
**Vladyslav Krut:** Last week went pretty I would say uneventful because I primarily was working on getting infrastructure set up you know first week of the project not a lot of use of AI not a lot of discoveries that let's say matters primarily catching up on what happened in the iOS world and apparently some of the technologies and approaches I used to use are not needed anymore. For example, like Swift G for images is just obsolete now because you can just call it I didn't know until Friday.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** Now I do. Okay.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** Uh so yeah, it was pretty uneventful generally speaking. Nothing too crazy. Uh on Friday I would say uh the interesting part began because on Friday I I followed your advice and I was like okay before I proceed with any more like setup integration infrastructure stuff like that let me actually like get my hands dirty and try to implement something and well I would like to say that and I did no I tried and I did not succeed and yeah I will be talking a lot I like about what happened,  
   
 

### 00:01:38

   
**Filippo Tosetto:** Okay,  
**Vladyslav Krut:** what are my discoveries from Friday and today and what went generally speaking. Uh but yeah,  
**Filippo Tosetto:** please  
**Vladyslav Krut:** third check like not crazy.  
**Filippo Tosetto:** I survived.  
**Vladyslav Krut:** Yeah, like normal  
**Filippo Tosetto:** Okay. Okay. Nice.  
**Vladyslav Krut:** stuff. Yeah. And I met Okay.  
**Filippo Tosetto:** Please, I'm all  
**Vladyslav Krut:** So I have actually a huge uh doc with notes in front of me on the other screen  
**Filippo Tosetto:** ears.  
**Vladyslav Krut:** primarily because on the meeting that we had on Friday uh with tech AI transformation. it become clear that apparently I will be share talking a lot on this meetings on from the following week because I will be getting out of ex on first hand experience. So I will be sharing my findings. So I started noting all of this and yeah I already have probably too much one one day one day  
**Filippo Tosetto:** Okay. Okay.  
**Vladyslav Krut:** in okay uh  
**Filippo Tosetto:** Do you do you want to share at least the the highlights?  
**Vladyslav Krut:** yeah I want to share and I have some let's say questions some aspects that I will be sharing for sure with the whole team but maybe I would also discuss them with you earlier maybe you have solved some of them already.  
   
 

### 00:03:18

   
**Filippo Tosetto:** Mhm.  
**Vladyslav Krut:** Uh so okay the first thing that I actually did and I'm kind of proud of is that I implemented a I believe reusable skill for uh typography setup for importing fonts registering them and this is like a skill that you can drag to your  
**Filippo Tosetto:** Not  
**Vladyslav Krut:** project. Run it and it will ask you for a set of fonts and register them like one prompt until done and ready to be tested. And I think I will just create a pull request to to Victor's repo. Uh Mau  
**Filippo Tosetto:** Victor's report, the the the general repo.  
**Vladyslav Krut:** shared the experience this one.  
**Filippo Tosetto:** Yeah. Yeah.  
**Vladyslav Krut:** Uh okay maybe this one.  
**Filippo Tosetto:** Yeah. That is the official one.  
**Vladyslav Krut:** Uh okay by like in Victors there's a lot of also knowledge that is being produced now. It's  
**Filippo Tosetto:** But that's Victor's thing. He's working on it by himself. Um, let's use the official one,  
**Vladyslav Krut:** Okay. Okay. Just a one skill that actually does everything correctly from one prompt.  
   
 

### 00:04:21

   
**Filippo Tosetto:** please.  
**Vladyslav Krut:** I had to restart it and rewrite it three times or something. But then it's like clean repo, one prompt, drag and drop fonts. Done. Done. Ready to be tested from start to the finish.  
**Filippo Tosetto:** Nice.  
**Vladyslav Krut:** Very nice. That was the first thing I did. empowered like now I can deal with this and then I tried actually to develop on boarding and no I am not but that's all right that's all right so uh where I started I started with uh using your  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** flow for new feature and uh by the way I'm not sure if I  
**Filippo Tosetto:** Mhm.  
**Vladyslav Krut:** tried the clean architecture pattern for mobile because I thought I did but today today when I started looking for it apparently didn't pull the last changes from the branch. So maybe uh it did pretty good job but it didn't use it. And the first say major or not major like a concern that I discovered is that IC probably doesn't really work for me at least on this stage.  
   
 

### 00:05:38

   
**Vladyslav Krut:** It works when you need to import something that's for sure works nice and  
**Filippo Tosetto:** What  
**Vladyslav Krut:** fine and if you are not planning to do any changes to it, right? Because if you import something and you feel like you want to modify it, there is no no way to do this,  
**Filippo Tosetto:** do you mean?  
**Vladyslav Krut:** right?  
**Filippo Tosetto:** What? Why? Why you say that?  
**Vladyslav Krut:** uh because then if you do any changes or you pull it again, it will override your changes to the local files on your repo and then we were like feel lost or or did they not some  
**Filippo Tosetto:** Why would why would you h interesting?  
**Vladyslav Krut:** feature.  
**Filippo Tosetto:** Why would you need to do a pull again?  
**Vladyslav Krut:** I feel like if I want to add another skill won't it pull everything or you know the like the idea  
**Filippo Tosetto:** That's a very interesting question.  
**Vladyslav Krut:** of usage behind it is that you commit you add your cursor folder to get ignore and then you share IC.log log in your repo with your colleagues and  
   
 

### 00:06:41

   
**Filippo Tosetto:** Yeah,  
**Vladyslav Krut:** this way if somebody's pulling what's in the log file they will just get a clean copy from is not your latest changes  
**Filippo Tosetto:** because we are not pushing the dot cursor  
**Vladyslav Krut:** and then if we are pushing our doc cursor folder why we need IC log in  
**Filippo Tosetto:** holder.  
**Vladyslav Krut:** the first place like we can use the tool to download something for us and then we cut it out of the project. It feels  
**Filippo Tosetto:** Vlad,  
**Vladyslav Krut:** like  
**Filippo Tosetto:** this is a very interesting question. Would you mind asking it in that chat that we have?  
**Vladyslav Krut:** Oh, yep.  
**Filippo Tosetto:** Because I'm not the right person to answer this.  
**Vladyslav Krut:** I  
**Filippo Tosetto:** It's probably Seria the right person, but he will also start a conversation which is what we want in general. So why wait next Friday?  
**Vladyslav Krut:** sure makes sense.  
**Filippo Tosetto:** Let's start this conversation today.  
**Vladyslav Krut:** I feel like I will also discuss a few more and maybe start a few conversation at the same time already.  
**Filippo Tosetto:** Sure.  
   
 

### 00:07:43

   
**Vladyslav Krut:** Yeah. Okay. So, this is the first thing that I I tried. I figured out that it doesn't really work. So, I cut IC completely of the project, copied and drag and drop what I wanted, restarted again and proceeded to the next, let's say, findings. So, one of the things that I feel like is one of the changes that I I feel like needs to be integrated into the flow that you shared is that uh it should store somewhere the summary and the plan after the first step and not only Girkin file.  
**Filippo Tosetto:** Can you Yes,  
**Vladyslav Krut:** I will explain why because uh in the very first prompt or for  
**Filippo Tosetto:** please.  
**Vladyslav Krut:** example in answering the plain stage I provided some of the technical details maybe Figma design maybe I did not had to work with like API model documentation stuff like that but if I would it I'm not sure if it going to be reflected in Girkin file or at least Figma designs the links and references that I shared were not in the girkin file.  
   
 

### 00:09:00

   
**Vladyslav Krut:** So,  
**Filippo Tosetto:** Should they  
**Vladyslav Krut:** it's either you're asking should they be or you're stating that they should  
**Filippo Tosetto:** be?  
**Vladyslav Krut:** be.  
**Filippo Tosetto:** No, it's a  
**Vladyslav Krut:** Well,  
**Filippo Tosetto:** question.  
**Vladyslav Krut:** I for sure want it to be somewhere. Maybe not in the girkin file. I will explain also why because then there is a third step called implement. And if it so happens that it doesn't implement what you want from the very first attempt, you are mostly going to uh fork a conversation. By the way, I discovered the feature fork. Nice. I really like in cloth code feature that lets you allows you to reset a conversation to specific point and I asked AI if there is feature for that in cursor and it was like no like sad but then I found the the fork and I'm like oh that works that's like the same problem uh but then uh if I have to restart implement step because I'm happy about something. Maybe I want to do some changes to the other skill the cursor uses to basically write the code.  
   
 

### 00:10:11

   
**Vladyslav Krut:** Uh then the context window is either completely clogged of what I don't want to see anymore uh or it may be even kind of full after the first two steps.  
**Filippo Tosetto:** Okay, because let's say first step there is a discussion where we talk to the AI I want to develop a new feature. This is my initial idea. Challenge my idea. That's what we do with AI. After this back and forward, we will have the idea foolproof. Let's say what do we want after this? We want an artifact that stores in a readable format for both the human and the machine what this feature is about.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** As you say, after this stage, this initial preparation phase, the context window could be very  
**Vladyslav Krut:** Uh,  
**Filippo Tosetto:** full.  
**Vladyslav Krut:** I feel like well I'm not sure it's full after this step or after gorgen file because I didn't really have a lot of problems here.  
**Filippo Tosetto:** Let's say that uh the Girkin file out the output of the Girkin file is end of phase one.  
   
 

### 00:11:34

   
**Filippo Tosetto:** I'm I'm thinking it's it's more like a brainstorming session now.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** What is preventing me of taking this girking file and spawn an agent? Agent spawning an agent mean clean context window to run the  
**Vladyslav Krut:** Yes, this is what I was thinking.  
**Filippo Tosetto:** implementation.  
**Vladyslav Krut:** So probably for the implementation I want to have separate agent or at least I want to have a clear window context window.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** It could be a sub agent that works. It could be a new like agent with which we as engineers  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** interact. One of two. But we need to have a clean context window before starting the implementation. But I also want to keep the the the outcome of the stage one.  
**Filippo Tosetto:** For me, the outcome of stage one is today the Girkin file. Is it the only outcome that we want? I don't know. I'm open to discussing this with you because what you say is very interesting. The girking file doesn't really store the design file for instance design link and maybe there are other points that we want to store somewhere.  
   
 

### 00:12:52

   
**Filippo Tosetto:** Technical design choices. We want for this app we want to use swift data. Very simple, very stupid. or um APIs use this swagger link to retrieve all the information about the API. Do we need to add this information to the Girkin file? So, sorry I'm I'm asking questions  
**Vladyslav Krut:** Yes. So we definitely need this data to be either in Girkin or in the  
**Filippo Tosetto:** here.  
**Vladyslav Krut:** other artifact. It for sure should exist somewhere and for now it doesn't. comprehend the feature in full. Maybe in the in the human readable format, we don't really need to talk about every corner case while in Girkin it will be described.  
**Filippo Tosetto:** What is preventing us? Sorry, again, this is more a brainstorming than anything else. What What you What you just described to me is a user story.  
**Vladyslav Krut:** Oh, well yes.  
**Filippo Tosetto:** User story contains  
**Vladyslav Krut:** I  
**Filippo Tosetto:** human readable description of the feature,  
**Vladyslav Krut:** reference to  
**Filippo Tosetto:** links to  
**Vladyslav Krut:** Excel.  
   
 

### 00:14:30

   
**Filippo Tosetto:** design.  
**Vladyslav Krut:** Yes, that sounds like a user story to me. It's enough to let's say as a human to open it like read it diagonally like okay this feature is for that and then either close it if this is not what I'm looking for or open Figma open swagger open any other tool if this is what I'm looking for and if I need any extra details so yeah that's a user Sorry.  
**Filippo Tosetto:** Interesting. Go on. Go on with your discoveries because this is very interesting.  
**Vladyslav Krut:** Okay. Uh then I how to describe it? I will talk about how stupid uh the Kimmy agent later. Not for now. Uh not for now. I was what I was doing after. So I was I feel like I need some kind of integrity check for the whole workflow. What do I mean by that? I already tried to do that and I failed because well I just didn't listen to me. I will be probably ask asking this question if maybe anybody from the chat found a solution.  
   
 

### 00:16:06

   
**Vladyslav Krut:** But what I want if AI is doing its job and some of the rules or skills or agents or scripts that it was told to use are not existent in the codebase if it cannot find it. I wanted to abort the mission and to ask because when we are building a tool we kind of want to make it reliable and what happens now is that for example the agent couldn't build the application just to verify that it compiles so it tried to invent a lot of weird stuff and I don't want it to I wanted to say this script is not executable because it's running in the sandbox which is not true but that's what It told me after I stopped it because I was watching it work.  
**Filippo Tosetto:** My experience and my experience is very limited here is that we should enforce this with rules. So you give if the AI is doing something stupid. So instead of running Xcode MCP to build the app just something like that and they start to run whatever script they they start to do.  
   
 

### 00:17:23

   
**Filippo Tosetto:** We need to enforce this in a rule saying to build the app use MCP. If not found,  
**Vladyslav Krut:** I have. Let me see.  
**Filippo Tosetto:** fail.  
**Vladyslav Krut:** I had what did I have a rule or a script? Let me see.  
**Filippo Tosetto:** A rule can be pointing to a script.  
**Vladyslav Krut:** Oh, yeah. Okay. It was a skill and I noted to use the skill. It's not a Okay, maybe I should put it into the rules and see if it works.  
**Filippo Tosetto:** For me, this is very interesting because you are the you're seeing all these problems. But go on, go on.  
**Vladyslav Krut:** So yeah,  
**Filippo Tosetto:** I like it.  
**Vladyslav Krut:** I will be I can also tell about cool things, but there are more more problems for now. Well, I didn't really have a lot of time to play with it yet. So, u yeah, some kind of workflow integrity I tried with skills, it didn't work with rules. I will also try still trying to kind like find the right place where to put what and also I feel like depends on what agent you're using some of them tend to ignore rules and some of them cannot find correct skills even if they are mentioned.  
   
 

### 00:18:38

   
**Vladyslav Krut:** Hello Kimmy. Yes. And none of them is reporting failures if anything doesn't work. This is probably a right time to tell about my experience with Kim. Um, so it tried to create a its own layer of abstraction around assets about images in Zap that I really didn't want to do. U so I stopped and I told it how to change it. Obviously keeping in mind that I will update the the other file so it doesn't do this mistake again. And then Kim is like okay let me write this down and then nothing happens like I can see in cursor in log nothing happens and it tries to build the project and like wait you didn't do anything. It's like, oh right, it got reverted. And it's four time in a row it tries to do it thinks that it tries to make an edit. It doesn't make edit and then it's like llinter is reverting the changes. Let me try again. It did it four times and then I stop it.  
   
 

### 00:20:00

   
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** And then the same experience when I was trying to explicitly teach it how to use this u assets folder that you can just do do UI image dot name of the file because it first tried to build its own layer. I didn't want it primarily because I also built a Xcode generated one before  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** but I didn't want to use this one either. So, and then it uses UI image named this not type safe optional initializer not compile time save and then I will now use and like copy paste the line with example and it's like I will use your image named allus didn't do this  
**Filippo Tosetto:** Yeah. Well,  
**Vladyslav Krut:** stuff is actually doing it  
**Filippo Tosetto:** but that's another story. Come on.  
**Vladyslav Krut:** like a lot of times. Uh then also about Kimmy uh I tried to make it specifically do certain tasks in sub aents because I didn't want to close the windows the context window and then it uh appeared to be unable to run a sub agent uh and just decided to do it itself.  
   
 

### 00:21:25

   
**Filippo Tosetto:** I need to do some  
**Vladyslav Krut:** The other time it was but sometime it's just like you know sub  
**Filippo Tosetto:** tests.  
**Vladyslav Krut:** agent is not sp spawning so I I just proceeded my main window that happened. Yeah.  
**Filippo Tosetto:** Okay. So, Kim is not good as it seems.  
**Vladyslav Krut:** I not sure for whom it seems like Kim is good to me like yeah this is uh what I started from. So I first told you about like fun more fundamental problem that I was like encountering but actually my notes is are starting from the quote I forgot to write anything changes aren't persisting hashkim this is the situation I  
**Filippo Tosetto:** What?  
**Vladyslav Krut:** told you about like linder is reverting changes obviously linder is not is like  
**Filippo Tosetto:** No,  
**Vladyslav Krut:** kimmy just not doing changes and then  
**Filippo Tosetto:** it it is. So on my tests, it worked fine, but I wasn't doing anything that specific. I was way more open. I didn't have rules like you just described for images for instance.  
**Vladyslav Krut:** And  
   
 

### 00:22:41

   
**Filippo Tosetto:** So uh for me it was just I need to build this specific screen build it and the result was as expected but I wasn't really guard railing regarding you know use uh this specific way of doing uh images for instance. This is very interesting. Okay.  
**Vladyslav Krut:** one more thing I have only last thing that Kimmy is doing like constantly is uh it encountered a lot of times with me situations that it cannot run a shell script. It's problem specifically of I don't know the chat that I had because I opened another window with Kimmy and it could no problem.  
**Filippo Tosetto:** That's context window. That's context window being filled and the AI start to do the random things.  
**Vladyslav Krut:** Yeah, but then agent was like what it came up with it it spawn sub agent to run a script and it proceeded doing it a few iterations after which is don't get me wrong it got this idea and it worked. Not sure if this is how I would like it to work, but that was actually fun.  
**Filippo Tosetto:** No, but we need more control.  
   
 

### 00:24:03

   
**Vladyslav Krut:** The problem.  
**Filippo Tosetto:** We need more control over over this.  
**Vladyslav Krut:** That's why I was talking about workflow integrity.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** Yeah, I wanted to to report if something is not working and it just refuses to for now. Maybe. Yeah,  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** maybe I will add a few more cups locked words like must should never have  
**Filippo Tosetto:** I think that is the way. I think that's the  
**Vladyslav Krut:** to  
**Filippo Tosetto:** way.  
**Vladyslav Krut:** I think I will tell you more when I find more.  
**Filippo Tosetto:** So at the end of the week, you didn't manage to write any new feature for FA for the face AI  
**Vladyslav Krut:** Oh no,  
**Filippo Tosetto:** rewrite.  
**Vladyslav Krut:** actually uh like on boarding is somewhat done.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** Uh it uh it doesn't well I restarted a few times and it should be working. Previews are fine. The problem like it's not building right now because it was supposed to add a permission description to info list but then it forgot hello Kim again.  
   
 

### 00:25:14

   
**Vladyslav Krut:** So yeah I this would make it work. Now on boarding is working let's say I wrote it already three times this different set of rules and every time it's like okay that kind of matches the Figma more or less it doesn't have in my workflow at least any more way to like do a pixel by pixel comparison or something like that or any tools to verify that it's actually reflecting Figma. uh but yeah as we discussed before the code is now cheap and coding wise uh on boarding is done a few times but I want to use pro on boarding because it's so linear and easy to let's say establish rules and skills that would work better than they are working now so each iteration is getting a bit better no iteration that I was happy with just  
**Filippo Tosetto:** Okay, this is uh interesting. Um, this is interesting to me because what you are doing is that you are not actually building anything in terms of features because the infrastructure is not ready yet.  
**Vladyslav Krut:** uh yeah I would describe it but I am building this infrastructure So I assume this is is maybe a way to go.  
   
 

### 00:26:41

   
**Vladyslav Krut:** I'm not sure if this is what I am expected to do. Maybe I should just use what we have and try to build an up with this instead of investing into into roles and sets and and rules and  
**Filippo Tosetto:** So I need to be honest here.  
**Vladyslav Krut:** skills.  
**Filippo Tosetto:** I was hoping this process would go much faster and somehow smoother, but probably we should put down a sort of percentage of your time spent into the infrastructure and a percentage of your time spent into actually progressing with the building part of the project.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** What do you think?  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** What do you think?  
**Vladyslav Krut:** Like if we keep the idea that our let's say primary goal is still to go to the ready application then I would say at least 70% should go towards developing features and not towards infrastructure. Then if this is what we say, I will lower a little bit my let's say expectations to the quality of the work AI does and you know just test it that it kind of works and then proceed to new feature proceed to new feature to see what where it gets us.  
   
 

### 00:28:08

   
**Filippo Tosetto:** Do you think this can be done iteratively? meaning I'm not expecting that hey AI build me the on boarding and the result is the perfect on boarding because I doubt with the level of of our tools today unless you spend the next month refining our tools we will get the perfect result there but what I'm the way I would work which is different because I'm I'm I'm work in a different way is okay the on boarding is 80% there it's fine I can refine it because it's my skill set to build iOS application so I refine it manually going to move to the next screen uh meanwhile I improve a little bit the infrastructure okay let's build the home screen okay with the infrastructure a bit more refined let's see the results okay well it's definitely better than before but this is also a more complex feature. So, um the results are 50% there. Why? So, it's more like feature by feature I would improve the tools instead of trying to keep refining over and over the tools. But this is my way of working.  
   
 

### 00:29:31

   
**Vladyslav Krut:** Uh well I can definitely follow this path. Nothing wrong with this. I why I for now like last two days maybe just stick to the plan that I was doing because to me it looked like the goal is to build a tool set and the application is like a bonus but I could got it wrong. So if this is what happen then uh I will just change a little bit the way of working and focus towards an application and allocate a bit less time on well or much less time on tooling and expect more of the team  
**Filippo Tosetto:** No, Vlad. You didn't you didn't you didn't  
**Vladyslav Krut:** to contribute to this. That's  
**Filippo Tosetto:** misunderstood at all because uh what I asked you to do was exactly this.  
**Vladyslav Krut:** okay.  
**Filippo Tosetto:** But now we need to start to put down some timelines around the work. Uh because you know that the the final goal by the end of the year obviously is to replace the external developers and for that I will need to start to to put down some dates.  
   
 

### 00:30:48

   
**Filippo Tosetto:** uh when is the developer for face AI at least mobile developer uh going to go when is Vlad being able to take over the full development of the application so that is the question that I've been asked so um bear in mind that there is  
**Vladyslav Krut:** Makes sense.  
**Filippo Tosetto:** no pressure on getting these people out of the way until at least until you know halfway through the year. But if we can start to prove this way before to say hey I'm sure that by the 31st of Mar May I will be the solo mobile developer for face AI. That is for me good enough. So I'm I'm now asking you by the way right now I want to share with you  
**Vladyslav Krut:** Yes,  
**Filippo Tosetto:** bless you all good don't worry don't worry I want  
**Vladyslav Krut:** I was supposed to mute when I cover and then I click twice.  
**Filippo Tosetto:** I want to share with you the exercise that I've done with Andre um please don't feel that you need to follow this exercise the same way because the application that he's working on are different plus he has the full product context on his side something that you do not have today because you just arrived in the company.  
   
 

### 00:32:16

   
**Filippo Tosetto:** So I'm going to share with you uh what I've been working on with Andre so you can understand what I mean by putting down some dates. So this is oops sorry this is a road map that I've been working on with uh with Andre and uh um is working on two main apps which is screen mirroring and IMO why I've decided to merge these two apps and give them to Andre because they share um a huge part of the codebase which Andre a already extracted in a single library which we call TV foundation kit. Um this to give you a very brief understanding um both IM mode and screen mirroring will connect to uh external TVs uh like Samsung smart TVs these kind of things and to do so they have some proprietary libraries that do that. What Andre has been doing is to remove the proprietary library, create uh this TV foundation kit by himself and now the job is to test it first which is what is doing and then replace it inside first and then screen mirroring after this.  
   
 

### 00:33:48

   
**Filippo Tosetto:** So we still have the external developers working with us. Andre will go on paternity leave first of all for a couple of weeks and then in the month of May he will  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** take over completely IMOIS and by the end of May he will be the solo developer in IMOIS. This could be done before but I want to keep as first um experiment for email list. I want to keep a very loose uh timeline for the first stop. After that it will spend the month of June to do the same for screen mirroring which is another iOS application. And finally it will do that for the IMOT Android application which is the month of July. Now I would like to play a bit with you to get down some dates for your deliverables. Again, this is between me and you. Not going to be sharing this with anyone else. So it's just to understand a bit what we could do potentially.  
**Vladyslav Krut:** Okay,  
**Filippo Tosetto:** So I'm going to open what I  
   
 

### 00:35:05

   
**Vladyslav Krut:** sure.  
**Filippo Tosetto:** have with you. And then we have um I called it environment setup this first initial phase. And I think you are there because you  
**Vladyslav Krut:** We can call it done.  
**Filippo Tosetto:** have  
**Vladyslav Krut:** Yes. If there is anything left, I will just do this when needed like Firebase integration or like cert. Yeah. When I need this, I will get there and we'll we'll do this. We can call  
**Filippo Tosetto:** I like to add uh AI in um iter iteration. I like this to put as where is it?  
**Vladyslav Krut:** Interesting how have chosen that place.  
**Filippo Tosetto:** Because I think this is something that needs to go on for a while and this is you  
**Vladyslav Krut:** I think this process may not be completed.  
**Filippo Tosetto:** iterating. Sorry.  
**Vladyslav Krut:** I I genuinely think that this progress may not be completed. I I feel like it will go on and on until and even after we completely replace external developers and have like really solid rule set but I feel like it will continue be going not not sure what we can what state  
   
 

### 00:36:44

   
**Filippo Tosetto:** Yeah,  
**Vladyslav Krut:** we can call done. If you have a definition of done,  
**Filippo Tosetto:** I agree.  
**Vladyslav Krut:** let's share where where we can discuss it. Of  
**Filippo Tosetto:** I agree with you. Let me keep it here for my brain sanity.  
**Vladyslav Krut:** course,  
**Filippo Tosetto:** I will remove it. But I agree with you. This is something that is never over. It's always iterating. So let's keep it like that for now.  
**Vladyslav Krut:** it's not only I'm doing this. I feel like it will be also collaborative effort.  
**Filippo Tosetto:** Yeah, you're right. Let's remove it then.  
**Vladyslav Krut:** Now, you you can leave it here for your own sanity.  
**Filippo Tosetto:** No, no, no, no, no,  
**Vladyslav Krut:** Don't get me wrong.  
**Filippo Tosetto:** no, no, no, no. Uh, let's work on face AI. So, let's say this week you start to work on face AI B2.  
**Vladyslav Krut:** on features like yes dedicated  
**Filippo Tosetto:** Yeah. Features. Features. Um,  
**Vladyslav Krut:** features.  
**Filippo Tosetto:** I'm going to put down at least 20 days.  
   
 

### 00:37:40

   
**Filippo Tosetto:** Not because I don't trust you, because I think we are not ready yet to say, "Hey, this is good until we start to actually work on this." For me, and you know what? I'm going to be honest with everyone and put that this is going to take Yeah. the the full month of April. One month. What do you think?  
**Vladyslav Krut:** But we will be five or six weeks.  
**Filippo Tosetto:** Uh one,  
**Vladyslav Krut:** If you're starting  
**Filippo Tosetto:** two, three, four, five, six. It's a bit too much. Six weeks.  
**Vladyslav Krut:** today  
**Filippo Tosetto:** You're right. Probably going to take less four weeks. What do you think?  
**Vladyslav Krut:** u well I still have some uh uncertainty about what exactly should be built but that seems uh very reasonable to get uh let's say 85% of the project um because we both know that the last a little bit is is always stretchy. So at this point we will be calling let's say all the core features done of course but then I assume we will have similar phase that we maybe have now in phase AI where we test and find some corner cases something that we do not consider maybe pay wall issues maybe you also told me that uh we are not remember who exactly but planning to integrate to develop a system that would replace revenue cat you told me or something that would manage a features in our app like remotely managing maybe  
   
 

### 00:39:31

   
**Vladyslav Krut:** some feature flags that enable or that could be enabled or disabled for users based on their uh payment status maybe region. No,  
**Filippo Tosetto:** No, I haven't said anything like  
**Vladyslav Krut:** no.  
**Filippo Tosetto:** that.  
**Vladyslav Krut:** Uh, at least about the pay wall and the premium features, I believe you told me that there will be another system that will allow enable  
**Filippo Tosetto:** Oh  
**Vladyslav Krut:** or disable specific features remotely for users.  
**Filippo Tosetto:** okay.  
**Vladyslav Krut:** So, I should keep this in mind.  
**Filippo Tosetto:** So so there is uh okay this is opening up another uh corner. Let's park it for a second and we are going to go back to this.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** uh just wanted to to put down some honest dates that I can  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** communicate and I think by the end of April we should be able to have face AI in your hands which give you  
**Vladyslav Krut:** Oh, in my hands.  
**Filippo Tosetto:** yes that does that doesn't mean  
**Vladyslav Krut:** I think so. Yes, very much.  
**Filippo Tosetto:** you know that there's not you will be working on it So you will be interacting with the PO with the QA etc. But I will probably remove Anton meanwhile.  
   
 

### 00:40:53

   
**Vladyslav Krut:** Okay. Yeah,  
**Filippo Tosetto:** What do you think?  
**Vladyslav Krut:** I think this is very much possible.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** Yeah, this amount of time should be well,  
**Filippo Tosetto:** So,  
**Vladyslav Krut:** it may not be completely enough to like rebuild everything that we have up until the level that we have, but it will be definitely enough to for me to have all the knowledge needed to just continue working and not rely on Antonet list. For example,  
**Filippo Tosetto:** Do you still think, and this is an honest, I would like your honest opinion. Do you think rewriting this up from scratch is the way to go, or would you prefer to take the current code base and refactor it to make it work for you?  
**Vladyslav Krut:** What do you  
**Filippo Tosetto:** You don't need to answer now.  
**Vladyslav Krut:** think?  
**Filippo Tosetto:** Think about it a bit because what we can do throwing ideas here is we can fork the current codebase and you work separately on our refactoring to bring it up to the standards that we want instead of you starting from scratch.  
   
 

### 00:42:12

   
**Vladyslav Krut:** I feel like even if I would consider it to be a better solution for the application,  
**Filippo Tosetto:** I  
**Vladyslav Krut:** it will discard a significant benefits for us of me testing an idea of creating an application from scratch using all the fancy AI tools that we are developing.  
**Filippo Tosetto:** agree. But we also need to be conscious of production times here. So for me, if you know by the 1 of May, you're okay to take over the app. Is it rewrite from scratch or is it refactoring? I'm okay either ways. But for me it's important that if I tell Gilor, which is the company where Anton's come from, um, on the 1 of April, hey, in 30 days, we don't need Anon anymore. I need to be sure that you will be able to take over and and that's why rewriting from scratch will take probably more time because of those edge cases that you talked about while refactoring the app is working today. What you're doing is just making sure that the code that you touch works as a as as it is today.  
   
 

### 00:43:36

   
**Vladyslav Krut:** Yeah, I have a suspicion. I did no effort to confirm this, but I have the suspicion that right now we have this weird stage full of corner cases where everything is like working but nobody knows how and why.  
**Filippo Tosetto:** Y  
**Vladyslav Krut:** And maybe not working but also nobody knows how and why. primarily because of the state the application is right now. Maybe there were made a set of let's say really poor architectural decisions. Maybe Anton is not aware of how what's happening in the app. I I why is it breaking every change? Like I I I don't  
**Filippo Tosetto:** because this app wasn't written by Anton.  
**Vladyslav Krut:** understand.  
**Filippo Tosetto:** Anton inherited a code base that was a mess and Anton spent the last two months trying to fix the mess.  
**Vladyslav Krut:** Okay, that uh makes sense. But then I also have an an idea that if if the app is developed from scratch  
**Filippo Tosetto:** Sure,  
**Vladyslav Krut:** in let's say correct way, all of those problems may never appear in the first  
**Filippo Tosetto:** but you need to bring it up to speed to what it is  
   
 

### 00:44:45

   
**Vladyslav Krut:** place.  
**Filippo Tosetto:** today. It's not that we remove Anton and it's okay if the app is not  
**Vladyslav Krut:** Sure.  
**Filippo Tosetto:** ready because you will need to take over development. That's what I'm thinking now. Look, don't don't answer now. I want you to think about it properly because it's not an easy answer in my opinion  
**Vladyslav Krut:** It it's not and especially it's not easy because I did take a quick look  
**Filippo Tosetto:** here.  
**Vladyslav Krut:** on on the codebase but I did never dig in let's say deep deep enough to get a a comprehensive understanding of what's happening why are the key features are working the way they So yeah, I will to answer this. I will for sure need some kind of investigation later.  
**Filippo Tosetto:** Um, I'm just going to put down something like this for now.  
**Vladyslav Krut:** I want to ask you uh when you're asking me  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** about uh will I be able to take on the development of the face AI on specific date. Uh let me think about how how I phrase this.  
   
 

### 00:46:21

   
**Vladyslav Krut:** Let's imagine let's imagine that we decide to not proceed with uh let's uh assume that we proceed with implementating it from scratch implementing it from scratch. So we discard the existing codebase that were a mess and then was kind of fixed by me being able to continue development and taking this project. Do you mean that the app should be at least on the same stage? This is what you mean.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** Yeah, it should be not less than what we already have.  
**Filippo Tosetto:** Feature  
**Vladyslav Krut:** Feature parity.  
**Filippo Tosetto:** parity.  
**Vladyslav Krut:** Okay. And as other option let's say it could be a fork of existing codebase on which I spent let's say same time five or six weeks you mentioned until the end of April and in this six weeks I need to let's say refactor and fix the application to once again have feature parity.  
**Filippo Tosetto:** Yeah, that's uh in my opinion the way to go. So one or the other. When you do refactor, you could start with unit tests. I'm going to write unit test for the business logic first and then I'm going to refactor the business logic so to make sure that everything works and on and on and on also for UI.  
   
 

### 00:47:46

   
**Filippo Tosetto:** The current UI in my opinion is not nice. There are some very weird things happening in the UI.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** So for me that will probably require a rewrite but then you're  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** only going to rewrite that part and not the full application. Why am I starting to think in this direction? Because there are a lot of things that will come for free. Remote configuration for instance. So activating the activating features from Firebase remote configuration is a thing that you will inherit if you just work on the current codebase. the full integration of all the third party tools is it amplitude firebase revenue cap it's already done you know uh there are some things that are already there that if you start from scratch you need to do from again  
**Vladyslav Krut:** What would prevent me let's say from just dragging the files and folders with the code that we are happy with with external libraries connectors maybe one of our let's say processing layers to you know build this bridge between what API returns to what app can work with drag them into the project from scratch and get all the things for free.  
   
 

### 00:49:15

   
**Filippo Tosetto:** I'm not here to debate this because I think you know  
**Vladyslav Krut:** Uh well,  
**Filippo Tosetto:** better.  
**Vladyslav Krut:** I may not know better in this specific case, but I also like that's a brainstorm like storm a year like if if the goal is to  
**Filippo Tosetto:** Uh  
**Vladyslav Krut:** save time and there are parts of the application that we are content with. The thing is to answer it like honestly and probably to make an educated decision. I will have to go and take a much deeper look into FAI and to find is the code that has been written is even testable like was it written in a way that supports being covered in unit test because it's probably it's not if it was a mess we don't know well I don't know yet I will need to go and take a look  
**Filippo Tosetto:** Can you give me an answer by tomorrow?  
**Vladyslav Krut:** Yes, of course.  
**Filippo Tosetto:** Nice.  
**Vladyslav Krut:** Let's have a quick chat tomorrow.  
**Filippo Tosetto:** Yes. Um,  
**Vladyslav Krut:** Maybe better for second part of the day if you  
   
 

### 00:50:22

   
**Filippo Tosetto:** yeah. and um I'm check my calendar is as usual very  
**Vladyslav Krut:** have.  
**Filippo Tosetto:** beautiful after lunch quick 15  
**Vladyslav Krut:** Yeah,  
**Filippo Tosetto:** minutes I'm just going  
**Vladyslav Krut:** true.  
**Filippo Tosetto:** to do uh okay I'm just going to send you half an hour and that's it and then we can discuss. My time is very running short. Uh I lost the window with you. Here you are. Um so  
**Vladyslav Krut:** If you were not sharing by the way,  
**Filippo Tosetto:** just No,  
**Vladyslav Krut:** maybe you were throwing me something, but I don't  
**Filippo Tosetto:** no, no, no, no.  
**Vladyslav Krut:** know.  
**Filippo Tosetto:** I was doing uh calendar things. So I would like to still keep the 1st of May as date for you to take over this app. I think six weeks should be enough.  
**Vladyslav Krut:** to be like completely honest like even if I either way we choose I will be able to take over of the project it's not a big project it's somewhat comp there is like one complicated screen like maybe just maybe I can take it over now because I have AI tools capable of explaining me things and the way they works like I I may not need five weeks to understand what's going there  
   
 

### 00:51:58

   
**Filippo Tosetto:** But pay attention because then you will start to work also on another app which is AI design.  
**Vladyslav Krut:** and then I will have a question on what's the way to time manage or what you know percentage of my work should be allocated to one or another  
**Filippo Tosetto:** 50/50 or depending. Let's say the baseline is 50/50. But there are apps that we require more involvement  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** because of marketing money. If we invest more in one app, the idea is for you to spend more time in that app.  
**Vladyslav Krut:** Oh, that makes sense. Yes.  
**Filippo Tosetto:** But this is a problem that I like to think about in the future.  
**Vladyslav Krut:** Okay. uh thing that I would like to ask now is that how for face AI is the road map is going to look like  
**Filippo Tosetto:** It's pretty easy. Um, I  
**Vladyslav Krut:** asking just to understand you know like are we is this app is supposed to continue growing a lot or this is more or less complete utility that we just need to make better you know what amount of let's say knowledge and expertise will be needed there because if this hub is not supposed to grow much more than it is already right now then you know then it may not make a lot of sense to either  
   
 

### 00:53:29

   
**Vladyslav Krut:** rewrite it from scratch or even to refactor it because we just need to release a few more features  
**Filippo Tosetto:** No,  
**Vladyslav Krut:** that that's good  
**Filippo Tosetto:** it's not ju just more. The idea here is for you to take completely over this application. Um  
**Vladyslav Krut:** And you're mean uh do you mean iOS only or all the platforms now?  
**Filippo Tosetto:** for me iOS only for now. So for me your work and this is something that is still open for me your work is  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** to take over the mobile development of two projects face AI and AI design.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** And with AI design, you also have Android. I'm still not convinced back end will be that easy to take over by a mobile  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** developer. And this is an ongoing discussion that we have internally. So for now, for me, the idea is this. Uh there's going to be a moment where your  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** time you're going to be faster to develop features than PO will be to produce the feature that you need to build.  
   
 

### 00:54:51

   
**Vladyslav Krut:** Um I also expect this moment to happen but for this to happen we both know that somebody need to invest some time and effort into the tool of  
**Filippo Tosetto:** Yeah, but but don't worry,  
**Vladyslav Krut:** course.  
**Filippo Tosetto:** you're not you're not the only one working here. Meaning don't worry that I feel that there's a lot of we've been projecting a lot of responsibilities on your shoulder and I don't think it's right. Uh because there's a it's not like that. There is Serio working on it. There's me, there is Andre, there is Andre, there is Manu. two new hires starting today. So while you are in your little garden trying to do this kind of things, there are other people trying to do the same things. And the idea of these Friday meetings is for us to share this knowledge and I'm expecting to refine more and more this process over the next two months. So that but this is in my head blood. You come to me and say hey Philippo um I have to work for three days on face AI this week because we have the road map has these new features.  
   
 

### 00:56:09

   
**Filippo Tosetto:** Sure no problem. Blood already knows everything because you already organized with the PO. that you already share the perfect user story and you do the coding part in two three days. It's about capacity planning and that's my job. So do not worry. No one is expecting you to work at the same time on features for both applications. It's about me organizing your work in that sense based on road maps.  
**Vladyslav Krut:** Okay. Okay. Thank you. Uh also I will appreciate if I uh understand the plan that's kind of important for me. Uh so organizing the the how did you the capacity right one  
**Filippo Tosetto:** capacity planning. Yes.  
**Vladyslav Krut:** application another application tool building producing refining. So for now I will spend the rest of the day investigating PCI and decided deciding should be rewrite or refactor. What is this?  
**Filippo Tosetto:** I'm going to send it to you. Please do not change anything. But this is the road map for face AI for instance and for all the other apps.  
   
 

### 00:57:36

   
**Vladyslav Krut:** Hello.  
**Filippo Tosetto:** This document is share with all  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** the company. So this is the plan for face AI for the next three months.  
**Vladyslav Krut:** Okay. Nice.  
**Filippo Tosetto:** Uh probably with a bigger screen it's going to be easier for you to to to look at  
**Vladyslav Krut:** There's  
**Filippo Tosetto:** it.  
**Vladyslav Krut:** Oh, that's about holidays.  
**Filippo Tosetto:** And  
**Vladyslav Krut:** I also wanted to ask why you why did you what's this document about?  
**Filippo Tosetto:** yeah, one sec.  
**Vladyslav Krut:** Let's say yes,  
**Filippo Tosetto:** Let me finish here. So to each of this initiative,  
**Vladyslav Krut:** I open it.  
**Filippo Tosetto:** you have attached an epic with more information regarding that feature. So you have a better understanding of the feature itself.  
**Vladyslav Krut:** Oh, I see. I see. Yeah, it was even on this screen. It doesn't really show everything I need to  
**Filippo Tosetto:** No, no, no, no, no. The screen is very small.  
**Vladyslav Krut:** see.  
**Filippo Tosetto:** Right. Um, just to wrap up the conversation, that document I share with you, the holidays one, uh, it's very simple.  
   
 

### 00:58:46

   
**Filippo Tosetto:** Um, whenever you require a day off, you do it through uh, factorial. Totally fine. But what we would like to do is also to keep track on this holiday spreadsheet. uh why because this is all the people working in in engineering right now and especially in periods like summertime and Christmas time we would like to see always if people are if that there is at least one of us there it's a it's just a a bird's  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** eye view on all the engineering department today on who is in holiday or not don't worry nothing more than  
**Vladyslav Krut:** We have a factory, we have a tool and but we also need a  
**Filippo Tosetto:** I know I know but because we don't have  
**Vladyslav Krut:** spreadsheet.  
**Filippo Tosetto:** visibility on everyone through factorial I cannot see I can see you but I cannot see the people that works with Andre for instance it's yeah it's a limitation of  
**Vladyslav Krut:** Oh, okay.  
**Filippo Tosetto:** the tool itself  
**Vladyslav Krut:** I see. Okay.  
**Filippo Tosetto:** Okay. Uh,  
**Vladyslav Krut:** Sure.  
   
 

### 00:59:58

   
**Filippo Tosetto:** one last point is, do you need anything else from me this week to move forward?  
**Vladyslav Krut:** Um, no, I don't think so. For now, I feel like what I need is to do only investigation of how FI is looking and what what would be the best way to proceed here. And then starting from tomorrow we will um maybe craft a new let's say plan on how to proceed and what even will be my bloggers tasks goals and and so on and so  
**Filippo Tosetto:** what I think and I'm going to um ask this question as an  
**Vladyslav Krut:** forth.  
**Filippo Tosetto:** open question. Think about it and tomorrow you answer. Would you like to sit down me and you to craft a road map or the deliverables for the next five six weeks regarding face AI for instance? Think about it. You don't need to answer now.  
**Vladyslav Krut:** That's if we proceed with creating a new one or if you proceed with refactoring or both.  
**Filippo Tosetto:** I think both because you still need a way to say okay for new app from scratch is about okay let's work this week I'm gonna work on the home screen next week I'm going to work on the beard filter the week blah blah blah I'm going to work on monetization in case of rewrite sorry yeah rewrite from scratch in case of refactoring probably you need something similar as  
**Vladyslav Krut:** But it will be  
**Filippo Tosetto:** which is this week business logic around filters,  
**Vladyslav Krut:** Yeah.  
**Filippo Tosetto:** next week UI for main screen, the week after about this and this and that.  
**Vladyslav Krut:** Yeah, I I think some kind of plan I will absolutely need if we decide to proceed with uh refactoring. Yeah. Okay, I got the question. I will think and give you answer tomorrow alongside with the other more important answer and thank you. Have a nice  
   
 

### Transcription ended after 01:02:28

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*