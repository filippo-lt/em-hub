# Transcript — Victor 1:1, 2026-10-09

> Source: Granola "Víctor / Filippo - Weekly 1to1", id 1fbe4be8-c764-4e8f-8c22-20b7d77924bc. Microphone = Filippo.

Microphone: Good morning.

System audio (Víctor Jalencas): Good

System audio (Víctor Jalencas): morning, how are you?

Microphone: Uh, busy as usual.

Microphone: Busy, busy. No, I'm fine. It's Friday, we're gonna have Monday off, can recharge a bit.

Microphone: It's good, it's good. What about you?

System audio (Víctor Jalencas): I'm

System audio (Víctor Jalencas): fine too, yeah.

Microphone: Yeah, all good.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): getting into the new season of kids in the university with new channels and so on.

Microphone: Ooh.

System audio (Víctor Jalencas): So it's a bit, it's a bit, but now that things are rolling and I'm falling into the routine, which is good.

Microphone: That's good, that's good. Nice, nice. Victor, what do you have for me for today?

System audio (Víctor Jalencas): So,

System audio (Víctor Jalencas): well, I have the response to the initialization thing.

Microphone: Oh, nice.

System audio (Víctor Jalencas): I was

System audio (Víctor Jalencas): reading through it now. In Flutter, the different SDKs just register a class.

System audio (Víctor Jalencas): A native class.

System audio (Víctor Jalencas): With the runtime, and this class just sets up the communication pipes.

System audio (Víctor Jalencas): So that later Dart code can do things with it.

System audio (Víctor Jalencas): In the case of Meta and TikTok, they buffer the possible deep links.

System audio (Víctor Jalencas): That the app may have been invoked with until.

System audio (Víctor Jalencas): The Dart code is ready to process them.

System audio (Víctor Jalencas): But they don't do anything else. They just are there inert and no one initializes or runs any code.

Microphone: Okay.

System audio (Víctor Jalencas): So,

System audio (Víctor Jalencas): and

System audio (Víctor Jalencas): it's curious because I, at the suggestion of Sergio, I started using Codex. For as my agent.

System audio (Víctor Jalencas): And

System audio (Víctor Jalencas): normally with Kilo, you're— when you're working up in a directly in a project, you're isolated and it has no context. But Codex guessed that all of these questions that I was doing in the screenshot folder were because of the MarkTechKit Flutter planning. It was, it was, how does it have the context?

Microphone: Yes.

Microphone: Yes.

Microphone: Welcome to the future.

System audio (Víctor Jalencas): There's like a leak.

Microphone: Yeah, no, I agree. These tools are— now that we have access to the harness themselves, It's much more powerful than before. Before, you only used a model because Kilo doesn't really work as an harness per se. And now these tools, you see how you can improve things much more.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): yeah, yeah.

System audio (Víctor Jalencas): Amazing. Well, so it prepared me a Markdown document, which I haven't fully read, but it still suggests that we do all of the phase 1 work as native code.

System audio (Víctor Jalencas): And then, and the, but it's a suggestion we can do.

System audio (Víctor Jalencas): Whatever you want.

Microphone: Okay.

System audio (Víctor Jalencas): But

System audio (Víctor Jalencas): right now in Flutter, all of the MarkTech work is done as Dart code.

Microphone: I'm still not understanding how this translates to the Native version of it.

Microphone: So one thing, what we are trying to do is a wrapper.

Microphone: Totally got that part.

Microphone: But even if we were to use the native Dart, how does this translate to the lifecycle of the 2 native codes? That is what I don't have an answer yet.

System audio (Víctor Jalencas): I will continue inquiring in that direction.

Microphone: All right, good.

Microphone: Good progress. I like this.

System audio (Víctor Jalencas): Yeah.

Microphone: Nice.

Microphone: What else do you have for me today?

System audio (Víctor Jalencas): So,

System audio (Víctor Jalencas): um, the— well, what I wrote on the agenda.

Microphone: GitHub Security Scanner.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): uh, what do I integrate this for? Oh yeah, because this question, uh, that I posted yesterday about the, the Docker image.

System audio (Víctor Jalencas): David walked back and forth on just to run all of the scan as a separate pipeline.

System audio (Víctor Jalencas): Inside Docker, but I think that's overkill. I mean, it's a lot of overhead rising up a Docker container.

Microphone: Why?

System audio (Víctor Jalencas): Just for running 3 command line.

System audio (Víctor Jalencas): Commands, it's— I can— I think we could just include this in our pipelines as standalone commands and that will be easier.

Microphone: I think that David suggested that because he doesn't have the full context on how CodeMagic works.

System audio (Víctor Jalencas): I guess,

System audio (Víctor Jalencas): yeah. And also now I'm realizing that link I put is, yeah, it's for another reason, another thing.

Microphone: Okay.

System audio (Víctor Jalencas): GitHub offers a built-in Secrets and security scanner.

Microphone: No worries.

System audio (Víctor Jalencas): I don't know if you can click that link or you need admin permissions.

Microphone: Yep.

System audio (Víctor Jalencas): Can you?

Microphone: Oh yeah, yeah, I can. I mean, How much does it cost?

System audio (Víctor Jalencas): So it

System audio (Víctor Jalencas): offers to, apparently it's free, but I guess this is just the setting the foot in so that later they can upsell you.

System audio (Víctor Jalencas): To more expensive options.

Microphone: Right.

System audio (Víctor Jalencas): And also it

System audio (Víctor Jalencas): runs on the whole organization, all of the repositories, which may take forever.

Microphone: I'd rather not, personally, considering the amount of repositories that we have running.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): Okay, I

System audio (Víctor Jalencas): just wanted to note it so that we know that there's an option there also, or it should.

Microphone: Good one.

Microphone: My How I would run this is security gives us the task list and we execute in a smart way.

Microphone: Meaning that, yeah, sure, we're going to run those 1, 2, 3 checks in CodeMagic, but Let's please do it in a nice way instead of importing a Docker image, waiting for the Docker image to— I mean, it's going to kill all the— I mean, how long is it going to take to run a build?

