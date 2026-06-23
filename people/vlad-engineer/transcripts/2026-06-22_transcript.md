Jun 22, 2026

## Vlad / Filippo \- Weekly 1:1 \- Transcript

### 00:01:22

**Filippo Tosetto:** Good morning.

**Vladyslav Krut:** Hello. Good morning.

**Filippo Tosetto:** How are you

**Vladyslav Krut:** Pretty well, thanks.

**Filippo Tosetto:** doing?

**Vladyslav Krut:** It was the very first weekend in a few months that I did not uh screw up a sleep schedule during the weekend. So, today I'm fresh,

**Filippo Tosetto:** Nice. Nice.

**Vladyslav Krut:** which feels really nice and really uncommon to

**Filippo Tosetto:** Nice.

**Vladyslav Krut:** me.

**Filippo Tosetto:** Feels nice. It's quite uncommon. Okay. Sounds good.

**Vladyslav Krut:** Yeah,

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** that's exactly what I meant.

**Filippo Tosetto:** All right. Okay. Um, how is the temperature where you are in Valencia?

**Vladyslav Krut:** It's valency. Yes.

**Filippo Tosetto:** Right.

**Vladyslav Krut:** Well, outside it's somewhere between desert and the hell.

**Filippo Tosetto:** Yeah. Same here.

**Vladyslav Krut:** Uh like I don't know 32 in the shadow

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** and god knows how high on the sun we have.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** Oh, I just saw uh severe uh high warning temperature whatever

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** warning from the material materological company yellow level yet.

### 00:02:35

**Vladyslav Krut:** It's just the

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** beginning.

**Filippo Tosetto:** I spend my weekend pretty much at home with the AC on and uh that's it. My dogs are not even going out anymore. Pretty much because it's just insanely hot. It's not fun. Don't like this.

**Vladyslav Krut:** Not fun.

**Filippo Tosetto:** No.

**Vladyslav Krut:** Yes, I

**Filippo Tosetto:** No. Not fun.

**Vladyslav Krut:** agree.

**Filippo Tosetto:** Not fun. Uh nice. So, Vlad, how was your previous week?

**Vladyslav Krut:** Yes. Previous week uh went pretty well. I have a few list of things on my list to discuss. Generally speaking, all good. On AI design, I did spend significantly less time. They got majority of the unusual stuff done. Everything as you said, as you anticipated. Yes. Now I'm limited pretty much to ma maintaining CI code magic and checking PRs. Oh, speaking about PRs, I built like a prototype of the tool like the first and maybe second iteration. It doesn't really do a lot of job for me,

### 00:03:47

**Filippo Tosetto:** Nice.

**Vladyslav Krut:** but what it does is it's a cloud loop that every half an hour checks for the repositories that I am observing and sends me a message to Google chat that I have a PR that I need to review. uh it also does a classification of the PR based on two two metrics. It actually proposes the matrix against what I had in my mind before and I like this version more. So now it gives me like either it's approval or I need to take a look and ask the questions or it definitely requires some rework and it gives me a level of confidence and so far the first two categories looks like what I can approve without even checking because it usually comes with some questions like but the tests are not covering the scenario this ad mode ad mode thing is affecting a lot of providers with their

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** GDPR compliance and I'm like I genuinely don't care that's what I

**Filippo Tosetto:** Yes.

**Vladyslav Krut:** do and it consists of the skill to like fetch the fetch PRs and then separate skill to triage this PR the the new word for me I never use it before now I

### 00:05:14

**Filippo Tosetto:** Mhm. Triage.

**Vladyslav Krut:** do triage Okay.

**Filippo Tosetto:** Yes.

**Vladyslav Krut:** Well, I know it exists now. I didn't know before. And it marks the PR that it did present me with a separate list in the I didn't can create a repo for it just in the text file. So, if this is something that you would like, I can send it to you. Uh yeah, I think I will eventually add another layer on top of it to automatically approve or to leave some clarifying comments. But even for now, it's already a game changer. I'm just like I'm reading a summary from the AI instead of summary from the PR.

**Filippo Tosetto:** Yeah,

**Vladyslav Krut:** It It's better. It It just looks better.

**Filippo Tosetto:** clearly.

**Vladyslav Krut:** I use Sonnet 46 for all of this, which is like half a scent for a PR review, and I don't really care. It's fast. It's only running notifying me from 10:30 till 5 every day Monday to Friday because I yes it did notify me on the weekend and I was like wait a second this is not what we are doing here so yeah I

### 00:06:23

**Filippo Tosetto:** Exactly.

**Vladyslav Krut:** can send you files related to little

**Filippo Tosetto:** But it so it it's just a prompt pretty

**Vladyslav Krut:** project uh two

**Filippo Tosetto:** much.

**Vladyslav Krut:** skills and a prompt yes and a common that runs it.

**Filippo Tosetto:** I freaking love code. You can do these things.

**Vladyslav Krut:** Yeah, like very nice and easy just a slash loop 30 minutes run and then the skill not skill the script check that goes and fetches and then agent in which it was open is processing further.

**Filippo Tosetto:** Love it.

**Vladyslav Krut:** Yeah,

**Filippo Tosetto:** Love it.

**Vladyslav Krut:** pretty easy and it's really easy to build on top of it something if you want. Absolutely. Yes. Really convenient. Took me like an hour or so maybe for the first iteration. Something like that. For the second, yes, absolutely easy. I was surprised to see how easy and convenient web hooks for Google works. Nice. That's convenient.

**Filippo Tosetto:** You mentioned that the results are posted to Google chat to

**Vladyslav Krut:** Yes, I created a private space for my reminders for my own and it now sends me all the

### 00:07:35

**Filippo Tosetto:** you.

**Vladyslav Krut:** PRs there. I can also add another type of notifications there in the future if I would like to. So, you will have to replace the web hook if you want to use it as

**Filippo Tosetto:** Can you?

**Vladyslav Krut:** well.

**Filippo Tosetto:** Yeah. No, I like it. Interesting. I never thought about it. Can you read data from Google chat?

