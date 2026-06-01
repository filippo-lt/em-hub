Jun 1, 2026

## Vlad / Filippo \- Weekly 1:1 \- Transcript

### 00:00:00

   
**Filippo Tosetto:** Good afternoon.  
**Vladyslav Krut:** Hello.  
**Filippo Tosetto:** All good.  
**Vladyslav Krut:** Well, I had better days.  
**Filippo Tosetto:** You went to the doctor this  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** morning.  
**Vladyslav Krut:** So on Saturday I got sick like full scale getting cold, you know, like with temperature weakness and stuff like that. So I planned today on Monday morning go to the doctor.  
**Filippo Tosetto:** No.  
**Vladyslav Krut:** So I went. Uh now it's I'm better. I'm not as bad as it was on the weekend, but it also means that I lost the weekend. I didn't go to my friend's birthday, stuff like that. So, yeah, that sucks. And today, yeah, I went to doctor. I wasted insane amount of time there because of Spain.  
**Filippo Tosetto:** because of south of Europe. Yes.  
**Vladyslav Krut:** Yes. Okay. And now I'm back and I'm seeing a lot of stuff for me is required for AI design. And I'm like,  
**Filippo Tosetto:** No,  
**Vladyslav Krut:** okay,  
**Filippo Tosetto:** no, no,  
**Vladyslav Krut:** it's like eight different  
   
 

### 00:01:26

   
**Filippo Tosetto:** no. Vlad, Vlad, let me stop you here. Nothing requires your any action from you in AI  
**Vladyslav Krut:** tasks.  
**Filippo Tosetto:** design. So do not stress out about this. Already handled everything because this is I know exactly what's the problem there. It's they need to read the documentation. Developers need to read the documentation.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** As easy as that.  
**Vladyslav Krut:** Many times it is.  
**Filippo Tosetto:** So,  
**Vladyslav Krut:** Yeah. I spend my Thursday somewhat like that. Yes.  
**Filippo Tosetto:** um don't worry, we can uh I'm following up.  
**Vladyslav Krut:** I You're wrong.  
**Filippo Tosetto:** Sorry.  
**Vladyslav Krut:** I said I assume it's not like burning urgent but it's still like a lot of messages and I'm like okay let me think where should I start and I well I did some progress it turned out I didn't have a proper access to play console to  
**Filippo Tosetto:** already.  
**Vladyslav Krut:** for now by the way how did you fix it are we allowed to  
**Filippo Tosetto:** Already fix that.  
**Vladyslav Krut:** add as testers external developers and their personal accounts or not Yeah.  
   
 

### 00:02:43

   
**Filippo Tosetto:** Oh no, I fixed another thing on the play console.  
**Vladyslav Krut:** Okay. Well, they have one more is asking to add one of his accounts.  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** For some reason, we he cannot test it because of device restriction on his atex external. So, he asked to add his personal one and I'm like, I've just got access. I'm not really sure if we allow it to do that. Miguel flagged that we may not be able to do that. Uh but then they Miguel asked me to figure out if we are allowed to do that or not. And I'm like okay let me  
**Filippo Tosetto:** Plug me in the conversation so I I know what we are talking about and I'll do a bit of research on other  
**Vladyslav Krut:** see.  
**Filippo Tosetto:** apps. I I doubt we can allow people to add their personal accounts but let me let me do my investigation on that  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** point.  
**Vladyslav Krut:** taking you right now because I will forget  
**Filippo Tosetto:** Yeah. U the second burning issue on AI design is the implementation of the quota system  
   
 

### 00:03:41

   
**Vladyslav Krut:** later.  
**Filippo Tosetto:** and parapet and we go always back on the same problem which is developers don't understand how revenue cut works. Um,  
**Vladyslav Krut:** Yeah, I noticed this part. Not sure if I understand how it works, but usually when something doesn't work,  
**Filippo Tosetto:** look,  
**Vladyslav Krut:** I go to documentation first and then asking  
**Filippo Tosetto:** it's um it's not as straightforward.  
**Vladyslav Krut:** people.  
**Filippo Tosetto:** Let me I'm going to explain it to you so that you have this knowledge uh yourself. Um, revenue cat assign um user ID every time a new installation of the app happens.  
**Vladyslav Krut:** Yeah, this part is clear.  
**Filippo Tosetto:** Um, if you download the app on your phone, you open it, you killed it, you delete it, you reinstall it, you delete it, you install it, you delete it, you install it, you will always have a different ID  
**Vladyslav Krut:** Yes, that's how we have 285 Alexis  
**Filippo Tosetto:** until until  
**Vladyslav Krut:** accounts.  
**Filippo Tosetto:** you do a purchase.  
**Vladyslav Krut:** Oh.  
**Filippo Tosetto:** In the moment you do a purchase that ID becomes the associated ID to your device.  
   
 

### 00:05:06

   
**Filippo Tosetto:** So that let's say that download the app once you have ID  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** one delete it download the app two twice your your ID is two you delete it you download the app third time your ID is three and you make a purchase. From that moment on your ID is three and that is called  
**Vladyslav Krut:** And that's what's called original ID,  
**Filippo Tosetto:** correct. Now when you delete the app,  
**Vladyslav Krut:** right?  
**Filippo Tosetto:** you reinstall it and you open it again, it's going to be four. Your ID is four.  
**Vladyslav Krut:** Until you restore the purchase,  
**Filippo Tosetto:** Correct?  
**Vladyslav Krut:** right?  
**Filippo Tosetto:** In that case, you go back to three and one, two, and four are going to become all aliases for the user ID three.  
**Vladyslav Krut:** Yeah, that makes  
**Filippo Tosetto:** What am I sus?  
**Vladyslav Krut:** sense.  
**Filippo Tosetto:** My suspicious suspicion right now is that on AI design they don't use the original ID. They use the alias. What's happening is that they made a purchase and they fetch the data with the alias instead of the original ID.  
   
 

