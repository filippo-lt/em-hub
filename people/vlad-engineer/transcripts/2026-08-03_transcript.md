# Vlad / Filippo — Weekly 1:1

**Date:** 2026-08-03, 11:00 CEST
**Participants:** Filippo Tosetto, Vladyslav Krut
**Source:** Granola (`9a99d847-6384-422f-b42f-381bf12378d9`)

> Auto-transcribed. Speaker labels mapped from Granola's `Me`/`Them`. Names and technical
> terms are frequently garbled by the transcription ("market kit" = MartechKit, "apps fire" =
> AppsFlyer, "revenue cut/kit" = RevenueCat, "cash" = cache, "print" = sprint, "damian advisor"
> = Damien, "Olexi/Lexi" = Oleksii). Read accordingly.

---

**Filippo:** Good morning.

**Vlad:** Good morning. How is it for you? Counting days.

**Filippo:** I'm counting days. Yes, I am. I have to be honest, I'm counting days. This week is very hard for me.

**Vlad:** Five days left. It's very close.

**Filippo:** Well, you too actually. Yeah, yeah, I'm a bit jealous. I was thinking this morning.

**Vlad:** For me it's four.

**Filippo:** Vlady's been smarter than me on this.

**Vlad:** Yeah I love starting from Friday and finish on vacation on Monday. I didn't do on Monday finish but that's what I usually do — it feels so good to have like easier week immediately after, just one day makes a difference. Monday is very annoying.

**Filippo:** I feel like, yes, it is. I agree. How was a weekend?

**Vlad:** I don't know, it just fly by. Nothing bad happens which is good. Nothing really good as well — my partner is a little bit sick so no outside activities or fun stuff happened. Very chill.

**Filippo:** Do you actually do outside activities with this weather?

**Vlad:** I mean when I mean outside I meant something not at home — there are inside activities but also the other part of the city, but we skipped all of them this weekend. Outside activities mean to walk a dog at about 9 a.m and then at about 1am.

**Filippo:** Okay. Yes.

**Vlad:** Deep into the night.

**Filippo:** Yes. Totally understand. I'm doing pretty much — I wish I was doing pretty much the same, but 1am I am sleeping since few hours already.

**Vlad:** I would love to be there but I cannot walk the dog and I don't want to sleep to be honest, this very early for me.

**Filippo:** But are you one of those early birds or late owls? Which one of the two are you?

**Vlad:** I am one of the owls. I am the person who goes to sleep pretty late and then wakes up pretty early. Well, it goes back to my childhood when the night was the only time when everybody was just leaving me alone and I could do whatever I want, so it feels this time to be like very self centered and safe and I'm really enjoying nighttime. But then I have to wake up in the morning.

**Filippo:** I understand. And for me, that's early in the morning. I wake up at 6am. Yeah, do gym. And for the first couple of hours of the morning, I am with myself. So you can do your own things and it's just quiet time. Yeah. For you, it's the night.

**Vlad:** I see. I like your approach more but I have tried, I cannot embrace it for myself, just doesn't work. I forced for the whole month to wake up at about 6:30. And it was probably the worst month of life I had — well not the worst but one of the strong candidates for sure.

**Filippo:** It comes with age.

**Vlad:** We will see.

**Filippo:** We will see. Yes, you are still 20.

**Vlad:** I believe you.

**Filippo:** You're still 29.

**Vlad:** Yes.

**Filippo:** Okay, there's plenty of time in front of you. There's plenty of time. Don't worry. Okay Vlady, last four days before your holiday. So you lead.

---

## RevenueCat API key for the backend engineer

**Vlad:** So let's start by something nice and simple. Remember last week I asked you for any type of access on AI Design for backend engineer to improve the Langfuse tracing — he needs to query status of the subscription of the user. The recommendation you provided was to just query RevenueCat directly, it's very easy, and I do agree. However I do not have access to generate an API key. Do you have one? I will resend you a link now, I have it open already so it will have to look for it.

**Filippo:** Can easily do that.

**Vlad:** Here you go. Obviously only read only, whatever may be needed we do.

**Filippo:** So let's do it together. New — this AI Design, new secret API key. Which name should we give it?

**Vlad:** It could be just backend.