**Vladyslav Krut:** Not sure. So far, web hook is only for post. Uh maybe. Well, I assume you should have some kind of access to do this.

**Filippo Tosetto:** Yeah, because the the the natural uh extension of what you just mentioned is code post to Google chat and it post as a question uh this is a simple PR it's just a bump in uh up version should they approve yes no and so you can approve directly from chat and it goes and does the work for you instead of switching context you yourself. But that would means that you need to read from Google chat.

**Vladyslav Krut:** Uh h do we have in Google chat this type of interactive buttons like in Slack the way to respond it directly in the

### 00:09:03

**Filippo Tosetto:** Oh yeah, I don't know.

**Vladyslav Krut:** chat because that's what

**Filippo Tosetto:** No idea. No idea. No idea. Need to do a bit of research around this. Could be very

**Vladyslav Krut:** This if this is possible then we can have two buttons and each of these

**Filippo Tosetto:** powerful.

**Vladyslav Krut:** buttons or only one button like a proof can also be a web hook created from within the code itself as a callback. It should be doable like I'm not sure what exactly tool but it definitely should be doable but I have never seen any type of you know like button or prompts in Google chat.

**Filippo Tosetto:** interact. Yeah,

**Vladyslav Krut:** Yes, Slack can do this um this tool.

**Filippo Tosetto:** it's Yeah,

**Vladyslav Krut:** Not

**Filippo Tosetto:** Google chat is a bit it's not great for this kind of things.

**Vladyslav Krut:** sure.

**Filippo Tosetto:** It's a bit old old school.

**Vladyslav Krut:** Yes. I don't like it any single bit.

**Filippo Tosetto:** No, me neither. But uh it comes for free. Slack is very expensive compared to to Google chat.

### 00:10:11

**Vladyslav Krut:** Okay. Well, it's probably

**Filippo Tosetto:** Yeah. Cuz the when you buy Google

**Vladyslav Krut:** reasonable.

**Filippo Tosetto:** Workspace uh account so every account that we have, every email that we create, we have access to all the tools that Google provides. So it's one subscription for everything. Slack will be something different.

**Vladyslav Krut:** Make

**Filippo Tosetto:** Anyway,

**Vladyslav Krut:** sense?

**Filippo Tosetto:** blood, thank you. This is great and it's actually more future proof than building a piece of software or a script or anything that does that for you. This is much more um advanced I would say. Congratulations. Nice.

**Vladyslav Krut:** It feels pretty basic to me, but it gets the job done, so I'm not complaining.

**Filippo Tosetto:** But why do you need something more complex? If it's doing the job, why

**Vladyslav Krut:** Naturally,

**Filippo Tosetto:** not?

**Vladyslav Krut:** I want to be able to not even open it anymore. You know, like this my level of amition like it's not automated until it's fully automated.

**Filippo Tosetto:** Yes,

**Vladyslav Krut:** But I think this will have to wait a little

### 00:11:23

**Filippo Tosetto:** but you need to test it.

**Vladyslav Krut:** bit.

**Filippo Tosetto:** And if you see that the simple PRs are working, you can just tell clothes to approve the simple ones by by

**Vladyslav Krut:** Well, this part of course can do.

**Filippo Tosetto:** itself.

**Vladyslav Krut:** I think is all the guys working on a design. They're not particularly trying to make PRs simple and atomic you know they're just okay there's a ticket there is a feature that needs to be implemented and there is a PR that solves the problem a thousand lines and if so far if cloud says big PR like let's say a thousand lines it just goes like low confidence I am not sure there are concerning things and I'm like reading this concerning things decide to approve maybe I will play the classification using some kind of 1 to5 or 1 to 10 scale regarding confidence so I can easily you know adjust to the threshold upon which it can go and review and automatically approve. Sounds like a good

**Filippo Tosetto:** So um do you know the concept

**Vladyslav Krut:** idea.

### 00:12:37

**Filippo Tosetto:** of evolves?

**Vladyslav Krut:** Uh, I think not. Like that sounds very familiar and I'm pretty sure I was working with it at some point,

**Filippo Tosetto:** So

**Vladyslav Krut:** but I'm maybe

**Filippo Tosetto:** uh it's a concept that I'm starting to use in another project.

**Vladyslav Krut:** not

**Filippo Tosetto:** I'm going to tell you about it later, but it's very you can you can uh think about it as unit tests or AI. Let me explain a bit more. So as you know AI is not deterministic. So if you write a prompt, you may have different results out of this. It's not like a function that you write in code.

**Vladyslav Krut:** That's

**Filippo Tosetto:** In code, we have unit tests. Create a function sum and you can write a lot of tests around this unit tests. And uh you always should be able to have the same results. In AI development, you still need a way to test your prompts so that from a specific input, a prompt gives you a similar output or an acceptable output.

### 00:13:49

**Filippo Tosetto:** And so e evals are just a list of inputs and outputs and the variable is your prompt. And so you need to create a sort of list of possibilities as input. In your case, the specific case you have different type of PRs, oneliners, complex, touching, securities, touching, whatever. The output that you expect approve, not approve, uh, danger, whatever. And where you work, where you loop is to improve the the the prompt itself.

**Vladyslav Krut:** Okay. I definitely did not work with this concept at all. Uh, sounds good and

**Filippo Tosetto:** It's not for this use case probably.

**Vladyslav Krut:** interesting.

**Filippo Tosetto:** I'm just giving you this information as something that maybe in the future you will need because your work can be more with AI prompts.

**Vladyslav Krut:** Yeah, that sounds good.

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** But can you test for Yeah,

**Filippo Tosetto:** Nice.

**Vladyslav Krut:** sure. Nice to

**Filippo Tosetto:** Uh exactly, exactly.

**Vladyslav Krut:** know.

**Filippo Tosetto:** Um so AI design things are moving back to they're back to boring normal now I

**Vladyslav Krut:** Yeah.

### 00:15:08