### 00:06:20

   
**Vladyslav Krut:** where when we are talking about they are using alias instead of the original they are using that ID where like back end or mobile because mobile doesn't I don't think mobile allows us to like have a clear  
**Filippo Tosetto:** Mobile. Mobile.  
**Vladyslav Krut:** separation whether revenue get identifier is regional or an alias.  
**Filippo Tosetto:** It does. It does. There is a way to retrieve the original ID.  
**Vladyslav Krut:** H really okay that's very new is the tricky way  
**Filippo Tosetto:** There is a way.  
**Vladyslav Krut:** like work out you know  
**Filippo Tosetto:** I don't remember the name,  
**Vladyslav Krut:** like okay I will I  
**Filippo Tosetto:** but if you check the documentation, it's  
**Vladyslav Krut:** will and what happens if you uh got your ID3 you got a torches you  
**Filippo Tosetto:** there.  
**Vladyslav Krut:** reinstalled the application you get ID4 you perform performed another purchase and after that you pressed restore. What will  
**Filippo Tosetto:** Well, if you try to do a second purchase,  
**Vladyslav Krut:** happen?  
**Filippo Tosetto:** if your subscript if your previous subscription is still alive, let's say, you're just Apple will force you to do a restore.  
   
 

### 00:07:33

   
**Vladyslav Krut:** Oh,  
**Filippo Tosetto:** So, you're unless you're buying a different  
**Vladyslav Krut:** okay.  
**Filippo Tosetto:** product,  
**Vladyslav Krut:** Okay. Then what if you buy a different product?  
**Filippo Tosetto:** your ID will still become three, the original ID. And that's it. you're just purchasing a second  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** product.  
**Vladyslav Krut:** So there is no way to make. Okay. I  
**Filippo Tosetto:** Um,  
**Vladyslav Krut:** see.  
**Filippo Tosetto:** there must be a way for you on mobile to restore the original ID though because otherwise how can you fetch from the back end/parapet the quotas  
**Vladyslav Krut:** What I thought it may be incorrect as now you're explaining is that mobile is only aware about the ID revenue gives us which may be either original or alias and we don't have a way to distinguish and then this separation or look up for the correct original ID is something that happens on back end. That's what I  
**Filippo Tosetto:** you know, no, no, no, no, no, no. Sorry, I may have misspoke before.  
**Vladyslav Krut:** thought.  
**Filippo Tosetto:** There are no two methods to get the ID of the user.  
   
 

### 00:08:52

   
**Filippo Tosetto:** It's simply that after you make a purchase, you need to refresh. So, ask again to revenue cat your ID.  
**Vladyslav Krut:** Oh, okay. This part. Okay, then sure. This part is clear.  
**Filippo Tosetto:** And with that information you can ask again to the back end,  
**Vladyslav Krut:** Makes  
**Filippo Tosetto:** hey give me my quotota.  
**Vladyslav Krut:** sense. See, I see now it's I see the API. There's only one API. It's called app user ID, but you got to ref it after the purchase.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** And you may need to override what you had before. Oh, that's explain so many bugs. Yeah, fine. Okay.  
**Filippo Tosetto:** So the the back end uh think about it that the back end itself doesn't know anything about revenue cut or anything. It just takes the ID that you send from the mobile and send it over to parapet to say hey give me the quota for this user.  
**Vladyslav Krut:** Okay, then does parapet execute this look up or parapit or always returns the account that is being requested and doesn't matter if this is an alias or an original one.  
   
 

### 00:10:06

   
**Filippo Tosetto:** Assume that it doesn't do a look look up.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** It does, but assume it doesn't. Why am I say assume it doesn't? Because the refresh takes time. So revenue cat do the um um what's the word reconciliation of the ids in time. So it's not an atomic operation.  
**Vladyslav Krut:** Mhm. Okay. Makes  
**Filippo Tosetto:** So I make a purchase with ID4 which is a  
**Vladyslav Krut:** sense.  
**Filippo Tosetto:** restore but before revenue cat recognize that I'm actually user three it takes a bit of time.  
**Vladyslav Krut:** Makes sense.  
**Filippo Tosetto:** So the best way to do this is I make a purchase or a restore. I refresh my user ID from revenue cat and then I use this one to ask parapet what's the quota.  
**Vladyslav Krut:** Okay. Okay. That should not be difficult to implement on mobiles at all.  
**Filippo Tosetto:** No, it's not. I see.  
**Vladyslav Krut:** It's really It's really not.  
**Filippo Tosetto:** But again, you need to read the documentation as a developer to understand how revenue cat IDs work and how parapet works.  
   
 

### 00:11:33

   
**Filippo Tosetto:** And we have the documentation for both things. You just need to go through it as a developer. Blood, you're smiling.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** I've seen your PR, your huge PR.  
**Vladyslav Krut:** Yeah, I was not really expecting anybody to review  
**Filippo Tosetto:** No, I didn't review it. I was just curious.  
**Vladyslav Krut:** it.  
**Filippo Tosetto:** I went as through it. I just curious to see what actually happened in there. And from what I see, good job. Um,  
**Vladyslav Krut:** Thanks.  
**Filippo Tosetto:** it was much needed.  
**Vladyslav Krut:** I believe so. Yes.  
**Filippo Tosetto:** Yes. So, what's the state of things  
**Vladyslav Krut:** So what we have now we have  
**Filippo Tosetto:** now?  
**Vladyslav Krut:** a new API being used for everything but retouch tool primarily because we had this work around uh around the quarter deduction on retouch and we already have a ticket created and like a bug ticket for this sprint. So I was like okay let me not break it keep it as it is because there is a reason it was implemented this way that I'm not aware of and we will discuss it this this week and then I will migrate it and implement it in a way that it's expected in the way that product will define I hope this week other than that uh what we have we have a project like when you upload a picture for the very first time or take a  
   
 

