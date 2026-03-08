Jan 19, 2026

## Andrey / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Good afternoon.  
**Andrei Marinov:** Hello. Good afternoon.  
**Filippo Tosetto:** Hello. How are you?  
**Andrei Marinov:** Doing well.  
**Filippo Tosetto:** I'm I'm good.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** It's a It's a good Monday. It's good Monday considering what's coming tomorrow and the days after. So, it's it's good Monday. I'm okay with this. Um, are you ready for your uh um operation?  
**Andrei Marinov:** Yeah. Not like I have a choice. Uh,  
**Filippo Tosetto:** Fair point.  
**Andrei Marinov:** Wednesday.  
**Filippo Tosetto:** When is it again? Is it this Friday?  
**Andrei Marinov:** This Wednesday.  
**Filippo Tosetto:** Wednesday.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Okay,  
**Andrei Marinov:** Actually,  
**Filippo Tosetto:** sounds good.  
**Andrei Marinov:** Wednesday I get admitted and then on Thursday it's is the actual surgery.  
**Filippo Tosetto:** Um, okay, that's good. Yeah, makes sense. Usually it's like that. Okay. I want to talk to you about a few things today and then I need your help for something but let's keep that at the end just as a separate topic. Uh because I just on boarded a new app and I'm having some issues with certificates and stuff.  
   
 

### 00:02:15

   
**Filippo Tosetto:** So I'll let's talk afterwards. Anyway, um before jumping into details for each app, I want to give you an overview of the current recruitment that uh that I'm planning and uh uh which is I already asked for a substitution for uh Salman and uh I will proceed with requesting a substitution of the full team for IMOD Android uh and this is going to happen today and this is because um once the app goes online we change team and we go with ana and you get the app in the growth part so we're going to remove it from the launch team and you're going to get the Android part in the full uh IM mode uh Android so that's the idea um this one as well. Uh and that is it in terms of recruitment for the moment. Once these two positions have been um filled, I will proceed with the rotation of the full AI design team because that's for me in the next line for priority. And uh um finally uh most likely towards second half of February we are going to rotate the last thing that we have which is for screen mirroring which is not with you but it's fine don't worry.  
   
 

### 00:03:51

   
**Filippo Tosetto:** Um first few questions for AI design for you. Do you have any idea if all the the AI lab changes have been deployed?  
**Andrei Marinov:** uh like the ones that we're currently working on uh excluded.  
**Filippo Tosetto:** I don't know. This is where I'm trying to have a bit of visibility because  
**Andrei Marinov:** So, uh last week like we talked about uh they got back to us with from the I live team get back to us with some feedback uh that's currently being implemented by  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** someone.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** So those aren't uh any previous requested feedback was implemented.  
**Filippo Tosetto:** Okay. So,  
**Andrei Marinov:** The one with the iOS code.  
**Filippo Tosetto:** the famous document that we were waiting last week that is in the work right now. Cool. That's uh that's good to understand because I'm I'm I'm losing track on all of this. Um which is fine for me because I was already pl thinking that it would take at least uh a few more days. Do you have an idea on how long it's going to take?  
   
 

### 00:05:09

   
**Andrei Marinov:** Um, not really. The Latin says that it shouldn't take more than a couple of days, but uh, let's see how much it takes someone to do it because he does not agree with their estimate.  
**Filippo Tosetto:** which yeah we know that uh okay good to know um that problem on the back end on Friday uh the the that you were investigating what was that  
**Andrei Marinov:** uh not resolved yet. Basically uh Khalid the backend engineer that we let go uh he was using an environment file that had certain Firebase credentials. So when you plug that in into your local environment you can do a release of deploy of the back end. And it seems that Salmon does not have that uh particular environment. And I was going with the uh Julian and the other guys to try and figure out how we can get that. And I was trying to reproduce it on my end, but it's still in progress. We we do still need that.  
**Filippo Tosetto:** Yeah. Okay. This is something I need to get my head around as soon as possible to unify the way back ends are managed in terms of secrets and all of that.  
   
 