System audio (Víctor Jalencas): Forever, I don't know.

Microphone: No, no.

System audio (Víctor Jalencas): GitLeaks is already fast enough, and Semgrep is also fast.

System audio (Víctor Jalencas): Less than 30 seconds, even though Semgrep, the open source edition, as I mentioned yesterday, is very poor.

Microphone: Yeah.

System audio (Víctor Jalencas): But if it checks the checkbox, I'm happy.

Microphone: It's a day.

Microphone: It's just a checkbox. It's just a checkbox. I think the GitLeaks one is more important. And I agree, should block builds. Because if you're putting there, you know, an OpenAI key, that happened in the past, by the way.

Microphone: So for that, I'm okay to block, but for the second one, code quality, come on, really? It's also a bit outdated, in my opinion, as a check.

System audio (Víctor Jalencas): Yes.

Microphone: Consider it.

System audio (Víctor Jalencas): Yeah, CodeScene or any of the new ones.

System audio (Víctor Jalencas): Probably do better.

Microphone: Anyway.

Microphone: I agree with you, Docker way too old.

Microphone: Overhead, my suggestion is let's run a POC for iMode iOS with what you suggested.

Microphone: The simple commands.

Microphone: And that's it.

Microphone: Yeah.

Microphone: Great.

Microphone: When do you think we can get this POC ready?

System audio (Víctor Jalencas): Depends. I'm gonna finish the security check today.

Microphone: Okay.

System audio (Víctor Jalencas): I mean, I started with 2 tasks for Firebase on my mod.

System audio (Víctor Jalencas): One already finished, but today I ran the verification just to make sure with Codex again. And the other, I'm about to write the rules and create a script for recreating them if need be.

System audio (Víctor Jalencas): And yeah, I could do that.

System audio (Víctor Jalencas): At least one of the comments or 2 today.

Microphone: I would like to have the full POC.

Microphone: Wednesday already?

System audio (Víctor Jalencas): Sure,

System audio (Víctor Jalencas): sure, yeah.

Microphone: I mean, Monday we don't work.

System audio (Víctor Jalencas): Oh yeah,

System audio (Víctor Jalencas): Monday will work.

Microphone: Wednesday.

System audio (Víctor Jalencas): Yeah, yeah, Wednesday is fine. Yeah.

Microphone: Yeah. Okay.

Microphone: Just taking notes.

Microphone: Okay. And iMOD uses those Fastlane shared lanes?

System audio (Víctor Jalencas): Yes, but

System audio (Víctor Jalencas): as a proof of concept, I would like to keep them isolated. I mean, I don't want to pollute other projects with surprises.

Microphone: Got it.

System audio (Víctor Jalencas): And break their pipelines.

System audio (Víctor Jalencas): With a warning, I want to refine the command and all of the options and all of the report so that it runs fine and then maybe upgrade it or promote it to the shared lanes.

System audio (Víctor Jalencas): If at all.

Microphone: I like it.

Microphone: If by Wednesday we have a proof of concept that we know is working, we can, I can talk to the other engineering managers, say, guys, this is working, add it to your whatever.

Microphone: And please by the end of October. That's it.

System audio (Víctor Jalencas): Okay.

Microphone: So the only thing that we need to do is to make sure it works for iMOD and we don't see any surprises, which I doubt, honestly, what can go wrong with this?

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): no, I don't expect any surprises. Yesterday I mentioned a private key, but it was a false positive.

Microphone: Okay.

System audio (Víctor Jalencas): I mean, it was in my repo, but not— I mean, my working directory, not in the repo.

Microphone: There are going to be repos that are going to break.

System audio (Víctor Jalencas): Possibly,

System audio (Víctor Jalencas): yeah, especially if we put the strict mode.

Microphone: Yeah.

Microphone: Which I'm fine with.

Microphone: That's the reason why we have these checks.

System audio (Víctor Jalencas): Hey, that's the goal. Yeah.

Microphone: Okay, great.

Microphone: Anything else related to this topic?

System audio (Víctor Jalencas): Nope.

Microphone: Nice.

Microphone: So jumping on iMOD.

Microphone: Yesterday.

Microphone: I spent 2 hours of my life doing the PO job.

Microphone: So First.

Microphone: I cleaned up, I closed the running sprint, which was 1 month old.

Microphone: I also reopened, I also opened a current sprint.

Microphone: By putting in this board everything that is open today.

Microphone: And majority of things are tasks that Andrej opened through his agents, and I'm going to ask him to do a cleanup of all of this. And I'm assuming that each task that he has in open is also corresponding to a PR that he has open.

Microphone: I need him to clean up all of this before he leaves.

Microphone: The plan is on Tuesday to start a fresh sprint.

Microphone: With the full team.

Microphone: You? Slava, QAs, and Martos if he decides to participate.

Microphone: To give you a sneak peek is that must-have is iPhone Duo. Again, not full design, blah, blah, blah.

Microphone: IPhone Duo, the app is working.

Microphone: And then I added a few security tickets, the blocker ones, because I don't want to overflow you with this, with tasks for iMode.

System audio (Víctor Jalencas): Okay.

Microphone: IPhone Duo. I don't know if you had the time to check, to think about it.

Microphone: When do you think we can have a Decent build working for iPhone Duo.

System audio (Víctor Jalencas): Um.

System audio (Víctor Jalencas): There's quite some work to do, but I guess

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): guess, well, I don't know for sure, but my guess is that once we fix the layout in one of the screens or 2, the other will fall in line as a domino.

Microphone: Yeah.

System audio (Víctor Jalencas): For the same reason. So I guess within 1 week we could, we could get most of the work done, the 80%.

Microphone: I was hoping one day.

System audio (Víctor Jalencas): Oh, okay.

Microphone: Damian created a skill to do the work.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): Oh, we

System audio (Víctor Jalencas): can start with that.

Microphone: Do you think that by Friday we can try to get that done?

System audio (Víctor Jalencas): Yes,

System audio (Víctor Jalencas): yes, I will, I will just fire it in parallel and all stuff.

Microphone: Exactly.

Microphone: Okay.