### 00:13:09

   
**Vladyslav Krut:** selfie we have a project and we store the original image with unique identifier. And then every time the user applies any kind of filter or modification, we save a step or a modification on top of this uh original image. And then we do this iteratively many times. We persisted all these changes which what and that allows us to do undo and redo at any time and reference any of the images in history after the application restart for example.  
**Filippo Tosetto:** Yep.  
**Vladyslav Krut:** U then we have some not like workarounds but no that's actually not work that's how it's supposed to work. So uh now when we are using the original the the ID that is stored on the back end we have quite a lot of tools that allows the user to modify locally apply some kind of filters like background adjust vignette uh LUT filters whatever you have like 13 tools 10 doesn't matter obviously back end have no idea about these images as they were applied locally So we every time the user want to apply any kind of remote filter, the application goes and checks if the last modification applied has this backend image ID.  
   
 

### 00:14:37

   
**Vladyslav Krut:** And if it does, we just use this image ID. We reuse it. Otherwise, we execute the analyze endpoint once again to upload what we have and to obtain the one and then send the processing which is supposed to reduce our loading time quite a lot. U then we do not store all the like details and metadata of each specific step because I don't believe we may need it at any time. I will explain what that means. That means that uh the history of changes inside one specific screen. So let's say I opened a adjust tool and while I am on the adjust screen I am keeping the history of the local adjustments but once I use the user presses apply we create the final snapshot persisted to the database and then eliminate all the previous steps because we don't need need to catch them at any time and that's pretty much how it works in simple all terms.  
**Filippo Tosetto:** and this is the implementation that I've seen pretty much.  
**Vladyslav Krut:** Well, that's how I implemented  
**Filippo Tosetto:** Yeah.  
   
 

### 00:15:52

   
**Vladyslav Krut:** it.  
**Filippo Tosetto:** Which in my head is how it's supposed to work. Why wasn't it working like this before?  
**Vladyslav Krut:** That's a very good question. But now we also have possibilities like we can open the project. We can undo three steps. For example, we can export this image if you if we would like save it locally applying all the watermarking logic and whatever other premium flag checks we have. Redo this again. We have an opportunity to duplicate a project that we had before but before it was not needed because we were creating new project every time user pressed apply. There were absolutely no point. Now there is a point.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** Now we have the opportunity to undo some changes and persist this undone state. So like eliminate last few modifications which I feel like was necessary like  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** why didn't we have this opportunity before? Why didn't we have persistence across app launches for the logic at all? Uh well now we have to me it feels like now it's working the way it's supposed to.  
   
 

### 00:17:06

   
**Vladyslav Krut:** like a proper document based  
**Filippo Tosetto:** Yes. Yes.  
**Vladyslav Krut:** application.  
**Filippo Tosetto:** That's how it should work for documents in general. This case images, but that's Yeah. Okay. Um, you also mentioned the fact that from a performance point of view,  
**Vladyslav Krut:** Of  
**Filippo Tosetto:** the fact that we don't keep sending over and over and over the same image to the back end, we gain a bit of  
**Vladyslav Krut:** course I did not measure it but as we don't have the image uploading  
**Filippo Tosetto:** performance.  
**Vladyslav Krut:** anymore we of course expected to see some reduction and if it's necessary I was thinking about this but not in the scope of that we are we can add specific login if we decide that we need. So, but I would leave it up to product to decide whether we want it or not. We have ause now to log the back and forth and I don't think we have  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** anything to optimize or to speed up or to reduce regarding image processing locally. That's almost state-of-the-art almost.  
   
 

### 00:18:08

   
**Vladyslav Krut:** I am saying always because there are some uh filters that are being applied locally that are probably not supposed to do a few concurrent operations on the main thread. But this will be worked in the other scope of the of the in the scope of some other  
**Filippo Tosetto:** Yeah. Yeah. Great.  
**Vladyslav Krut:** tasks.  
**Filippo Tosetto:** Thank you. This is very very nice. Um, so now you have a few other things to work on which are part of that list that that you provided and I know that Reuben already started to add other tickets as well.  
**Vladyslav Krut:** Yes, I saw there are few the ones that he added looked very  
**Filippo Tosetto:** So  
**Vladyslav Krut:** like adequate to work on to me and his reasoning was to create a vision that we are delivering something other than tech debt. And what we what he added are small tasks that are quick to do but that have  
**Filippo Tosetto:** yes,  
**Vladyslav Krut:** somewhat noticeable impact. That was his  
**Filippo Tosetto:** exactly.  
**Vladyslav Krut:** idea.  
**Filippo Tosetto:** So you met Reuben, you started working with him.  
   
 

### 00:19:27

   
**Filippo Tosetto:** How's your perception?  
**Vladyslav Krut:** Uh well so far it was really good all the time but one meeting one Friday I feel like Friday is our freaky Friday day I don't know what was that why why so what we had on Friday on Friday well one day before on Thursday Reuben proclaimed that we will not be dedicating time to develop and to test the application on smaller devices.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** Interesting move. Okay, I don't care. I don't need to be asked twice. Then on Friday, Alexi asked Reuben to specifically clarify what small device means and proposed a list of like screen like up until which screen we do support and like what where should we stop? And in answer to that, Reuben created a task or an epic separate one for like bugs existing for smaller screens without defining what smaller screens are. And by doing that, Reuben brought insane amount of confusion between Alexi, Maria and I was also like so we do test it, we do not test it, but we report error in this bug in this in this ticket, but we don't test it.  
   
 