### 00:06:34

   
**Filippo Tosetto:** um sort of trying to get the same level of details we have in iOS and Android pipelines for back end basically because what I'm seeing is the more project that we have touching back end the everyone is doing his own thing and when one guy leave like just explained we are in  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** this thanks thank you Um, okay, great. I know that you guys did a submission last week. Have the client been released?  
**Andrei Marinov:** uh 1.2.0 was released. Uh we're still in preparation for  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** 1.2.2.  
**Filippo Tosetto:** And what's the difference between the two?  
**Andrei Marinov:** Uh I have to pull the the tickets exactly.  
**Filippo Tosetto:** I know. Okay. No,  
**Andrei Marinov:** I don't know them on my head.  
**Filippo Tosetto:** no. it you it was not a big feature specifically for this 2.2 release. It was more like random things.  
**Andrei Marinov:** It's like continuous iterations. Uh every sprint is like being released.  
**Filippo Tosetto:** Yeah. Okay.  
**Andrei Marinov:** We release try to release after each sprint every two  
   
 

### 00:07:48

   
**Filippo Tosetto:** Okay. So,  
**Andrei Marinov:** weeks.  
**Filippo Tosetto:** yeah, which is what I will talk to you about afterwards. Um, regarding this garden feature that uh, everyone thought it was ready to go that I had to rush through getting a back end developer. I guess if Salman is working on the AI lab improvements, this is not going to be touched anytime soon.  
**Andrei Marinov:** Uh that's the interesting thing on what he's working on. We he was asked today in the chat just to see exactly what he was doing. So that's pending an answer. But basically currently he's implementing the feedback from uh AI design. He's doing all the he's plugging in nano banana instead of uh JBD image generation. Uh so he's either like halfway through garden design or he has not worked at all.  
**Filippo Tosetto:** Okay. Is there a way to see these kind of things?  
**Andrei Marinov:** I mean, there's the repo, but it's up to him if he pushes to that repo.  
**Filippo Tosetto:** What about Jira which is kind of the main point here?  
   
 

### 00:09:10

   
**Andrei Marinov:** Uh, he sometimes updates it, he sometimes  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** doesn't.  
**Filippo Tosetto:** Because I see here an AI guardian design for AI but is still in to-do and what I see from him is interior design flow implementing new AI PE.  
**Andrei Marinov:** Yeah. So I guess he's currently working on the AI design AI lab feedback at the  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** moment. That's what he's committed to last.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** So if I had to guess, he hasn't started curtain design.  
**Filippo Tosetto:** Okay. And let me check. How long did it say it's going to take? Eight hours.  
**Andrei Marinov:** Yeah,  
**Filippo Tosetto:** Is this Let's ask from  
**Andrei Marinov:** that's the estimate from  
**Filippo Tosetto:** Ben.  
**Andrei Marinov:** Ben.  
**Filippo Tosetto:** And in your experience, is it something that is actually uh followed or is it like don't  
**Andrei Marinov:** No.  
**Filippo Tosetto:** care but do whatever I  
**Andrei Marinov:** Um,  
**Filippo Tosetto:** want?  
**Andrei Marinov:** last last week he tagged you in one of the chats and he said basically I don't agree at all with this estimate.  
   
 

### 00:10:26

   
**Andrei Marinov:** Uh, I believe and we kind of left it at okay and we talked internally about replacing him.  
**Filippo Tosetto:** Yeah. Okay. Got it. Oh, no. Sorry. It's 26 story points. I was checking the the wrong one.  
**Andrei Marinov:** That's ours still.  
**Filippo Tosetto:** 20\. Yes. So, 26 hours. I think it's going to be easier if I do like this. Yeah. 76 hours. Okay. Okay, which makes it four five day four days roughly.  
**Andrei Marinov:** So on standup today he didn't show and I did ask Milo who is like the project  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** manager QA on their end and he said he asked the Android guy to where someone is at I don't know why I mean they probably sit next to each other or something like that but he also did not know uh the Android guy.  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** So because they were asking when when is the backend engineer going to  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** do 937 which is the first one API endpoint for G flow and I was like I mean that's not done at all the next story the one that we're currently looking at.  
   
 