**Filippo Tosetto:** guess why mostly what

**Vladyslav Krut:** Uh mo mostly. Yes.

**Filippo Tosetto:** is uh

**Vladyslav Krut:** Code magic keeps like throwing random problems at us all the time.

**Filippo Tosetto:** h

**Vladyslav Krut:** Especially like Android build I it feels like it's like 50/50 randomizer. Sometimes fast lane can do its work, sometimes it cannot. I know they probably can, you know, go and debug and enable variables mode and feed it to a to make it work. uh volmer try it a few times do a thing or two say confirm that manually it's like locally it's works and I'm just procrastinating like I don't want to dive deep into this Android is not my area of expertise when I can read the error and immediately know where to look for it so I'm like I will be just retry restart restarting or retrying the job which is not optimal at all but I don't want to invest My time is just

**Filippo Tosetto:** Uh, I like the last part just yet. For now, it's okay if it works.

**Vladyslav Krut:** yellow.

**Filippo Tosetto:** If it's just a matter of retry, I'm okay with that.

### 00:16:22

**Filippo Tosetto:** In the future, maybe you need to spend a bit more time to fix this. But for today, I'm okay. As we said, 10 15% of your time as a baseline.

**Vladyslav Krut:** At some point it will annoy me enough so I will want to get it fixed more than I don't want to deal with it. Well,

**Filippo Tosetto:** But Vlad,

**Vladyslav Krut:** pretty much everything in my life to be

**Filippo Tosetto:** it it's like PRs.

**Vladyslav Krut:** honest.

**Filippo Tosetto:** Last week you were very annoyed. So you spend one hour of your time to automate part of this.

**Vladyslav Krut:** Yes.

**Filippo Tosetto:** So let's reach that time when you're going to get very annoyed. So you're going to invest the time unless priorities changes obviously, but that's another story. Okay.

**Vladyslav Krut:** Yes.

**Filippo Tosetto:** Um I've seen your progress in face AI. Very good.

**Vladyslav Krut:** Yeah, I agree. I also believe so. Regarding splash time reduction, the fact that app takes forever to load, I I measured it's 71% reduction. I got numbers and analytics.

### 00:17:34

**Vladyslav Krut:** I actually did recording. Don't know why they bother, but I proud to say it's

**Filippo Tosetto:** I'm curious to hear what is taking that long.

**Vladyslav Krut:** 71%.

**Filippo Tosetto:** What was taking that long? Yeah, that's f that face.

**Vladyslav Krut:** Okay. So there were a few suboptimal let's say things like it goes well let's start from the most fun part somebody and probably Anton but I'm not sure was trying to implement a 3 second timeout so uh the application starts doing all the work that needs to be done from the very beginning and if it takes more than 3 seconds, it kind of like aborts the operation. It doesn't abort it. It just moves it uh off to the background and then proceed with the application so user can use it. But they did not succeed in implementing this exact idea and instead they just added permanent 3second delay on top of any other work that is being done. This is what allowed me to get insane amount of like improvement just deleting one line.

**Filippo Tosetto:** And this is the demonstration that cheap developers are delivering cheap

### 00:19:19

**Vladyslav Krut:** Well,

**Filippo Tosetto:** work.

**Vladyslav Krut:** at this point I am like no it cannot be true. This is somebody added this delay artificially. So then later they get they get a task to work on spike to reduce the loading times and then we'll spend then they will spend like two three days figure out what's happening and then present awesome results. This is my hypothesis. I refuse to believe that people are that stupid. I believe it was very considerate plan for the future as it sometimes work with outsource

**Filippo Tosetto:** Vlad,

**Vladyslav Krut:** developers.

**Filippo Tosetto:** you're young. You're young. I've seen things in my life.

**Vladyslav Krut:** But is actually good. I mean if I wouldn't care at all would be working like freelance or outsource or

**Filippo Tosetto:** Um,

**Vladyslav Krut:** whatever I think I would doing things like that sometimes when I want you

**Filippo Tosetto:** but you're smart enough that you care about what you

**Vladyslav Krut:** know

**Filippo Tosetto:** produce. Why would you do something like that?

**Vladyslav Krut:** so I can have like three three days of work paid

### 00:20:45

**Filippo Tosetto:** Nah. No. You're smart enough. You wouldn't do that.

**Vladyslav Krut:** That's not about being smart. That's about being fair.

**Filippo Tosetto:** No.

**Vladyslav Krut:** There there's a better word, but I don't remember it in English. like not trying to consciously scam people, you know, who you work with.

**Filippo Tosetto:** Yes.

**Vladyslav Krut:** About generally speaking,

**Filippo Tosetto:** Yes.

**Vladyslav Krut:** being a good person, not about being

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** smart.

**Filippo Tosetto:** But you're smart enough to find a way to still have two days off without creating extra work for

**Vladyslav Krut:** Oh,

**Filippo Tosetto:** yourself.

**Vladyslav Krut:** it's not about getting X. It's like one line. Come on. It's so smart and clever and so far I'm not having like a lot of free time but I of course could because I'm smart but I'm not doing that. So u yeah

**Filippo Tosetto:** Um, what about uh I mean you have couple of tasks left for this sprint,

**Vladyslav Krut:** I have two of them.

**Filippo Tosetto:** right?

**Vladyslav Krut:** One is to rewrite the editor screen.

### 00:21:56

**Vladyslav Krut:** uh the the one that is uh that you see before

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** you choose a filter you want to apply so effectively a preview

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** screen that genuinely speaking does nothing at all which is incredibly complicated over a thousand line and I don't know why and it smells all of it and I don't know why it's so

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** difficult uh so this doesn't have working right now on Friday I tried using kilo models because I'm testing kilo now to help me address this problem. So I have a few findings on kilo generally speaking uh did not make any progress whatsoever like I did not find a good enough kilo models I would trust with this type of work while claiming planning stage like it will just allow

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** me to make less decisions let's say so yeah I will

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** work on it today and maybe tomorrow. It looks very big. And so far, this is the biggest like piece of s\*\*\* code that we have in the app.