### 00:21:02

   
**Filippo Tosetto:** Epic.  
**Vladyslav Krut:** What is happening? And yeah, this was very interesting conversation because Alexi rejected completed to be flexible  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** about this. And I'm using the word flexible because this is one of the examples how after this meeting, Maria in DMs asked Alexi to be more flexible and sometimes shut the f\*\*\*\*\*\*. I probably was supposed to stop recording.  
**Filippo Tosetto:** It's okay. It's okay.  
**Vladyslav Krut:** I think that's fine. And um yeah, so from now on, Alexi will try to be a little bit more flexible and sometimes keep it quieter when something is not  
**Filippo Tosetto:** Okay.  
**Vladyslav Krut:** clear. While I am still not really convinced on what's a small device and why don't we support them like I not talking like first generation SE phones but iPhone 13 mini is existent popular and SE third generation is very popular. Why don't we how and we have a design we have a in Figma four variations dark team light theme and the same two for smaller devices. So designers are doing their job defining how it should look.  
   
 

### 00:22:26

   
**Vladyslav Krut:** So now we should not be testing it. Like  
**Filippo Tosetto:** I think. But this is me inferring.  
**Vladyslav Krut:** why?  
**Filippo Tosetto:** It's I don't have enough data here to support my claim. But I think the number of people using a small device is such a little number compared to the rest that it's not worth to spend the time. And we do this in other in all the other apps by the way. So we have apps with way more users than face AI and we rarely test on small device. I agree with you. The definition of a small device is very very blurry. So having it clear would help a  
**Vladyslav Krut:** Yeah,  
**Filippo Tosetto:** lot.  
**Vladyslav Krut:** at least this one I feel like Reuben could have defined a device size especially considering Alexi pro provided a list like sorted  
**Filippo Tosetto:** Reuben is not that technical so you need to help him. It's not a it's not against understanding. It just need a bit of handholding with specific things. So if you found that it was a bit lost, it's probably because he doesn't understand that part yet.  
   
 

### 00:23:43

   
**Vladyslav Krut:** That's what  
**Filippo Tosetto:** So my ex my experience with him is he's willing to  
**Vladyslav Krut:** they  
**Filippo Tosetto:** learn about things but he needs to be of training on specific parts. That's it.  
**Vladyslav Krut:** see.  
**Filippo Tosetto:** So try to use simple words to explain. Hey Reuben, um maybe with data uh iPhone I don't know 13 mini um was out in 2021 and uh this is the the majority of the market that has it only 3% while on this size we have so try to provide the claims with some data so we can understand all of this.  
**Vladyslav Krut:** Okay, that's something that I think I can do.  
**Filippo Tosetto:** Um my advice, you will see a huge difference between Herardo and Reuben. Uh Herardo, let's forget about the experience. Uh but Reuben is very organized and he needs order. So the this next this month will be about him getting to understand a bit more the whole application the team how you guys work and it will require writing how the application  
**Vladyslav Krut:** that's what I thought originally that okay we can get anything defined from  
   
 

### 00:25:03

   
**Filippo Tosetto:** behaves  
**Vladyslav Krut:** Ruben but we should not do this on the standup instead we should write it in the chat and let Ruben time to do a research and to think about this and maybe he will come and consult consult later and he was doing that. He was coming to me in DMs and asking how this work, how that works. So generally speaking, the experience is positive.  
**Filippo Tosetto:** So  
**Vladyslav Krut:** I think now team needs to understand that maybe being on the call  
**Filippo Tosetto:** yes,  
**Vladyslav Krut:** answering difficult questions or making decisions life is not a move.  
**Filippo Tosetto:** and that's Why I think your skill of being able to push back in a nice way that I've seen happening in a few meetings, you need to use that a bit with Reuben because Reuben likes to talk a lot, likes to have very long meetings. So my ex Yes,  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** my experience with Reuben is hey give me I need to do some research personally  
**Vladyslav Krut:** Not  
**Filippo Tosetto:** before answering. I will write you a document on Slack channel or whatever in the in the so you have all the information that you need.  
   
 

### 00:26:19

   
**Filippo Tosetto:** It doesn't make sense for us to stay here to discuss about this. So again, it's about communicating with  
**Vladyslav Krut:** Yeah. And now it maybe even not about me protecting my time.  
**Filippo Tosetto:** him.  
**Vladyslav Krut:** It's more about protecting his time because because Yeah. I noticed that moment once he's lost, it's it's like very stupid AI, you know, going spiraling on the spot, not getting anything.  
**Filippo Tosetto:** I've seen Ruben stressed twice and it's exactly for this reason. So stop him say, "Hey, let me provide better information. I'm going to write you the proper document or Rajira ticket or anything." It will save your time and his time.  
**Vladyslav Krut:** Makes sense. Yeah, we'll be doing this way from now  
**Filippo Tosetto:** Um, nice. So, again,  
**Vladyslav Krut:** on.  
**Filippo Tosetto:** thank you so much for this. Um, and thank you for being proactive in this way in the team because it's a one of the skills that I like about you that you are very open and describe this thing. No, but it's it's it's very important when you do my job having to deal with a lot of different type of developers.  
   
 