### 00:11:51

   
**Andrei Marinov:** So how can we wire it up when it's not done? And they were like yeah the previous guys just gave us an API endpoint that uh they're pretty much all the same. So, uh, he gave us the endpoint even though it wasn't done and then he connected it later on so we can do our job. And I was like, if it's pretty much the same, you can just reuse what's currently in there and we'll do the same thing. And they were like, okay. That's that's that's about how it  
**Filippo Tosetto:** Oh man. All right. Got it. Okay. Um Okay. We know this situation is fixing as soon as possible. uh I'm on top of it. I just need procurement to be on top of it as well. But yeah, this team is not going to last long in general because everything that is happening is clear to me that on one hand Salma is not really committed to the project and it doesn't care. Uh and on the other hand, the front- end developers are too junior to to work pretty much.  
   
 

### 00:13:06

   
**Filippo Tosetto:** the fact that you have to point out every time how to do a release. Okay, next. Um, any other blocker or slowdown that you see in this app?  
**Andrei Marinov:** uh for the next release it's going to be the garden stuff the garden design the packing implementation of it so that's that's the big thing at the moment  
**Filippo Tosetto:** Okay. But the back the back end is not really the blocker here.  
**Andrei Marinov:** um yeah  
**Filippo Tosetto:** It's SMA blocker cuz I had the back end ready to go  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** whenever. So, okay.  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Um, anything else on this project that you think it's worth reporting?  
**Andrei Marinov:** I think we went through a lot of it. Pretty much everything.  
**Filippo Tosetto:** Yeah, I think so. Okay, let's talk about our second beautiful app which is IMOD iOS. Um, just three simple questions. I probably already know the question, the answer to most of them, but just please run run me through it.  
**Andrei Marinov:** So on Wednesday, Mi said like we'll talk on Friday to do like the the whole road map thing and talk about next stuff to work on.  
   
 

### 00:14:41

   
**Andrei Marinov:** Then he was out. He didn't join the the standup. He said that he had a co- overlap and uh he didn't join then so we couldn't discuss that and then he wasn't really around on Friday and then he's off today on PTO and he's back on Wednesday. Unfortunately I'm not going to be here on Wednesday. So I guess we'll catch up later on. how everything is going and where we're looking to be. Uh, as far as all the other questions, uh, cheer back quarantine improved, not really planning, no, no estimation yet as well. Uh, the guys are pretty much running out of things to do on the current development stuff. Uh it's again the the priorities uh at the moment are to uh work on 2.2 which is the TPOS release. Uh there were a couple of bug fixes that still needed to be made some super changes and Alexi to test. Uh we're pretty much done with that almost. So this the team is performing well. Uh, and I guess next up is we have another spring schedule for some other things.  
   
 

### 00:16:13

   
**Andrei Marinov:** I'm not sure exactly what they're going to be like, but yeah, maybe I can uh share the the backlog here if you want to. I assume he's seted up some sprint. This is the one that we'll be picking up next and estimating and planning. But it's basically pay wall redesign, setting screen,  
**Filippo Tosetto:** Mhm.  
**Andrei Marinov:** that sort of thing. So yeah, as you can see, uh we're looking to ship this one as soon as possible, which is actually this one. Uh, this one the guys are wrapping up on and this one is to be worked on next, but we haven't had anything any meetings about it yet.  
**Filippo Tosetto:** And I see that a third a third a  
**Andrei Marinov:** And the guy we're pretty much done.  
**Filippo Tosetto:** third of the next sprint is about technical death again. Not a third  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** but  
**Andrei Marinov:** for  
**Filippo Tosetto:** in your opinion do you need two developers?  
**Andrei Marinov:** uh we can probably do with just one and  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** ARM is back this week.  
   
 

### 00:17:30

   
**Filippo Tosetto:** Okay. Um on my end the situation is the following. I talked to Fernando and Jorge which are the PO and PN leads and they explained the current situation that Mikall has been promising the next sprint since mid November pretty much and that you have been filling all the holes with technical debt. Unfortunately, the technical debt is not infinite and especially because Mataniano is starting to ask serious questions about the need of two developers in this project. So, I need to justify those two developers and what I can see is that they've been working well. They have been delivering what you asked to but in the moment the product that you finish the technical that product doesn't have a plan for the foreseeable future on uh on new features. I explained this to the guys to to the two leads and they were extremely surprised about this. So I'm also wondering what are you talking about with your people but that's another story. And um they promised me that they will investigate the situation. And there is a chance in all of this that I see happening which is they do not have any more ideas on how to work on this project to improve it.  
   
 