### 00:23:09

**Vladyslav Krut:** Once I'm done with this, we will have a few minor things like screen protection or subscription status, maybe settings. I didn't really check what's in settings. I don't think I need to don't expect any fundamentally new big features being integrated into settings. So, this is the biggest problem we have in Zap right now. And once it's addressed, and it will be addressed because it's a simple screen,

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** come on. You have gender picker there and that's it. The bottom sheet menu is already separate entity that I rewrote before. So yeah once this part is done it will be very pleasant to work with. Let's say integration of all the new feature will be pretty smooth I expect.

**Filippo Tosetto:** I'm going to ask you a question that I already asked you a month ago, a couple of months ago. Now that you have been through all this journey, which yeah,

**Vladyslav Krut:** Rewrite up or rewrite rewrite

**Filippo Tosetto:** rewrite or refactor, what's

**Vladyslav Krut:** everything from scratch. It would be much faster and the state of the code would be much better and it would be covered

### 00:24:15

**Filippo Tosetto:** your

**Vladyslav Krut:** with unit test by now. Absolutely. Yes. No consideration whatsoever should be taken when approaching new project like that. Not at all. Zero doubt. Just take what you have, throw it into the garbage bin and

**Filippo Tosetto:** Um,

**Vladyslav Krut:** restart.

**Filippo Tosetto:** just as an exercise, what do what would you do with AI design?

**Vladyslav Krut:** What's it called? What you want to do with it?

**Filippo Tosetto:** Yeah. No,

**Vladyslav Krut:** No.

**Filippo Tosetto:** no,

**Vladyslav Krut:** No.

**Filippo Tosetto:** it's just hypothetical.

**Vladyslav Krut:** I I'm

**Filippo Tosetto:** Hypothetical. Let's say tomorrow we're going to switch priorities and blood. We need you to work on AI design. What would you do? Because AI design is much more advanced than it was space

**Vladyslav Krut:** Well, I would take a look onto the road map first because like

**Filippo Tosetto:** AI.

**Vladyslav Krut:** not every project needs to be written for the sake of having good code. You know AI design in comparison to SA works.

### 00:25:31

**Vladyslav Krut:** It feels good. It feels nice. It's there are no lags, random broken animations. It's not frustrating experience for the users to do. So what do you want to do with this project? Maybe maybe it's pretty much done and maybe we are continuous throwing you know like AI features that are not interconnected with the current codebase. So we don't need either refactoring or rewriting. So yeah first road map and what's the plans for the app.

**Filippo Tosetto:** Yeah, good

**Vladyslav Krut:** Then if we are coming to the conclusion that okay we need

**Filippo Tosetto:** point.

**Vladyslav Krut:** to continue like working and developing the application for a somewhat long time because obviously if you have road map for like three six months probably not worth it already like if this

**Filippo Tosetto:** Got

**Vladyslav Krut:** is a life cycle of the application and is going to be done and completed no reason to rewrite

**Filippo Tosetto:** it.

**Vladyslav Krut:** it at this stage.

**Filippo Tosetto:** Good answer. Very good answer. Nice. Now, what you're saying makes total sense.

### 00:26:39

**Filippo Tosetto:** The the the key differentiator here in my opinion is AI design works. as you

**Vladyslav Krut:** So what is working?

**Filippo Tosetto:** said.

**Vladyslav Krut:** If we don't have, you know, like 400 bugs that needs to be addressed across the application, why would we touch it?

**Filippo Tosetto:** Fair

**Vladyslav Krut:** If you only have new new features,

**Filippo Tosetto:** point

**Vladyslav Krut:** let's just write new features as we believe we should and that's it.

**Filippo Tosetto:** and treat the rest as technical debt if there is any. Nice.

**Vladyslav Krut:** Yeah.

**Filippo Tosetto:** No, it's uh it's actually the third option. You are totally right.

**Vladyslav Krut:** Not not every app need to have a good code.

**Filippo Tosetto:** Okay, thanks for the answer. Uh checking my list. Actually, you started to talk about kilo code and I'm curious about your first feedback.

**Vladyslav Krut:** So first feedback as I was testing on Friday before we get any normal models I tried a few of them. I have my notes here.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** So I tried the in theory the best one the best of the cheapest one the Nexus N2 Pro from Nvidia according to their chart this is one of the like most powerful of the free ones and it's just awesome I have never had so full comprehensive and fast testing like I try to use it sends me 4054 server error Time out error doesn't produce any output.

### 00:28:26

**Vladyslav Krut:** You try it a few times and then you switch to other models. The best model ever.

**Filippo Tosetto:** Okay, that was an easy

**Vladyslav Krut:** Easy test.

**Filippo Tosetto:** test.

**Vladyslav Krut:** Yes. Uh then I tried the second what seems to be the good one of all of them is the pool site Lagona M1. Uh so I asked it to review the editor screen. It did like surface level code style analysis. Nothing of value, no flagging or reporting genuine problems like the logic or network calls being in the view, not in view model. It took a lot of time for it like five or so minutes. Uh nope.

**Filippo Tosetto:** No

**Vladyslav Krut:** Just don't try this ever again.

**Filippo Tosetto:** good.

**Vladyslav Krut:** And then I tried the third one. Step one, step 3.7 flash. And this one was somewhat not bad. It took like 25 30 seconds. So I was not expecting anything good from it. But it gave me a list of 24 findings and all of them were valid.

### 00:29:37

**Vladyslav Krut:** It was not talking about you know fundamental difference this screen against the rest of the codebase. But it did find generally 24 fixable actionable problems on the screen and I feel like I may you know run this model for like every file in the project that for the code sanity like some

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** surface level bugs checking stuff like that because this is very fast it's free completely free so no limitation whatsoever and I feel like the same model can probably fix all them because yeah they're small like move a piece of code

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** to other place extract something that's supposed to be re reused to separate function uh some little networking issues being executed on main main thread I'm like yeah sure why not confusing naming like the property being named one thing but used for something else I'm like that's a good one so this is something that can work I would not use it for anything bigger?