### 00:27:35

   
**Filippo Tosetto:** Having someone that communicates in a proper way is always a plus. It's true. Um,  
**Vladyslav Krut:** more from Germany  
**Filippo Tosetto:** it's Germany. Uh, I'm not sure I can work with German people. It's personal. Uh, yeah.  
**Vladyslav Krut:** They're very direct associating with their  
**Filippo Tosetto:** Um,  
**Vladyslav Krut:** communication.  
**Filippo Tosetto:** you never work with uh people from the Netherland then?  
**Vladyslav Krut:** Everybody is talking about that. I honestly really like working with these guys. It sounds very rude,  
**Filippo Tosetto:** muted. No,  
**Vladyslav Krut:** but it's so efficient,  
**Filippo Tosetto:** I agree. I agree with you. I agree with  
**Vladyslav Krut:** but it sounds rude. But then it's not like they're angry.  
**Filippo Tosetto:** you.  
**Vladyslav Krut:** Then after the work is done, you can go together to bar and be like friends, colleagues. Fine. No  
**Filippo Tosetto:** Yeah. Yeah, I agree.  
**Vladyslav Krut:** problem.  
**Filippo Tosetto:** Why not? Um, another point here is we literally have one month time to get this up to a good state.  
   
 

### 00:28:40

   
**Filippo Tosetto:** So,  
**Vladyslav Krut:** That's not just one month.  
**Filippo Tosetto:** what I need from  
**Vladyslav Krut:** That's the whole month.  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** That's a lot of time.  
**Filippo Tosetto:** But yeah,  
**Vladyslav Krut:** Okay, I will shut up  
**Filippo Tosetto:** you never H exactly.  
**Vladyslav Krut:** now.  
**Filippo Tosetto:** Something that you need to learn is when you talk about deadlines and timelines, always double it.  
**Vladyslav Krut:** Okay. Yeah, that would save somebody one day.  
**Filippo Tosetto:** But uh no, the important part for me here is twofold. The first one is to know if you have any blockers and we need to make sure that if the blocker is coming from product they know about it and is documented somewhere. I'm saying this for political reason. So hey I'm still waiting for the document on how Firebase works writing in the common chat.  
**Vladyslav Krut:** I see. Okay, I understand  
**Filippo Tosetto:** Ruben is not that kind of guy. Just write it there though.  
**Vladyslav Krut:** for for all of us. Safe safety.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** Yes.  
   
 

### 00:29:53

   
**Filippo Tosetto:** Or in a Jira ticket. Totally fine. As long as it's documented in a public space.  
**Vladyslav Krut:** Yeah, makes sense.  
**Filippo Tosetto:** Uh second, if you see something big that will delay you, please let me know because in the moment you tell me,  
**Vladyslav Krut:** Okay, I will  
**Filippo Tosetto:** I can start to jump in and uh tame expectations from the product side of things or from QA as well or from QA as well.  
**Vladyslav Krut:** or what?  
**Filippo Tosetto:** Expectations from QA as well.  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** That is it on my end regarding Face AI. These tickets that you have are still  
**Vladyslav Krut:** uh in face AI.  
**Filippo Tosetto:** okay.  
**Vladyslav Krut:** Yes, everything is either clear or I am good enough to imply what needs to be done. On Friday, I started investigating some of them. A few of them I pushed back to Reuben and I saw he did some progress. I saw a comment of Dimitrio designer regarding the loading animation that we were expecting for a very long time  
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** and oh it seems like he added something Demetrio.  
   
 

### 00:31:13

   
**Filippo Tosetto:** Yeah.  
**Vladyslav Krut:** So yeah, this one will be resolved. The rest is either clear or I will make it clear with Rubik's help.  
**Filippo Tosetto:** Perfect.  
**Vladyslav Krut:** Yeah, I know what to do. I have a plan.  
**Filippo Tosetto:** Perfect.  
**Vladyslav Krut:** I understand why the tickets that were not in the pen there all good like face AI in a very good and clear shape for me now to work  
**Filippo Tosetto:** Perfect. I'm very happy about this.  
**Vladyslav Krut:** on  
**Filippo Tosetto:** So, I'm going to leave it like that. again. Let's forget about um Thank you. You see you see uh one another  
**Vladyslav Krut:** nice progress.  
**Filippo Tosetto:** point regarding FAI is that Andreo is no more working with us in this app is been moved to another project because he wasn't doing much in this project. It was wasted time for him.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** Uh so if we need any backend work or any backend investigation, please let me know as soon as possible so I can find someone to  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** help.  
   
 

### 00:32:22

   
**Vladyslav Krut:** for smaller tasks or questions. Is it okay if we contact him or it's better to not have to go to back end and look  
**Filippo Tosetto:** That's that's no uh if you can find the information by yourself,  
**Vladyslav Krut:** myself  
**Filippo Tosetto:** try but is still in the company. So feel free to ask him anything that is a blocker. I mean if you still have something pending from last week, he's a nice guy. He will help you.  
**Vladyslav Krut:** already reported the skin filters are not working. So I We'll first take a look myself then probably involve  
**Filippo Tosetto:** Nice.  
**Vladyslav Krut:** and  
**Filippo Tosetto:** Good. Wait, you just been in the company three months.  
**Vladyslav Krut:** yes sounds about right from  
**Filippo Tosetto:** Yeah. Yeah. You arrived on the 2nd of March.  
**Vladyslav Krut:** March. years from March.  
**Filippo Tosetto:** Hey,  
**Vladyslav Krut:** Exactly three months anniversary.  
**Filippo Tosetto:** happy anniversary. Nice. Um, before we jump on a design,  
**Vladyslav Krut:** Thanks.  
**Filippo Tosetto:** I'm curious. What is it?  
   
 