System audio (Víctor Jalencas): Since Codex, I've seen that Codex takes a screenshot by itself and so on.

Microphone: Oh no, it's great. It does also has a simulator integrated, so it's going to run the code by itself and that does the whole flow, so it's much quicker.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): So I will start work and check on it from time to time just to make sure it doesn't hallucinate or do stuff.

Microphone: Okay.

Microphone: That's what pretty much everyone is doing, by the way.

Microphone: Okay, good. I don't know if you noticed, but in the iMode chat, designers finally came to us, say, guys, we're gonna start to work on proper designs for iPhone Duo.

System audio (Víctor Jalencas): I'm

System audio (Víctor Jalencas): not sure I'm in those chat groups because I remember

Microphone: Oh yeah, the iMode one, literally the iMode.

System audio (Víctor Jalencas): Ah,

System audio (Víctor Jalencas): well, in that case, I did not— maybe it's in a sub-thread or something. I did not.

Microphone: Sure.

Microphone: I shared with him the folder with all the screenshots and videos that you took.

System audio (Víctor Jalencas): Okay.

Microphone: So I am expecting something to come our way.

Microphone: Sometimes.

Microphone: Very soon with a proper design for this. But for now, we must make sure that by Friday we get a working version of the iPhone Duo because they are releasing the phone next week, is it? Is it next week?

System audio (Víctor Jalencas): I don't

System audio (Víctor Jalencas): know the exact date. Yeah, wasn't it the 20-something?

System audio (Víctor Jalencas): I don't

System audio (Víctor Jalencas): know.

Microphone: Release date.

Microphone: October 16th.

System audio (Víctor Jalencas): Oh, okay.

Microphone: Okay.

System audio (Víctor Jalencas): Do you

System audio (Víctor Jalencas): know if the company will provide us with actual test devices?

Microphone: I seriously doubt it.

System audio (Víctor Jalencas): Okay.

Microphone: Worth checking though, worth checking.

Microphone: Maybe they can buy one or 2 to leave in the office and as a test device. Yeah.

System audio (Víctor Jalencas): That

System audio (Víctor Jalencas): would be it.

Microphone: I can ask Matteano, I can ask Matteano about this point. Okay.

Microphone: Question regarding the security tickets.

System audio (Víctor Jalencas): Yes.

Microphone: Have you had a chance to go through some of them?

System audio (Víctor Jalencas): Yes.

System audio (Víctor Jalencas): Actually, I had one completed a couple of weeks ago, the same day or the day after you created the tickets, but I didn't run a thorough verification. But yeah.

Microphone: Yep.

System audio (Víctor Jalencas): The app menus are hardened.

System audio (Víctor Jalencas): And now I'm working on the device, the TV details, the rate tab.

System audio (Víctor Jalencas): And the feedback.

System audio (Víctor Jalencas): There's

System audio (Víctor Jalencas): a way I found to— remember that we said to key the updates by the user, the Firebase UID, so that no one can overwrite others' comments and so on. We could do it so that old versions keep working.

Microphone: Yeah.

Microphone: Yep.

System audio (Víctor Jalencas): And only new versions are required to use the UID because we can also add a condition on the Firebase, on the app version.

System audio (Víctor Jalencas): So that we check the version. If it's an old version, we don't require the UID, the user ID. And if it's a new version, we require the UID so that further or future updates are with UID. But that's not I mean, that way it's not real security because someone could impersonate that it's working with an older version. Anyway, the probability of something— of someone figuring this out is very remote.

System audio (Víctor Jalencas): I think.

Microphone: I have a question for you because

System audio (Víctor Jalencas): Yes.

Microphone: By— as I've been running this audit for all the apps that I have, One thing that I noticed is that 99% of the data that we are storing in Firebase Firestore, so which is the problem today for us, is only written by the app.

System audio (Víctor Jalencas): Correct.

Microphone: Never read.

System audio (Víctor Jalencas): Neither by the app, nor by backend, nor by product, which is the one I was guessing would have an interest in knowing the TV distribution or whatever.

Microphone: So

System audio (Víctor Jalencas): As far as I know, no one is reading back that information.

Microphone: So why are we even writing this data? First question.

Microphone: Second question.

Microphone: Is If we only need to write, why do we need to create Why can't we create a rule where apps can only write to Firestore and not read?

System audio (Víctor Jalencas): That's the one I'm using.

Microphone: Okay.

System audio (Víctor Jalencas): That's the one I'm using. Yeah.

Microphone: So it's independent.

System audio (Víctor Jalencas): All right, right only.

System audio (Víctor Jalencas): Record. Yeah.

Microphone: I guess it's independent of the user ID in this case, because you don't care about retrieving that information.

System audio (Víctor Jalencas): No, but

System audio (Víctor Jalencas): you care about overwriting it.

System audio (Víctor Jalencas): Well, some of the records.

System audio (Víctor Jalencas): Have a timestamp. So unless you faked the timestamp, there was no way to overwrite it.

System audio (Víctor Jalencas): I mean, one document with exact same Fields, or actually, I don't— I'm not sure how these fake databases or object databases work. How do you request an update instead of a new creation? But

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): guess you have a key so that the record ID or whatever is overwritten.

System audio (Víctor Jalencas): I'm

System audio (Víctor Jalencas): a

System audio (Víctor Jalencas): bit fuzzy on this as well.

Microphone: Uh,

System audio (Víctor Jalencas): But yeah,

System audio (Víctor Jalencas): the idea is create write-only rules.

System audio (Víctor Jalencas): So that the app doesn't need to— but yeah, one of the things we wanted to prevent is some user just overwriting the record of a different user by faking its own ID.

System audio (Víctor Jalencas): The

System audio (Víctor Jalencas): record ID, but if they're using the Firebase ID, there's no way to fake it.

Microphone: I'm I'm starting to question if we even need to write all this data.

Microphone: Because if no one reads it, Why do we need to write it?

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): who cares if we stop writing?

System audio (Víctor Jalencas): Maybe

System audio (Víctor Jalencas): when— well, in the daily next week, we can ask, hey,

System audio (Víctor Jalencas): Is