**Filippo Tosetto:** Yep.

**Vladyslav Krut:** No, not at all. Uh, but for code sanity, yeah, why not? Maybe for PR PR reviews it could be used, but S is already pretty much free and it's way superior.

### 00:30:58

**Vladyslav Krut:** So,

**Filippo Tosetto:** It is.

**Vladyslav Krut:** why would I try?

**Filippo Tosetto:** I'm curious. Have you tried Have you tried any of the Chinese

**Vladyslav Krut:** No, I did not.

**Filippo Tosetto:** models?

**Vladyslav Krut:** I believe I had like five or six uh free available to me. and I I opened the dashboard on their website regarding the quality of the model. So I searched the model, got it indexes and then decided what to try. I was not specifically focusing Chinese versus not Chinese. Another was limiting to free models only. I'm not even sure where these were coming from.

**Filippo Tosetto:** Okay, because I don't uh I don't have access to it and I'm not in that chat you guys have regarding feedback. So I have no idea what's happening.

**Vladyslav Krut:** Well, since today we supposed to have other models available like I believe trial is has started today and it will be uh will be going for the next three months if I remember correctly.

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** We got a spreadsheet in which we are encouraged to report our findings.

### 00:32:15

**Vladyslav Krut:** I'm not looking forward to filling this type of reports, but the things that I I feel genuinely important I will share. I don't believe that this testing of free models was anywhere close to be necessary. Like why why did I even do this? Why did I waste my time on Friday? I don't really know. They asked for it. I followed and then I was like wait a sec who specifically asked

**Filippo Tosetto:** What?

**Vladyslav Krut:** me and yeah that's my bad. I was not supposed to ignore this request and just continue working as I was. That's all right. It's not a big price to be

**Filippo Tosetto:** Yeah,

**Vladyslav Krut:** paid.

**Filippo Tosetto:** my suggestion wait half a day, one day when this kind of requests come through because there's a lot of people that can do that work for you.

**Vladyslav Krut:** Yeah.

**Filippo Tosetto:** They are less busy.

**Vladyslav Krut:** So who cares who's going to be using free models

**Filippo Tosetto:** Yeah,

**Vladyslav Krut:** anyway

**Filippo Tosetto:** exactly. Okay. Okay, good to know.

### 00:33:23

**Vladyslav Krut:** regarding the software itself which is I believe to be a noticeable problem is uh it's the way when you type at when you're searching for a file that you want to link it it just doesn't do what you expect. So I was looking for editor and then view and view model like source files in iOS project

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** obviously as it works seamless in the cursor.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** Uh but then it it started to suggest to me first a folder then editor border color color set then some assets like images that are being used then editorial.cube cube which is animation file and further down it did not suggest me file that I was looking for. So you got to type more which is seems minor but actually very

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** annoying

**Filippo Tosetto:** But have you tried it in the CLI or in VS Code or any other way?

**Vladyslav Krut:** in VS code. I was doing all that in VS code and

**Filippo Tosetto:** Okay. Okay. Good to know.

### 00:34:36

**Vladyslav Krut:** I cloud code does it well somehow let's view actually that was not supposed to be a case because that's a CLI uh in cursor it works the best of them all in kill I was like okay editor view model when I wanted to get the file that I was looking for min well that's inconven convenience. I I not sure this will be a decisive factor at any point. So far this one problems they

**Filippo Tosetto:** um I believe but things may change that we will reach a point in the future probably at the end of Q3 where every person can choose one Google. So you will be able to say oh yes I want kilo code because I have access to all these other models that cursor doesn't allow me or I prefer cursor because of what you just described or I want cloud code but with cloud code you obviously have a very limited amount of tokens to be used because it's super expensive. So let's see how this exploration goes. But in my opinion, it's worth exploring also because you have extra tokens to use for anything I guess.

### 00:36:00

**Filippo Tosetto:** I mean on top of of cursor.

**Vladyslav Krut:** So far I believe Sarah shared a model that is GLM po 5.2 which for him is like oppus but

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** cheaper. So,

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** I will maybe take test this one soon. Should be my to go model,

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** I believe. Uh, didn't do this just

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** yet.

**Filippo Tosetto:** Uh few points on my side. Um, last week I talked to Reuben regarding trying to reduce the number of dailies, but he is against it because he wants to have at least one point of contact every day, even if it's short. I did

**Vladyslav Krut:** Well,

**Filippo Tosetto:** try.

**Vladyslav Krut:** thanks for trying. I appreciate this. It's not that bad so far. Uh,

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** I started doing a cheesy or somewhat clever things like uh now when I know or I have a suspicion that Reuben uh may want to talk for longer or break the boundaries of the meeting.

### 00:37:17

**Vladyslav Krut:** I just book a little time slot directly after this meeting so I have a reason to say Robin I have another meeting. Thanks for thanks for planning. Let's plan better next time. Uh that's what I do.

**Filippo Tosetto:** Yeah. Yeah.

**Vladyslav Krut:** I don't think we have anything like groundbreaking something that actually needs to be addressed quickly. Not at all. Like come on me working QA guys are barely even testing because all the technical stuff will be

**Filippo Tosetto:** No.

**Vladyslav Krut:** tested during the regression fundamentally not ticket by

**Filippo Tosetto:** Um,

**Vladyslav Krut:** ticket.

**Filippo Tosetto:** let's speak about what's going to happen next week. So technically speaking, you should finish the current sprint with all this technical fixes that we promise we will deliver by the end of this month, which is going to happen. Um,

**Vladyslav Krut:** Yes.

**Filippo Tosetto:** I'm battling with Reuben for a road map for starting from next week for sure. While the QAS are going to do the the regression, they're going to find stuff. So you may have to fix them.

### 00:38:24

**Filippo Tosetto:** But I received a couple of epics that are that are not good because the quality

**Vladyslav Krut:** the quality or the priority.