### 00:33:31

   
**Filippo Tosetto:** How you expected  
**Vladyslav Krut:** Oh, hell no.  
**Filippo Tosetto:** it?  
**Vladyslav Krut:** I feel like my job description has changed like three times since then.  
**Filippo Tosetto:** Yeah. Yeah.  
**Vladyslav Krut:** I I feel like I am getting accustomed to chaos and ambiguity. It's like okay teams are changing,  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** projects are changing, plans are changing. I'm like, okay, expectations are also changing.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** So I may not really need to fulfill what was decided a week ago anymore which is I guess well well nice for me not sure if  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** it's nice for the process in the company we're working in uh but okay we are in the middle of some kind of transformation let's do this another part that the thing that we were talking a lot is our general AI transformation I feel like this idea uh not like died but it's it's going much slower than we were expecting. The idea were to you know to develop tools and then apply these tools to make the A do like all the work in the world for us.  
   
 

### 00:34:46

   
**Vladyslav Krut:** I feel that's just not happening at the moment. People are contributing here and there for the to to our shared intelligence but nothing like game breaking was introduced for a very long time and I'm not sure if it will be also models are changing the the way I work is changing pretty fast I don't really believe in girin files being the source of truth for AI to execute big chunks of work like now even when I was doing this huge refactoring which is obviously more difficult task than writing a feature because I had to describe what needs to be done fighting what's there much more difficult task so it's just me a plan and many AI agents working against the plane against the plan and that that's and then set 4.6 to to just write the code with it. But it's all about the plan. Yes. And I don't I haven't used all the fancy skills for that. And I don't think I can reuse any of this to be honest because I was Yeah. Okay.  
   
 

### 00:36:10

   
**Vladyslav Krut:** Let me see how that will work. Okay. We are missing that piece. Let me have this agent to review that phase of the plan. Well, Oppus 4.8 made everything simple. It's just so  
**Filippo Tosetto:** Yes, it is.  
**Vladyslav Krut:** good.  
**Filippo Tosetto:** I'm I'm having exactly the same conversation. I had it uh this morning with Andre and Andre is working on a different level. Andre is outsourcing 90% of the work to agents. So, it's less because he showed me a few things. is working on a completely different type of application. While the application you're working on is uh relaying on a back end where you send data, you receive data and you display this data in different ways. Andre's work is much more hardware level and there's a lot of business logic involved because he needs to connect to a lot of different devices outside of his of the phone. So TVs, a lot of different TVs. So what he do what he did was to first and foremost take the current current code base which was as bad as the one that you're dealing with and what it did was to where possible create a lot of dependency injection so to create self sustained modules with the s\*\*\*  
   
 

### 00:37:37

   
**Vladyslav Krut:** Yes, makes  
**Filippo Tosetto:** code doesn't matter. So what it did was just to break the connection and create dependency injection  
**Vladyslav Krut:** sense.  
**Filippo Tosetto:** there and then outsource to the AI full unit test coverage of each module  
**Vladyslav Krut:** Smart. I see. Yes.  
**Filippo Tosetto:** and obviously it removed all the UI part of this and now for the business logic is at 95% test coverage. Still s\*\*\*\*\* code doesn't matter because now what he's doing is one by one he's refactoring each module by yes the unit test to check against so it can outsource the AI this flow so what I  
**Vladyslav Krut:** I see.  
**Filippo Tosetto:** see is two people working in two different ways you more into planning with AI on how to implement the feature or fix the feature or change the implementation because it's clearly wrong and on his hand is doing something slightly different but you're working on a totally different project you and him. So each part is dealing in its own way.  
**Vladyslav Krut:** Yes.  
**Filippo Tosetto:** So I asked him that's great how would you do this process for AI design for instance he was working on AI design until a month ago because  
   
 

### 00:38:58

   
**Vladyslav Krut:** No.  
**Filippo Tosetto:** I'm curious he said I will write UI tests first.  
**Vladyslav Krut:** UI tests.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** H.  
**Filippo Tosetto:** So UI tests implement the the sorry fix the  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** code. So refactor whatever you need to refactor. But you have the fixed part which is the UI test.  
**Vladyslav Krut:** Oh, it made me thinking like one of the tech tasks that I will be doing on face AI about unifying like 11 screens into one configurable one. That could be a move  
**Filippo Tosetto:** You have UI test for every screen.  
**Vladyslav Krut:** here.  
**Filippo Tosetto:** Then you change the implementation and you put the AI against itself to make sure that the implement the the UI test pass.  
**Vladyslav Krut:** Yes, that's absolutely can work. Still one of the biggest challenges I face is not about how my K work. is is like I am not delegating it a lot of work to do while I am away primarily because it needs to be stopped when it's going off rails when  
**Filippo Tosetto:** What do you mean?  
   
 

### 00:40:26

   
**Vladyslav Krut:** it's experiencing problems that it doesn't know how to overcome it's trying solutions spiraling and it needs to be stopped otherwise wasting a lot of tokens  
**Filippo Tosetto:** But if you have a guardrail, which is a test,  
**Vladyslav Krut:** No,  
**Filippo Tosetto:** would  
**Vladyslav Krut:** like for example doesn't know how to solve concurrency problem.  
**Filippo Tosetto:** this  
**Vladyslav Krut:** It it just doesn't know what to do with sendables. That's one of even when you connect this axum concurrency skills it just sucks it. it see compiler warning or error and it's like oh I don't know I should add a weight or a sync or maybe throw checked continuation or maybe I will mark the whole view model as a main actor or then now it's no that's actually the right thing but you need to be aware about the rest that's actually the best thing it could do but now there are many problems that needs to be solved and it's just not going anywhere so I while I was doing this major refactoring, I had to be here and be like staring at it and checking is this doing something that I feel like is correct or should I abort the mission and maybe for one specific part of the task use smarter model or give a clear instructions.  
   
 