**Filippo:** No, no, it's good. V2 obviously. We don't need charts. No, we don't need this actually.

**Vlad:** Maybe something else completely here, not charts — customer information I believe.

**Filippo:** Subscription. Read all the invoice. I doubt.

**Vlad:** I also doubt customer configuration, not sure what's included. Yeah very useful hint.

**Filippo:** It's pretty much the only thing we need, but let's keep it like this. And then project configuration. I doubt we need any of this.

**Vlad:** So no, no — just customers.

**Filippo:** Cool. Okay. Generate. And then would you be able to read the API key now?

**Vlad:** No, for me the list is empty.

**Filippo:** So you don't see this.

**Vlad:** I don't see none of that.

**Filippo:** Okay. So there you go.

**Vlad:** It will stay in the history, I don't have to copy it. Okay nice, thank you, your help here — that was very easy.

**Filippo:** No worries. Nice.

**Vlad:** So then I just start talking about MartechKit probably.

**Filippo:** I think so. Unless there is any other AI Design related thing.

**Vlad:** No, everything else I have cleared myself, all good and chill.

---

## Holiday coverage for AI Design

**Filippo:** Okay. So I have a question before we jump on the big topic, which is — we are both off for one week. So there's not going to be any... I mean, we are overlapping our holidays for one week. So we need to design a reporting line, meaning if someone has a problem in AI Design. Do you think there could be any issue here, or whatever is going to happen can be delayed? So what are the guys working on right now?

**Vlad:** They are doing pretty much UI stuff. At some point I completely lost and stopped trying to understand what exactly part of the home screen they were designing right now — the bother with animations, with how often they want to do these transitions, the home screen to promote users to like press something. It's like okay that's cool, that's not really what I would be involved. Let's say everything goes very really smooth there. Sometimes the CI is breaking, primarily for Android — last time I fixed it about two weeks ago, we did not have any more issues. So that's one of the things that sometimes Vladymer asks me to do is just to restart a build. Don't know why, majority of the issues fix there. It would be nice if we can assign somebody with access as a contact point to just restart the build on Codemagic. Other than that, yes.

**Filippo:** Okay. Interesting. Yeah, sounds good to me. I'm going to ask Andre to do it. He was working on this project before you, so I'm going to ask Andre to be the point of contact for this.

**Vlad:** Okay that's a good idea, and that's pretty much it I believe. Sometimes the requests are coming like "oh we don't have access, the Figma has broken". I hope nobody breaks Figma while we are away.

**Filippo:** Well, if someone breaks Figma, that's a product issue that they need to solve, not an engineering issue.

**Vlad:** Oh it was about—

**Filippo:** Yeah. So they need to talk to Miguel.

**Vlad:** Sometimes they ask me "can we do a copy from development to production" and like yes we can, give me a few hours — and then Miguel is like "I better do it myself manually" and I'm like nice, thank you, appreciate it.

**Filippo:** But that's exactly how we should do these things. So product wants power to do this. Right. They want write capabilities in production, but then they ask us to do the things. One or the other. If you want the access, we can give it to you, but then you need to do the work.

**Vlad:** I believe he has access.

**Filippo:** That's it. Yes, it does. Yes. Okay, so AI Design project is moving forward.

**Vlad:** Yeah.

**Filippo:** Good. I'm very impressed with the improvements that Dmitro has been doing so far. In terms of AI improvements, I think he's a good engineer in that sense. Not sure about the backend part of it. But hey, he's young, is learning, so I'm okay with that.

**Vlad:** Looks pretty content with his PRs.

**Filippo:** So that's great. That's great. I'm not really content with Kilo's peer reviews, but that's another story.

**Vlad:** I also not really. I haven't asked guys what they think because they are being reviewed all the times and they are applying fixes, addressing stuff. When Kilo reviews my PRs it's like three out of four comments is something that I will not look into because it's incorrect, like straight away incorrect. One out of four types helps.

**Filippo:** Yeah. I agree.

**Vlad:** So better to have.

---

## MartechKit — the analytics buffer PR and the identity problem

**Filippo:** Okay. Martech SDK.