System audio (Víctor Jalencas): this data even needed? Because it's just a liability for us.

Microphone: It is a big liability.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): because we have a lot of home network IPs.

System audio (Víctor Jalencas): And brands and we know, or I don't know if it's there, but maybe it's the name of the Wi-Fi, I don't know.

System audio (Víctor Jalencas): I don't know.

System audio (Víctor Jalencas): So there's a lot of details that we shouldn't have.

Microphone: For instance, why are we collecting device info here?

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): don't know. I, my, my If this was a normal company, I would say so that we can have a market distribution.

System audio (Víctor Jalencas): report or, yeah, you know, make a market study and know which brands are more common and so on.

System audio (Víctor Jalencas): But details such as their serial number or whatever.

Microphone: But we have a We already have this information in Amplitude. If we were to do market research on the most used devices manufacturer and version, That information is in Amplitude. So I'm wondering.

Microphone: Why do we have this in the first place? Is maybe this coming from Andrei's research? So this is something that we can ask Andrei.

System audio (Víctor Jalencas): No, because device info, well, device info, the funny thing is device info is iOS only, discovery feedback is Android only.

System audio (Víctor Jalencas): So

System audio (Víctor Jalencas): they're writing kind of the same level of information but in different formats.

System audio (Víctor Jalencas): So that's

System audio (Víctor Jalencas): probably bringing why your teams did not speak between them.

Microphone: I don't see any important data point here. The only thing that I can say is that maybe RateApp is potentially used by someone, but in that case, we need to remove the revenue platform ID.

System audio (Víctor Jalencas): The

System audio (Víctor Jalencas): revenue cat ID is there so that if the same user writes the app again, It's overwritten or the old Is discarded or whatever, but I don't know if They can coexist at all. I mean, it's possible that since the created date is different, we have both.

System audio (Víctor Jalencas): Records.

Microphone: Victor.

Microphone: Can you do me a favor and write in the IMO chat if anyone is using this data? Because if they are not, we stop collecting this data.

Microphone: And we remove it.

System audio (Víctor Jalencas): Yeah.

Microphone: It's going to save us so much work that I don't see the reason for it.

System audio (Víctor Jalencas): Fine. Yeah, I'm glad to do it. I'm glad to Discard this liability.

Microphone: Because if we remove the collection of this data, not only from a security standpoint, we are free.

Microphone: For IMO at least, but also all the data masking tasks that we have to hide the revenue cut ID, do this, do that.

Microphone: They're going to disappear. We don't need to work on that.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): And while you're at it, if you check the real-time database,

Microphone: Thank you.

Microphone: Real-time database.

System audio (Víctor Jalencas): Yeah, and

System audio (Víctor Jalencas): the databases and the storage below.

System audio (Víctor Jalencas): Yeah, real-time database. This is where we store for some reason.

System audio (Víctor Jalencas): The menu configuration for Android. Why

System audio (Víctor Jalencas): does

System audio (Víctor Jalencas): it need to be a real-time database? No reason. This should be a normal file store.

System audio (Víctor Jalencas): Because there's no, no, it's not time sensitive at all. It's static.

Microphone: What is this about?

System audio (Víctor Jalencas): Here.

System audio (Víctor Jalencas): So on iOS, most of the apps, most of the TV models The app queries the TV, hey, what apps do you have installed? The TV responds and then this populates the app menu.

System audio (Víctor Jalencas): For most of them.

System audio (Víctor Jalencas): And for others, it's just static hardcoded in the code. For Android, we query the TVs.

System audio (Víctor Jalencas): And then we override some of the responses with— this is for screen mirroring. This is like This could be a real-time database. This is for signaling since the devices are behind the NAT, I mean behind the firewall and so on, you need to initiate the connection backwards, so to speak. So these are As a Signaling.

System audio (Víctor Jalencas): Intermediary.

System audio (Víctor Jalencas): But

System audio (Víctor Jalencas): for

System audio (Víctor Jalencas): the other database, it's just the menu and we override some of the icons for some reason, I guess.

Microphone: But this should be in Firestore.

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): agree, agree.

System audio (Víctor Jalencas): And

System audio (Víctor Jalencas): what was— well, I could ask about this as well, but just wanted to make you aware that this is here.

Microphone: Thank you. Thank you. I haven't— this is new to me because in my head, real-time database is used for something that is not this one. So I didn't even check.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): yeah, yeah.

System audio (Víctor Jalencas): So this is where the menu information lives for Android only.

System audio (Víctor Jalencas): And for some TV models.

System audio (Víctor Jalencas): And

System audio (Víctor Jalencas): it's static, and so yeah, no need to be the This is already hardened, this part, the real-time database.

Microphone: Okay.

Microphone: Okay, thank you.

Microphone: We need to fix this.

Microphone: Well, the good news is that product doesn't have much for us to do, so we have plenty of time to fix all this technical debt.

System audio (Víctor Jalencas): Yeah, the

System audio (Víctor Jalencas): thing is to fix this for good, we would need to force an update or otherwise only the new applications will look into Firebase.

System audio (Víctor Jalencas): Yeah, I'm Okay, and I don't know if you have more about iMode. I wrote an entry into the agenda for a couple of weeks ago. I requested an AI to look into the codebase and tell me what are the More impactful things to update and so on.

System audio (Víctor Jalencas): So there's, well, I don't remember the full report, but one of the things that I noticed is that there's a lot of duplicated code.

Microphone: Yep.

System audio (Víctor Jalencas): Because there's the SwiftUI version of the controller and the UIKit. And every time we add, well, I don't know how often do we add new controls, but We need to do it in duplicate.

System audio (Víctor Jalencas): It's like it's, uh, the SwiftUI version is catching up, but it's not there. So for now we keep using SwiftUI kit.

System audio (Víctor Jalencas): Eventually, I guess it was Andrei's idea to move over.

Microphone: My question here.

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): don't know.

System audio (Víctor Jalencas): Yeah, sorry.

Microphone: Sorry.

Microphone: No, no, please.

System audio (Víctor Jalencas): So we also have some abstractions.

