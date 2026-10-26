# Transcript — Vlad / Filippo Weekly 1:1, 2026-09-28

**Source:** [Granola](https://notes.granola.ai/d/6b1a296c-931a-4694-baea-82198498dd1b) · 11:00 CEST · F = Filippo, V = Vlad

**Filippo:** Good morning, Vlad.

**Vlad:** Hello, hello.

**Filippo:** How are you doing?

**Vlad:** Honestly, I am not doing great. About on Friday, I got sick, so I was sick the whole weekend, and I am still not feeling great today. Still debating whether I should go to medical center, get my sick leave, or I am fine and will walk it out.

**Filippo:** Oh.

**Vlad:** Oh.

**Vlad:** Like that.

**Vlad:** It happens sometimes.

**Filippo:** Is it flu or anything? Okay.

**Vlad:** It Yes.

**Vlad:** Just typical, you know, throat and cough.

**Vlad:** Regular stuff after every single trip, train, plane, and stuff like that.

**Filippo:** Regular.

**Filippo:** Vlad.

**Filippo:** Feel free to take any day off you need.

**Filippo:** Please.

**Vlad:** Yeah.

**Filippo:** Please.

**Vlad:** My debate is, do I really want to go to medical center? Because I hate this process with my whole soul. If it would be not that difficult, I would already go there and probably get The Baja Medic, we call it, basically pretty much documented by

**Vlad:** now.

**Filippo:** Yeah.

**Filippo:** Yeah.

**Filippo:** Think about it properly.

**Vlad:** I

**Vlad:** will.

**Filippo:** Yeah.

**Filippo:** Yes, please.

**Filippo:** Okay.

**Filippo:** Please.

**Vlad:** And

**Vlad:** there we go.

**Filippo:** Go.

**Vlad:** Yes,

**Vlad:** regarding the work-related stuff.

**Vlad:** So let's talk.

**Vlad:** Well, maybe let's talk AI design first.

**Filippo:** Yep.

**Vlad:** I feel like here I have the very clear point of where to stop.

**Filippo:** Yeah.

**Vlad:** Yeah.

**Vlad:** And as the 4th thing I wanted to discuss is not even about the Martech Kit or whatever else or security is the QA complained to me. that some time ago there was a change apparently in the North project.

**Vlad:** level, and they removed the split from QA backlog.

**Vlad:** QA in testing.

**Vlad:** columns. So now everything— now all the tickets that developers complete immediately goes to under testing.

**Filippo:** Okay.

**Filippo:** Yes.

**Vlad:** Pretty much.

**Vlad:** And probably it's expected from the North project perspective. However, Miguel now complains that QA is wasting a lot of time and because they There are so many tickets under testing and they spend actively time on all of them and the metric goes down.

**Filippo:** Yes.

**Vlad:** Which looks expected to me considering that we removed the split from backlog to in testing.

**Vlad:** Oh, hmm.

**Vlad:** However, I still don't understand, like, what the hell?

**Vlad:** Like, I

**Vlad:** told QA to not be worried about that. I did not ask Miguel what the hell.

**Filippo:** Let's put it like this. Thank you for reporting this, Vlad. Really appreciate. Do you do the, you know, the passing the communication? Now I understand why Miguel came to me on Tuesday with this.

**Filippo:** Because, ah, looks like the previous QA was faster, this one is slower and is spending so much time in this and that.

**Filippo:** Right.

**Filippo:** Miguel.

**Filippo:** Do you have the work done? Yes.

**Filippo:** No, but I'm gonna show you the charts on why, because it's a Thank you for reporting that, Vlad. I will, if I see the need, which I don't right now, I will raise it with them.

**Filippo:** North project team that doesn't exist anymore.

**Filippo:** I will take into consideration, but don't worry about this kind of things, please, because we have other

**Vlad:** I'm not

**Vlad:** worried if QA are worried, so that's why I'm like, I feel like it's partially my responsibility to make sure that they are not stressed because of no reason whatsoever.

**Filippo:** I'm gonna talk to Miguel and I'm gonna hear his reasoning, and then I'm gonna talk to Oleksii and I'm just gonna Yeah, put your money, it's fine, no one is gonna complain about this.

**Vlad:** Okay.

**Vlad:** Sounds good.

**Vlad:** Okay, with that done, that was simple, really nice.

**Vlad:** I was

**Vlad:** doing a little bit of progress regarding the Martekit integration, and I believe that there is no available fix for The TikTok issue that I raised on Wednesday, not spent

**Vlad:** a

**Vlad:** lot of time since then because I had, all of us had only 2 days of work since then.

**Filippo:** Yeah.

**Vlad:** So

**Vlad:** apparently I didn't know that, but today I'm smarter than I was last Wednesday, so I will show

**Vlad:** you my—

**Filippo:** Even though you are sick.

**Vlad:** Well, I

**Vlad:** see the tendency of getting smarter pretty much every day.

**Vlad:** This is a Martech kit.

**Vlad:** package file.

**Filippo:** Yeah.

**Vlad:** So apparently this section here with declaring dependencies, it

**Vlad:** goes

**Vlad:** into the project resolution.

**Filippo:** Yeah.

**Vlad:** Even if none of the other.

**Filippo:** Yeah.

**Vlad:** Targets or products are linked.

**Filippo:** Yep.

**Vlad:** Which is

**Vlad:** a noticeable problem because it does, well, not link it into the binary, but it breaks the compilation on before the compilation. Breaks the package resolution if the app has any of these dependencies, and of course.

**Filippo:** Yeah.

**Filippo:** Yeah.

**Vlad:** AI design has dependency to TikTok.

**Vlad:** Through the.

**Vlad:** Ads package global, the Google wrapper.

**Filippo:** Mm-hmm.

**Vlad:** Which is

**Vlad:** a problem, and as you told me last week, I am not a developer of MartaKit anymore, I am a user, so I will probably open a GitHub issue or something. And make sure that somebody, most likely Victor, knows how to fix it.

**Vlad:** Which

**Vlad:** also means that no progress.

**Filippo:** Perfect.

**Vlad:** No further progress on Market Kit will be done in AI Design until this is resolved.

**Vlad:** I tried a

**Vlad:** few other versions. I obviously tried not linking.

**Filippo:** Perfect.

**Vlad:** Please.

**Vlad:** It still couldn't even work because the entry point to the TikTok SDK is anyway here in Market Kit TikTok.

**Vlad:** So.

**Vlad:** Even if the resolution was solved and the package graph was established correctly, I still couldn't import what I need to provide to MarkTechKit to, well, do the init and stuff.

**Vlad:** But yeah.

**Vlad:** It's not an only issue.

**Filippo:** Can I ask you a question? Would you mind asking Damian how it did the integration in Tattooist?

**Vlad:** Sure.

**Filippo:** Because Tattooist AI design are exactly the same.

**Filippo:** Mm-hmm.

**Filippo:** They should have the same libraries and they are definitely using ads in both of them.

**Filippo:** So the TikTok issue.

**Filippo:** Can be happening both.

**Filippo:** So just to make sure that If Damian found a way to do it.

**Filippo:** Great.

**Vlad:** Okay.

**Filippo:** If this is a problem that is more across the board, I will raise the priority and ask Victor to drop everything else and work on it.

**Vlad:** Makes

**Vlad:** sense. I will do this today.

**Filippo:** Thank you.

**Vlad:** The same

**Vlad:** issue, by the way, is supposed to happen to Firebase. However, on Firebase, it by accident works.

**Vlad:** By accident, I mean that this ads group wrapper, whatever, specifies the version of Firebase up to the next major.

**Filippo:** Yeah.

**Vlad:** And the version that TikTok, that Marta Kit links is falling into this range.

**Filippo:** Okay.

**Vlad:** It

**Vlad:** works by, but not by design, by accident.

**Filippo:** So this is a problem that will arise over and over again because the libraries that we are using within the Market Kit are not exclusive of the Market Kit because As you just explained, an ad library.

**Filippo:** So one is going to use TikTok. So there's going to be a conflict. The other one, the major one is Firebase. An app can use Firebase in all the other capabilities and not only the one that we use in Market Kit. So I'm assuming this is a spread problem.

**Filippo:** I don't know if Damian found a way to fix it or to use it in a different way. Investigate with him, and otherwise we're going to push Victor to find a fix as soon as possible.

**Vlad:** Okay,

**Vlad:** the correct fix from the investigations that I have done so far is to have— to not have like one core package.

**Vlad:** A few optional linked ones, but rather a few completely separate packages with bridging.

**Vlad:** So

**Vlad:** it's usually done by a few different repositories, but we can go monorepo because it's much easier and have a few folders just inside. So when you want to link something, you link it.

**Vlad:** Only

**Vlad:** what you need.

**Vlad:** And the rest is not even participating in the resolution.

**Filippo:** Yeah, but this is going to disrupt the current architecture. We're going to need to migrate to a new architecture, and it's going to take months to get this done.

**Vlad:** Oh,

**Vlad:** I'm not.

**Vlad:** Okay.

**Vlad:** Like,

**Vlad:** that's— the complexity here is to move a few files and to create a few more package.swift files in the correct way.

**Filippo:** Hmm.

**Vlad:** What is the correct way? Well, some trial and error will be needed, but it's not about months.

**Filippo:** Okay.

**Vlad:** Well,

**Vlad:** anyway, I will talk to Damian and then either open it.

**Filippo:** And let's do the, the

**Vlad:** Or report that, okay, we found, he found the fix and I am implementing it now.

**Filippo:** Because I like also the flow that we are building here because you are just finding an issue, but tomorrow someone else will find an issue and we need a process to triage those issues. to put a service level on those issues. Yes, you're going to have an answer in 48 hours, something like that, and dispatch a fix.

**Filippo:** I need this process to be ready, and I think this is the first step. So talk to Damien, and then we'll take it from there.

**Vlad:** Okay.

**Filippo:** Nice.

**Vlad:** Okay.

**Vlad:** Probably I will anyway open a GitHub issue because if Damian has found a fix, let's open an issue to add the line to troubleshooting or to integration guide so we have the process.

**Filippo:** Great idea.

**Filippo:** Great idea. Thank you.

**Filippo:** Thank you. You're helping me a lot on this.

**Filippo:** I really appreciate this.

**Vlad:** Nice.

**Vlad:** Then what do I have here? Else.

**Vlad:** I

**Vlad:** also was doing some certain level of investigation about the analytics events in AI design, and so far we have 4 analytics providers.

**Filippo:** Yep.

**Vlad:** AppsFlyer, Amplitude, Google Analytics, and Meta, and 75 events total. And guess where they sent these 75 events?

**Filippo:** No idea what.

**Vlad:** To

**Vlad:** Optin.

**Filippo:** What?

**Vlad:** To

**Vlad:** all of them.

**Vlad:** Well, okay, I'm lying just a little bit. AppsFlyer has 4 events, Amplitude 64, and Google Analytics and Meta 75 out of 75 events goes to both of them. Anybody is using them. This is something that I will raise with Miguel probably today as well if I have enough time, otherwise tomorrow.

**Filippo:** Please.

**Filippo:** Thank you.

**Vlad:** And

**Vlad:** that I feel like all I had about iDesign.

**Filippo:** Let me add a couple of points here.

**Filippo:** Well, you answered my question regarding the integration, how it's going, could you have it done by the end of the week? But obviously the answer is, well, until I have this fixed first, I cannot move forward.

**Vlad:** I don't think so.

**Vlad:** Well, there

**Vlad:** is a little possibility, but most likely I will just not be investing my time here and waiting for something.

**Filippo:** Yep.

**Filippo:** Second point that I have is the Firestore rules that I asked about to close, to make them less public at least.

**Filippo:** For both AI Design and Face AI.

**Filippo:** Is it one of your points?

**Vlad:** No, I

**Vlad:** forgot to have it in writing, but actually

**Vlad:** it

**Vlad:** was one of my points in the different note. Yeah, it's done on both AI Design and

**Vlad:** Face AI.

**Filippo:** In prod.

**Vlad:** In

**Vlad:** prod.

**Filippo:** Yes.

**Filippo:** Thank you, Vlad. Really, really nice. Thank you.

**Filippo:** Really appreciate that.

**Filippo:** Great. Let me give you a bit of an explanation of what's happening.

**Filippo:** Regarding this specific point. So, these Firestore rules was just one of a few initiatives that are happening.

**Filippo:** The security team of Leadtech is going through all the repositories, all the apps, all the websites, all the backends, everything, and they are asking us to do an audit.

**Filippo:** Of all the security issues that could arise.

**Filippo:** Your work? A month ago? Yes.

**Filippo:** Kind of.

**Filippo:** Doing this before being asked to do it.

**Filippo:** Thank you, Vlad, really.

**Vlad:** Right.

**Vlad:** I really hope that the correct decisions were made there.

**Filippo:** Uh, 2 outcomes.

**Filippo:** The first one is something that I'm preparing, which is called Whitebook, is a security whitebook for AI design.

**Filippo:** And as there are 3 apps that are very, very similar one to the other in terms of general architecture, which are AI Design, Face AI, and The Twist, I wrapped all of them within the same whitebook.

**Filippo:** And it's literally is all about these apps use these technologies, they have a backend that use these technologies and the security holes that could be like, you know, The third-party API keys are safe in the secret manager, and the app uses, you know, all these kinds of things.

**Filippo:** And yes.

**Vlad:** Secret manager.

**Vlad:** Committed.

**Vlad:** Very broad ones.

**Filippo:** Yes, so, and I'm moving to the funny part here, is that obviously we cannot deliver a security whitebook with holes in it.

**Filippo:** So we agreed with the security team that I'm going to ship the whitebook with the fixed part, but I will create an epic with all the tickets that needs to be fixed beforehand.

**Filippo:** And you already started the work.

**Filippo:** In that sense. So you're saving me a lot of time, at least for AI design. So what is going to happen is that I will take your work and I will add a few things.

**Filippo:** That I found myself.

**Filippo:** Or that the security team highlighted first.

**Filippo:** And this is going to happen for AI design.

**Filippo:** AI and the Twist, then we will need to schedule the work in this.

**Filippo:** And I'm not asking you to do the work at all because this is something that the team needs to do.

**Filippo:** And I'm just gonna give you the Explaining what's happening.

**Filippo:** Much.

**Filippo:** So that you know why and what.

**Filippo:** There is another point here, which is In this initiative, there's also the fact that the company would like to have the ISO 2000-something certification.

**Vlad:** Okay.

**Filippo:** And this is going to happen in most likely beginning of next year.

**Filippo:** But we want to do a sort of trial run in December, and to do so, we need to comply with specific rules.

**Filippo:** The first of these specific rules is that if our software, our apps need to store personal information from a user, those information points need to be somehow masked.

**Filippo:** Or, you know, use a SHA-256 kind of algorithm to make sure that they are not readable by a human being.

**Filippo:** And this has led to the creation of a list of items that we'll need to check.

**Vlad:** Okay.

**Filippo:** And needs to be sorted.

**Filippo:** But before sharing this with you, I'm going to do an interesting exercise.

**Filippo:** I'm going to sit down with Miguel and say, Miguel, do we need this data point in the backend? These are the data points, these are the data points, these are the data points, because if we don't need them, we're going to remove them.

**Vlad:** I believe

**Vlad:** Miguel should have all the answers by now because I asked these questions recently and he had a chance to think about it.

**Filippo:** And Great.

**Filippo:** I do not accept just in case.

**Filippo:** Store this here just in case we will need it in the future. Doesn't work like that.

**Filippo:** Or we need it today and you bring me the reasons.

**Filippo:** Or I'm gonna remove it.

**Filippo:** So sorry for the long speech, but I wanted to give you the full context of what's happening and to give you all the information that you need because I'm working with the security team. I'm gonna ask you to push the developers to get these things fixed.

**Filippo:** And there's going to be a conversation with product as well.

**Filippo:** That's it, give you the full rundown of the situation.

**Vlad:** Makes

**Vlad:** sense. Okay, thanks.

**Vlad:** By the way, regarding Miguel, and just in case, recently on the sprint planning he had

**Vlad:** an idea to

**Vlad:** The imaginary scenario.

**Vlad:** If the parapet is down.

**Vlad:** And

**Vlad:** we cannot retrieve.

**Vlad:** the user's quota.

**Vlad:** Let's have it stored somewhere else, for example, in Firestore. Of course,

**Vlad:** no.

**Vlad:** Yeah, that's what I thought, but I was like sitting listening to this idea. And my autistic part got out and I just questioned why.

**Filippo:** No.

**Filippo:** No.

**Vlad:** And

**Vlad:** I kept silent. I just was waiting for an answer. Obviously there were no,

**Vlad:** no,

**Vlad:** just in case. Did Parapet before was down? Did we spot any outage now? That's what I thought.

**Filippo:** Parvet is live since 6 months.

**Filippo:** And despite bugs, because it's a piece of software, there are bugs and nothing is saying the contrary, it's never been down.

**Filippo:** And if it goes down, we have bigger issues. It's like the only reason because that thing goes down is because Google is down. And I think that there's Other issues around that point, and I don't think people will be playing with our silly apps if Google is down and, you know, everything else going around it.

**Vlad:** Okay.

**Vlad:** We see

**Vlad:** Amazon down like 3 times a year. We know how it goes.

**Filippo:** Yeah.

**Vlad:** Should not be worried too much.

**Filippo:** Yeah.

**Filippo:** And no, exactly.

**Filippo:** Perfect.

**Filippo:** Talked about— I'm checking my notes here. We talked about AI design, we talked about the Market Kit integration.

**Filippo:** We talked about the Firestore rules that you fixed.

**Filippo:** Sounds great.

**Filippo:** Okay, security we talked about.

**Filippo:** Anything else related to this area?

**Vlad:** Mm-hmm.

**Vlad:** No, I don't think so. This area is pretty clear and this one done nice.

**Filippo:** Great.

**Filippo:** Should we move to the other big area?

**Vlad:** Race check.

**Filippo:** Yes.

**Vlad:** Yes,

**Vlad:** let's go.

**Filippo:** Do you have any points for me?

**Vlad:** Yes, just a few.

**Filippo:** Yep.

**Vlad:** So I had a little bit of time on Friday. Well, not like I had a little bit of time. I just agreed that I will spend half of my time there. So I did my first hour. Set up all the dependencies. It was much more difficult than I would like to.

**Vlad:** As usually it happens with all of that.

**Vlad:** I did run it on localhost emulator and the project. I did run a search, so I did this part.

**Vlad:** It works.

**Vlad:** It's

**Vlad:** weird, but it works.

**Filippo:** Why it's weird, I'm curious.

**Vlad:** I don't know. I was reading this documentation. It's like it's telling you what to do.

**Filippo:** Yeah.

**Vlad:** But I

**Vlad:** don't even know how to explain that.

**Vlad:** It's like usually when you have an instruction, you have an order of actions.

**Filippo:** Yeah.

**Vlad:** Like you do this, then you run this command, then you launch this file, then everything works.

**Vlad:** set.

**Vlad:** of actions.

**Vlad:** But either without specific order.

**Vlad:** Or a guidance like, so you do this.

**Vlad:** But you don't know what to expect and how to treat it. Is it correct or not? Did it work? I did run tests.

**Vlad:** Okay, it doesn't report me.

**Vlad:** Did it succeed? Did it not? It's now just open.

**Vlad:** I have a server now.

**Vlad:** Why do I need this? Is it a success? Is it not success? Move.

**Vlad:** And

**Vlad:** it

**Vlad:** spreads pretty much across the whole document.

**Filippo:** Yeah.

**Filippo:** Yeah, that's all AI generated.

**Vlad:** That

**Vlad:** is very familiar to me.

**Vlad:** Yeah.

**Filippo:** Do you, for me, this is going to be a very interesting experiment.

**Filippo:** Do you think So how did you run it? By hand? So it was you? Going to the command line and writing npm run tests, these kind of things?

**Vlad:** Yes.

**Filippo:** Why didn't you use an AI to do it?

**Vlad:** I wanted to

**Vlad:** have at least a little bit of an idea what's happening there.

**Filippo:** Yep.

**Filippo:** Okay.

**Vlad:** Just

**Vlad:** tiny bit because AI reporting me.

**Filippo:** Sounds good.

**Vlad:** Yeah, tests are green and I would like.

**Vlad:** What tests? How do I check for myself? I feel like on this type of project, when I have no expertise myself, I need to get at least some.

**Vlad:** And that

**Vlad:** actually leads me to one of the questions.

**Filippo:** This.

**Filippo:** Please go on.

**Vlad:** Do

**Vlad:** you use any IDE for this project at all?

**Filippo:** Do we need— do we use any IDE?

**Vlad:** IDE, the

**Vlad:** software like Visual Studio or whatever else? At

**Vlad:** all,

**Vlad:** like sometimes, maybe.

**Filippo:** Okay.

**Filippo:** Why would we?

**Vlad:** That's what I thought.

**Filippo:** But This is not right or wrong.

**Filippo:** This is

**Vlad:** Unusual.

**Filippo:** An interesting moment in history for me.

**Filippo:** And I'm very curious about your opinion in this.

**Filippo:** Because you are more towards leaning towards the old ways, meaning you check the code, you check, you read, you go through everything.

**Filippo:** But this specific project was built to the bleeding edge of agents doing things.

**Filippo:** I have my opinion.

**Filippo:** And I have my strong opinion in some areas.

**Filippo:** But I'm curious to hear from you.

**Vlad:** Oh

**Vlad:** well, okay.

**Vlad:** I

**Vlad:** did not do much more for now. Like, I am not ready if I— I am not sure if I would like to give up on my personal human intelligence yet.

**Filippo:** Yep.

**Vlad:** Like,

**Vlad:** yes, AI should do the work.

**Vlad:** Absolutely.

**Filippo:** Yep.

**Vlad:** I want to at

**Vlad:** least understand what was done because imagine I'm taking a certain ticket and I'm being asked later like, what, did you fix that? And I'm like, I assume

**Vlad:** so.

**Filippo:** I agree.

**Vlad:** I

**Vlad:** hope it works.

**Vlad:** This part I am not ready to embrace yet.

**Filippo:** So to answer your question, IDE, I use Visual Studio.

**Vlad:** So

**Vlad:** you do use it.

**Vlad:** Or

**Filippo:** I'm not a developer. I mean, I I participated in the project on the first part.

**Filippo:** Because I was interested in the setup of the project.

**Filippo:** And I was mainly involved in the documentation.

**Filippo:** Part.

**Filippo:** Because in my head, and actually I proved myself right, if I was going through the initial phase of the documentation to set up the project itself, so what does this project do? Let's talk about architecture.

**Filippo:** Let's talk about data flow.

**Filippo:** Let's talk about data model.

**Filippo:** I went through every single document, every single word. I fixed whatever I felt that was wrong.

**Filippo:** And that is an exercise that I try to do every day.

**Filippo:** I try to do it every 2 to 3 weeks because I believe that any drift in the documentation is going to break this process that we have in place.

**Filippo:** Do I know anything about the code? I do.

**Vlad:** But

**Vlad:** not because you need to.

**Filippo:** But I don't need to.

**Filippo:** I don't need to.

**Filippo:** Do I know about the architecture? Yes, I do, a lot. I know a lot of things about the architecture of this application.

**Filippo:** I know how each module interacts with the other.

**Filippo:** And I know where each part of the application runs.

**Vlad:** Okay.

**Filippo:** I also know about why we made specific choices.

**Filippo:** And if I have to fix a bug.

**Filippo:** Create a new feature.

**Filippo:** Or do anything.

**Filippo:** Let's say that once a month I ship a couple of PRs in terms of, you know, live code.

**Filippo:** I know what's happening there because I read the plan and I challenge the AI, but that's the way I work.

**Vlad:** That makes

**Vlad:** sense. That's also similar to what I do even with technologies that I know.

**Filippo:** Am I reading the code afterwards? No.

**Filippo:** No, it's for me, it's for me as in my person, it's a pointless exercise.

**Filippo:** Because I don't understand the syntax of the code because it's TypeScript. Yes, I can read it, I can jump through it, but it's a pointless exercise because it's so much code generated that I have no idea how to interact with it.

**Vlad:** Okay.

**Filippo:** I'm not saying this is the right approach.

**Filippo:** What I strongly believe is that the first part that I talked about, knowing about architecture and the documentation itself, so how decisions are made, that is mandatory. There is no way around it. If you don't know that part, I don't need you.

**Vlad:** Yeah,

**Vlad:** that's where the difference between vibe coding and still engineering lies.

**Filippo:** Yeah.

**Vlad:** Yeah.

**Filippo:** And to close this loop.

**Filippo:** I strongly also believe that we need someone in the team and we are hiring someone in the team.

**Filippo:** That knows about web development because not knowing the ins and outs of it.

**Filippo:** Is wasting a lot of our time.

**Filippo:** 4 small details that they— I cannot take care of.

**Filippo:** Give you a simple example.

**Filippo:** The UI.

**Filippo:** The actual, you know, what you see in the screen, it's a nightmare.

**Vlad:** From

**Vlad:** whose perspective? Like, why? What's wrong there?

**Filippo:** Try.

**Filippo:** Because the AI doesn't know how to do proper UI.

**Vlad:** I thought

**Vlad:** this is the only part that AI actually perfected.

**Filippo:** No, it's exactly the opposite for me.

**Vlad:** Hmm.

**Filippo:** If Alex comes to me and says, oh, Filippo, can we please change the font size in this specific area of the application to be 2 points bigger, and I'm making a very silly and simple example.

**Filippo:** I don't know how to do it.

**Filippo:** And the result is that I need to waste a lot of tokens.

**Filippo:** Get a partially wrong result.

**Vlad:** Why? What's why?

**Filippo:** Because AI is stupid.

**Vlad:** Mm-hmm.

**Vlad:** AI is

**Vlad:** actually very smart.

**Filippo:** No, no.

**Vlad:** The way you use it, it may not be smart.

**Filippo:** But this is where I think the knowledge of the actual language and the actual technology is going to help a lot.

**Filippo:** You can spend the time to learn about this.

**Filippo:** Hey AI, teach me about how to do this.

**Filippo:** Increasing 2 points size of the font in this area, and maybe you can be guided through that and you learn for the next time.

**Filippo:** But what I found is some big limitations there and a lot of wasted tokens.

**Vlad:** And

**Vlad:** probably time as the biggest limitation here.

**Filippo:** Yep.

**Filippo:** Yep.

**Filippo:** Yep.

**Filippo:** Sorry, I was giving you the full speech.

**Vlad:** Okay, good.

**Filippo:** Any other points regarding TraceCheck? For now.

**Vlad:** Yes,

**Vlad:** a question.

**Filippo:** Yep.

**Vlad:** How do we authenticate in localhost and in dev environments? Shared dev.

**Vlad:** What type of account can we use to do pretty much anything here?

**Filippo:** Let me talk about the dev. So the one that is live under dev.tracecheck.com, you can do whatever you want. You can use any email that you come up with, like test@email.dev. Probably not that one because that's probably already been used, but it's very

**Vlad:** Okay.

**Vlad:** I, I,

**Vlad:** example@gmail.com or something like that, that's a placeholder one, and it threw an error at me. So I was like, oh well, okay.

**Filippo:** Yeah.

**Filippo:** Do vlad@test@leadech.com and honestly you can use any email that you want there. It's not mandatory.

**Filippo:** For now, unless you need to test any email inbound to your account. In that case, I strongly suggest to use an alias for your current email address.

**Filippo:** Why I say that? Because we have a lot of transactional emails like, hey Vlad, you have been registered to our service. Oh, we just completed the look up for your email address and receive an email. So if you need to check those emails, use a proper email address. Otherwise, if it's just about testing anything else, go with anything that you want.

**Vlad:** Okay, by

**Vlad:** the way, I was opening dev.tracecheck.com and probably found the bug.

**Filippo:** Yes.

**Filippo:** Which is?

**Vlad:** Which is it? Initiated a search for my phone number.

**Vlad:** It

**Vlad:** after completed in the address bar.

**Filippo:** Yeah.

**Vlad:** Uh, the— my phone number. So we decided to go and do a full search, full request, full pipeline from the beginning without me.

**Filippo:** But you haven't.

**Vlad:** Confirming it.

**Filippo:** That's very strange.

**Vlad:** I did confirm before, like last week or something.

**Vlad:** So now when I entered into the address bar trace check, tapped enter, it decided to redo everything.

**Filippo:** Okay.

**Filippo:** Here you go, your first task.

**Vlad:** Okay,

**Vlad:** that was my next question. I was like, I feel like I have read some documentation and I can try to do something about it. What should I do first? That's what.

**Filippo:** Yeah.

**Filippo:** So I put in your calendar 2 sessions for tomorrow and Friday, and what I intend to do is tomorrow is to go through a proper technical walkthrough.

**Filippo:** So all the knowledge that I have regarding the architecture, why we do things and specific things, what services we are using, and it's more about to give you the know-how of the full application and next steps for the future.

**Filippo:** On Friday, what I wanted to do is more like a live.

**Filippo:** Coding session, me and you. So I'll show you how I do things.

**Filippo:** I go through specific details.

**Filippo:** How I interact with AI, all the things that I set up around this.

**Filippo:** But.

**Filippo:** The plan.

**Filippo:** Is for you to start to get proficient in this and to start to open PRs.

**Filippo:** So.

**Filippo:** Go for it, have fun.

**Filippo:** Enjoy yourself.

**Filippo:** Try.

**Filippo:** Play with it. Break things. No, please don't break things.

**Filippo:** But, um, I told you.

**Filippo:** Spec-driven development.

**Filippo:** Pretty straightforward.

**Filippo:** Talk to the AI, generate a plan, read the plan, fix it.

**Filippo:** Outsource the coding part.

**Filippo:** You will see that in the moment you open a PR, you have 1 million tests running.

**Filippo:** Through the CI, you also have KiloCode running.

**Filippo:** It's pretty safe.

**Filippo:** I would say to open a PR.

**Vlad:** Okay,

**Vlad:** makes sense.

**Vlad:** So we

**Vlad:** don't do human review here at all, right? We don't read code. It doesn't really make sense. We read the AI function and the result of the tests.

**Filippo:** That's what I do.

**Filippo:** That's what Andrei does.

**Filippo:** There are some instances where I ask him or he asks me.

**Filippo:** To review.

**Filippo:** Something specific.

**Filippo:** And mainly the way I do it is the following.

**Filippo:** I read the PR description.

**Filippo:** To understand the context.

**Filippo:** I read any connected epic or user story.

**Filippo:** I check.

**Filippo:** The specification file that is always attached to an EPR, and that's it.

**Filippo:** If I want, I probably take, you know, Opus 5.5, run a code review on it.

**Filippo:** But it's just to be extra sure if you are touching, you know, the money path or some serious part of the application.

**Vlad:** Makes

**Vlad:** sense.

**Filippo:** You're not convinced, but

**Vlad:** Okay.

**Vlad:** No,

**Vlad:** no, no, here I'm completely fine. Like, that's probably the best we can do considering we are not web developers.

**Filippo:** It works.

**Vlad:** Nice.

**Vlad:** 90% of the time. Now I feel like for projects like this, it's maybe good enough.

**Filippo:** Mm-hmm.

**Filippo:** I think we are more towards the 99.5% of the times it works.

**Vlad:** Oh,

**Vlad:** wow.

**Vlad:** Beds.

**Filippo:** It's me.

**Vlad:** Very high percent.

**Filippo:** It's making money.

**Filippo:** It's making much more money than Face AI, trust me.

**Vlad:** Anything does much more money than PCA. Even I do more money.

**Filippo:** Um, actually, let me see. I'm curious now.

**Filippo:** Um, did it

**Vlad:** €81

**Vlad:** per month.

**Filippo:** 21 years.

**Vlad:** Was before.

**Filippo:** No.

**Vlad:** I made

**Vlad:** more money just by being on this meeting, probably.

**Filippo:** No, no, I'm checking.

**Vlad:** Yeah.

**Filippo:** Yes.

**Filippo:** Yes.

**Filippo:** Okay.

**Filippo:** Uh, Oh, we can do this through Power BI actually. We have some data points there.

**Filippo:** Electrojets.

**Filippo:** Trace check.

**Filippo:** Statistics.

**Filippo:** Yeah.

**Filippo:** So what's the day-to-date? $28,000 yesterday. We made $4,500 just yesterday.

**Vlad:** Nice.

**Filippo:** It's around— let's see your monthly revenues.

**Filippo:** Yeah, it's around $50K per month for now, but it's gonna grow much, much bigger.

**Filippo:** Much, much bigger.

**Vlad:** Okay.

**Filippo:** Uh, Blood.

**Filippo:** Any other questions? TraceCheck.

**Vlad:** Okay, I

**Vlad:** assume it worked. I tried what you recommended regarding the authentication.

**Vlad:** It accepted the email from the second press of the button, though not from the first one for some reason. Doesn't matter.

**Filippo:** Are you testing in local?

**Vlad:** No,

**Vlad:** I'm on dev.tracecheck.com.

**Filippo:** Okay.

**Filippo:** Yeah.

**Filippo:** Because in local it's a bit more complex. You need to ask your AI to mint a cookie and do some crazy things.

**Vlad:** Okay.

**Vlad:** Okay.

**Filippo:** Guys, be more complex.

**Vlad:** And

**Vlad:** regarding the payment on dev.tracecheck, can— how do we work around this one?

**Filippo:** Let me share my screen.

**Filippo:** Because So It's in Spanish. So first of all, in here you have a sort of debug.

**Filippo:** Kind of tools.

**Filippo:** So you can run the mock.

**Filippo:** Lookup.

**Filippo:** So you just use some phone numbers and the results are going to be fake, just mock.

**Filippo:** If you need to do some specific tests on the layout, for instance.

**Filippo:** Otherwise, you set the live one.

**Filippo:** Provider row view, these are some sort of debug things that we added because we needed it and you will probably want to test this kind of things. Like, this is for testing the 2 variants, the monthly subscription or the 1-day intro offer, these kind of things. But we can go through this once we need to.

**Filippo:** What I wanted to show you is something else.

**Filippo:** Just going to run the pipeline right now.

**Filippo:** Let's wait a second.

**Filippo:** This is clearly fake, by the way.

**Filippo:** All of this is fake.

**Vlad:** Yeah.

**Vlad:** Yeah, I can tell.

**Filippo:** Give it a bit to go through it.

**Filippo:** Come on.

**Vlad:** I did

**Vlad:** run it with my both Spanish and Ukrainian phone numbers. Yeah,

**Vlad:** I

**Vlad:** know it's like, but also I know that it uses some dark, uh, maybe somewhat illegal databases. I don't really know because it found some information about me from one of the providers, and the information that it found is how my name was stored in somebody's contact list.

**Filippo:** Okay.

**Filippo:** We don't use anything illegal here.

**Vlad:** Oh, I

**Vlad:** believe so.

**Vlad:** The database is legal. How they got the data is a different question.

**Filippo:** That is something I cannot tell because we are using some third-party services to do that.

**Vlad:** Sure.

**Filippo:** Okay.

**Filippo:** Perfect. So now you reach the paywall.

**Vlad:** Yep.

**Filippo:** And the good thing is that if you press the credit card here, and in here you have a Stripe kind of debug screen.

**Vlad:** Okay.

**Filippo:** Bending.

**Filippo:** And here you can see the correct one and a lot of other test credit card numbers.

**Filippo:** To recreate some specific errors.

**Filippo:** So kind of fraudulent— how do you say this in English? I forgot.

**Filippo:** Illegal? No.

**Vlad:** No, it's

**Vlad:** something about fraudulent, but yeah, after seeing it, reading the Spanish, I'm like, I don't know.

**Filippo:** You understand? Yeah, yeah, yeah.

**Filippo:** And in here you can literally just use this one or this one or this one.

**Filippo:** And you can go through the payment based on these numbers.

**Filippo:** That's it.

**Vlad:** Okay, convenient.

**Filippo:** So where is it? I can go through the correct one.

**Vlad:** Yeah, this

**Vlad:** seminar button is not to confirm. It's very important.

**Filippo:** And then you can pay.

**Filippo:** And now the full thing is running.

**Filippo:** That's it.

**Filippo:** If you want to run a test, that's it.

**Vlad:** Okay.

**Vlad:** Makes sense. I see.

**Filippo:** Okay, any other question?

**Vlad:** Yeah, the

**Vlad:** last one that I partially got an answer, but I didn't really get, is it a joke or not, about the first ticket.

**Vlad:** Do I fix the, like, what do I do? Do I fix the thing with? It's making a search just by opening the link.

**Vlad:** Or do I

**Vlad:** do anything else, take from Jira some tickets or whatever?

**Filippo:** Can you reproduce the problem?

**Vlad:** Yes, in

**Vlad:** fact, you can reproduce the problem. I will send you a link.

**Filippo:** Oh, I trust you.

**Vlad:** Open it.

**Filippo:** I trust you.

**Vlad:** Where

**Vlad:** is your contact?

**Vlad:** As

**Vlad:** you're sharing the screen, it will be maybe funny to see again.

**Vlad:** So

**Vlad:** you click on the link.

**Filippo:** Oh, this thing.

**Vlad:** I erased it.

**Filippo:** Got it.

**Filippo:** Got it.

**Vlad:** Probably not

**Vlad:** by design. Not sure how big is this issue, but you definitely wasted a token now.

**Filippo:** Interesting.

**Filippo:** So if in the URL you have a phone number or an email and the URL is the one that is created once you press the button, the submit button, And your browser has that in sort of cached and you open the website and it goes directly there.

**Filippo:** You wasted a token, so you run the lookup.

**Filippo:** Basically.

**Vlad:** Yeah, it

**Vlad:** doesn't really matter if you— I believe it doesn't matter if you already have it cached or not. If you have session, probably opening it in incognito window will do the same, but then prompt you to create an account.

**Vlad:** I can also test this.

**Filippo:** I don't think this is a bug. Let me explain why.

**Filippo:** The only reason why you may have that specific URL cached in your browser is because you run that search yourself.

**Filippo:** Or do you see any technical reason that I cannot see? I mean, unless I share it with you as you just did.

**Vlad:** Oh

**Vlad:** well, you can So if somebody would like, for example, to waste a bit of your money, I have this link.

**Vlad:** And I can run about 100 requests per second for different phone numbers.

**Vlad:** Will it do the lookup for all of them?

**Filippo:** We cache the requests. So if you search for your phone number,

**Vlad:** Yeah.

**Filippo:** We will not run it again.

**Vlad:** Okay.

**Filippo:** And we keep these results for 30 days.

**Vlad:** Okay.

**Filippo:** And we won't let you pay either.

**Filippo:** Because, you know, that would be wasteful.

**Filippo:** But if you send me the link, I will pay.

**Filippo:** So for me, this is not a bug.

**Vlad:** Okay.

**Vlad:** Then let's think about something else that I actually should do.

**Vlad:** Because yeah, I can play with codebase and stuff, but it's better if I do something useful.

**Vlad:** And take me more time, but at least I know that I have a clear goal and vision and acceptance criteria.

**Filippo:** I have quite a few things, don't worry.

**Filippo:** Let me check.

**Filippo:** Let's select this.

**Filippo:** This afternoon I will go through the Jira board.

**Filippo:** And see what's open and prepare the next sprint.

**Filippo:** I will start to assign you some tickets.

**Vlad:** Okay.

**Filippo:** And because these are bugs.

**Filippo:** Yeah, this is too technical for you just yet.

**Filippo:** No, rather.

**Filippo:** Yeah.

**Filippo:** Okay.

**Filippo:** Oh, I like this one.

**Filippo:** This is a good one.

**Vlad:** Pretty big list

**Vlad:** of open questions there.

**Filippo:** Yeah.

**Vlad:** Yeah.

**Filippo:** I will go through them.

**Filippo:** And prepare the user stories.

**Filippo:** In few words.

**Filippo:** It's actually much simpler than this AI SLOP here, and I'm going to rewrite this.

**Filippo:** As a user, I can ask the TraceCheck customer service.

**Filippo:** To remove my phone number from the searches.

**Filippo:** Hey, I noticed that my phone number is coming up with a lot of things.

**Filippo:** I want to hide my phone number so that no one can search my phone number.

**Vlad:** Sounds.

**Vlad:** Interesting.

**Filippo:** The reality of things is it's much simpler than it is because first of all, we need to, this is not going to touch the front end per se.

**Vlad:** Okay.

**Filippo:** I mean, no, it's not. No, it's not. It's not a paid feature. It's something that people send an email to customer service and we need to find a way legally. need to find a way to not display this phone number to anyone else.

**Vlad:** Is it a paid feature? Yeah.

**Vlad:** Okay.

**Vlad:** Oh,

**Vlad:** okay.

**Filippo:** So as we are using third-party services, We can ask us.

**Filippo:** We cannot ask third-party services.

**Filippo:** To remove the phone number.

**Filippo:** I know the solution.

**Filippo:** But I'm gonna let you think about it.

**Vlad:** I

**Vlad:** immediately think about some kind of exclusion list.

**Vlad:** That we check against.

**Filippo:** Yeah, that would be.

**Filippo:** That would be the solution. So I think that will be an interesting exercise for you. I will prepare it.

**Filippo:** The proper.

**Filippo:** Epic and user stories, and then I will assign them to you from tomorrow that we're going to start the new, the new epic, the new sprint.

**Vlad:** Okay.

**Filippo:** How does it sound?

**Vlad:** Say

**Vlad:** again, sorry.

**Filippo:** Yeah.

**Filippo:** How does it sound?

**Vlad:** Oh

**Vlad:** yeah, sounds good.

**Filippo:** Nice.

**Vlad:** Let's do this.

**Filippo:** Great.

**Filippo:** Other points, Vlad?

**Vlad:** No,

**Vlad:** that was the last one.

**Filippo:** Perfect. I have 2 quick points for you and then I need to jump on an interview.

**Filippo:** First one.

**Filippo:** Very, very soon you will hear from HR because they are doing some Career path.

**Filippo:** Formalization.

**Vlad:** Okay.

**Filippo:** Corporate things, Vlad.

**Filippo:** Uh, on to

**Vlad:** So, quality.

**Filippo:** Sorry?

**Vlad:** So

**Vlad:** nothing to do with reality.

**Filippo:** No, no, no, it is something that it will be.

**Vlad:** Oh.

**Filippo:** Real? And it has to do with your career path within the company and mine as well and everyone's. And it's just a matter of formalizing this because as of today, there is no way. So if you come to me and say, hey, Filippo, I want to progress to the next level or I want to reach this specific level, I would say, okay.

**Filippo:** Let me talk to HR.

**Filippo:** So this is a way to literally to formalize this and to put down a framework.

**Filippo:** For you to know how to progress or to move horizontally if you want.

**Filippo:** So this is more an FYI, this is going to come as a presentation from HR in the next weeks.

**Filippo:** They already gave us the presentation.

**Filippo:** And now they are formalizing for everyone in the company.

**Vlad:** Sound good?

**Filippo:** Great.

**Vlad:** Especially if it involves potentially some money, yeah, I'm all up to it.

**Filippo:** I guess so. Yeah, obviously this is the process usually.

**Vlad:** Come on.

**Filippo:** On another note, we are starting to formalize the holidays plan for the rest of the year.

**Filippo:** So what I'm going to ask you to do is do you mind or coming up to me with the list of your holidays until the end of the year, or you put them down here yourself, or you already send me the request through Factorial? Up to you.

**Vlad:** Uh, I will book.

**Vlad:** vacation in December, or at least take a date, take a look at dates,

**Vlad:** and

**Vlad:** I should

**Vlad:** probably request it through Factorio first, right?

**Filippo:** That's the idea. So this spreadsheet that I'm sharing with you is informal.

**Filippo:** And it's more for us managers to understand.

**Filippo:** Who is going to be around during Christmas time, for instance, in this specific period, or if there is some overlapping, missing people, and this kind of things in general. So this is more informal. So if you want to play with it, say, hey, I was thinking about this specific time period, but I don't know yet.

**Filippo:** Feel free to use this spreadsheet. Otherwise, if you're ready for updates, go through Factorial and we go through the usual channels.

**Vlad:** Okay, okay.

**Vlad:** I

**Vlad:** will do this.

**Vlad:** In the

**Vlad:** next few days.

**Filippo:** Yeah, as long as we get something sorted by, I would say, October, that would be great.

**Vlad:** Okay.

**Vlad:** I think my November is pretty much booked, but December I still have plans. I did not really do anything about these plans just yet. 4 months should be far away from now anyway.

**Filippo:** Yeah.

**Filippo:** Vlad.

**Filippo:** That is it.

**Filippo:** You are leaving us.

**Filippo:** November, okay.

**Filippo:** That's going to be a pain.

**Vlad:** Hi,

**Vlad:** what? What's there?

**Filippo:** No.

**Filippo:** No.

**Filippo:** Don't worry.

**Filippo:** It's a fact that Andrei is going to leave.

**Filippo:** The 30th of February— February, sorry, of October, and obviously you will be full-time in TraceCheck.

**Filippo:** And I can see that you have 1.5 weeks off, so I'm gonna need to come up with a plan.

**Filippo:** For your absence.

**Filippo:** It's something that I just need to plan in my head. That's it. So nothing that needs— you don't need to worry about it per se.

**Vlad:** Okay,

**Vlad:** that makes sense.

**Filippo:** Anything else, Vlad?

**Vlad:** That's it.

**Vlad:** Little probability of us finding somebody before that, right?

**Filippo:** Even if I find someone today and is going to join in a week, the onboarding, this person will not be 100% proficient by.

**Vlad:** 2 months? No, most likely not.

**Filippo:** Meet.

**Filippo:** November, once

**Vlad:** Oh, this

**Vlad:** person will probably be more proficient than I will still.

**Filippo:** Uh, yeah.

**Filippo:** I don't, I don't know.

**Vlad:** Oh wait, but yeah, we have— okay, maybe not.

**Filippo:** You know, there's

**Vlad:** All this

**Vlad:** AI-oriented workflow is still not a lot of companies adopted from what I can hear from friends.

**Filippo:** And I have to go now, but I'm interviewing a lot of people for this position and the technical exercise is to use AI and I haven't seen anyone with the level of proficiency that we expect for this position.

**Filippo:** It's very, very far away.

**Filippo:** What we see right now.

**Vlad:** Mm-hmm.

**Vlad:** I also see this around.

**Filippo:** Yeah.

**Vlad:** Yeah.

**Vlad:** It's probably because all the engineers who know how to do this type of stuff in the companies are working in the companies that encourage doing this type of stuff, and they're not looking for change.

**Filippo:** So one thing is

**Vlad:** There.

**Vlad:** Mostly happy in this position, being in front of the race rather than outdated.

**Filippo:** Yes.

**Filippo:** Exactly.

**Filippo:** Speaking of, have you used the KiloProxy?

**Vlad:** No, I

**Vlad:** did not. So far I use Kilo directly.

**Vlad:** And I like it more than Cloud Code UI, at least.

**Filippo:** My suggestion, give it a go because I'm discovering some interesting things through it. I'm using KiloProxy to use all the Kilo LLMs.

**Filippo:** Models.

**Filippo:** Through Codex.

**Filippo:** And Codex is actually very advanced.

**Filippo:** Just a suggestion, you can play with it.

**Vlad:** I dropped

**Vlad:** Kotlin because I generally speaking don't like Google models. Okay, I will.

**Filippo:** And, uh,

**Vlad:** I think about mixing the 2 now.

**Filippo:** OpenAI, not Google models.

**Vlad:** Yeah, GPT.

**Filippo:** Codex.

**Filippo:** But for instance, one thing that will be helpful is these harnesses have the connection to Chrome. So if you Develop web, you can ask the model to use Chrome directly to do all the tests by themselves and do computer use and all of that. Trust me.

**Filippo:** It's powerful.

**Vlad:** Noted.

**Vlad:** Codex and Harness proxy. Yes.

**Filippo:** Vlad, I need to jump.

**Filippo:** Have a good one.

**Filippo:** Go to a doctor.

**Filippo:** Or not, your choice.

**Vlad:** My

**Vlad:** choice. Yeah.

**Filippo:** All right.

**Vlad:** Thanks.

**Vlad:** The rest of your day and interview.

**Filippo:** Thank you. Have a good one.

**Filippo:** Thank you. Bye.

**Vlad:** See you.