### 00:19:06

   
**Filippo Tosetto:** That could totally be I have we reached feature all the features that we wanted. Now it's just about keeping one developer busy with you know a bit of technical debt bug but fixing and small improvements here and there which I'm totally fine with. I have no issues whatsoever. I just need to know so I can plan accordingly both the two developers becoming one and your time as well because obviously if you have way less time thing to do here we can start to work on IMO Android in this case which was pushed into you but that's another story um and this is the old conversation so far um there is another big elephant in the room here which is next week I will be in Barcelona because there's the famous QBR so the uh quarterly business review something like that where the product team will be presenting the road maps for the next three months to the board. Those road maps must have been passed through us before going to the board. So, whatever is going to happen there is not going to be nice, but I'll keep you up to date on this.  
   
 

### 00:20:30

   
**Andrei Marinov:** I think that we have mentioned that he's going to Barcelona probably for  
**Filippo Tosetto:** Yeah.  
**Andrei Marinov:** that.  
**Filippo Tosetto:** So, all the engineering managers and all the POS are going to be in Barcelona and there's going to be probably a big arena where we are going to fight. I'm imagining this. Let's see. Anyway, um we know we know the situation. I reported to the right people and it's no more up to to us. Uh what I what I can tell you is that I will probably remove one of the two developers uh in the next couple of weeks. I will let you choose which one you prefer to work with. And most likely as I don't want to burn the second developer as it seems to me that they are working well I will try to repurpose him in another project as easy as AI design no idea or screen mirroring no idea but I don't want to remove a developer that is performing well and let him let it go while we have other projects that needs developers.  
   
 

### 00:21:40

   
**Filippo Tosetto:** So that's my plan. What do you think?  
**Andrei Marinov:** Yeah, that sounds good. Uh, so today Art was a bit late to the standup and since he hasn't been around for like two weeks, I asked the guys what's going on. Is he going to be back this week? Is he still out sick? And they didn't really know. One of them said that he heard something about Arton going to work part-time for some reason and not full full-time, but then Arton joined like a bit later and he didn't say anything and um he seems to be back in order and looking well. So ideally if I can I will keep part but just so you know  
**Filippo Tosetto:** Good.  
**Andrei Marinov:** uh there might be something there where he wants to work more of a part-time and he's maybe discussing that with Ana. Uh yeah.  
**Filippo Tosetto:** Okay, good to know. Thanks for sharing. Uh this is valuable information. Um and let's see how things are going to move forward.  
   
 

### 00:22:50

   
**Filippo Tosetto:** Okay. Anything else on IMO iOS on your side? In all of this madness, how is the product doing regarding, you know, technical debt, code quality and all of that?  
**Andrei Marinov:** Uh we are crushing through a lot of technical dep stories. Uh I still have months of work for it. So lots more there to do. But we've been focusing on dependency injection and getting that into different modules of the app so that uh we would have an easier time writing unit tests.  
**Filippo Tosetto:** Okay. So jumping here while we are at it. If it were for starting to enabling the llinter, what do you  
**Andrei Marinov:** That's uh yeah we can do that.  
**Filippo Tosetto:** think?  
**Andrei Marinov:** Is that the thing where we scan the currently changed files and uh if there are issues there surface them more aggressively.  
**Filippo Tosetto:** This is something that we can discuss between us. I I don't know just while you have free developers I want to just speed up this process as this is for Q1 this two items.  
   
 

### 00:24:12

   
**Filippo Tosetto:** So the sooner we start to to to do this the better it is. Obviously please do not do it today. It's more like do you think it will be valuable and is it going to be an easy process  
**Andrei Marinov:** Uh, depends on what we settle on, but probably yes or both.  
**Filippo Tosetto:** because what what I could do to we could do tomorrow uh during the advisor um kind of weekly we could propose to test this approach with one project and this project being IMO Android uh iOS. What do you think?  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** Is it something that would make sense in your  
**Andrei Marinov:** Yeah.  
**Filippo Tosetto:** opinion?  
**Andrei Marinov:** Uh we just need to land on what we want to implement.  
**Filippo Tosetto:** I agree. Yeah. Before moving forward, we need we need decisions uh at all level.  
**Andrei Marinov:** uh  
**Filippo Tosetto:** Perfect. Nice. Thank you. Let's move to your new best friend.  
**Andrei Marinov:** on that for the assessment uh I did a brief assessment of the tech I I think I wrote to you last week basically there's the usual uh tech that stuff and u architecture let's call that um there were some minor things as far as security so overall there's nothing uh that will stop the release as far as I can see I think it's perfectly fine to release it.  
   
 