System audio (Víctor Jalencas): Like for every TV model, we have like big switches.

System audio (Víctor Jalencas): Invoking the same command on every TV set.

System audio (Víctor Jalencas): A specific adapter. But if they, if we were, if we use it through polymorphism, we could just simplify this. If we make a protocol and all of the libraries conform to that protocol.

System audio (Víctor Jalencas): That would remove a lot of Big switches that are all over the place.

Microphone: For me, all of this can, you can work on this once we close the security, you know, the priorities in that sense.

System audio (Víctor Jalencas): Yeah, yes.

System audio (Víctor Jalencas): Since you said, well, we don't have much to do on iMode in terms of features, well, there's a lot of technical debt that could be cleaned up.

Microphone: But that's exactly what I told Martos on my catch-up with him this week. It's like, yeah, well, we don't have much. Don't worry. We have plenty. Don't worry. I'm going to fill the roadmap for the next 3 to 6 months with things. Don't worry about it. If you don't come to me with the roadmap, we fill it. It's totally fine.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): Okay, I

System audio (Víctor Jalencas): will then send you this report over email so that you can check it at your leisure.

Microphone: So Thank you. That would be very, very useful. Thank you so much.

Microphone: I'm out.

Microphone: One last point.

Microphone: They want to build this website, iMode Discovery. It's going to be a self-contained service, so not relation yet with the app.

Microphone: User.

Microphone: Creates an account, pays through the web.

Microphone: And do this browsing. It's like a TV guide. We talked about it several times.

Microphone: Considering that I want you to focus on iPhone Duo security fixes and everything else, I'm going to kickstart this initiative with Andrei, possibly next week. He's going to stay with us just for a couple of weeks so at least he can start the initiative and let's see where, how far it goes.

Microphone: But I will involve you in kickoff.

Microphone: And any conversation, because you will need to obviously take over somehow.

System audio (Víctor Jalencas): Yeah.

Microphone: So no hands-on for you, but I want you to get this on your radar because you may need to jump on in.

Microphone: Afterwards.

Microphone: On the same topic, I'm trying really, really, really hard to get a web developer.

Microphone: From the web department, web projects, even a junior one that could help us to work on this kind of initiatives.

Microphone: I'm not expecting this person to be fully proficient in crazy agentic way of working or to work on specific complex business logic, but to work on the front end.

Microphone: Which is extremely time-consuming, having this pair of hands can help a lot.

Microphone: So just to get to let you know that this is happening also.

Microphone: I don't know if it's going to happen or not. Let's see if web people want to work with us.

System audio (Víctor Jalencas): Okay.

Microphone: Let's see, let's see.

Microphone: Okay.

Microphone: So this is everything on my end for iMode.

Microphone: And unless you have anything else for iMode, I wanted to go back to the Martech SDK quickly.

System audio (Víctor Jalencas): Yep.

Microphone: I'm I'm starting to think How to speed up this.

Microphone: Initiative.

Microphone: We are receiving a lot of pressure here right now because not only Martech wants this done, but now Matteano wants this done because And on this, I'm with Sanchez. They finally start to— Martech start to be on top of their end of things and they start to be more proactive.

Microphone: As you've seen, Sanchez opened a PR just to update the library version, which is something that I really like because that's on them, and to open this kind of PRs is not really dangerous, and the responsibility is on them.

System audio (Víctor Jalencas): Yeah.

Microphone: That's good.

Microphone: The good news is that the apps that are using these libraries, it's just an update.

Microphone: This is very good, but it's also very bad because now they want all the apps to have these libraries installed, which makes sense.

System audio (Víctor Jalencas): Which makes

System audio (Víctor Jalencas): sense. That was the goal in the first place.

Microphone: So

System audio (Víctor Jalencas): Sorry, someone at the door. Let me—

Microphone: Sure, go for it, no worries.

System audio (Víctor Jalencas): Victor

System audio (Víctor Jalencas): Jalencas.

System audio (Víctor Jalencas): Because it says

System audio (Víctor Jalencas): All

System audio (Víctor Jalencas): right, let's talk about some

Microphone: All good?

System audio (Víctor Jalencas): Sorry, I

System audio (Víctor Jalencas): can't hear you.

Microphone: Yeah, I was muted. All good?

System audio (Víctor Jalencas): Okay, you're all good.

System audio (Víctor Jalencas): Sign delivery.

Microphone: Okay.

Microphone: Nice. What were we saying? Martech SDK Flutter version.

Microphone: Pressure from pretty much, how can we speed this up?

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): don't know.

Microphone: How can we speed this up? I'm thinking— oh, sorry, now it's my turn to add to the door.

Microphone: See? Grazie mille, arriviamo subito.

Microphone: Se ce la fai, se no scendo io.

Microphone: Che sono roba di due settimane, sa, secondo me sarà pesante, però dipende quando è finito tutto. Tra mezz'ora.

Microphone: Sorry about that, we do it in turns.

Microphone: How can we do this faster?

System audio (Víctor Jalencas): I

System audio (Víctor Jalencas): don't know.

Microphone: Have you tried

System audio (Víctor Jalencas): I don't want to put more pressure on David José, so I haven't asked, hey, do you have this?

Microphone: Have you tried to outsource this to AI? See what the hell is coming out of this.

System audio (Víctor Jalencas): Well,

System audio (Víctor Jalencas): that, that the document I prepared was, was prepared by Anna and not by me.

System audio (Víctor Jalencas): What do you mean? What? What?

Microphone: Coding.

Microphone: Code-wise.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): that's, that's what I'm doing with most everything.

Microphone: Yeah, yeah, no, what I'm asking is What is— why is this taking long enough to get this?

System audio (Víctor Jalencas): I don't

System audio (Víctor Jalencas): know, maybe because I read through every conversation and so on, most of the thought blocks.

Microphone: Hmm.

System audio (Víctor Jalencas): It's a disqualification.

Microphone: No, because I'm wondering, can we get an MVP ready? And fix things.

System audio (Víctor Jalencas): Oh yeah,

System audio (Víctor Jalencas): yeah, yeah, yeah, yeah, certainly.