**Vlad:** Yes. Here you are almost up to date with what was happening. You have reviewed the PR, or maybe Claude reviewed the PR. I have done a part with analytics buffer — it works, it works nice, it's stable, it's a part we can call done. There is a second part to this ticket though, that you described it in the ticket, and I have figured out that we may want to do something about it as well. Configure can technically fail and there is only one failure point, it's a very easy and small point — it's attempt to fetch over the network customer information to get original user ID.

**Filippo:** Yes.

**Vlad:** Now we are just using non-original one, the one generated, which is probably not what we want.

**Filippo:** Wrong. It's wrong.

**Vlad:** It's wrong because we will be sending all the events to wrong ID, and then next application launch we will fetch the better one, the original one. But how should we handle it? Like should we make configure failable and propagate an error and attempt to retry if the user is offline — is this what we want?

**Filippo:** I'm going to describe the behavior because I don't have in my head the code right now. I'm going to describe.

**Vlad:** Yes, I have the code.

**Filippo:** Let's go back to the basics. We have different blocks that are interacting with each other. You have Amplitude, RevenueCat, you have AppsFlyer. In the future we're going to have other blocks — soon Braze will come. So we need a way to be able to track and reconcile the user between all these blocks. What are all these blocks? They are mainly receiving data from our application, from each application. And we need a way to reconcile the user between all of these blocks. So you have a way to query Amplitude with this user and getting all the data for this user in Amplitude, but then using the same ID I can go to RevenueCat and find the information about this user in RevenueCat, and same in AppsFlyer. And this is good because they allow us to do two major things that are the core business of this company, in apps at least in general. Which is: from a product perspective, we know what the user does with our app — press button A, B, C and go through this flow. And then we know that they purchase something because we can find the same user in RevenueCat. But we can also track the journey of the user from the moment they tap an ad in Instagram, for instance, and we can track their journey throughout the purchase. Why is that? Because we know if an ad is successful. So if I have three ads, A and B, and the majority of the users pressing, seeing the ad A are purchasing, we know that this is a good ad while B is a shit ad. So we put more money in ad A. So this is the basic logic of our business, and what we decided to do is to build this library, Martech SDK, that shields all this logic from the developers. Because it's not complex — but considering the turnover of developers, external developers, and the number of apps, we don't want to burn them with this logic. We know this. That's why we're rebuilding this. Okay, so the question here is which of these IDs are we going to use to make sure that we can track users across the different building blocks. And the decision has been taken to use RevenueCat original user ID.

**Vlad:** That makes sense, yes.

**Filippo:** Why is that? Because RevenueCat works with aliases, but always has the original user ID in mind. Okay, you know how the original user ID works, which is every time a fresh install of an app is running, a new alias is created for a user. This alias becomes the original user ID in the moment a user makes a purchase.

**Vlad:** Or restores one, yes.

**Filippo:** The restore is because ID that was created once purchased.

**Vlad:** Makes sense, yes.

**Filippo:** And so this is for us the ID of the user, and that is the ID of the user that must be used everywhere. That's the logic. Does this help answering the questions that you had? Or is it just creating more confusion?

**Vlad:** It was nothing really new, it doesn't answer, it doesn't create the confusion. The concern here is there is a scenario — for example offline users, being offline, where original RevenueCat ID cannot be obtained. In that sense we do not want to use any kind of other identifier. We do not want to use a temporary one or an alias. What we want is to force a user to come back online and retry and then obtain the original one, and only after that we proceed with the setup of all the other building blocks. This is what we want.

**Filippo:** Correct. Correct. Yes.

**Vlad:** Therefore we have to surface this error, make pretty much configure method throw, and explain it in our documentation — that for the SDK to work, all the adopting applications will have to manage this, will have to retry, show some kind of alert "user is offline" or something, and then retry until the user gets back online, and only upon obtaining the original user ID we can proceed. It's a blocking — that's a big decision.

**Filippo:** Question to you. Can we cache? So instead of throwing an error and giving the responsibility to the developer to restart, can we somehow—

**Vlad:** Like—

**Filippo:** —think the following? I'm sure that all the building blocks have an internal cache that they will handle initialization even in offline state.

**Vlad:** Yes, yes. Well RevenueCat is a weird one because user will not be able to make a purchase without, obviously.