### 00:41:52

   
**Filippo Tosetto:** Interesting.  
**Vladyslav Krut:** I for the very like trivial and repetitive and simple tasks I can do a loop right for example that thing that I did before don't remember about what part but I already did the adv once and I left for four hours and it still was working and it done everything nice but with something that matters I don't think  
**Filippo Tosetto:** to go back to the point that you made about the AI transformation not moving much for me it's moving but I have a broader vision than you it's moving it's moving in a lot of different directions and the company as a whole the app division is making huge improvements. Are these improvements shared with everyone? No, they are not. Why? Because each one of you guys is working in a different way. And I I still don't know which one is the correct one. Probably all of them depending on the use case.  
**Vladyslav Krut:** probably just have different workflows for different types of problems.  
**Filippo Tosetto:** So the the old girking file part I partially agree with you because if you start an application from scratch, you can focus only on writing the girking files and outsourcing the implementation to the AI.  
   
 

### 00:43:28

   
**Filippo Tosetto:** until a certain point.  
**Vladyslav Krut:** Oh, well,  
**Filippo Tosetto:** Until a certain point,  
**Vladyslav Krut:** yes.  
**Filippo Tosetto:** I'm very very interested to to talk to each one of you to see how you guys work because I'm catching good ideas here and there from each one of you. It would be nice to find a forum where to talk all together. I don't know if the one that we have on the Friday is the right one though. It's too broad. It's too many  
**Vladyslav Krut:** It's very broad and I feel like people are talking mostly the same  
**Filippo Tosetto:** people.  
**Vladyslav Krut:** uh problem tokens models reduce save money and give more this type of problem. The first few when Sier was like presenting learning opportunities were insanely good and now I'm like well I will sit there with my screen turned off with my camera off and hoping for something smart being  
**Filippo Tosetto:** I agree. I agree with you. I have the same feeling. I'm It's been a month or even more that I don't come because I have other things.  
   
 

### 00:44:39

   
**Filippo Tosetto:** But the value that the first couple of meetings were was g were given is completely gone.  
**Vladyslav Krut:** I feel like Serio shared the information that he had and now that that's it.  
**Filippo Tosetto:** Oh, well, let's  
**Vladyslav Krut:** It's not that easy to share an experience.  
**Filippo Tosetto:** see.  
**Vladyslav Krut:** You can only share  
**Filippo Tosetto:** But it's also not deterministic.  
**Vladyslav Krut:** knowledge.  
**Filippo Tosetto:** It's not that, hey, this is how you use AI in this specific use case and it always works. It's not as easy as that.  
**Vladyslav Krut:** Is really not that deterministic to be completely honest.  
**Filippo Tosetto:** That's the point. That's the point. All right. Um, use it the best way you can. And what I'm what we can do is if you come to me like every week with this kind of problems, maybe I can bring you ideas on possible solutions that I've collected from talking to a lot of people like this  
**Vladyslav Krut:** Okay, that sounds good.  
**Filippo Tosetto:** UI test part for instance. Uh if it  
**Vladyslav Krut:** What about like time and performance?  
   
 

### 00:45:54

   
**Filippo Tosetto:** works  
**Vladyslav Krut:** UI tests take insanely long time to build and run and for AI to observe the results and to like that's you can run it overnight but you cannot run it while you're still doing something else. Well, unless work trees of course we can always do that but  
**Filippo Tosetto:** or trees,  
**Vladyslav Krut:** okay once again is a problem because I'm trying to  
**Filippo Tosetto:** there's A caveat.  
**Vladyslav Krut:** be somewhat  
**Filippo Tosetto:** There is a caveat.  
**Vladyslav Krut:** conservative.  
**Filippo Tosetto:** Andre is paying by himself a Codex license to have much more access to tokens. There is not that constraint. But this is not something I we should be pursuing because that's the company that needs to provide  
**Vladyslav Krut:** Yeah, I believe so. I'm always pay also paying for my cloud license, but I'm not using it here. I'm using my side  
**Filippo Tosetto:** with yes,  
**Vladyslav Krut:** project.  
**Filippo Tosetto:** which is what I do as well, but that's another story. Anyway, um before we go, quick one on AI design. Um I'm interested to know how much time you have been spending in this project so far roughly, just to get a  
   
 

### 00:47:20

   
**Vladyslav Krut:** more than I would like almost whole Thursday. Uh but it actually worked really well. I solved completely iOS problem with upper test. I had a lot of meeting with Alexi and with Volvo and with somebody else. No, that's maybe it. Uh I tried solving that upper test problem with Android and I give now you know when I read the documentation.  
**Filippo Tosetto:** Oops.  
**Vladyslav Krut:** Okay, it's working the same as on iOS. I don't really know what was the problem with uh certificates. I believe you solved this part in the end. Not sure what went wrong there, but yeah, the whole Thursday I was dealing with some weird crap on AI design, but with results that's all right. Now, today I have like six I believe it's six open conversations. Two of them I already told you, the other few we can discuss or I will just go and explore them later. Why is either me or Ahmed QA who are supposed to define should we deploy parapet and link fuse integration on back end or not  
   
 