Microphone: By doing them.

System audio (Víctor Jalencas): Even if David has some suggestions/improvements.

System audio (Víctor Jalencas): I could start implementing on ChatAI now.

System audio (Víctor Jalencas): And see what comes out of it.

System audio (Víctor Jalencas): And leave it working in semi-automatic mode. Yeah.

Microphone: I know it's, uh,

System audio (Víctor Jalencas): I can

System audio (Víctor Jalencas): say it.

System audio (Víctor Jalencas): Create a branch, don't push anything, but keep working and let me know when this is done. Yeah.

Microphone: Well, until we have Android parity, we can't release this.

System audio (Víctor Jalencas): No, no,

System audio (Víctor Jalencas): but I can, I can, we can verify that it works on iOS.

Microphone: First of all.

Microphone: Exactly.

Microphone: So I'm trying to get my— trying to find the best way.

Microphone: To start to show some progress in this, saying, hey guys, don't worry, we are working on it.

Microphone: We are testing on an app already.

Microphone: The library is here, iOS, we are facing some issues here and there.

Microphone: To get also, if we want David Nunes to help, having a piece of code for me, it's something that it could potentially help a bit more.

System audio (Víctor Jalencas): Yeah.

System audio (Víctor Jalencas): And

System audio (Víctor Jalencas): specific questions.

Microphone: Yeah, yeah.

Microphone: That's what I think.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): I will find it the way. Yeah.

Microphone: If you can get something running by next week, just to get the ball rolling, that's important part for me, and then we'll take it from there.

System audio (Víctor Jalencas): Very

System audio (Víctor Jalencas): well.

Microphone: Nice.

System audio (Víctor Jalencas): And we

System audio (Víctor Jalencas): also have an idea of how long it will take to complete. Yeah.

Microphone: Thank you.

Microphone: Yeah, good.

Microphone: If we notice that this is something that doesn't work because of what we just discovered regarding lifecycles, Probably it's worth changing approach and involve more people. Say, hey guys, we don't have the capacity or the skills to build this from scratch because we thought that the wrapper would be enough, but we noticed that there are some blockers here. Can you help us build this from scratch? And maybe José David Núñez— Jesus, 3 words for a name? Maybe he can build it.

Microphone: Because he already started to do something for the other app, so maybe he can build it.

System audio (Víctor Jalencas): Maybe, yeah.

Microphone: But my idea is the course of action, let's build an MVP, even a throwaway MVP, try to integrate it in chatbot, see how it goes, and we take it from there.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): okay. For what it's worth, my initial idea about doing the Flutter version would be to replicate the Swift or Kotlin code in Dart. But David Català explained me why it was better to use the native one.

Microphone: Yeah.

System audio (Víctor Jalencas): I'm trusting them on this.

Microphone: Okay.

Microphone: Oh yeah, absolutely, absolutely.

Microphone: Okay, good.

Microphone: That's a lot of things for next week.

Microphone: I'm trying to say SCUF. Stuff holding.

Microphone: So just, I'm gonna send you a quick note in chat afterwards, but just to close the priorities.

Microphone: Security POC for the pipelines by Wednesday.

Microphone: I mode backlog.

Microphone: Sorry, iMode iPhone Duo by Friday, at least a build with something.

Microphone: Obviously, if you have security tickets that you can tackle, that would be greatly appreciated and move forward with the Martech version of Flap. Flutter version of the Martech SDK. If you manage to get a scaffolding or something by Friday, that would be ideal.

System audio (Víctor Jalencas): Perfect.

System audio (Víctor Jalencas): I'll get as far as I can by Friday.

Microphone: Nope.

Microphone: Yeah, yeah, yeah, yeah, nice one. Thank you, Victor. Anything else on your plate?

System audio (Víctor Jalencas): Nope.

Microphone: I have a direct question for you then.

System audio (Víctor Jalencas): Okay.

Microphone: It's, um, Context.

Microphone: My wife works as a head of customer service for lastminute.com. You know that website?

System audio (Víctor Jalencas): Let me

System audio (Víctor Jalencas): know. Okay. Yeah. Is it still alive?

Microphone: Uh, yes, they, they are alive and they are kicking because they bought a lot of other companies. So they have a Spanish version of it. So then The brand Lastminute itself was a British brand that was bought by an Italian company that bought also a Spanish company, a German company, and a French one. And so they are now worldwide. They kept the name lastminute.com, but in reality, The original one doesn't exist anyhow. That's not the point. So she is the head of customer service for that, and she handles all the customer service for each, which means thousands of agents.

System audio (Víctor Jalencas): Okay.

System audio (Víctor Jalencas): Okay.

Microphone: Not the AI agents, people.

System audio (Víctor Jalencas): Yeah.

System audio (Víctor Jalencas): 3 people.

Microphone: I mean, she has obviously an org below her and team main, a lot of things there. So my wife doesn't really know anything about coding.

Microphone: Zero, nothing. And she's not really Technically savvy in that sense. She knows how to use the basic things.

Microphone: Yesterday she called me in her studio, which is on the other room, said, oh, look what I did with Claude between meetings. She's spending most time of their day meetings, and she showed me something.

Microphone: And I was like, yeah, yeah, okay, this is the usual dashboard that Claude Code creates. And then she started to show, no, no, no, no, look, it's a full website.

Microphone: And it gets the data from their data providers, and then you can interact with agents with this. You can create scorecards, and it's all real time, raise the data, and then each team leader can have their own version of this. They can interact with it.

Microphone: She literally built a SaaS for managing a full customer service.

Microphone: In a couple of weeks between meetings.

Microphone: And I was like, shit.

Microphone: So you literally just show me that our job, engineers, programmers, developers, Doesn't mean anything anymore.

System audio (Víctor Jalencas): I'm

System audio (Víctor Jalencas): not sure I agree.

System audio (Víctor Jalencas): Have you checked the code?

Microphone: Who cares?

System audio (Víctor Jalencas): Who

System audio (Víctor Jalencas): cares? Security cares.

Microphone: Okay.

Microphone: If you put one, so what she showed me is a product that probably would take one year ago.