**Filippo:** But so my question to you is — and again, this is not the situation, it's more like conversation — can we hide this complexity from the developers? So that when configure is called, we have a flag saying offline; the app goes online, this flag is switched, and only in that moment we retrieve the original user ID and we set it into the full family of building blocks.

**Vlad:** I believe that we can. The app pretty much every single app will anyway throw some kind of error when they're trying a notification, Superwall, or to load whatever onboarding home screen they want. All of that will be on hold, the app will be retrying anyway, all the apps should have some kind of alert to retry. So we can just have some kind of, I don't know, polling. Every second or two.

**Filippo:** It's an edge case.

**Vlad:** It's very much edge case, and we should absolutely cache original user ID to some kind of user defaults, some local storage, upon at least one successful activation, because it will not change. I'm not sure if RevenueCat does cache of the customer information — I will settle the documentation, I don't know yet. If it does not then we just copy it locally, and it will be a major edge case. Like imagine you just downloaded the application successfully, you had internet, now you opened and you don't have it anymore. The problem here — let's say an edge case, and usually majority of the apps we do not even want to handle this one.

**Filippo:** No.

**Vlad:** But in an SDK that is effectively lying to all the adopting apps, that's a serious concern at least. We can just document that as an edge case. Configure method has already been made idempotent. That's the word, right?

**Filippo:** Correct, yes.

**Vlad:** You can call it multiple times with no issue whatsoever.

**Filippo:** The quickest path here is: recognize there is an issue or an edge case, and let developers handle it. You're suggesting that the configuration will not fail for all the SDKs because they do have a caching system internally. The only failing point here is the propagation of the user ID, because we cannot retrieve the original user ID in any way.

**Vlad:** There is a concern that if we initialize Amplitude, we set a specific user ID to the Amplitude and then we change it on the fly — the old events are already gone, so we should probably—

**Filippo:** No, no, that's — Amplitude has a very smart way of handling this, which is a post reconciliation. Let me explain. If you start to send events to Amplitude, and after two seconds when you receive the original user ID from RevenueCat you set in Amplitude "hey, this is the user ID", the previous events will be reconciled and so you don't lose the history. So it's not considered as two different users. Yeah, it's smart. Unless you set a different user ID before.

**Vlad:** Hence current behavior is very much broken. And the fix is pretty easy.

**Filippo:** Reason.

**Vlad:** What about AppsFlyer? Well, very different one, because difficult one. We have only one event there. And it cannot be triggered anyway before the configure is called and completed. However, once again, it's an SDK — it cannot be like "oh we don't care about this scenario". We should be caring about this scenario.

**Filippo:** Yes. Okay.

**Vlad:** And we don't know exactly what will happen with all the other building blocks when we add them. And we probably should not be worried too much until we decide to add them, because when we are adding them it will still be probably a decent chunk of work across the whole SDK, wiring all around. So we will have time and task and it will be clear what are we working on at that point. We will amend the solution then.

**Filippo:** For future building blocks it's just going to be additions. It's not that we're going to change how things are working today. So it's just going to be adding a new building block. The only question mark here — and thinking about already the next one which I already know which one is going to be, that I'm starting the conversation today, and actually that gave me a good point, I'll tell you in a second — for me the important thing is the order in which these are going to be initialized.

**Vlad:** The order of building blocks. Okay. Doesn't sound too difficult.

**Filippo:** That's the only debatable thing that needs to be decided before we integrate it in the Martech SDK.

**Vlad:** Still don't see any concern. The only variable part is the first step, which makes the rest very easy.

**Filippo:** Let's go up a bit on one abstraction layer, which is: considering this is an edge case, do you think it should be handled today, or we can defer it by first letting developers know about this edge case?

**Vlad:** I will say the solution with letting developers know, making it available, is a very simple solution. And pretty effective one. Like for none of the developers it will be difficult to just call configure one more time, and inside the configure we are taking care of "has it been configured before" — we can call it millions of times and it will not do any harm to us. It's a very simple fix, yes.

**Filippo:** Idempotency, the word you said before?

**Vlad:** It's not exactly that I believe, it's more about "can we make sure that this is the same process being restarted". This is a different tool for which I don't have a name. Doesn't matter.

---