**Filippo Tosetto:** the quality um how does it work?

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** The workflow is PM creates a PRD. From this PRD, an epic is created by the product owner. And engineering managers are gates for this epic to become workable or not. Meaning that the excuse is that hey, we need to put down some highlevel estimate for this epic. So I need to read it as an engineer manager before passing to the developers. The reality of thing is that it's a big gate where we simply stop initiatives that are not well described or they don't contain information or they are not they don't bring business value or like in this case they are simply badly AI generated without bringing any information to the developer.

**Vladyslav Krut:** Reuben told me recently that they are being forced now to use clot.

**Filippo Tosetto:** So

**Vladyslav Krut:** Their management told them to use it for everything. And apparently this is where we are getting.

### 00:39:45

**Filippo Tosetto:** uh yeah, sure. So I'm using code to bounce back their PRs, the uh epics. It's fine. Uh do you want to play the game? I'm going to play the game. For me, it's just spawning an agent. I don't waste time, but my agent is way better than theirs because I know what I'm doing obviously. Also, I also read the output of the agent while they apparently don't. Um, anyway, um, let me give you a bit of an explanation of what's happening. Uh, because I want your opinion on this.

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** So the epic is called makeup tool

**Vladyslav Krut:** Sure. Oh, yeah.

**Filippo Tosetto:** and it

**Vladyslav Krut:** Did take a look at it before. Okay.

**Filippo Tosetto:** contains a lot of blah blah blah like multi-layered composition environment. What the hell does it even in mean? Um, the engine must natively snap cosmetic texture to face coordinates using local tracking anchor and allow continuous realtime bleeding. Huh? What?

**Vladyslav Krut:** Yeah,

### 00:41:06

**Filippo Tosetto:** Um

**Vladyslav Krut:** it's fine.

**Filippo Tosetto:** uh there was another one that was like yeah I'm going to if the face mapping model detects several profile angles low light environment or part what do you want us to build so I've done the engineering manager which was when You get this. You take the PO. Hey, can we have a quick chat? Sure. Okay. I've been through your epic. It's going to take probably six months to build this. Why? How? Why? And so you throw at them all the possible questions which is showing that whatever the AI wrote here doesn't really make sense because If we can build all of this, there's no problem.

**Vladyslav Krut:** Sure.

**Filippo Tosetto:** But it's going to take the next six months.

**Vladyslav Krut:** Like this only view is

**Filippo Tosetto:** And so,

**Vladyslav Krut:** limited.

**Filippo Tosetto:** exactly. So, I simply asked Reuben, what do you want to build? Because if we start from your goal, probably we can find a better way to define your goal because this AI generated epic doesn't make sense.

### 00:42:31

**Filippo Tosetto:** And the answer is I don't know. He started to explain to me a few things and like, "So, you want what we already have today?" "No,

**Vladyslav Krut:** Oh,

**Filippo Tosetto:** no, no. I want something else." So, I send him off to an investigation. Let's see what it comes back with.

**Vladyslav Krut:** okay. I see. Nice job.

**Filippo Tosetto:** Engineering man engineering manager at their best.

**Vladyslav Krut:** Yes, it it sounds so satisfying at least listening to this

**Filippo Tosetto:** It's just time consuming which is 80% of my time is doing this. So blocking anything coming in your guy your ways because the people on the other end doesn't they don't really know the technology that we are using. Reuben is great at organizing the work of people, but sometimes he doesn't understand what's behind it. So, I've been doing this game with him for a while now, so we know how this works. Um, what is probably going to come back and I know because I've done already the research for him, but I'm not going to tell him is that we are going to probably Yeah, but you know it's let him do his job.

### 00:43:51

**Vladyslav Krut:** Jesus.

**Filippo Tosetto:** Um, you know, um, we are probably going to integrate an SDK provided by Yukam. you come is this um AI thingy that we are using in the back end and they provide uh client SDK to do things. So probably this old epic about building things is going to be about integrating an SDK. I'm just giving you this information because probably this is going to come your way for next sprint. But as of today, I don't have anything in the pipeline for next sprint beside fixing bugs. Don't worry, I have a long list of things for you. So, if nothing can come, nothing reasonable will arrive for FCI, I have a few other things for you to work on. So, you're not going to go on holiday. You're not going to be doing nothing.

**Vladyslav Krut:** a little bit sad, but

**Filippo Tosetto:** H Yeah. Yeah.

**Vladyslav Krut:** okay.

**Filippo Tosetto:** Uh so that is the epic state of things. Uh there is probably an integration regarding a beard uh filter thingy.

### 00:45:21

**Filippo Tosetto:** I already checked that it's 90% work that needs to be done um by the PO because it's all about writing all the missing prompts. So the only part for you is to improve the current way you call the beard filter and it's about switching a couple of um parameters. So it should take you

**Vladyslav Krut:** So far there no there are no filters in the codebase or in the app whatsoever. So it will be more like connecting a new one.

**Filippo Tosetto:** correct.

**Vladyslav Krut:** I saw in API doc we have endpoint for be which means that it will easily it will be easily integrated into the rest of the codebase.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** however I did all this refactoring. So I assume it to be a very easy task but I did notice that Reuben may not really be aware of how it's configured and what needs to be done on the fire store side. So I told him that he it may take about 3 days or so because I

**Filippo Tosetto:** So regarding that uh regarding

**Vladyslav Krut:** expected primarily because of

### 00:46:26

**Filippo Tosetto:** that um I've created this I sharing with you I will share it with you I've dispatched clothes to do this. It is a huge huge spreadsheet that contains all the filters with all the variants and how they are configured in fire store.

**Vladyslav Krut:** Okay,

**Filippo Tosetto:** I'm going to share this with

**Vladyslav Krut:** that's how did you get it out of fire

**Filippo Tosetto:** you.

**Vladyslav Krut:** store?

**Filippo Tosetto:** Uh I just ask code to go and fetch all the data.

**Vladyslav Krut:** Oh,

**Filippo Tosetto:** You can uh you should use let me share this with

