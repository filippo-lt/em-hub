# Transcript — Vlad / Filippo Weekly 1:1

**Date:** 2026-08-24, 11:00 CEST
**Source:** Granola (meeting id `7e9d737a-f90e-413a-a009-cfc1e282808e`)
**Participants:** Filippo Tosetto ("Me"), Vladyslav Krut ("Them")
**Note:** auto-transcribed; speaker names and some technical terms are garbled in places (e.g. "Vlady"/"Vlad", "market kit"/"MartechKit", "Vlachslav"/"Viacheslav", "Damian"/"Damien", "apps flyer"/"AppsFlyer", "k3"/"Kimi K2-class model", "cloud"/"Claude").

---

**Me:** Hello. Hello.

**Them:** Hello. Good morning.

**Me:** Good morning. How are you doing?

**Them:** Well, I'm feeling extremely lazy today, but other than that, I'm fine.

**Me:** It's still summer, I guess, so we kind of feel this drag throughout summer. No.

**Them:** Not really. It's cloud and windy day. It's awesome weather to be outside, to go for a walk. It's not scorching hell anymore. That's why. And I believe we have a rain forecasted for today. Type of.

**Me:** Fair point. So you like going out during rainy moments?

**Them:** In August in Spain. Yes, absolutely. Never thought I would enjoy it before, but now when I live here, yes. And you, how was your vacation? Did you disconnect?

**Me:** Yes, I did. Yes, I did. It was very good for me. Two weeks in the mountains green, nice fresh air. No many devices around me walks like 10, 15 kilometers a day. In 10 days I walked 120 kilometers. Very nice. So now I'm very well rested. I'm happy to be back. And, yeah, it's. It's good. It's good to see your face to. To be back in the craziness of the company, but. Yeah. What about you? You. You've been on holiday as well.

**Them:** Yes. Yes. I was around a week on holidays. I went to Bilbao for what I thought I was planning was six days. In reality appeared to be four because of the flights. So two days were dropped. And on my way back, I guess I got sick and the rest of vacation I spent at home. So mixed feeling. The first part was absolutely awesome. I loved it. It was. Yeah, 25,000 steps every day.

**Me:** See?

**Them:** Lovely. Nice weather. Nice air to breeze. And. And the second part is not nice. Just.

**Me:** Yep. Yep. Speaking of which Vlad, you need more to take more holidays.

**Them:** I will. I think I will ask you somewhat closer to October if it's possible to take unpaid time off while planned.

**Me:** Unpaid. Unpaid. What do you mean? You don't have enough days?

**Them:** Yes. I don't think I will have enough days for what I'm planning to take because I have a three days planned in September about like five or six in November.

**Me:** Okay.

**Them:** And then I am now looking on what to do on Christmas. And so far it says that I still have three days available. I would maybe like five or six or something.

**Me:** You know what? Well, we can talk about it later on. But I think you can do unpaid or even you can borrow from next year. But I don't know. This is something I can investigate.

**Them:** Okay. Or I can read. Maybe there are some policies that I can read through.

**Me:** Yeah. When. When you said unpaid leave, I was like, oh, God, this is gonna go. He's gonna go away for a month. No, it's for a couple of days. I don't think it's going to be a big issue, especially during Christmas time.

**Them:** Okay. Nice to know that it's technically possible regarding the borrowing from the next year. It sounds fine, of course. But next year I will have to borrow more. Like, come on.

**Me:** Fair point. Fair point. Nice. Nice. Look, let me investigate and I'll let you know regarding this.

**Them:** Okay, it's nowhere close to be urgent. I feel like it's not necessary to talk about this until October for sure, maybe even until November.

**Me:** Yeah. Yeah. Sounds good. One thing I'm gonna ask you is, could you request your days off from now until the end of the year? As soon as possible, or at least the September and you said November ones.

**Them:** September and November. You already approved.

**Me:** Oh, I did. Oh, okay. Great.

**Them:** Maybe we did not enter them to the spreadsheet where we duplicate Factorial.

**Me:** Spreadsheet. Yeah. Yeah, but it's more for having a vision of the whole engineering department. So we kind of know if we can fit all the people during times like August and Christmas. But okay, we can talk about it next week after looking at that. Nice. Nice. So how was your coming back after your not great holidays? Pretty much.