Microphone: 20 developers, 6 months.

Microphone: Today, her plus one developer that knows exactly what to do in terms of security, that was my only argument in terms of security.

Microphone: That's enough.

System audio (Víctor Jalencas): Also,

System audio (Víctor Jalencas): there's this new concept of prompt depth.

System audio (Víctor Jalencas): Which is how are the prompts maintained and reviewed and so on, and how long will it take for these applications to apply improvements? As real tech debt accumulates behind the scenes without no one knowing.

Microphone: But who cares, Victor? Who cares?

System audio (Víctor Jalencas): Who

System audio (Víctor Jalencas): cares? Because every time it will be more costly and more brittle.

Microphone: But then she can build a new one in 6 months because She will have different needs because she built a product to solve a problem that she has today.

System audio (Víctor Jalencas): Oh yeah,

System audio (Víctor Jalencas): yeah, that's true.

System audio (Víctor Jalencas): She can rebuild it.

Microphone: In 6 months, hopefully this problem is going to be solved.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): yeah, yeah.

Microphone: So she can build something from scratch.

System audio (Víctor Jalencas): Yeah, last Wednesday in the office when I was speaking to Sergio, I was just browsing the Kilo Dashboard, the usage, and saw that David Sanchez spent in a week, spent like $2,000 or more.

Microphone: Yep.

Microphone: That's normal.

System audio (Víctor Jalencas): And he said, yeah, yeah, but in his Signal Beacon thing, he, the team, are like constantly creating pull requests. And I mean, it's worth for them because this creates so much value.

System audio (Víctor Jalencas): And he reminded me, well, or I asked him about all of the guardrails that he put in place so that this doesn't fall like a house of cards and so that's why he's so used to just throwing PRs here and there, and that's why it's doing it with us.

System audio (Víctor Jalencas): Because he just trusts the system, the harness, to keep things safe.

System audio (Víctor Jalencas): And that's why when he started contributing into our code, he just, he made some things that were not up to our standards because we hadn't set guardrails for him to work in our repo.

System audio (Víctor Jalencas): Maybe that's one of the things that we consider, we can consider in the future so that his team can make improvements or solve their own needs.

System audio (Víctor Jalencas): Without going through us, or at least they can do it in a safe way without us having to shut down every pull request because we don't like the approach or whatever.

Microphone: So I'll give you another example.

Microphone: TraceCheck, it's a website.

Microphone: That Me and Ray built.

Microphone: And me and Ray have zero, zero knowledge about web backend and all of that.

Microphone: We built it in 6 weeks.

Microphone: And is making around $150K a month now.

Microphone: We were spending around $2K per month— per week, sorry, per week in tokens.

Microphone: But it's now making $150K per month.

Microphone: We don't care about the code.

System audio (Víctor Jalencas): Yeah, at

System audio (Víctor Jalencas): some point, at some point it's an implementation detail. Yeah.

Microphone: Because Who cares?

System audio (Víctor Jalencas): You care about the space.

Microphone: If The whole If I understand the business logic and I know that if the user press this button, this button calls the backend, the backend calls Parapet, Parapet talks to Stripe and blah, blah, blah, blah.

Microphone: Isn't this enough?

System audio (Víctor Jalencas): Yeah, at

System audio (Víctor Jalencas): some point it is, because in the same way as compiled code is a byproduct of the written code, of the legible code, at some point the whole code is a byproduct of the specs, and that's what you care about.

System audio (Víctor Jalencas): And

System audio (Víctor Jalencas): if

System audio (Víctor Jalencas): you need to rebuild the code, I mean rewrite the code, From time to time, who cares? Because as long as it's, as you can verify that it's safe and it matches the specs and so on and doesn't do anything stupid. Yeah, I, when I'm coding now, quote unquote, and I, now that I trust the tools, I spend less time checking the code itself. And that's why when you ask, that's why when you sometimes ask me a question about some details, I don't know, I didn't bother to read through every line of code. I only check

Microphone: Coding.

System audio (Víctor Jalencas): the shape of it and some specific points, but my code reviews are more specific for some details that I'm checking after, not everything.

Microphone: Yeah.

Microphone: Yeah.

Microphone: For me, it's still important for us to understand The logic, the, the How the tool, how the tool, how our software works, but the implementation details, they are gone for me. That doesn't make sense.

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): yeah, yeah.

Microphone: And, um, I think it is time to put in place more automations.

Microphone: I'll give you an example of what I did.

Microphone: Please check.

Microphone: We have tons of documentation, tons, because we write— we don't write.

Microphone: We read the documentation.

Microphone: We don't read the code.

Microphone: So that a human being can understand what's happening, data flow and blah, blah, blah. But this documentation is also for the AI. So as AI writes the documentation, Sometimes There is a tech debt in terms of documentation, so they start to drift.

System audio (Víctor Jalencas): Mm-hmm.

Microphone: And I started to notice that it was happening more and more and more because more code, more features, more things. So what I built was A loop.

Microphone: That every morning Goes through a certain amount of documents because it cannot go through all the documents that we have. So it takes, it keeps a ledger.

Microphone: Of this, today I read document A, B, and C.

Microphone: And what it does is to check for any logical drift in the documentation.

Microphone: And when it does, Find something.

Microphone: If it's something simple, automatically opens a PR. If it's something that requires a human intervention because it's more complex and say, hey, I don't know what you really mean here. Is it A or B? It does open a GitHub issue for me.

Microphone: And every morning I have the list of GitHub issues and I check that.

Microphone: It's working like a charm.

System audio (Víctor Jalencas): Yeah.

Microphone: I'm planning, I'm planning, I'm trying to do the same for code. I don't have really much time to play with all these tools, but this shows me that We, it's time for us to get there. So when you mentioned something before with iMode, that there's plenty of things to be done.

Microphone: For instance, UIKit to SwiftUI migration.

Microphone: Is it something that we can automate? Not one task.

Microphone: As a whole? On a daily basis.

Microphone: Pick one view controller.

Microphone: Translate this in SwiftUI and make sure that the 2 things are working as expected.