## The Thursday release cut

**Filippo:** Yes. Good. What is the next step for closing this set of work?

**Vlad:** So today's progress is very obvious — making it failable, delivering the API. And then let me check what other tickets do we have in our board.

**Filippo:** I closed the previous sprint, I started a new one.

**Vlad:** I see, I am looking at the epic node of the board. Should I be looking at the board specifically? Okay let me check what's on the board itself. Here, okay.

**Filippo:** There's a lot of tickets, yes, but this sprint is one month long. And for me the important part is the MartechKit correctness epic.

**Vlad:** Then. So after that I believe what should be done. The question — do we have it as one of our goals to have a next version released before our vacations, or it doesn't really matter?

**Filippo:** For me it will be a huge advantage. That's why I would like your opinion on what can be delivered by Thursday evening. And then, looking at these tickets, what can be delayed?

**Vlad:** Okay I see. So the stuff that absolutely should be delivered is the update of the documentation — like probably a fundamental rework, just remove what's there now and add something useful. Then let's take a look at what we actually have. Parts that I do not really understand is ticket 91 about AppsFlyer that fails to start silently — what is this about? Oh, this is exactly about what we were talking about today, right? About RevenueCat that couldn't be started.

**Filippo:** Yes and no. Let me explain a bit more, and this is part of a problem that I had with the current implementation, but I think you're already fixing most of it. Which is: the way it was implemented before, all the failures are silent.

**Vlad:** Yes.

**Filippo:** This is a problem because as a developer I must know if something has been working or not, because I can take matters and fix them. As in "hey, the Martech SDK has failed to initialize AppsFlyer — oh shit, I need to do something in my code to prevent this specific case", or at least I would like to have a log for this failure. Because today everything fails silently.

**Vlad:** I feel like majority of the files already have logs since my Friday PR, I will have to double check. But what can fail in AppsFlyer? There's like no—

**Filippo:** If you don't fetch the original user ID it will fail. If you check the code of AppsFlyer, the initialization code, there is a guard saying "hey give me the user ID, if I don't get it I just fail".

**Vlad:** Let's see, I did not find this part just yet. Oh yeah, I see. But this is a funny one — this case is unreachable. It gets the app user ID from RevenueCat, however in case of failed fetch the Martech SDK stores exactly this into this value, an alias that is available even offline, that cannot fail. So despite it being marked as `throws`, it's not, it cannot happen. In the first step when we initialize RevenueCat we attempt to fetch, and if not we set a value that we — therefore AppsFlyer cannot fail. Well, now by the way, after diagnostics pull request, it already tracks that it has skipped and the localized reason, the whole report is in diagnostics and printed to the console. But it's also has never been possible.

**Filippo:** This code is misguiding whoever is reading the code. Because what it tells me is that in case this fails, nothing happens, no one knows.

**Vlad:** That's correct, and that's where I spent my morning today pretty much. Because yes, this is very much misleading, this specific part. Now we have an error, we did not have it before. But this part — you go there and you see the signature and it's like "yes sure it is throwing, it's clearly error prone", but then you go to how it's called, you see how configure works. In configure we just get an API key, we call absolutely safe method configure with the key, nice. Then we call populate cache. This function is the problem. It waits for the customer info, but if it's not available it's like "oh not a problem, we have another one", and it happens here in configure immediately. It's not something where we have a race condition or something.

**Filippo:** Yes.

**Vlad:** This value will never be nil, it cannot be nil, it cannot throw right now even though it is marked as one. And it is marked as one here again — it just cannot happen. Which, yeah, I was also curious why the hell we have an actor here. We are not talking about the technical implementation. Yeah, this is a problem. But AppsFlyer cannot fail, which is probably a good thing. However it can start with the wrong ID, which is a bad thing.

**Filippo:** What is that customer info, what is it returning?

**Vlad:** We use it only for original user ID. What else we have there I do not really know, let's take a look.

**Filippo:** So customer info is not the original user ID — we need to fetch the original user ID somehow.

**Vlad:** Original user ID is a part of customer info. So this is verification, and this is how we get our original app user ID.

**Filippo:** Okay, so that customer info will return the original user ID if present, or a nil.