**Them:** It was difficult. Well, not really. It was pretty chill and. Okay. It was somewhat difficult. Not difficult — complex, because the things I was working on, they're pretty complex. I was addressing MartechKit issues. That was the only pretty much part that I was working on. AI Design feels very much asleep. Today we had three people, including me on the stand up — Alexis, iOS guy and QA guy. And that's it. Last week it was three to four people every day. Nothing is happening there. Gerardo is replacing Miguel while Miguel is on holidays. Vlado is not appearing on the stand up, so nobody knows what's happening, which is fine. They have a Jira board. They know what they're supposed to be working on. I doubt they're working on it, actually. But I feel like that's kind of expected. Well, the pull requests are being created and I'm approving them. So I assume the activity is happening.

**Me:** For me, this is good, meaning that things are moving forward. You see code going through. And so from an engineering perspective, we are doing a good job. You're approving the pull requests. Things are moving. If product cannot move forward, well, there's nothing we can do about that.

**Them:** Yes.

**Me:** So please keep reporting back regarding AI Design. I'm expecting when Miguel comes back from holiday to have a bit more clarity on the structure. It is a bigger conversation regarding the sort of restructuring there is going to happen in product regarding families and who's gonna own what and the people involved. But from an engineering perspective, nothing is going to change. It's more about on the product perspective, how they're going to change. I don't know anything right now, so I cannot tell you anything about this right now.

**Them:** Okay. Tell me something. But you know something.

**Me:** Yeah. One thing for sure is that Edo will not be part of AI Design. It's just there to support if needed.

**Them:** I was hoping so. Yeah.

**Me:** Oh, yeah. Everyone is open. So I shouldn't say these things to you.

**Them:** That's fine. We are not recording and not transcribing, so that's fine.

**Me:** One thing. I want to thank you because you actually managed to do a release of MartechKit before your holiday, as you promised. That's good. That's very good. And you closed a couple of the most important issues there. So well done.

**Them:** Thanks. Yeah.

**Me:** Good. So what's going last week while I wasn't around?

**Them:** So last week, Damien found an issue with TikTok integration to be.

**Me:** Yeah, I reported as well that same issue time ago.

**Them:** Yeah, but. Okay. Okay. Damien tried to fix it. And he generally speaking addressed the main bug. However, he touched a lot of areas that needed more work but left a few. We had comments that maybe we're not, like, completely part of the pull request Damien was hoping to do. So later I contacted him and I offered the help and he accepted my help. So I finished the pull request, basically. Addressing all the surrounding issues. This is the pull request that you — no, this was merged already, successfully approved and everything is fine with it. So TikTok is now working as expected.

**Me:** Just to understand — fix the bug for TikTok but also touched other areas.

**Them:** That's it, only really. Yep. Basically what he had to do is he had to introduce one breaking change, which is to have a separate identifier for like numeric identifier of the application, not the Apple bundle ID that we put like com.mau.whatever, but the numeric one. But as it was already a breaking change and he was patching things in the TikTok configurator, if I remember correctly, the entity that was never supposed to be public, [I] asked him also to just make the entity not public and a few more things. Yeah. So I ended up doing it myself. So then I left a bunch of comments and addressed them.

**Me:** Okay. Okay. Sounds good. Have you found Damien's contribution valuable?

**Them:** It's like, yes. And the rest of the stuff that I ended up doing myself, I should have just, you know, done myself in a separate PR. I just saw an opportunity to, you know, to hop onto the pull request with the breaking changes. So I decided it would be nice to, you know, address some issues that I was just not wanting to do until we have a reason to.

**Me:** Okay, got it.

**Them:** And yes, it was [an] opportunity with breaking changes. It could be a separate pull request and then Damien would just have closed the pull request completely. Oh, sorry. Closed the ticket. And then I would do the rest of the cleanup and safety for adopting apps and stuff like that. Yes, it was valuable.

**Me:** Okay. Why am I asking this? Having a senior developer that works directly in apps, Damien in this case, to be part of the Martech team not to write the code, but somehow to give us feedback. That's what I'm trying to understand. Is it valuable? Should I try to get more of Damien's time around this? That's what I'm trying to see, if it makes sense.