Microphone: Can we do that? Don't know. It's a question. Can we do that?

System audio (Víctor Jalencas): Yeah,

System audio (Víctor Jalencas): exactly, exactly.

System audio (Víctor Jalencas): Yeah, and the way that SecuWorks is like 2 levels ahead of us.

System audio (Víctor Jalencas): He told me that in Forethought or whatever is his name, he's like, he's top 1 and he's producing like 6 months of worth of work for every real month.

Microphone: Yeah.

System audio (Víctor Jalencas): It's like, and so on.

Microphone: But I believe that.

System audio (Víctor Jalencas): And yeah, yeah, yeah, he just, and he showed me a lot of tools that I didn't know about.

System audio (Víctor Jalencas): And that things that he's applying, wow, I try to keep up, but I just can't. I cannot see him in the horizon.

System audio (Víctor Jalencas): I'm amazed. And I realized that I need to catch up.

System audio (Víctor Jalencas): Put

System audio (Víctor Jalencas): some work into improving my game.

Microphone: I honestly I honestly think that If we don't step up our game, And it's more like a general, not me, you, it's more like a we as in engineers, developers, in 6 months our profession is gone.

Microphone: After what I've seen coming out of my wife's cloud code, no, no, she used cloud in general, not cloud code. She doesn't know about code.

Microphone: I was scared.

Microphone: I was, I am honestly scared.

Microphone: If she does, she just have an idea, she knows what you want.

Microphone: And she built it.

Microphone: Yeah, code debt, tech debt, whatever you want to call it.

Microphone: She can throw it away and rebuild it from scratch. Who cares?

System audio (Víctor Jalencas): Yep.

Microphone: Sorry, there was more.

System audio (Víctor Jalencas): No, no,

System audio (Víctor Jalencas): no, I agree with you. We need to show value in some other way in which we apply our experience.

System audio (Víctor Jalencas): Because your wife and others have not had their fingers trapped in the door, as we say in Spanish, no? She has not been beaten back.

Microphone: Oh yeah.

System audio (Víctor Jalencas): By some, by something she did not realize was happening and so on.

System audio (Víctor Jalencas): So that's, I hope that's where we can provide value.

System audio (Víctor Jalencas): I'm more doubtful about the current juniors and the people who is now in the university.

System audio (Víctor Jalencas): They

System audio (Víctor Jalencas): will

System audio (Víctor Jalencas): have to reinvent themselves as something else.

Microphone: There's going to be less engineers.

Microphone: And those engineers are not going to be in any way, shape, or form similar to what we have today and we used to have.

Microphone: They will not write code at all. They will talk to the system.

System audio (Víctor Jalencas): They will

System audio (Víctor Jalencas): be more like product people.

System audio (Víctor Jalencas): Technical productivity, you want, or whatever, they will know.

System audio (Víctor Jalencas): How to get what they want done.

Microphone: Yeah.

Microphone: I think there's a, I can see a clear split between As you said, product people, so more developed soft skills, understanding what the other person wants, like having this figure working with my wife.

Microphone: Say she goes with a problem and this person helps to solve it, but instead of having 12, 20 developers, just has one.

Microphone: And on the other end, I see people being more like system engineers.

System audio (Víctor Jalencas): Mm-hmm.

Microphone: Security.

Microphone: Automations.

Microphone: Making, making, creating infrastructure to make sure that whatever the AI creates is within the boundaries.

Microphone: You mentioned it before, you know, creating those safeguards so that David Sanchez doesn't break anything.

Microphone: I think what we can contribute to is to create those safeguards.

System audio (Víctor Jalencas): Yes,

System audio (Víctor Jalencas): and the tooling, yeah.

Microphone: Imagine if we don't have to build or keep up to date the SmartTech Kit, SmartTech Pack, the Flutter version. SmartTech team can do it, and we are confident they are not going to break anything.

Microphone: That is what we need to aim for.

System audio (Víctor Jalencas): Yeah, I agree.

Microphone: Victor.

Microphone: That's it.

System audio (Víctor Jalencas): Okay.

Microphone: Have a good weekend.

System audio (Víctor Jalencas): YouTube.

Microphone: Thank you.

System audio (Víctor Jalencas): Enjoy Spain's National Day.

Microphone: I am gonna enjoy it. What, what is it? Is it Independence Day? What, what's the

System audio (Víctor Jalencas): Actually, it

System audio (Víctor Jalencas): commemorates the discovery of America.

System audio (Víctor Jalencas): Well, discovered it, the, uh, Chance, uh,

Microphone: I'm confused.

Microphone: An Italian person discovered America with Portuguese money and you celebrate this?

System audio (Víctor Jalencas): Yes,

System audio (Víctor Jalencas): because all of the benefits came to the Spanish crown and to expand the influence of the Spanish Empire back then.

Microphone: True.

System audio (Víctor Jalencas): Into South America and Philippines eventually.

Microphone: That's true.

Microphone: That's true. That's so.

Microphone: So

System audio (Víctor Jalencas): It was

System audio (Víctor Jalencas): called until a couple of years ago, I think it was called Hispanic Day, and it was also kind of a mandatory celebration in Latin America, but now it's more like a Brother Spanish Brotherhood or something like this. I don't even know the name right now, but they just, they, yeah, they whitewashed it.

Microphone: Okay.

Microphone: Okay.

Microphone: Okay.

System audio (Víctor Jalencas): Because a lot of Spanish and Hispanic descent people are shamed by what really was. It was just like a genocide.

Microphone: Okay.

Microphone: Pretty much, yes.

System audio (Víctor Jalencas): Yeah.

Microphone: Yeah.

Microphone: Okay.

Microphone: Victor, I'm going to jump on the next call talking about Paywalls and Xero and all these kind of things. Yay! Woohoo!

System audio (Víctor Jalencas): Have fun.

Microphone: Thank you. I will definitely have a good weekend.

System audio (Víctor Jalencas): You

System audio (Víctor Jalencas): too.

Microphone: And see you on Tuesday.

System audio (Víctor Jalencas): Bye-bye. Cheers.

Microphone: Have a good one. Bye.