### 00:25:47

   
**Andrei Marinov:** It is uh the biggest thing was the ATS equivalent where everything is HTTP but we have that on my mode as well iOS so it's not like uh what's going to be a big departure from the iOS side. Uh so yeah, nothing that jumps out at me that would uh prevent the the release of the app tech.  
**Filippo Tosetto:** That's that's very good good to hear because before  
**Andrei Marinov:** with the caveat that I have no idea of Android.  
**Filippo Tosetto:** Christmas Andre I I know um we are you are in my same position before Christmas I did through uh a cursor uh an exercise similar to this and if pointed out a few things uh but they have been solved the majority of them uh beside the security point that you found out about which is also in iOS. So it's live. We have to to to go on with that. There were some issues regarding error um reporting errors to the user but that's more UI stuff which I know you have no control over. Uh and for that I will rely more on Oscar while he's testing.  
   
 

### 00:27:08

   
**Filippo Tosetto:** Um, for the very little time that you spent here in this IMO Android, do you have any red flags from a product perspective? How the app is run from a product perspective?  
**Andrei Marinov:** Uh, not yet. I literally got invited on on Friday. So, it's just been like half a day.  
**Filippo Tosetto:** No, no problem. So overall status in your opinion of the project beside the very bad quality of the code. Anything else?  
**Andrei Marinov:** Um, nothing to point out yet.  
**Filippo Tosetto:** Okay.  
**Andrei Marinov:** I'm still very early.  
**Filippo Tosetto:** So yeah, agree. So I'm what I'm going to do is I'm going to use this week as a sort of buffer uh before giving the green light. And if you have a bit more time to run through things just to see if actually this app is we can release it without incurring any major problems. Uh and then probably towards the end of the week if you don't come back to me with anything major I will give the green light on the coding side for the release and then I will meanwhile talk to to Oscar regarding the QA side.  
   
 

### 00:28:34

   
**Filippo Tosetto:** As I said, the sooner we get this up in the store, the better it is because we can rotate the team, get a better team, and start to work on it properly as a full kind of uh product growth perspective. Cool. I want to talk to you about something else now. And uh um it's more like an uh for you for uh to to give visibility to you what's going to happen in the next few weeks. So since November um or even before probably uh there's been um a talk about what's called north project. North project is a a huge initiative that will tackle all MA um projects all the apps but also all the web subscriptions and all the departments involved and I'm not going to bore you with all the details but what is it and why is it going to be in put into place what is it is standardization of the way we work across all the projects So that that goes from a simple all the Jira boards will be the same with all the Jira states to other things like all the sprints must be two weeks and there must be at least one release every couple of sprints at least one.  
   
 

### 00:30:16

   
**Filippo Tosetto:** uh two uh moving to calculating story points no more in hours but more on effort so the usual progression of 1 135 7 whatever I don't remember top of my head uh but also and this is something that is very very interesting in my opinion and that is going to help us plan which is all the jira boards must have one month one rolling month of estimated user stories ready. So, one month of user stories ready and three months of product road map. How does this product road map come into play? They're going to be Jira epics and they will have highlevel estimates. So what am I expecting here is that the PMS will present to engineering managers three months product road map that we will discuss with you guys developer advisors and ask for you you know we we will do probably a high level estimates but we want to run things through you to make sure that it is feasible and on your end you must check that in the Jira board there are enough user stories to fill one month uh after the current sprint plus all the um agile ceremonies must be done in the same way and all of this.  
   
 

### 00:31:56

   
**Filippo Tosetto:** Why do we want this kind of homogenization of of all the way we work uh across all the apps? Because as of today I mean you have visibility you have IMO that works in a way IMO Android that works in another way you have AI design that works in a totally different way this is not sustainable first of all and second if we need to track and measure the um productivity of the developers we need a way to compare apples to apples you know Um and that's it. That's the in a nutshell what is north project. The north project will be rolled out in the coming weeks app by app. I know that we will start with apps the first week of um first week of February. uh but for us I think it's going to uh catch us in the second week of February with uh all the launches apps and then it's going to go to IMO the third week of February. So we still have time and there's going to be probably you know I wouldn't say delayed but some feedback once they start to roll this up uh to to the first uh uh projects.  
   
 