**Them:** I don't really see how you get more of his time to provide us a feedback without him, you know, like actually doing stuff. Yeah, it would be nice to get a feedback from somebody who is adopting MartechKit across different apps. That would be absolutely valuable. Yes. How exactly can you achieve that? [It feels] like that's more up to you. Well, we can ask if there are any other issues or struggles or APIs not clean or documentation is misleading. But generally speaking, getting more of his time here.

**Me:** With most exposure to apps, meaning that he is on top of three different apps — video app, photo app and the iMote, but also Tattooist. So he would be the perfect person here because each of these apps may have their own, you know, peculiarities. So he will use the MartechKit in different ways.

**Them:** I hope he won't. But we will see. I'm trying to design it in a way that it's used equally easy everywhere. But we will see how actually that works.

**Me:** I mean. Yeah. Because there are two levels here, and this is my past experience. One thing is the integration that you are trying to make as seamless as possible and looking at how you refactor the code, but also documentation. You are on a very good track. So thank you for that. The second part that we haven't yet seen, but I'm expecting in the future is usage every day. So I'm expecting sometimes there's going to be bugs. There are going to be hard to reproduce and we need proper tooling to allow developers to debug those issues. And that's why I'm trying to think what is the best way to get Damien involved in all of this. But this is a bigger conversation and it's more like bouncing ideas with you.

**Them:** It would be definitely great to get a bit of his time here. I'm not sure how exactly.

**Me:** I'm gonna find a way. I'm gonna find a way. Okay, nice. Thank you.

**Them:** So let's go to the first part of the week and the second one is spent working on AppsFlyer and request tracking and IDFA order and problematic setup and that part. That part was actually very difficult because there is no universally correct solution. There is a sacrifice that we will have to make on one of the sides. And I believe I found the cheapest one. So let me try to, you know, condense the information into one point. We ask for IDFA. When we request tracking and the user may either approve or reject — if they approve, all good; if they reject, it's also fine. Both ways AppsFlyer starts with an answer. Either we provided IDFA consent or we did not provide consent and then AppsFlyer starts. The issue can happen if the app has tried to request the tracking, but the system prompt did not appear. This is—

**Me:** How, how can that happen?

**Them:** That can happen in about six different ways. And three of them are kind of important. Why [I] know about this? It's because there was a thread on Apple's forum where the Apple engineer responded on how it could happen. Majority of the issues are not actually issues for us, but there are a few that we need to be aware of. So one is that if another system prompt is being shown, like maybe notifications or something, the system will not queue the system prompts up. It will just discard the other one. So that can happen and we should be aware of this and we should be prepared for this. And I believe I added this type of handling. It's based on trying again when the app is active next time. Sorry, not the app is active — the app becomes foreground. Why it's important is because the system prompt puts the app to background effectively for a little bit.

**Me:** The system prompt sends the app in the background.

**Them:** Well, the event that [the app] goes to foreground fires after closing the prompt.

**Me:** Okay.

**Them:** That's a partially important thing. So what I did to address that is now we actually fail the request tracking. This function will throw and the adopters are prompted to just retry.

**Me:** Yeah.

**Them:** With information with the reason. There are a few cases there. So this is the important finding that we did. And another situation that we need to be aware of and address is that if the app is not in the foreground, the prompt will not be shown. [This should] generally speaking not be an issue. However, it may be, for example, if we call it — I didn't know that it's new, by the way — from the application delegate immediately, like from `didFinishLaunchingWithOptions`. Apparently at this moment app is not in the foreground yet. I didn't know that. But we should not be calling it from app delegate. We should be calling it later. And this is another reason now why this function can fail.

**Me:** I didn't know either.

**Them:** So the solution is again just retry. And there are a few — like it should not be called from an app extension. Obviously, we would not, you know, and a few more minor cases. But these two were somewhat important. To give developers visibility and to allow them to retry. Then back to the AppsFlyer and tracking and order. There is a situation when the ATT prompt is shown and the user just walks away or, you know, closes the app, not kills it, but sends it to background. Then we have a hard choice to make. Like do we wait for the user forever before we start AppsFlyer? That's a bad answer. We should not be waiting forever to start AppsFlyer. Probably we should start AppsFlyer as soon as we can. But until my PR is merged, we started only upon successful receipt [of an] answer to the ATT prompt. Oh, no, it was not a very new thing. It was described in the ticket that you created.