**Vlad:** If we can get an info then it will have original user ID. The only issue is that it's being fetched from the remote so it may not return anything at all. Here is what we have — quite a lot of properties actually, first seen, request dates, there's a lot of stuff here, entitlements as well.

**Filippo:** So yeah, I know this data. My question is what is our code doing?

**Vlad:** If we cannot get an original app ID we just get an alias, asynchronous safe offline alias, which — I have traced it deeply into RevenueCat, apparently it can actually be nil and there is a thrown error, however I believe this is not supposed to happen. I did not find a way how we may not have either device cache or whatever magic is happening here. I think we would have a lot of crashes if that would be possible.

**Filippo:** That code — yes, my question still stands. What is our code doing? It's twice the same thing.

**Vlad:** At what point?

**Filippo:** So why do we have a do-catch here?

**Vlad:** In case the app is offline for example, this call will fail, we cannot fetch it, therefore we will just fall back to this one. Not report an error, nothing at all. Just ignore the problem and never retry it.

**Filippo:** And that app user ID is an alias provided by RevenueCat.

**Vlad:** Yes, it's a current ID of the current installation. So we will attach it to AppsFlyer, we will set it to the Amplitude, we will proceed as if it is an original one — however it's not.

**Filippo:** What is the problem with that? Is it better to fail? Because as you said, the only reason why this is going to fail is if we are offline. So is it better to fail saying "hey we are offline, no one has set any ID"?

**Vlad:** I cannot really state confidently that it can fail only in case of offline. This is just the most obvious case, you know. Maybe RevenueCat server is down — could it be true?

**Filippo:** But then we are still asking RevenueCat to give us a user ID.

**Vlad:** Possibly. But that's an identifier pretty much of the installation, of the device. It's local.

**Filippo:** Which is the alias that we are talking about.

**Vlad:** Yes.

**Filippo:** I don't know.

**Vlad:** What is also very misleading is that I believe we provide access to the apps to get this user ID. So it says internal but it's actually public through the chain of calls, so apps can use it.

**Filippo:** Yes.

**Vlad:** And if it was obtained incorrectly the apps will also rely on the incorrect ID further in their work. So in Superwall, in — I don't know — "email to contact us" screen, we will have a whole bunch of my—

**Filippo:** Okay. Let me ask you a question here. According to how you implemented this, I have a specific use case in mind, which is: as a user I download the app, do a purchase, so I get assigned an original ID — okay, let's call it One. I delete my app. I delete my app, I reinstall it, open RevenueCat, open the app, and I get assigned an alias which is Two. Then I do restore purchase, so the alias is associated with my original user ID which is going to be One. What is going to happen inside the MartechKit here?

**Vlad:** Okay. Yes. A good question. We have a listener somewhere that actually subscribes to RevenueCat — it's a public API, but we have a listener somewhere here, a stream to which we subscribe and which we use to basically get a stream of events. In case we get new, better, more fresh customer info we will override, we will set original ID updated. And we also export for some reason to apps from here.

**Filippo:** Okay, so — we need to expose it to apps, by the way. Reason being, give you a simple example: we need it for Parapet.

**Vlad:** I am not sure if we have any place in the documentation where we recommend using this, and we definitely do not use it in Face AI. However, okay, I got it — we should expose it and we should document it somehow.

**Filippo:** Yes.

**Vlad:** What should the app do, like what should we use?

**Filippo:** As a user of this SDK I'm expecting that the — I don't know what's called user ID, that's called a user ID, I don't know what's the real name here — is always the correct one. So that for instance if I'm using Parapet in my app and I need to fetch the quota of a user, I'm using that specific ID to retrieve the quota.

**Vlad:** Oh my god. We should absolutely 100% prohibit — let me show you what doing this. I believe in Face AI this line exists, which is fetch of the incorrect identifier and then using it for network calls, for quota pages and so on and so forth.

**Filippo:** And that's why Oleksii cannot test it.

**Vlad:** And that's why Oleksii cannot test it. Like, he has no idea what's happening there, and in the moment when we were looking for this type of errors I also did not have any reason what's happening there.

**Filippo:** Using this library you don't need to know about the ins and outs of how aliases are matching. If you have an API exposed that gives you a user ID, you're going to use it.