### 00:33:19

   
**Filippo Tosetto:** What do you think?  
**Andrei Marinov:** That sounds great. I mean more standardization I feel like we will help our things a lot. Like for example I design we use ours and I mode we used story points and yeah it's not as easy to jump between the two projects. I'm not even sure what we use on my old Android if it's story points that are very shocking to me. But uh yeah, that sounds like a good idea. As far as uh which one would be the the hardest one to comply, I feel like between AI design and I multi there it's pretty much a tie uh for different reasons uh to to standardize. Uh if you're changing the team, it will be a good time to switch to story points. and on AI design for IM mode. Uh like we've discussed, we have some uh road map issues. I don't know where we want to be and how we get there. So yeah, I wouldn't say that one of the two is like harder to comply than the other one.  
   
 

### 00:34:32

   
**Andrei Marinov:** They both have issues. Yeah.  
**Filippo Tosetto:** different issues for different projects pretty much. Okay. Yeah. Uh it's going to be interesting to see this thing. Uh I have no I'm happy that this is going to happen. I'm very curious to see if it's sustainable over time because it seems to me that from an engineering perspective we are pretty good at keeping processes running and it's the other side of of the fence that seems a bit more slippery but let's see let's see okay I just wanted to talk to you about one last point here which is something that David Matano started and I think it's good for you to know in general. Um so Latiano created this uh OKRs for Q1 and uh it's mainly for him and obviously it cascade down to us which cascade downs to you but uh I want you to be aware of what we are planning to do this quarter because this will help you plan in general in my opinion and I think the idea is split in different areas and I'm just going to go through them and I'm going to give you a brief description.  
   
 

### 00:36:08

   
**Filippo Tosetto:** So first objective is to strengthen the team in general and uh we are trying to close the first uh the the last position that was open since 2025 which is to hire another developer advisor that will work with us me and you. And um the good news is that um went through a set finally went through a set of interviews with some good candidate this uh this uh since we came back from holiday and uh we extended an offer to an old colleague of Andre uh Andre Montenegro and uh let's see because we also extended an offer to a guy in December but he rejected it so we are back to square one. The good news is that we also have a couple of other very strong candidates in the pipeline. So I'm sure somehow we're going to cover this as soon as possible. Which bring us to the second point which is hiring another developer advisor for under Montenegro. And so that is it. Uh these are things for web don't care. Um this is interesting.  
   
 

### 00:37:21

   
**Filippo Tosetto:** Creation of a new internal growth team for a key application. This is very very interesting in my opinion. I'm not sure how this is going to be defined on what, but basically the idea is to start to hire an iOS developer or a team of iOS developers to work on an internal app. No idea in which way this is going to go. But the point here is that well we have apps that are making tons and tons of money. see AI cleaner instead of outsourcing the development maybe is the case to bring the developer inhouse so we control every aspect of it. No idea. This is out of my control. Let's see. Uh your teams don't care. This is something that me and you care a lot which is uh the rotation of the non-performer contributors and we already have some uh beautiful uh KRS so key results which are potential IMO Android rotation of the old AI design external team and rotation of the screen mirroring team. I added another point I need to discuss with because for me there is a bit of friction here on how to on board a new external team or person and uh so the idea for me would be to formalize this but I want to discuss Mataniano if he thinks he's a good idea.  
   
 

### 00:38:47

   
**Filippo Tosetto:** Moving to objective two which is maximize the operational efficiency and we are going to go down to monthly performance analysis that goes to the developers user stories delivered story points delivered the data in forward that I share with you and the no QA state for each user story goes down to QA things that  
**Andrei Marinov:** Singing.  
**Filippo Tosetto:** probably but you know describing test cases and then s as well and here we're talking about what I just explained so a month of ready user stories in each project and three months road map for each uh project which will lead to finally being able to create a capacity plan for our project which in the case of IMOS having this visibility would help a lot today to schedule you you know, oh, we need just one developer or we need two developers just for a month. So, these kind of things. Um, this is about QA advisor which already started in a few of my projects and most likely it's going to trickle down to all my projects. Uh, but uh the idea is instead of our internal QA to duplicate the work is just to do an advisor role and they will check 20% of the user stories.  
   
 