**Me:** Yeah. But now I realize a lot of problems are related to this. Okay. Okay.

**Them:** So we should have some kind of timeout after which we just start AppsFlyer without the knowledge about the consent. And proceed. This way we keep the attribution, but we don't have IDFA. Which I decided that it's completely fine based on the statistics that I found on web for this in the last years that about 60, 70% of users do not give consent anyway. So like losing one, it's probably cheap. But we keep the attribution. That's important — was not the case before. Now we will do this. And then it's like what timeout should we choose? Well, I have decided to go for a minute.

**Me:** It's a long time.

**Them:** It's a long time. But I also found in AppsFlyer SDK there seems to be a separate function specifically designed for our use case. And it's pretty much called like "attempt to start after certain timeout provided user gives or gives not an answer", like something like that. So we can — yes. So we can [tell] AppsFlyer to run before actually requesting a prompt and AppsFlyer will wait for this timeout. And if AppsFlyer does not get an answer in that timeout, it will just start anyway. And what I really hope — I believe I checked at some point, [I] just forgot the answer — [is] that if the app gets killed before the timeout expires, it will retry, it will catch everything that's needed and restart on the next application launch. I was checking this and I forgot the answer. I assume [it] caches this because I opted for this option.

**Me:** Why do we need to wait to start AppsFlyer? Can we not start it on app launch?

**Them:** If we do not wait for it, like there is no way we can attach [the] user's consent to already started AppsFlyer ever.

**Me:** Oh.

**Them:** So it's an unrecoverable state.

**Me:** Got it.

**Them:** So we can assume that [the] user [will] never give us consent and then we start AppsFlyer immediately. But that's probably also not really what we want. We want to harvest the permission when possible.

**Me:** No, absolutely not.

**Them:** And situations when [a] user got the prompt and decided to hold on for a minute are pretty rare, I feel like.

**Me:** Okay, got it. Thank you. This is very deep and it required this analysis. Nice. Thank you so much.

**Them:** I have redone my solution three times at this point because I was discovering new things.

**Me:** But it's a very complex topic.

**Them:** So.

**Me:** Engineering tasks can be two things — [either] long tasks because you have a lot of things to develop, or very deep tasks. I don't feel MartechKit requires a lot of code overall.

**Them:** Now it's like [a] very tiny amount of code and a huge impact in overall complexity.

**Me:** I have a question which is, in your opinion — now, let's park Vlad working on the MartechSDK and think about Vlad as the developer that needs to integrate the SDK and work in apps like in Face AI, for instance. Do you think the knowledge that you are acquiring today can be helpful as a software engineer working on an app? Or you don't care as long as you know it's working. And you don't have to think about these things.

**Them:** As just a developer working on the adopting apps, I probably do not need this type of context. Like, no, I don't think it's necessary.

**Me:** I still think that you would need a high level understanding [of] what's happening. So [why] exist in our [stack] AppsFlyer, Amplitude, RevenueCat. How the information flows regarding the case that you just described.

**Them:** So if developers do not have this information, they have today — we will have an implementation as we had before MartechKit. So everybody is doing something. There are a lot of bugs [and] issues. Somebody is hoping, trying something. Parapet is not working. Oh, no, maybe not the Parapet is [the] issue. Events are missing. Why is [it] there missing? QA still lost. That's what happened. But that was happening because nobody knew, not just the, you know, high level context and how the data should flow, but because nobody knew what is expected.

**Me:** Interesting.

**Them:** If they would just know that, okay, this needs to be done. Like, yeah, data should flow from RevenueCat ID in this order to these libraries — that all would be pretty much pretty easy and they would not need to think about a lot of cases. That's definitely way too deep. Like if as a developer to me somebody would give a library and tell me, just call this at this moment and this function later and then you catch errors and you retry in these two cases and you report other ones. I would be like, great. I will do exactly that.

**Me:** But — and. What if I come to you, I'm a Martech person, come to you and say, hey, Vlad, Face AI has some attribution issues.

**Them:** Then it would be funny. We would have exactly what we are having today. Developer going, trying to fix something themselves, not being able to and coming to development advisor or engineering manager and altogether [we] locate and find issues, maybe even on the Parapet side.