**Vladyslav Krut:** okay.

**Filippo Tosetto:** you. You should use uh Google cloud platform CLI and ask cloud to connect to that to fetch the data and based on your permission you will be able to fetch this data or not. But I've done a bit of back and forward. What I asked him is to create a sort of uh general description of what we have today, what is enabled, if it is premium, uh and a few other things in general, uh like the engine, um the the key, the variant key for that specific thing on how it's configured in a fire store and then for each one also the configuration itself as in the JSON and obviously the different images

### 00:48:14

**Vladyslav Krut:** I see.

**Filippo Tosetto:** uh that are there and I think this was important to be done because otherwise no one knows how this thing works because the team changed three times over since the beginning of this app.

**Vladyslav Krut:** Yes,

**Filippo Tosetto:** Um,

**Vladyslav Krut:** absolutely.

**Filippo Tosetto:** regarding the beards filter that I talked about one second ago, there is a bit of clean up to be done in the back end. It will work, but maybe it's a chance for you to get your hands dirty a bit in the back end. It's literally cleaning up the uh the parameters that the uh API accepts because they some of them are not used anymore. So there was a a refactoring of the beard filters.

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** Uh it was working on in a way and now it's working with this new uh filters is working on another and the API call still receives the old parameters but they are not needed anymore because it's not implemented in the app. So it's not that we are breaking something by changing this in the API itself.

### 00:49:31

**Filippo Tosetto:** But if this is going to come your way, we can discuss about it and I can point you to the right things to be done. I think it's actually a really interesting exercise for you to get a bit of backend coding without breaking anything pretty

**Vladyslav Krut:** I believe so.

**Filippo Tosetto:** much.

**Vladyslav Krut:** I just checked in the API. It says it only accept image ID and mode which is basically what to do.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** But hey,

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** no problem. Can be done.

**Filippo Tosetto:** Cool. What else is on my list? Epic. We talked about it. Anything on your

**Vladyslav Krut:** Yeah,

**Filippo Tosetto:** end?

**Vladyslav Krut:** I have two probably points that I would like to, you know, to tell you. Not sure if I want to act on it anyhow.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** Uh,

**Filippo Tosetto:** Okay.

**Vladyslav Krut:** one of them about AI design and what seems to be Miguel not trusting his engineers and I have one very specific example that is being repeated a few times now that um they're planning a new feature for example now they're doing the ads and they needed to add a new quarter to parapet and then uh Miguel is coming to me to get a confirmation whether we will or or will not

### 00:51:00

**Vladyslav Krut:** need some kind of back end changes to get this implemented. And I mean like you have your development team in front of you. They can tell you why like I did not tell it this way. I just told him that yeah of course it will be needed. Come on. How would be backend know what quarter to use? Because I am not the dump. But they there are also development teams there that could probably go and take a look and give much better answers than I will give just sitting here.

**Filippo Tosetto:** um yes I noticed let me explain the reason nothing to act nothing to act about here there's no action points

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** but historical reasons uh before this team. We had a very very bad team and their estimates were completely all over the place or small things that would take one to two days they were estimating two to three weeks. So yes uh before you Andre was the uh developer advisor and it was much more handson let's say because of the bad quality of the team itself.

### 00:52:22

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** So Miguel still doesn't really trust these people because it's like oh my god are they saying telling the truth? Uh so he always try to check with an internal source of truth which in our case it's us.

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** 99.9% of times your job is to say whatever they're saying. Yes. Yes. Miguel. No. No. That's correct. Yes. Obviously if you spot something just raise your hand. But I feel that this team beside that part of not reading documentation but for the normal tasks they can be trusted to be

**Vladyslav Krut:** Yeah,

**Filippo Tosetto:** honest.

**Vladyslav Krut:** I also feel like this. I have spoken quite a lot to Vol and to Alexi. No problem on my side. Seems very trustworthy and experienced. Yeah, would be great.

**Filippo Tosetto:** So,

**Vladyslav Krut:** Also read the documentation.

**Filippo Tosetto:** so when the next time that this happens, we're going to make sure that you read with Miguel.

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** Just say,

**Vladyslav Krut:** the history.

### 00:53:32

**Filippo Tosetto:** "Yeah, that's it.

**Vladyslav Krut:** Okay, sounds good. And one more thing is u about Reuben and Face AI. So he proposed as the first thing to have a pretty

**Filippo Tosetto:** Mhm.

**Vladyslav Krut:** strict conversion of what's the story point means to days ask us to work it this way. I was battling just a little bit but then I was like oh whatever whatever you need no not correct

**Filippo Tosetto:** You know, this is Luben has been fighting this battle since day

**Vladyslav Krut:** decision

**Filippo Tosetto:** zero. And let me be be very very clear. I don't care.

**Vladyslav Krut:** That's pretty much what I said like I I put

**Filippo Tosetto:** Which which is pretty much your feeling.

**Vladyslav Krut:** 13 story point on the I don't believe this true but okay I will if three days equal 13 story point I will put this number Oh,

**Filippo Tosetto:** I don't care this all north framework story points days all of this overhead at this stage is just noise for me and I'm I'm know this is a manager should me say this kind of things But I strongly believe that especially with the use of AI,

### 00:55:04

**Vladyslav Krut:** heat.

**Filippo Tosetto:** especially with the current code base, especially with the fact that this app, we don't know where the this app is going to go. I don't care. Do you want to use days? Use days. You want to use story points, use story points. Create a map. Five story points equal one day.

**Vladyslav Krut:** Exactly.

**Filippo Tosetto:** Is it that the map?

**Vladyslav Krut:** Yes. Eight is two days, 13 is three days.

**Filippo Tosetto:** That's it. Fine.

**Vladyslav Krut:** Okay. Uh, and the other thing that Reuben pro sounds like he's not aware that we got some kind of green light to ignore parts of the North Project policies. is Herardo was well aware. Reuben seems nobody told him.

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** Should I be the one who tells him or we just pretend like that never happened?