### 00:48:35

   
**Filippo Tosetto:** You  
**Vladyslav Krut:** like and what Ahmed is doing in that list  
**Filippo Tosetto:** shouldn't.  
**Vladyslav Krut:** with me okay like I'm development advisor potentially it's my problem I just don't know how to approach this question but what's Ahmed do is doing in this list and he proposed nice solution Ahmed was while we don't solve the problem with parapet let's not deploy it to  
**Filippo Tosetto:** What's  
**Vladyslav Krut:** pro just yet like okay yeah this is how smart I support this idea but still like why I'm being asked that and what is  
**Filippo Tosetto:** I'm very lost as well on this point.  
**Vladyslav Krut:** happening  
**Filippo Tosetto:** Why are we Why do we want to Okay. Um  
**Vladyslav Krut:** Ahmed answered the question and it seems like everybody satisfied. Don't think about this too much. Once uh we get solve other problems question will be raised again maybe next week. So don't worry  
**Filippo Tosetto:** Ahmed will live in a month's time and it's not our decision.  
**Vladyslav Krut:** I know well what we can do.  
**Filippo Tosetto:** Eddie doesn't know yet. So, please keep this information for  
   
 

### 00:49:46

   
**Vladyslav Krut:** Oh sure no problem.  
**Filippo Tosetto:** yourself.  
**Vladyslav Krut:** I'm very easy to not talk with people about  
**Filippo Tosetto:** Um, let's say it like this.  
**Vladyslav Krut:** something.  
**Filippo Tosetto:** I want you to be involved in this project like as a light touch just to unblock people and and say the smart thing without spending too much time. But if you're spending days on this, this is going to become a problem for me.  
**Vladyslav Krut:** I only spend Thursday because I know that you were off.  
**Filippo Tosetto:** Thank you.  
**Vladyslav Krut:** That's why pretty much for you and I was not about  
**Filippo Tosetto:** Thank you. Um  
**Vladyslav Krut:** you know wait for you to block everybody. Okay guys don't know what to do. I will try to figure out not planning to do this every time they have  
**Filippo Tosetto:** thank you.  
**Vladyslav Krut:** problems unless you ask  
**Filippo Tosetto:** No because we are paying these people. We are paying these people as senior people and that is the point  
**Vladyslav Krut:** me.  
**Filippo Tosetto:** here. It's not only about showing nice picture and fetching data from a back end.  
   
 

### 00:50:49

   
**Filippo Tosetto:** The work is a bit more complex than that. And if every time a small complexity come into play, they just running to me or to you, we have a problem.  
**Vladyslav Krut:** Uh, well, we do. Well,  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** we also have a task that you reassigned to yourself. It was assigned to me originally like an hour ago.  
**Filippo Tosetto:** Already fixed.  
**Vladyslav Krut:** Okay,  
**Filippo Tosetto:** Already fixed.  
**Vladyslav Krut:** nice.  
**Filippo Tosetto:** Yeah. And I haven't done anything. I just pasted the URL to Sonet and I told fix this. And this is an example of how it should work from another app.  
**Vladyslav Krut:** Oh, okay. That's important part. You you had a reference to another app.  
**Filippo Tosetto:** I have access and you do as well have access to all the repository for all the apps.  
**Vladyslav Krut:** That's true. But you got to know where it's working. I don't It's my going to be my first Android app.  
**Filippo Tosetto:** Ask me,  
**Vladyslav Krut:** Okay,  
**Filippo Tosetto:** ask me,  
   
 

### 00:51:49

   
**Vladyslav Krut:** I can ask you.  
**Filippo Tosetto:** ask me. Uh, okay. Uh, AI design, do not spend too much time.  
**Vladyslav Krut:** Yum.  
**Filippo Tosetto:** If you face that you need to solve complex issues. Let me know. Maybe I already solved it. I don't want you to get too much here. It's just for me to outsource some time to you. That's the whole idea behind this project also because the project is not complex and the only hard part is this qua system integration which is just seems to be the hardest thing in the world just because it's slightly off the the usual.  
**Vladyslav Krut:** I guess everybody struggled  
**Filippo Tosetto:** Um yeah but that's solved. So let me know if you are stuck on something. Ping me. I can jump in or they can  
**Vladyslav Krut:** Okay.  
**Filippo Tosetto:** wait.  
**Vladyslav Krut:** About Volo and uh in purchases testing, I tagged you in the beginning of this meeting.  
**Filippo Tosetto:** I'm going to look at it and answer accordingly.  
**Vladyslav Krut:** Okay. Thanks.  
   
 

### 00:52:58

   
**Vladyslav Krut:** That I believe should be all from my site. Checking my notes.  
**Filippo Tosetto:** Yep.  
**Vladyslav Krut:** By the way, we again ah you were there. Sorry, you were there. Oh, that's it. That's this is regarding  
**Filippo Tosetto:** I was clear. Huh? I was  
**Vladyslav Krut:** the solar slop and the other provider of devices and upper test testing. you were on this meeting and you answered that you should not be testing. You were there.  
**Filippo Tosetto:** Yes.  
**Vladyslav Krut:** No, no more questions or concerns from my side  
**Filippo Tosetto:** Yes. Blood.  
**Vladyslav Krut:** view.  
**Filippo Tosetto:** Thank you again. Any feedback for me? Always ask this.  
**Vladyslav Krut:** No, you're doing a great job from the at least from the position that I can see.  
**Filippo Tosetto:** Anything that comes to mind,  
**Vladyslav Krut:** Of course we'll  
**Filippo Tosetto:** I'm always around. And let me know.  
**Vladyslav Krut:** do.  
**Filippo Tosetto:** I'll let you go. Thank you so much for your time. Have a good day.  
**Vladyslav Krut:** Thank you. You too.  
**Filippo Tosetto:** Bye-bye.  
**Vladyslav Krut:** Bye.  
   
 

### Transcription ended after 00:54:14

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*