**Vlad:** Yes. However we allow users to access a user ID from this protocol. Which one? Not this one — this one.

**Filippo:** Isn't this—

**Vlad:** Why would they use a throwing async SDK from MartechKit if I as a developer of the app can just go and call — where was it — asynchronous not throwing API. Why would they go through long difficult chain?

**Filippo:** Why wouldn't— We need to prevent this?

**Vlad:** We cannot allow users to access purchases directly. It was very debatable before, I believe it should not be debatable anymore. Not import RevenueCat directly. It will be much bigger job though. It's definitely something we should do.

**Filippo:** But it will be — this is the single most important reason why this SDK exists, and this is the single most important point of failure in all the attribution chain that we have.

**Vlad:** Yeah absolutely.

**Filippo:** So for me it is very important that in the SDK things are done correctly. If we cannot do it correctly, because sometimes we cannot, we need to inform the developer that there is a problem so they need to take matters on their own and do things on their own. So if on this do-catch — and I'm just saying — we need to throw a big error saying "hey I cannot get the original user ID, do something yourself". The developer needs to know.

**Vlad:** I agree.

**Filippo:** Today there are too many silent failures here.

**Vlad:** Today there are much less silent failures than we had last week.

**Filippo:** So great, we're going to add one million libraries to this SDK, but if the single line of code is still wrong we keep failing.

**Vlad:** Yeah, yeah, we are doing this absolutely, that happens.

**Filippo:** Okay, throwback — so "AppsFlyer never fails" for me is a symptom of the fact that we are silently failing, the developer doesn't know what's happening. You are assuring me that this is no more the case because through your fixes this has been somehow surfaced.

**Vlad:** It cannot fail because the other API is designed pretty much incorrectly. From the AppsFlyer code it looks like it's failable — not the case.

**Filippo:** But imagine that you're integrating this library in Face AI and you say "oh I need to check exactly how this thing is happening" and you go through the code — what do you think?

**Vlad:** Why coded like this.

**Filippo:** But you know, it's like "oh but I don't have this information here, if it returns so it fails I don't have this information here, how can I prevent this?" Because for some reason my app does something specific with AppsFlyer that no other app does.

**Vlad:** By the way, interesting question — why the specific app does something so weird. But okay, let's probably different discussion.

**Filippo:** But that's the thing. And for me this is the single most important part here: we need to let developers know that something has been happening inside our library. Is it a single log that appears in their console, I don't care. Is it an assert failing, is it a throwing error, whatever we want. But as a developer I must know that Amplitude has succeeded, integrated and is configured, that the events are going, that AppsFlyer is correct, that the IDs are correct. Because maybe I as a developer don't need to know all the ins and outs of this library, but as a part of this business I need to know what's happening there, and I need to decide what to do with the failure itself.

**Vlad:** Yeah, that's very correct and very obvious and I believe it is mostly true already. However, like the majority of the cases we are talking about — the corner case that non-developers will encounter. So even if we have a print and assert failure, I don't know, something that will crash the build in debug only, developer will not see this. Developers are working with internet.

**Filippo:** We have a point in our code that tells everyone that is using this — is it a piece of documentation, is it something that "hey, in case your app goes offline you will receive this error"?

**Vlad:** Yeah, we should probably just refine this flow a little bit and document it properly, make sure it appears in log, make sure that we expose something like this that I added recently and I will do for AppsFlyer startup — is four different states, by the way, we have this one separate now — and prompt developers in case the offline is encountered, just call configure again. There's no issue with this because before it was crashing but now they are safe to do this.

**Filippo:** Imagine you are integrating RevenueCat in your application and you have that huge website full of documentation. It's up to you as a developer to go through the documentation because the documentation explains all the edge cases. Okay, so as a provider of the library we should be doing the same. You as a developer, you can completely skip reading documentation, but that's on you. We are giving you the tools to go through all the edge cases, it's up to you to take this information or not. "I'm failing to attribute the user" — well, there is documentation, we are throwing an error, if you're not catching the specific case, it's on you.

**Vlad:** Absolutely.

**Filippo:** Before it wasn't like that. Before there was just a return.

**Vlad:** Yes, now we have a warning, but we should just do better.