### 00:40:16

   
**Filippo Tosetto:** So some basic things here there are a few things that in my opinion are quite interesting and um regards you as well 100% of pipelines with sonar cube and llinters integrated Victor will be leading this but you know still we'll need our help creation of technological initiative to reduce identified critical technical debt No idea but I think it's a matter of understanding what is the common denominator in all the projects and trying to solve it by creating you know a lit tech package or something like that. Um this is for SRE so Google cloud platform usage and permission and all of that and uh um increase the technology division of MA and LIT tech. In few words what I want to do here is to start to migrate all the backend repositories that are in lit in the lit corp GitHub account and migrate them into Roska. Why is that? because we have more control first of all and second we have all those permissions with the groups that we can easily move uh kick out developers and integrate the whole thing with the rest of the pipelines.  
   
 

### 00:41:46

   
**Filippo Tosetto:** Why write an architecture and quality requirement document for development testing? Oh, this is going to be fun. This is mainly for Victor. Uh, I guess this is going to come out as a sort of developers guideline. No idea. Um, to control all the apps of our portfolio, which means I'm at Android completed thanks to you. Yeah, already. The other one is screen just being  
**Andrei Marinov:** What does control mean?  
**Filippo Tosetto:** advisor because having you there means that we know what's happening and if not you can investigate uh as of but but you know as of  
**Andrei Marinov:** You're  
**Filippo Tosetto:** today I'm for instance I'm completely blind for screen mirroring. I have no idea. And this is probably the first stop that I will give to the new developer advisor. Uh there's also obviously M\&A and this is also interesting in my opinion which is integrate AI tools into daily workflows, code review, documentation and all of that. uh for me this is something that needs to happen very very soon because it's going to help us and I think all the rest is not important for us because one is mainly for M\&A uh so we have a I don't know how much you know about M\&A but it's basically we are acquiring apps and companies and uh it's a nightmare because we need to get those apps to use our processes and it's not as easy as it seems.  
   
 

### 00:43:38

   
**Filippo Tosetto:** And as last point, uh we have we are launching a set of our applications into China, which is we are sort of forking our code base and create another version of the app in China with a Chinese account. Uh and Andre Montenegro is on top of this. Any question? Any  
**Andrei Marinov:** Seems straightforward.  
**Filippo Tosetto:** ideas?  
**Andrei Marinov:** uh which specifically I mean there's a lot here on the architecture the AI tools the cross team engineering stuff that's also interesting the pipelines I think that will be easy uh the technical depth that's going to be very interesting as well there's a lot there tons of ideas on all of these I lesson.  
**Filippo Tosetto:** I think we will discuss to about some of them together in the coming weeks because I think you you could have very interesting inputs on the AI tools but also uh where is it  
**Andrei Marinov:** Yeah, that's probably the most interesting for  
**Filippo Tosetto:** yeah but also on the technical that part by having visibility of the code bases you may already have an idea of what's there but I think also on this one could be very interesting on the pipelines in general.  
   
 

### 00:45:10

   
**Filippo Tosetto:** Okay. Um that was my last point to give you visibility in general. Is there anything you would need me you need from me to unblock you to do anything?  
**Andrei Marinov:** I guess uh since I'll be out until the end of the week and I also might need some dates next week as well depending on how I go about uh if there is anything should I tell people to reach out to you or Okay.  
**Filippo Tosetto:** That's the best thing to do. Um, just write a message saying I'm out for x amount of days. Just ping and you ping me and you you add me. Uh, I'm trying I usually try to read the all the chats for all the apps where I'm invited at least once a day just to see if maybe something is is missing. But please tag me there so people know that they can talk to me directly. Thank you. And I don't know if you had already this planned, but if you could spend just do you do you have you created a sort of document for um the assessment that you did for IMO Android?  
**Andrei Marinov:** Uh just like uh for some of the technical that stuff, nothing else. But yeah.  
**Filippo Tosetto:** Yeah, if you can just share it just well. So I I have a bit of an idea what's there. Um, cool. That's it then. That's it. Great. Thank you. I'm going to stop presenting this. I'm going to stop also the the onetoone recording notes because yes,  
   
 

### Transcription ended after 00:47:02

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*