**Me:** Where I'm trying to go here is I'm very happy that you are developing this very deep knowledge. And I think that someone in the whole engineering team outside of Sergio['s] orbit should have this knowledge. Okay, what I'm questioning is should this knowledge be centralized in one or two people, or should we spread this knowledge even at a high level to everyone? Because there's gonna be issues. And before people start to come to you saying, hey, Vlad, MartechKit is not working. Maybe we should give them the tools and the knowledge. So that they can do a very high level debugging saying, oh, attribution is a problem. Well, probably it's not because of MartechKit. It's because I've done XYZ.

**Them:** All the knowledge that I just gave you in a condensed way, I keep it in the repo as well. It's not been, you know, held and protected. It is spread [in] some parts across troubleshooting, some of the integration guide. Some pieces of information that link to that Apple thread directly attached to certain classes.

**Me:** Okay.

**Them:** So I feel like if you ask AI to debug [a] very specific issue, it will go and read through sources as well maybe and will find possible root causes.

**Me:** Okay.

**Them:** So I'm not like protecting this info. I know very well for a fact that I don't have excellent memory and I will forget it myself. As I already did today regarding comments and — well, AI also does that by default. So it's not like it's difficult or something.

**Me:** Okay. No, I'm not questioning. I mean, I know you're not holding that in [or] hidden somehow. Now it's just an idea of creating a simple document, high level, explaining how data flows. That's it. Something that I believe all the people working in this company must know. That we use AppsFlyer for attribution, Amplitude for event tracking and RevenueCat for, you know, purchasing stuff. I'm wondering — and again, this is more like a brainstorming than anything else — is MartechKit the right place [for] this knowledge? Does this knowledge belong to Martech itself, probably, and they need to be the one advocating for it? I'm thinking, I'm thinking.

**Them:** I am curious. So I have now this understanding from the engineering perspective because I was digging into the separate SDKs. Figuring out how they work. Like that's how I obtained my knowledge. Is the data flow from the Martech perspective [looking] different or the same as to what I have discovered from iOS-specific digging into [third-party] libraries?

**Me:** Martech dictates how those libraries interact between themselves and with our apps.

**Them:** So does Martech dictate at which point in time we should start AppsFlyer, for example? Oh, so maybe I have accidentally broken this contract. Because I decided to start it earlier. To schedule it earlier. Okay, let's put it this way.

**Me:** And no. Let me explain. I know that they have some rules in mind, but there is also the technical feasibility of those rules. From your words, we cannot start AppsFlyer before the user gives consent.

**Them:** I know we can. We just will not have the knowledge about the consent.

**Me:** Yeah, but that's the point. So if in, let's call it the Martech algorithm — I don't know how they work themselves — but if they expect AppsFlyer to be the first thing that needs to be initialized and then all the rest consequently, what you just described to me is a way that it cannot happen because we are waiting for user's input here.

**Them:** Yes.

**Me:** Unless we initialize it with the wrong information, which I'm assuming it's not something that we want.

**Them:** So it's not like we are getting a fake ID. We are just not getting an IDFA. Like not the wrong one. But no IDFA — which is what will anyway happen if the user rejects the tracking.

**Me:** This is a case where we need to discuss with Martech.

**Them:** Let's then discuss with Martech. I'm very sure that this is the cheapest way we can get. But let's make it look like it was their decision and not ours.

**Me:** There is a chat you've been invited to with some Martech people.

**Them:** A few of them in fact. One, I assume — MAU app smart SDK, maybe this one.

**Me:** That is correct. That's the right place to ask this kind of questions.

**Them:** [I'll] pin it somewhere because it's very easy to lose. Okay, will not happen.

**Me:** I will just put it as, hey, I'm trying to fix a bug here and I'm wondering if this is the right way to move forward — or try to find a way where you get this information out of them. Word of advice. I don't know if you read the amazing article that was running around the last couple of weeks regarding "meat proxy". There was an article where the title was "don't be the meat proxy".

**Them:** No, I didn't.

**Me:** And it is related to AI slop and people just copy and pasting these massive blobs of text into chats. So Martech team sometimes is a bit of a meat proxy.

**Them:** How do you battle it from your side?

**Me:** Just ask questions. Just keep asking questions.

**Them:** And you say agents contradict themselves and then they [are] forced to think actually. Okay.

**Me:** Correct. Yes. Yes. Okay, Vlad, thank you so much. In your opinion, this fixing and refactoring, how long are you going to run it for?

**Them:** I would say we're close to be done with specifically fix[es and] refactoring.

**Me:** Okay.

**Them:** This is the last ticket that I have for iOS. Well, there's one about tests, but that's only about tests. So that's not like something serious.

**Me:** Okay.

**Them:** It is a last big batch of actually behavioral fixes. Should we refactor it later to have the state not be static and be testable? Oh, well, maybe not — [we] have now tests that run in series, which is okay. It's a little bit longer, but it's still under a minute. So maybe we don't really care. We can just keep what we have.

**Me:** Okay.

**Them:** Yeah. Like the [purist] in me wants to get it right, but in the sense that it will not bring any value to anybody. So it's maybe not. And after that, what I was planning to do next is the debug UI to give [to] adopting apps and then integration test run with Face AI [which] should be like one prompt and then AI Design. And it—

**Me:** For me, but this is something I will discuss tomorrow in the daily with Victor as well. There are a few priorities. Just to give you visibility: completing this round of fixes, obviously integration on AI Design, iOS 27 tests to make sure this library works with iOS 27. Because guys, [in] one month time, even less, iOS 27 is going to be out. Our apps will be used in iOS 27. Have we tested it?

**Them:** [It's] not [something] any of us did. In fact, I don't really know what's planned to be in iOS 27.

**Me:** Okay. That's my point. So usually it can go two ways — or extremely good or extremely bad. These two, three things. Then there is the old Braze integration, which I'm gonna delay. And then meanwhile, I'm expecting to get the Android version fixed. I have questions regarding that in a second. And then Flutter released. Looking at the calendar, most likely mid-September. This is what I have in mind, but I want to discuss tomorrow with you and Victor regarding this timeline and kind of get into a close of the August huge sprint [and] start to be a bit more proficient in terms of two week sprints, proper tasks there and try to be a bit more, you know, predictable in terms of releases and what is expected there.

**Them:** That's right.

**Me:** Let's try, let's try.

**Them:** [It's] not like we are making buttons and text and screens here. Let's try.

**Me:** No, but I think with a bit of planning we can go there. I'm not expecting the iOS version of this SDK to have any more major issues after you complete this batch of fixes. So the next would be, you know, integrate this new SDK [with] Braze, for instance — this should take you one sprint and that's it. I'm not expecting any major work refactoring and doing crazy things.

**Them:** [I] hope that will be the last one.

**Me:** Yes. So Victor is back. Have you managed to meet, to talk a bit?

**Them:** Yes, we had two [syncs] before last week.

**Me:** Okay.

**Them:** It went pretty well. It looks like Victor [has] taken ownership over Viacheslav's findings. He prepared a list. He sent it to me. I promised to take a look later and never got back to [it] because I [in]formed Victor and Victor says he's gonna take care and create tickets and stuff. So it's like, okay, maybe it's not my problem. Maybe it should be. I haven't really decided. The timing was perfect. I contacted Viacheslav on Monday before Victor was back, if I remember correctly. The list was not yet ready for him. He provided [it] by Tuesday. And on Wednesday in the morning we [could] start taking a look at [it]. So that's it.

**Me:** Sounds good.

**Them:** Generally speaking, sync with Victor went pretty well. I explained a few things — a few of the most game changing decisions that I made [and] the reason behind them. And Victor just agreed on all of them. He was like, yeah, that makes sense. Sure. Yeah, like that.

**Me:** Good. Good.

**Them:** We do not have any more conversations regarding any points. I think.

**Me:** No, no, that's — as he has been away for three weeks and during these three weeks a lot [of] things changed, I wanted to hear from you if everything went the right [way] in that sense.

**Them:** Yeah, everything went pretty smooth. I explained a few decisions and he [said], oh, yeah, sure. They cannot test [the] edges anymore because we have [to] get three points. So let's not have them.

**Me:** Okay.

**Them:** True.

**Me:** Sounds good. Vlad, I need to catch up with David Matellano in 15 minutes, but apparently [Viacheslav] has been assigned 50[%] of his time on MartechSDK. Martech pack. Sorry. Yes.

**Them:** Okay.

**Me:** That's what I requested before my holiday. Apparently this seems to have gone through. So I will involve him more and more on this because by briefly checking the Jira board, the backlog, I see a lot of tickets there.

**Them:** The document is huge. Yes.

**Me:** Considering that neither you nor Victor is an Android expert, [we need Viacheslav] involved in this and to spend the right amount of time to fix things and go out with something stable. Once we have something stable, I believe adding features in the future shouldn't be that hard. But first, the core of the library needs to be stable. Exactly what you're doing for iOS.

**Them:** Yes, that's true. Without that, it would be pretty difficult to make Flutter, I believe.

**Me:** Correct. What do you think about him in terms of — I'm not debating the skill set, I think from a skill set perspective, from what I've seen in the past and [what] I'm seeing right now [it] is pretty good. I'm debating his commitment. What's your perception?

**Them:** Assuming he had half of his workload being dedicated to Martech pack while the whole week while I was off. The Friday before, maybe Thursday before, not sure. And then Monday and Tuesday, it took him to prepare this list. And he told me that this is a functional [bug list], the architectural review is coming soon. And I [don't] know if it has ever came. I'm not sure that he was [dedicating] all this time towards Martech pack.

**Me:** Okay.

**Them:** The skills, though, I feel like I kind of struggle to evaluate. I have [read] a few of the points from the list he sent and [it's] like, okay, it sounds smart to me. I do not really understand everything that it says here, but [it] sound[s] smart. But also AI does it all the time. Even when it's saying something extremely stupid. So it's like every single item from this list needs to be run through, you know, [a] non-biased agent asked to verify. I think this list is honest. I don't think it was one prompt, you know, and fire and forget. And here is the output.

**Me:** Honest.

**Them:** I think it look[s] valid to me.

**Me:** [Okay.]

**Them:** From what I saw on iOS, some of the issues are the same. It looks honest, but it needs to be checked if you want to make some decisions here.

**Me:** I'm going to investigate this throughout this week. First, I need to take care of other priorities. But as long as this guy is involved and works on it, I'm happy that — again, 50[%] of his time should be here. And I'm going to drag him into this project. If he's not really committed... I'm assuming he hasn't shown his face during the dailies.

**Them:** Okay. You did not come to the [dailies].

**Me:** Okay. That needs to change.

**Them:** Oh, yeah. I was like, camera was open. Yeah, he did not come yet.

**Me:** Yeah. Okay. So I'm going to push him to be part of this because we need him to report back on his doing every day.

**Them:** Okay.

**Me:** Nice.

**Them:** Sounds good to me.

**Me:** Vlad. Anything else related to this?

**Them:** To this? No, I don't think so.

**Me:** Okay. Nice. So let's close MartechKit, Martech SDK, whatever you need to call this. Anything else?

**Them:** Did you see that they accepted Kilo [Code] as our primary tool?

**Me:** That was my next topic. It's interesting because most of the senior devs working in MAU — you [are] one of those — have complained about Kilo.

**Them:** Like, I certainly — I tried for a week, and then I decided that this tool is just not ready, not suitable to be doing the work that I'm doing. So I stopped even participating in testing. I was like, why would I force myself to make things with the tool that is not suitable?

**Me:** I do not [know] the full reasoning behind it. I will get it in 10 minutes. But I know for sure that one of the big, big, big decisions driving [this] here was the availability of cheap models.

**Them:** Who is using cheap models? Like very cheap. The models that are nearly free.

**Me:** I don't know.

**Them:** Who is doing this and why? And that's unrelated. Second is Cursor gives you almost the same list.

**Me:** But I don't have information right now to discuss about this topic. I just wanted to let you know if you haven't heard that Cursor will go in mid-September and you now have Kilo Code to do everything. What I've seen also by reading that email is that there are different sort of tiers and from a base perspective, we are part of the MAU team. But if you start to use this tool in an agentic way, as we did, for instance, to develop TraceCheck website, you will be moved to a different tier. Why is this? So that if we use [an] agentic way of working, we are spending much more money, obviously, but this budget is not touching the MAU budget. That's the reasoning behind this.

**Them:** Okay. This part of reading I understand here.

**Me:** [Cursor] didn't allow us to do this before.

**Them:** It's very obvious. Yes.

**Me:** Why is this? And this is a concept that I kind of agree on. There are projects that are working on a day-to-day basis which should have a budget. I don't know how much — $50, $100, $200, $1,000 a month per developer. And there are other projects that require way more involvement so that we unlock higher budgets. I'll give you an example: with Andre, we worked on TraceCheck web. And we were spending around one to two thousand dollars a week.

**Them:** Oh, wow.

**Me:** Yeah.

**Them:** That's [a] pretty expensive website.

**Me:** But why? Because we had a really short timeline to release a big website. And neither me [n]or Andre were web developers. So we simply set up this agentic way of working connected to Jira and a lot of tests and a lot of stuff. And so we managed to deliver this in record time. But Cursor doesn't allow us to do this and [other tools like] Codex or Claude Code allow us to do this. Kilo Code allows us to do this [and] to pick [the] model. We used [K3] for this. It was decently good, I have to say — not [Claude] 5 level. But decently good, I would say, Opus 4.7 level. Which is still pretty good. But as you say, [K3] is not one of the cheapest models. It is [a] Chinese model which is cheaper than Opus, but is not as cheap as it seems. Anyway, I will come back to you with all the reasoning behind it. I'm gonna have a chat with Miguel. We're going to move to Kilo Code. Let's learn the tool — I need to learn the tool myself. And let's see how it goes.

**Them:** Sure. Everybody is saying that CLI is better than VS Code extension.

**Me:** I don't use VS Code extension. [I] only use CLI.

**Them:** Okay, I started with VS Code extension. I was very disappointed. CLI [in the] promotional video, it's like, okay, that maybe.

**Me:** [Be] open-minded and let's try to work with this. One thing for sure is that in this AI craze, we don't have yearly contracts with these companies. We have monthly contracts so we can switch to the next tool whenever available because we know that in three months a new tool will be available. And maybe Claude is going to cut the costs. So it's going to be much better to move there. So, you know, you have seen what happened in the last six months or one year and [it's] just insane. Insane.

**Them:** Yes, I see both in the AI world and here in this company.

**Me:** I keep thinking about this. My wife works in [a] big company as well. This is the same situation, the same crazy situation.

**Them:** Oh, that's interesting. I still have friends in Revolut and they're saying that it's chill as always. Well, not chill. It's like stressful as always, but without any external reason, as always.

**Me:** If I'm not wrong, you mentioned that Revolut doesn't allow the use of AI or—

**Them:** [It] was not allowing it while I was working there. Later they made an exception, some kind of specific direct contract to get access to Claude. So Claude works on the corporate level without learning from the Revolut code base.

**Me:** Okay, so they're spending a lot of money.

**Them:** Separate. Yes, they are. They have infinite amount of money. It felt like always.

**Me:** [Point here is,] from what I see, the industry is all in a craze moment [at] the moment. And let's see how things are gonna move.

**Them:** In the frontier companies. It's like there are a lot of places out there that are just continuing [to ignore] the existence of AI [and] engineers refusing to adopt it at all, even, you know, for developing like in-house tools, like some trivial website or stuff like that.

**Me:** So they are dead pretty much.

**Them:** I would say so. Well, they're still making money from their achievements and accomplishments that they made before. So [it's] not like they're — they're still generating money. Maybe not as much as they could. But enough to keep the project and the company [a]float.

**Me:** For how long?

**Them:** We will see. I don't know. I am chatting with developers. I don't know [the] operational perspective.

**Me:** You should. You should, you should, you should. All right. Vlad, I think that's it for this week. Give me a couple of days to catch up with everything else because I'm sure September will bring some changes. Not in engineering, not in engineering. Things from [a] product perspective will change a bit. And so [it] we [will] see an effect [on us], but it is just to let you know. Once I have more information, I'll give you the rundown of things. And that's it. I guess I will see you tomorrow during the MartechKit SDK [and] Martech SDK standup.

**Them:** Okay.

**Me:** And have a chat with the Martech people regarding that specific initialization order for AppsFlyer.

**Them:** Yeah, I will prepare some kind of comprehensively small message.

**Me:** Yes.

**Them:** And do [it].

**Me:** Nice one. Vlad, thank you so much. Have a great day and have a great week. Bye bye.

**Them:** Bye.