**Filippo Tosetto:** Um, remind me which parts are we ignoring?

**Vladyslav Krut:** Well, the way I understood it when it was said just everything that could be can everything that cannot be enforced could be ignored.

### 00:56:11

**Vladyslav Krut:** So like we will have to move tickets across columns and fill mandatory fields but that's

**Filippo Tosetto:** I'm going to talk to him about it. Uh,

**Vladyslav Krut:** it.

**Filippo Tosetto:** not because I don't trust you. Is because if he comes to me, Reuben will comply. If he comes to you, then he will start to battle you and he's going to come to me and then let me do it. Let me do

**Vladyslav Krut:** Sure. I don't mind. Not like it's really bothering me.

**Filippo Tosetto:** it.

**Vladyslav Krut:** and he probably will be very surprised to see how we may be working on some of the features when uh I merge the pull request the feature become available for testing but I don't move the ticket to QA board so they can report issues quicker to me without feeling no QA pass for example this probably the biggest deviation that we have from Nor framework but it's

**Filippo Tosetto:** It's the big one yet.

**Vladyslav Krut:** so rewarding

**Filippo Tosetto:** It is less overhead for all the people involved.

### 00:57:17

**Vladyslav Krut:** Yes, absolutely.

**Filippo Tosetto:** And it was just the the the reality is that that was just created for product owners to see where the ticket is in the board.

**Vladyslav Krut:** Well, considering we don't have a lot of tickets and a lot of stuff going on on the board, Robin can probably understand that the only one ticket in progress is the only one that is being worked

**Filippo Tosetto:** Exactly. Exactly.

**Vladyslav Krut:** on.

**Filippo Tosetto:** Okay. Okay. Okay. Blah blah blah. Anything else on your end?

**Vladyslav Krut:** checking right now have had one concern.

**Filippo Tosetto:** Yep.

**Vladyslav Krut:** I didn't do really a lot of effort try to resolve it but I tried to login into my cloud app now I have it in the terminal and it now rejects my account because it doesn't give me that permission my administrator doesn't my administrator didn't assign me granted permission so I can continue using it in the terminal but I cannot use it as a separate app for some reason should I contact somebody about this or ignore for now considering I'm supposed to be anyway testing kilo

### 00:58:37

**Filippo Tosetto:** Which account are you using?

**Vladyslav Krut:** the vladislav.crite.com recruit at lit.com the the corporate email one it says that SSO is enabled so it opens the bitward and Microsoft thingy there it shows an error that I am not listed

**Filippo Tosetto:** Yeah.

**Vladyslav Krut:** enrolled in into the this program yes because

**Filippo Tosetto:** But then from the common line you can access

**Vladyslav Krut:** I have authorized before probably because of that so I still have some kind of I don't know maybe access token or

**Filippo Tosetto:** That

**Vladyslav Krut:** whatever. Try to log now. It says it sent me a link with verification code. I am about to look very stupid now. I know your IT administrator has blocked new account creation. Why creation? And you're not a member of any existing organization, but I am. So yeah, this is a little bit buggy. Do you know

**Filippo Tosetto:** as I don't know I I don't know the state of clothes code for individuals. I don't want to create any fuss around it. meaning that I rather you have access to it without knowing no one knowing about it because the other the other way could be hey

### 01:00:21

**Vladyslav Krut:** Makes sense.

**Filippo Tosetto:** I noticed that I access to it oh you shouldn't have access remove so I'm going to ask a few questions around let me ask a few questions around

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** like can we use cloud code do we have access and if you say no glad Don't do anything. Just keep using

**Vladyslav Krut:** Okay,

**Filippo Tosetto:** it

**Vladyslav Krut:** once again, not an big problem because I have all the tools in the world now at my disposal.

**Filippo Tosetto:** pretty much.

**Vladyslav Krut:** The ones that I like more and also the one that I'm supposed to be testing,

**Filippo Tosetto:** Yes.

**Vladyslav Krut:** which is conflicting a little bit, but it's all right.

**Filippo Tosetto:** Yeah. It's okay. It's okay. All right.

**Vladyslav Krut:** Sometimes that was the only thing on my list left.

**Filippo Tosetto:** Anything else?

**Vladyslav Krut:** The rest is fine.

**Filippo Tosetto:** In that case,

**Vladyslav Krut:** Yes.

**Filippo Tosetto:** but I wish you a great week. Let me know about anything else. And oh, I haven't told you. I'm actually coding this week.

### 01:01:29

**Filippo Tosetto:** I'm a developer again.

**Vladyslav Krut:** Nice.

**Filippo Tosetto:** I'm covering for I'm coding

**Vladyslav Krut:** Yes, sorry. Go.

**Filippo Tosetto:** uh I'm covering for Andre because he's off for a week.

**Vladyslav Krut:** Okay.

**Filippo Tosetto:** And uh we actually the good thing

**Vladyslav Krut:** Reject all the meetings that you had

**Filippo Tosetto:** is that this week most of the companies on holiday I mean a lot of people are talking taking days off.

**Vladyslav Krut:** because 24 Suan

**Filippo Tosetto:** Yes. And so um as we are working on this high priority project um it's a web web app. I'm actually coding this week. It's fun. It's very fun.

**Vladyslav Krut:** Yes, I

**Filippo Tosetto:** I'm uh I'm uh learning a lot of tricks with CL code

**Vladyslav Krut:** know.

**Filippo Tosetto:** which is my tool of choice. Um and I'm building interesting stuff, interesting automations. One day I will share everything with the rest of the team. First I need to to to learn a few tricks myself.

**Vladyslav Krut:** Okay, sounds interesting. Please share when you have anything to present to

**Filippo Tosetto:** Yes. Yes,

**Vladyslav Krut:** share.

**Filippo Tosetto:** I will. All right, Vlad. Have a great day.

**Vladyslav Krut:** Thanks. You too. See you later.

**Filippo Tosetto:** Bye-bye.

**Vladyslav Krut:** Bye.

### Transcription ended after 01:02:59

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*