**Filippo:** Yes.

**Vlad:** Like this line is also fine to be honest — and not fine. Just look at this, so pretty.

**Filippo:** I believe this is one of the cases where relying too much on AI is not going to help our cause. We can ask help, but we should pay attention what's happening here. It's not a silly UI element that we can vibe code easily. It's something that needs specific logic and needs someone to think about all of this and the ergonomics of the library itself.

**Vlad:** That's why it took me the whole Friday to address the comments on the PR. Because like, look at this — this is not human written, let's say. No human would leave this comment.

**Filippo:** And the part that is scaring me the most here is that we have the knowledge and the skills to address all these issues in iOS, but none of us have the knowledge and skill set to address the same in Android.

**Vlad:** I don't really see it here. Let's say it's not language specific issues we are talking about here, it's about ignoring error handling practices, or maybe not reviewing generated code, or not thinking "what if" — like if we have a try, why do we have a try, what can fail. It's not platform specific. It will be more difficult in Android obviously, however I don't believe we need a specific skill set to address the same errors on Android, especially considering that we probably can still rely on AI in preparing some kind of checklist of issues that were fixed in this scope, and then go and check if these issues are present in the same shape or form inside the Android SDK. And you can work from this point, you know.

**Filippo:** Correct. You're right. Correct. Yep. Okay, so now that we had this long discussion about the ins and outs of this library — what do you think we should focus on by Thursday, so before you go on holiday, and try to do a release?

**Vlad:** Getting an API in configure that fails. I would say that should be pretty easy and pretty straightforward addition. And documentation. And removing the two fallbacks that I just showed — this one should not happen at all, here we should throw an error, and the other one is local cached one as well. And updating the documentation. Like rewriting the documentation, explaining the diagnostics layer we have API for right now, and asking developers to respect the failure state and implement some kind of retry approach. It will give us stable, non-crashing—

**Filippo:** Okay.

**Vlad:** —and in like 99% of cases working library, with still a lot of issues inside, with some missing attributions here and there as described in the epics that you created. But at least it will be usable. And from what I can reckon now, the other fixes inside this epic will not require us to add or change public API, which means that we will be able to deliver fixes, we have a minor bump, and it will cost for developers nothing new to adopt. And they will use these fixes for free.

**Filippo:** I'll let you work on this. Yeah okay, I like it, makes sense. I think there's enough time to do this, two important parts. Obviously anything else that can slip in, please feel free to put it in.

---

## Getting Damien involved

**Filippo:** There is a person that is quite interested in this specific initiative, which is Damien, advisor that works on Photo app, Video app, all those other apps, and is always asking for features or reviewing features. And he was the one that brought up the whole original user ID issue. Then it has been fixed, not greatly, etc. So I'm trying to think what is the best way to involve him. Let me explain what I have in mind: adding another set of eyes of someone that is hands-on, that is using this library — not a staff engineer, I'm talking someone that is in the trenches, that said "hey I need this user ID because of XYZ". I think it's important.

**Vlad:** If we have another pair of eyes or hands, let's get him, absolutely. It will help, we need feedback, we need more people with different apps telling us how they use Martech SDK and what they're lacking. Because yeah, I can apply it to Face AI and AI Design. But that's only two apps.

**Filippo:** Let me talk quickly with Damien and see what is the best way to involve him in the initiative. Maybe not doing architecture decisions here, but having feedback — as you said, it's probably the best use of his time.

**Vlad:** Yes, we may ask him to review PRs maybe.

**Filippo:** Yeah, yeah, yeah.

**Vlad:** Optionally, I'm flexible about this one. But the feedback — if he's already asking questions and requesting features, please let's collect these requests, let's collect this feedback, let's process all of that and figure out what should be added to our roadmap and what can we achieve differently.

**Filippo:** This was a very interesting conversation, thank you as always. I'll let you work, I don't want to keep you for more time. Let me do the manager job and try to get more eyes on this library, because we need someone to use it and to give us feedback.

**Vlad:** Yes I agree.

**Filippo:** V, thank you so much.

**Vlad:** And thank you, we'll talk to you tomorrow.

**Filippo:** And we'll talk to you tomorrow, have a great day. Bye bye.

**Vlad:** Later.
