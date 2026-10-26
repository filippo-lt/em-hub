# Transcript — David 1:1 (weekly) — 2026-09-08

**Source:** Granola | **Slot:** 15:00 CEST | **Duration:** ~50 min

---

Me: David, good afternoon.

David Matellano Criado: Hello, man, how are you? Checking the agenda super quick.

Me: Hi.

David Matellano Criado: Um,

Me: Good.

David Matellano Criado: The points. And yeah. Okay, how are you, man?

Me: Not bad, not bad. Busy, very busy, but good. Good. Good way.

David Matellano Criado: I'd love to hear that. Man, let's not talk on the end there. Let's jump in.

Me: Let's go, let's go.

David Matellano Criado: So I didn't change your order because I believe that yours are more important. Security analysis, iMode, and screen mirroring.

Me: So. So good news, Andrej closed already those 2 ones. So we can mark them as mitigated.

David Matellano Criado: Okay, so just screen mirroring.

Me: Yep.

David Matellano Criado: Mitigated when? Today?

Me: Yeah, today. I don't think we have iMode here, but it was— we added the same rules there, so it's done.

David Matellano Criado: The same. I'm not going to put it here because is this the relationship with security, but I will tell them. Just let me write here on the channel they have with Paul and Miguel. So here it was. This.

Me: It's not yet live, David. Sorry. I should have checked. It's not yet live. It's gonna go live today.

David Matellano Criado: Okay. Tell me and I will write them when you have it.

Me: Yeah, sorry about that. Yeah. Yeah, we'll tell you.

David Matellano Criado: Don't worry, it's okay, it's okay. Don't worry, man. Let me just put it mitigating. Let me come back to in progress over here.

Me: Yeah.

David Matellano Criado: Okay, just for sake of my head, but thank you very much for following this point. A design security incident in one.

Me: So. This check that you kickstarted, that actually security kickstarted, has opened a can of worms in AI design. And we just discovered there was a API endpoint that was exposing all the third-party services API keys.

David Matellano Criado: Fuck.

Me: Uh, yeah.

David Matellano Criado: We are lucky.

Me: Well, we are, I think we are, because with all these holes, we are very lucky.

David Matellano Criado: No one has stolen our keys. So how are you doing? What are you doing? So changing the case, changing the APIs, what are the plans?

Me: Um, So Vlad is on top of— Vlad identified this amongst other smaller things, but they are deactivating this endpoint today. Obviously, they are working on it right now. And then we are gonna rotate all the third-party keys. That's it.

David Matellano Criado: But wait, so is the sample used by the apps?

Me: It is not, it's called debug/environments.

David Matellano Criado: Can buy whatever he wants. Okay, so ticket for this, something that they can catch.

Me: Not yet. I close the thing because it's dangerous. Then we have the ticket going to be ready. Yeah, I know it's work in progress.

David Matellano Criado: Okay. Don't worry, don't worry. So the thing here is, so to close the endpoint.

Me: Yeah.

David Matellano Criado: Until the end of the day.

Me: Yes, that's the idea.

David Matellano Criado: Apologies, I'm ranting because this kind of things, again,

Me: No, I'm more upset than you.

David Matellano Criado: And thank you very much for catching it. Okay. I don't know if you have, if there is a chance that to say to the, I don't know if there is kind of easy pick, like put an LLM Whatever you want more, Fable, maybe Astra to say, please check all the holes.

Me: This is what I asked Vlad to do, to be honest. After you catch this, we need to check all the other apps, yes.

David Matellano Criado: Okay. Thank you very much. To rotate the keys until when?

Me: Yeah, I'm gonna start tomorrow because I need product because I don't have access to all the Android services.

David Matellano Criado: Do not worry. Until the 18th.

Me: Yeah, let's wait. I mean, I'm really hoping to close this in a couple of days, but yeah.

David Matellano Criado: Awesome. The thing is, we are not going to die. It has been exposed, so whatever, but at least to have a plan to do this at least September, okay?

Me: Yeah. Yeah.

David Matellano Criado: Thank you very much for the heads up.

Me: We need to enforce our security policies, David, in all the apps because this is bad.

David Matellano Criado: I'm out. I am at this point during these last 3 weeks that I am kind of paranoid.

Me: Yeah.

David Matellano Criado: Which is nice. We are catching these kind of things, but then I need to jump off and say, okay, we have been living like this. We were focused at the beginning of the change of brand budget. Please, if you have the chance of Doing enough. If you look for the way that you can automatize kind of putting this kind of thing, it's all right. Then this is something that the security team must catch. I don't know why they didn't catch these kind of things. Another way the security team catch new things as we already saw, okay?

Me: Yeah.

David Matellano Criado: So in terms of, I understand you in terms of paranoid things that right now what is happening and suddenly I become like, whoa, whoa, whoa, whoa, whoa, whoa, I am alive. Yes, we are alive. We are breathing. So we have the basic checks. Okay. Please, if you find a way that you can apply Fable in a 200 requests, 100 requests, I don't know, maybe you said Matellano is going to be 500 requests per app. Go for it because it's an analysis that We are going to do, okay? Just raise the hand, tell me, and I will say to the people. But if we can find these kind of things that we can elevate a little this kind of paranoid state, it's okay.

Me: Yeah. Sure.

David Matellano Criado: We got it. It's all right. What we have right now, the official story tells us that those are the things that are open, which are the ones that we have. I mentioned iMode, it wasn't here. So this is the official story. I need to follow one narrative, which is security catches this. We are listening to them. Of course, we are not silly. We catch more things. Please solve them. Okay. But we need to go again. We need to catch the bubble. And this is our bubble. This is our bubble where we are living. This is the bubble where we are catching. For sure, there are things that can punch our bubble, but this is the thing that we already know. So we are going to protect against them. So AI design has more priority than any one of these right now. Okay. So you need to decide, go first with AI design, but at least do not kill ourselves thinking that We are going to die. No, no, no, we are still alive. We are with you. Okay, nice, nice catch. Thank you very much.

Me: Yeah, okay. Okay. Good. Good.

David Matellano Criado: Eye mode.

Me: So, oh, David, this is like you had to put 5 people in a room to discuss about this to finally have an answer.

David Matellano Criado: I'm working on at least not to be 5, to be 3. But I'm working on that. It depends on the people that we are going to fire. I have informed that we can also, and I'm going to show you, We can hire, we can fire more people, but they're not going to fire these people until growth say, I'm going to fire my people so we can all have good conversation.

Me: Yeah, yeah. I finally have clarity on what is this iMOD web that everyone has been talking about since May. So 3 phases, just to give you clarity as well. Phase 1, landing page. No problem. We're going to deploy it by the end of the month. Phase 2, web to app. You pay on web, you redeem on app. We know it works. We can do it. The third one is what they want to build the big website with the TV guide, this and that. I told them Q— end of Q4.

David Matellano Criado: Can I— let me— so until the end of October or end?

Me: September landing.

David Matellano Criado: Web to app, end of October. October.

Me: I would say October, November, yeah. We depend on CRO, so full functional website more like January, I would say, because we depend on— probably we depend on Parapet on this, but

David Matellano Criado: November. Tell me 2 things that the website is going to do.

Me: Now it's just going to do one thing, the TV Guide. What?

David Matellano Criado: Why do we need to wait until January?

Me: Because of the payment.

David Matellano Criado: Right now we can do the payment of Paxar.

Me: We can, but it's going to be a pain afterwards because we need to reconcile RevenueCat users and Stripe users all in one.

David Matellano Criado: So for multi, this is important, the narrative. If we would like to have a cross-functional product between Android and iMode and the website, we need Paxar. But remember to all the guys that guys, guys, guys, iMode nowadays doesn't share between iOS and Android. So please put your heads aligned. Maybe this is worth it. If we are making money, are we going to make more money? And this is the key on this company, and I still don't know it. And each time that I speak with Diego, he sees very clearly. Diego said, And in average, people does not come back to our things. If the people does not come back to our things, what do we want to provide a multichannel approach? They can pay on the web and they can pay then off the app. Why are we doing this?

Me: Yeah.

David Matellano Criado: So what I am focused on Parapet is to provide the capability of providing this. But for me, the interesting question from producers, guys, guys, guys, okay, this is super fluffy. This is very good Star Wars TV. Yeah, let's, let's, I don't, I don't want to be right. They want to have money. So, so the point here is, guys, is this something that is a really block? Because maybe we can do this and the end of this year and we can subscribe users into the website and just provide this functionality, but is going to be enough or not?

Me: What came out of conversation yesterday is we don't even know if users are going through the web, and so step 1 and 2 are going to help us to prove that people are going to pay on web first.

David Matellano Criado: Okay. But at least we understand more.

Me: Yes.

David Matellano Criado: Now I'm going to show you here the people that I am thinking for each family, whatever, all the sandwiches finished, then we see if we have enough people to do this. How many?

Me: Uh, the team disconnected. They're gone. All good. Tickets, IT tickets done, SRE tickets done.

David Matellano Criado: Product noise.

Me: No complaints. No complaints, no noise, nothing. Sal, complete.

David Matellano Criado: No.

Me: Emptiness.

David Matellano Criado: No news, good news in this case if product is not complaining. Be quiet. Because right now, well, Chat Ultra, the only thing that we need is if we have one developer for Chat Ultra, please, let's try to put that better. That's it. Okay.

Me: Oh, he already spent 24 hours in the app, already found a lot of holes. So I'm glad already to pay this guy.

David Matellano Criado: Very nice. Full stack engineer, Harry, I know that you have a message from me. I believe that is the normal process. I need to answer. I have until the end of the time. I am going to be in meetings until the, until your 6th. I will answer later.

Me: Ah. David, I'm a bit concerned about this person running the HR reviews screening. So yesterday we had an interview and the guy was asking us questions. Guys, is everything all right in the company? HR told me you're going through a complex restructuring. And then why HR are telling these things to candidates?

David Matellano Criado: But does it mean that they said that? No, I think that HR shares with the people that we're in a buy-in or on a carve-out process.

Me: The guy came out to us asking regarding the restructure, the internal reorganization of the company.

David Matellano Criado: Please create a channel with Steph and to say, Steph, I'm both Alex and you, project directors, must involve in all this kind of shit. And they said this to us, what did you tell? Is everything all right?

Me: Yeah. Yeah, yeah.

David Matellano Criado: Because I believe that it's worth it to explain to the candidate in the middle steps that we're in a carve-out merit process. Are we winning a purchase? I believe that this is something that we just tell at the end because we tell the premium, the incentives. But at the beginning, please talk with the staff.

Me: Yeah, incentive. Yeah. Yeah, I found it, it's very weird, maybe because I'm used to Inma, which she is very on top of things.

David Matellano Criado: I know I did several process with staff and it may be better, but I can't ask for a change. Boy, if you want, we can ask for a change, but not now.

Me: Yeah. Okay. No, no, no, no. No, no, no, no, no, no, totally fine. Just wanted to let you know.

David Matellano Criado: Back, please.

Me: Alex.

David Matellano Criado: Create a channel with Alex and you in private, not in general, saying, Irma, did that happen? Was it you? Maybe it wasn't her.

Me: Yeah, yeah, yeah. Yeah, yeah. Sure.

David Matellano Criado: Because the calls, I don't know if she was doing all the calls.

Me: Okay. Okay, good to know. Regarding what she said today, she got, I think, confused that the process usually is the HR screening. We do the interview where we ask questions. Yeah.

David Matellano Criado: 2 interviews on our side, 2 interviews on their side, then Diego and myself.

Me: Yeah. She thought that the technical interview was the first and then we're going to move to Diego and then you are involved as well with the— it's very confusing.

David Matellano Criado: No, I saw it quickly. I've been jumping from meeting to meetings. I would like to ask that I will do it until the end of the day if it's not an issue.

Me: Okay, you do it. Okay, perfect, no worries.

David Matellano Criado: But this is a normal process. Call, then if you want to introduce what we said, a quick call to check you or Alex to say it's all right. But 2 interviews, one with questions, another more technical. These 2 questions are you, Alex, and tech people, and finally the one myself.

Me: Yeah. Okay, it's the normal process. Okay, it's fine.

David Matellano Criado: Victor.

Me: Have you had the chance to talk to Victor?

David Matellano Criado: Tomorrow I have the one-on-one tomorrow with him and I will going to tell him that Victor, the line management is going to change. You are going to be working on the apps because of the Andres exit. Right now we are have more visibility, at least until the end of the year. You're going to be like this, and the change of management is going to be between the 14th and the end of the month.

Me: Perfect. Perfect. I'm gonna hold my horses until you talk to him.

David Matellano Criado: So yes, supposedly the one-on-one has been done today, but I didn't have the chance this morning. I need to move it tomorrow. These weeks are several things in parallel running.

Me: I know, I know, I know.

David Matellano Criado: So let me jump to this.

Me: Yes, please.

David Matellano Criado: The sandwiches.

Me: Let's talk about sandwiches.

David Matellano Criado: I translate the sandwiches into product naming. So what is my proposal, Filippo? This is threats and security, nothing changed. Photo and video. To split photo and video between 2 families or subfamilies, photo and video edition, the thing that we have with Andre, and he's going to reduce one iOS and one QA. Photo and video AI generation. Your scope, tattoo AI design, face AI. We keep all the 57 blocks, blood on top, and Veronica. That means that we remove all the AI Why I'm removing the Anadea team? Because they can't speak with the Chinese. The only thing is, if we go with the Chinese, we have to keep all the Chinese. I can offer you one Chinese that is going to leave A Cleaner. I can put it. Over here it worked, but I believe that having Vlad, one, one, and Mackenzie is more than enough to handle all of this, but I don't know, what do you think?

Me: On paper, it makes sense. I need to understand what the product is expecting here.

David Matellano Criado: That is the point. No one knows. So we close it. I am going to generate, though, this is a proposal. So everything then it has this kind of look and feel that I have shown to the team. Diego, which is state— if you want, I can show you like this. So storage of security is the same. Here we have one external developer iOS list, but the same that you have seen on the spreadsheet is here. video, I suggest to split between edition, Andres scope, and here AI generation. I show here in the scope and I recommend, this is my point, I am booking one or two people of products that they need to share these resources.

Me: Yeah. Yeah. Yep.

David Matellano Criado: Here I'm doing the same, one or two people of product sharing these resources. So here is my way to say, book, no, no, no, we need to start sharing. So this is the recommendation that I'm having and this is the scope that they have. Then core tools, and here are extra.

Me: Sorry, go back. Could you go back one second?

David Matellano Criado: Sure, sure, sure, sure, sure, sure.

Me: No, no, no, the sandwich for photo video. Okay, Serena, because we're discussing with Andre and he wanted to poach Serena from photo and video, but we can discuss.

David Matellano Criado: Serena Script is an en bloc.

Me: She's one of the best QAs that we have in the whole company.

David Matellano Criado: No, no, no, it can't. It got— no, no, no, no, no, no, no. 57 blocks at a pack.

Me: Okay. Okay.

David Matellano Criado: There is no, there is no, so the thing here is there is no, in the same way that I can't introduce a new device. So if we are going like this and we are going to put this scope, these guys are And these guys are a huge machine. You need to put user stories through them and then recommendations. Guys, you're the same mobile. Guys, you're the same backend. These kind of things.

Me: They come. I think Andre wanted to use Serena in AI design, which is 57 blocks. AI cleaner, sorry, AI cleaner.

David Matellano Criado: Nope. He has Jesse. If he wants to change, he change Jesse. And guys, even if you speak and you would like to do changes, Filippo, I don't care in a good way. I trust you, both of you, Andrea and you. The thing here is I need to tell I told you that this is going to be the headcount associated to here. You see over here, the blood is going to be between these and more things. Okay. So again, if I am doing something crazy, I need that you raise your hand.

Me: Yeah, yeah. Let me show me the rest and I'll tell you.

David Matellano Criado: Sure. So another huge train change. I said I'm tired about how product organizes things. So I'm going to change the families. My proposal is core tools makes our life easier. Core tools, office, screenshot, scanner, and faxer, faxes, as it is. You see David, analytics. Then core tools, traveling. What you do on travel? Translator, go and QR now. So I fix everything regarding David Català in one place and I say, problem solved. I don't know if it is going to fit, but at least it's, guys, like this is easier. Okay. Nothing changed here in terms of headcount, I try to push with David Català to remove this guy until the end of this year, but at least I keep him here. Finally, lifestyle and entertainment. We have here Víctor Jalenas. We have here the Viadex Labs Oleski, and we have here iMod and Screen Mirroring, and I also have here Chat AI Ultra. But I am not going to put it here until someone tells me. But what I guess, if Chat AI Ultra fits in any place, it's here.

Me: It does.

David Matellano Criado: It does, but supposedly what I am following right now is what I agree with my colleagues. Which was? Just this. Scope. There is a way that I need to start introducing this inside of any place because if they ask you to, hey, we need to do this quick fix. For the quick fix, you also need people. So I can say also to come back here. And to say Chat AI Ultra iOS. Android. Zombie move. At least those are for you in zombie mode. And also here I can say Goja. Mirage. Zombie mode. Both of them. So if something urgent happens, you have these people that need to tackle and we are aware in terms of company that we are not stupid. We understand what all the things that we manage and we have like this in the same way that the Cancel it over here. I'm going to change that also over here. Screenshot iOS. Zombie. And then you have in Photo and Editor. Ngoja.

Me: Wrong.

David Matellano Criado: And meet Ash.

Me: Wrong photo and video.

David Matellano Criado: You're right. You're right, you're right. In data generation. Ngoja. I'm Yuvraj. I don't want this color. Okay, so this is the complete scope. This is the complete scope. And then you have here It's kind of different because I don't have a space. At least I would like to show it. Okay. So coming back, apologize to this place. So life and entertainment, you have this scope, you have these people.

Me: Mm-hmm. Mm-hmm.

David Matellano Criado: And then we think about it. I do know that test check is not here, okay? But right now I'm focused on apps. So in the other way around is story app security, as you have seen, photo and video editor. Here I recommend one person of product, at most 2. Here I recommend one person of product, at most 2, but I would push harder to put one, okay, because this application is smaller. Here I am going to force the change to office and traveling. So we simplify the things here. This guy, but I will leave it when he comes back. And then you have all of this here. And on top of this, you have price check.

Me: Yep.

David Matellano Criado: So I'm already cutting this.

Me: I am.

David Matellano Criado: But in case that something happened, we cannot— so here, one guy is going to leave of iOS. I don't have any kind of issue print here. They are iOS.

Me: So I have 3 points for you. The first one is we may need a second iOS there. Because there's so many iOS, even going on Mirage, if something happens, having a second one. But I'm not gonna ask for it today. First, I would like to see

David Matellano Criado: Okay, when, when we face the exit of this guy, October, November, we can put it there.

Me: I'm hoping to have more clarity from a product perspective in that sense.

David Matellano Criado: Okay, so let me take this note.

Me: Because if we have one PO, we can do it. If we have 2 POs, it's gonna be harder. So that is my first point. The second point, having Vlad on top of all of this— yeah, yeah.

David Matellano Criado: One sec, one sec, one sec, one sec. Put this— ah, sorry, because you are not seeing, I was writing this note here. And now I am going to write it over here.

Me: Yep. Yeah.

David Matellano Criado: The second, sorry.

Me: Second point, Vlad on top of all of that plus TraceCheck, it's not gonna be. Possible.

David Matellano Criado: Okay, I need to put Vlad anywhere in utilities.

Me: Okay, leave it there, then we're gonna find.

David Matellano Criado: The thing is, people is going to, if I don't put Vlad, they are going to, and where is this guy?

Me: Okay.

David Matellano Criado: And they are going to say, I'm going to say intrinsic. And they say, but intrinsic, we are going to fire not one, maybe two. So, but we will talk about this. So, so, so I would say now, but this is the picture of Q4. Vlad is on utilities for sure. Vlad will be helping on Tristek until we have this offboarding of Andrei plus the new hiring of people. Next year, Vlad will be surrounded with you in terms of utilities in the majority of your time.

Me: Third point, I'm not convinced about blood, but we'll see when things start to happen.

David Matellano Criado: But when do you prefer to put it? So do you have a better place to?

Me: No, I understand. I understand David. I understand. I— it depends again if we're getting one PO or two. If we get two POs, there's going to be plenty of work. If it's going to be just one PO, it's doable. I said PO, PM, whatever you want to call this product person.

David Matellano Criado: So you said that if we have 2 POs for here, you need blood on top of this.

Me: No, if we have 2 POs, there's going to be a lot of work for one person only. And he cannot also tackle trace check while we find someone.

David Matellano Criado: I need you to balance with blood, and I don't know that.

Me: Yeah. Yeah.

David Matellano Criado: I don't have a clear answer for you. Do you foresee which kind of headcount will you help on this situation?

Me: Most likely it's gonna be me helping where we can. That's it.

David Matellano Criado: The only thing, Victor needs to get this.

Me: Victor is perfect.

David Matellano Criado: If Victor fails getting this, but the thing is, if Victor gets this and Martech, worst case scenario, or you focus more on utilities or you focus more on trade Check and blood, or this in my head is something like this. Until when? Until the new developers came to trace check. Once that you have one strong developer there, you have your blood there.

Me: Victor is here. Yeah. Yeah.

David Matellano Criado: So all of these changes at most start happening, are going to start sooner in October. For me, these are the first changes on product. And then we start to send the notification in October to the external companies. So in November, we do the changes. This is not for starting Q3. No, no, no, no. This is the end.

Me: Okay. Okay. Okay.

David Matellano Criado: This is my proposal to Christian and to Diego, and in this proposal I am changing the structure of the families. And I'm reducing the people. And this is coming because I see a situation which Diego said, I believe that we can be smaller. I said, you believe? I believe this is the play. But I said to Diego, I am not going to put anyone else on the street unless I have the when and who of product is going to leave. Because if not, we are going to be in a worse situation. Less people of engineering, more people of product. more noise. As you said, you were in a meeting with 5 people in order to understand something. Now, no, you need to be in a meeting with 2 people or 3 at most.

Me: Yeah. Yeah. My third point, and probably you're gonna like this one, this Viacheslav alone on iMode Android and doesn't have any roadmap. So we need an Android. But. Having this guy full-time here is a waste. He can help with MarTech for sure.

David Matellano Criado: It's okay, it's okay. I need to put the guy over here. I need to put that. I don't want to cut more.

Me: See you. Okay.

David Matellano Criado: Filippo, I am cutting. One here. So I am cutting a lot with this exercise. Again, I don't believe that we are going to go with this exercise, but I believe that it's nice to say, guys, we can arrive to this point. This is a possible scenario in the future. We have— if you count the amount of people, it's 1 iOS dev here, 2 iOS devs, 3 people plus 4, 7, maybe you need one more over here. And also, we are not going to replace Andrei. So this guy is going to be here because if not, I don't have any place to put it on the map.

Me: Okay. Yeah, the only point that I want to think properly about is putting 2 iOS developers on the photo and video instead of just one.

David Matellano Criado: Do you want to do it right now?

Me: But that's Yeah, let's do it if he's gonna— yes, let's do it. Sounds good. Perfect. Okay.

David Matellano Criado: State this.

Me: Hmm.

David Matellano Criado: So here we have Shimon Shu. This is the guy from Android. I'm going to have

Me: 57Blocks is gonna be happy.

David Matellano Criado: They are going to have the same amount of people as they don't know that we are firing the others.

Me: Yeah.

David Matellano Criado: So they are So this is 2 external developer less, this guy. So we have one change. And the change is here. Okay.

Me: Yep.

David Matellano Criado: Again, this is a proposal until I don't see the changes of product. I'm not going to ask for anything. Maybe I will do the QA things that I believe that are worthy to do, but this is more a conversation with Alex because Nikita, we saw that this is something that we can do, but at most in September, I'm going to perform one change in terms of QA, nothing else. The rest of this, I really believe with this org, and for me, this is the first time that I'm not thinking removing, I'm thinking making conversation better. You put me the example. If you have one person, so Andrea here is working well, one person of contact for this, easy to catch. Manuel also can work without much, he's more than Andrea here. I believe that having 2 people for all of this, I don't know why, but I believe that we're going to have 2, but it's okay. But less people is better. Over here, those are the same apps. They're completely the same apps.

Me: For me. We need one person, one product person here, one product person.

David Matellano Criado: One product person with Vlad or you is fast. That is the point. This is faster. I am removing the team because I really believe that this is going to— I'm thinking in velocity. I'm thinking in firing people. The collateral is that I'm going to remove one AI design team, the AI design team, because everybody agrees like this is going to be faster than having them. And then over here, core tools, this is simply I don't think that our families are fitting our necessities, are fitting the people of product that we have. So we decide to push also here, putting people product. And over here, I believe that Manuel Terán will leave. I need to handle this with David Catalán in his return because yesterday he didn't have the chance to get it to work. In this scope. Over here, we simplify. I'm on the screen with Victor. I believe that is more than enough to do everything that we need. Victor also must participate on the website.

Me: It's gonna be faster. Yeah. Yep.

David Matellano Criado: It should be fun and nice for him.

Me: Yeah, I think so.

David Matellano Criado: You like it?

Me: I agree with you. I want to see the counterpart.

David Matellano Criado: The counterpart. Let's see. Let's see what happened. Just to reiterate what I said, Daria, for example, we are not— she was a B2B and we are not going to continue his contract. It doesn't have any kind of sense. So we are joining here things that are So he will be leaving the station, example, the train of the area. There is, I believe, also another PM that he's in a situation where there is no deal where he lives. So he will be another guy that is going to leave. So at least 2 are going to leave, and then on the, on the Weso side, there are 2 that must leave. So there are 4 people that are going to leave in terms of individuals. the contributors of product, Carlos, and the one that you don't like too also, Germán.

Me: Cheers. Yep. Yeah. Erardo, Erardo.

David Matellano Criado: Gerardo, so these 2 must leave on October. Daria plus the product manager are 4 people of product list. I believe that we need to also let go or move to another project 2 more.

Me: Yeah.

David Matellano Criado: Removing sticks, I believe that we are going to be in a better situation. So having this information on my side, I would say, okay, if it's going to happen on October, when it happens, Only when it happens, we start to move the tickets in order to reduce this amount of people. Then if you get in a point that you are not here, neither Andre, neither David, I am not worried regarding this because we are tackling the— web is becoming huge. So right now we have Apollo, that is also a project that is with Heitor, and Heitor has— so there are several projects there. So you're having— you're starting having TraceCheck. So my idea here is you cast TraceCheck because it's a product that Can grow a lot. I don't think that you're going to be only with this in the future, but this is something that is going to grow a lot. So maybe what is going to happen, maybe you're going to be more focused on this because this is big. We will put the applications in another way. I know you have seen the revenue, but the revenue is mainly AI chat, then the chats. Then PDF and TraceCheck, we believe that this can be something like not AI chat, but maybe like PDF. So if it starts to grow right now, what they have asked are 2 engineers instead of 1. PM, 1 BA, web design. So they have asked for several positions. another one to say, guys, are we sure? Because then, yeah.

Me: Yeah. Um, if I can give you some info, I'm not convinced to devs. Without a roadmap is a good idea. We have a roadmap for one dev.

David Matellano Criado: Right now. They would like to hire. On top of Alex, product manager, 2 full stacks, one that we are hiring, another one, product analyst and product designer. To obtain internal resources rather than outsourcing right now. So it has sense in a perspective of this project has a lot of potential. Okay. This is not an app. It's a web and you're going to start filling this with iMode. For example, before our meeting, it was in a meeting where we were with the people of GDPR and they were saying, but we have requests And no one is tackling them because once that we go into the web, we have emails and many more things. And on TraceCheck, we're going to have a lot of user information. So those are the things that we need to tackle. Also, I was in meeting with fraud on the website. And Stripe, we need to take care a lot of the fraud and the way that we organize the accounts. So there is a lot of work over there that are referring to apps, that everything is on top of the App Store. I don't see Alex and a product manager and a product analyst.

Me: To developers.

David Matellano Criado: I need to be convinced after, but you open this and until in 2 months only receive the people. This is another way approach that, and I like this approach when you're doing this kind of exercise in terms of budgeting. We are not thinking about the work to do, we are thinking regarding the budget. This project is going to be huge. So how many budget do we want to allocate to this project? Okay, let's budget in a way people usually came. So what you're budgeting right now, you need 3 months until they start working. So being on it in September, those people that we are going to hire are going to be capable of doing things on boards or whatever in January because on Christmas no one is going to work. So looking for January next year, maybe having this team for this, it's not crazy.

Me: February.

David Matellano Criado: Okay.

Me: I don't know. I'm, I'm, I'm, and I'm telling you something that I keep telling Alex. It's like, Alex, think what you want to build first. Think about the roadmap because he's a bit all over the place right now. Analyzing a small detail here and then he's talking and doing massive marketing research and then doing design and then with this, Alex, what do you want to build? You need 2 resources. Ah, because José Nogueira told me so.

David Matellano Criado: Here's a way of you put money on a thing in order to see it grow.

Me: Yeah.

David Matellano Criado: So we decide as a company to put money on. So in these ways, product manager to full stack, product analyst and product designer, 5 people plus Alex, we are willing to bet, I don't know, maybe half million per year in terms of human beings, which is a short amount in terms if you compare it with campaigns. Okay. So for me here is how, it's not a question about these people, it's a question about is Alex ready to support these people? Because what I've seen is he needs help in order to work inside of a company. Because of that, do not worry If you see that this scope or these people are going to be reduced, I'm counting on you in helping a lot of Alex over there, okay?

Me: The market. Yes. Just one clarification regarding the 2 developers. So are they both reporting to Alex or are one reporting to the lead and lead to Alex?

David Matellano Criado: My recommendation here is, or one of them is clearly an engineering lead since the beginning, or if not, both of them report to Alex. And then we decide if one of them can, we see. him, her as a team lead, we become the team lead, or if not, we will hire a third as a team lead. The thing is, they are going to report to Alex, but they report to you.

Me: Yeah. Okay.

David Matellano Criado: It's important. On Factorial, they are Alex line reports. If Alex wants to have one-on-ones with them, nice, but you're your line manager. We take seriously the deadlines. So you need to do one-on-one with them or biweekly or whatever you are doing with the same as you are doing with Vlad and you were already doing with Andrei. Okay. They are the same for you. Okay, so you decide the structure and you recommend for sure you need to align with Alex as well. We don't align too much with product in apps, but I do align with Christian. Okay, in this case, you're Playing more the role between Christian and I is like Alex and you. You decide about the people. Alex is super open to speak with you, or at least has been also open to us. So I don't think that Alex wants to have the direct reports. We need to show that, no, no, in Factorial we are like this because this cost structure. And then to show to Alex, Alex, man, if you would like to say that you are his manager and to be close, would you act this?

Me: Yeah, no, no, absolutely.

David Matellano Criado: With that, we work, please. I don't think that you need to also use this conversation. You are going to explain, Alex, they are with you, Factorial. It's all right. It's a structure. It's okay. I am going to organize the one-on-ones. I'm going to do a normal line report for sure. I'm going to align with you regarding the rest of the things.

Me: Okay. My question is more for looking for one more towards the lead. And okay for the second one to be more like a.

David Matellano Criado: We are looking for a team leader advisor.

Me: Good.

David Matellano Criado: If, if so. But it was also, remember what I told you, this is the first developer in the future. If something grows, he or she will be the team lead if he or she is prepared. So nothing changed here.

Me: Nice.

David Matellano Criado: Security.

Me: Thank you.

David Matellano Criado: Whitebook. So there is one thing that we need to do in terms of security for the ISO 27001, okay, and it's the whitebooks. have the first one created, which is the FAXER 1, and is this document. And the idea is that you copy and paste it for each project, or if you can put, for example, screen mirroring enabled on the same one. If you can put all of your applications under the same one, all of them, but if not, to try to accommodate as much as you can. Okay, so please copy and paste GPT, David Català mixture with GPT-4. with template, with the Terraform also. So my point over here, I need to ask you, Filippo, so example. I need 2 apps finished until the end of the month on your side. iMode.

Me: On the month. Month.

David Matellano Criado: Yeah.

Me: I mode, let's put AI design as yeah. Well, if— oh yeah, yeah, we can do iMode screen mirroring because it's similar.

David Matellano Criado: Can you say screen, mirror, screen? I modern screen mirroring. And?

Me: AI design, I will say.

David Matellano Criado: Can I say 17th end of the month?

Me: I can't promise that.

David Matellano Criado: That is correct. End of the month. End of the month.

Me: 7 things is next week.

David Matellano Criado: The idea is everything that we don't finish until the end of this month, it will carry on and I would like to finish everything on October, okay? Let me write right here that I ask you. Peter, Filippo. Then each semester I will ask you to review it, which means to read it and to say that something changed. There is a good point doing this. Okay, this is not only for doing this internally. For the sake of security, at least we're going to have an architectural document because here we have the general description. So something that we can share on the onboarding of the people.

Me: Yeah.

David Matellano Criado: I believe that it's at least useful for this because you can see that we have several things. Then your approach that you would like to provide on your project, but everything is useful. Also, if this is something that an LLM can read, you can also use it. For your lead, okay, it has more or less sense, not only for the documentation, okay. Final point of my side, feedback from Alex. No, no, sorry, security and trust check. Sorry. This is here.

Me: Yeah.

David Matellano Criado: Then one question, do you inform to security that trace check exists?

Me: Okay. I haven't talked to security.

David Matellano Criado: Please to inform that. To share the TraceCheck website with Miguel Vaquerizo, no, Miguel Ángel Olmo and David Vaquerizo. We chat with them, guys, hello, how are you? My name is Philip, you know who I am, so you.

Me: Yeah. No, no, don't know them.

David Matellano Criado: I can create the chat. It is tracecheck.com, isn't it?

Me: TrustCheck.com, yes.

David Matellano Criado: Yeah. What is the name of the vertical? Do you remember? Stay focused.

Me: InfoSearch.

David Matellano Criado: Okay, so inform, it was the point. They will run the same that they are running for apps checks over there. Finally, nice chat that I have with Alex, our Alex QA. I had a one-on-one with him and he told me one thing that I am sharing with you, with Català, with Andrei in one-on-one instead of the In the weeklies, which is Alex has started, the people, the QAs are starting to feel that sometimes they are like speaking with AIs and machines only.

Me: Yeah.

David Matellano Criado: So he put an example that try to avoid. He said, there are something that things are coming to the QA team that are not being tested, neither not testing in a strong way, but no one saw them. And he put me 2 examples. The good one, Jose David usually checks everything before sending it to Alicia on fax and a screenshot. And he sent me on the trace check, Andrei is sending a lot of things and no checks on his side. So please, if you can talk with Andrei, with platform developers, saying, guys, it's nice to share things with the AI, it's nice to work with the AI, but please do the checks, small checks, basic checks before sending to QA. If you don't see that this is required, okay, if you don't see that this is required, don't do it. But if you are seeing that this, please, in the one-on-one, that's something like, guys, this is not something a big topic, but please, if you have this, do not forget to do this kind of things.

Me: No, no, David, for me it's a big topic and already we had already discussed with Alex about this. I already started to talk about this with Andrei because, okay, using AI but not in this way.

David Matellano Criado: Okay.

Me: I need someone, a human being that checks. That doesn't, I mean, if you look at a couple of user stories, you totally see what Alex is meaning and is like code mixed with AI jargon. No, let's roll, let's slow down, please. This is not the way already on top of this. Yes, yes.

David Matellano Criado: Yeah. Perfect. So if you are on top of this, it's okay. Again, I'm saying this to all the engineering managers. Just do the kindly reminder where you would like to do it. Again, Alex didn't say it as a huge thing. He said that Like as a comment and that's it. Okay. Regarding

Me: But it is important, David, especially if we start to outsource too much. Because if no one checks, we cannot outsource everything to QA. Come on.

David Matellano Criado: You're completely right. No, no, this point you're right. Okay, so man, I don't have anything else on my side. Do you have anything else? I'm checking the agenda right now meanwhile.

Me: No, I don't have anything else. One thing that I'm going to ask you and probably remind you next week as well is All these beautiful M&A apps that are today in the store. Should we create a plan to kill them, to remove them from the store?

David Matellano Criado: PDF, everything that we have regarding Toothseeker music and step content are going to be removed from the store, but in October. So if you would like to create something on your side and be quiet regarding this so we can share it with anyone. Thank you. Yes, it will be nice to have it. But until October and the communication, we will do nothing.

Me: Okay. Okay, perfect. And second question, more general. Does Sergio Wezo know about the whole situation?

David Matellano Criado: Serhii was just, so he knows last week that he is going to be on top of everything. He's happy about that. Right now he's starting to figure it out. I said to Christian, Christian, please tell me that I know, but no one knows that you know. Also, neither Andre, neither David Català knows regarding Sergio Hueso, okay?

Me: I haven't talked to anyone about this. I'm just— if he's gonna tell me something, because we have one weekly with Wezo, if he's gonna tell me something, just how I should react. That's it.

David Matellano Criado: It's important. The change, you can say that you know that there might be something changes. You know that there are going to be some changes related with launches. Also, you can say, Sergio, I believe that you're going to be impacted, but I don't have more details. I already know that David is telling me that there are applications that are going to be to the bench. You can put it in a high-level approach. Also, we remove the people and we don't have replacements, but nothing else. Why do I want to keep this play at least in our side to avoid creating any kind of noise? I don't like, for example, what Jorge does with you, with you and with all of you.

Me: Yeah. Yes, please. Yeah, yeah.

David Matellano Criado: When I share information with you is I'm sharing information from the source that I have, which is something that I really talk. Maybe we fail in the decisions, but what I am explaining to you is what I have aligned with my colleagues, I'm just telling you just to keep information to be prepared. Not to share it with the others. So then I don't know which kind of information you have, okay? But at least please try to reduce the noise. So if, okay.

Me: And thank you for David Sanchez noise. That you talk to Diego. I don't know who you talk to.

David Matellano Criado: Ah, no, it's okay. So Christian also spoke with me regarding this. So he spoke with Diego and I didn't know that, but David Sanchez also has something with Ben on the VA lab. And David Sanchez right now is suffering his inheritance. So his past is knocking his door. So I tell this to Diego. Diego said, it doesn't have any kind of sense. David Sanchez might be on top of this. Yo, please do nothing. Do nothing because Filippo is on top of this. If you have this information and it reaches you because it's time to speak with other people, just talk to me and I will talk with more people. But in a meeting after, Emilio, Diego, Christian were in a meeting regarding another complaint regarding the Ben and David Sanchez. And also Diego said, and this is one more on top of David Sanchez. And Christian came to me because we had a one-on-one. One last Thursday, he said, Matellano, what was the issue with the recent? Nothing urgent. It happened with Filippo. I just provide visibility to Diego, but nothing else. I said, okay. I said, what

Me: Good.

David Matellano Criado: What happened, man? The past is knocking to the door of David Sanchez. I know the people is super sensible with him and I know that he wasn't the best in the past, but don't you feel that he has improved? Christian, he has improved a lot. Also, I'm doing this because we are enjoying working with him. We are doing this and that and that. I said, okay, thank you very much. I said, Christian, I didn't want to make noise with you, with Diego. I just explained to him this case in the case that he Create noise because he can speak with other people, nothing else. And he said, no, no, it's all right, it's all right, but please, all the people is super sensible with David Sanchez. And I say, I got you. He's the past knocking things. Oh, it seems So the cycle is complete. Christian is aware. Oshavi Sanchez came to talk with me saying, Matellano, no, no, but this is good, Filippo, because the noise came in the opposite way.

Me: Oh God.

David Matellano Criado: We didn't have noise coming to me saying, Matellano, the tech team is not doing well, working well. And I believe that I did properly. You talked with me, I talked with my line manager, and I said, please do nothing. The ones that did They did something again. What I said was my main manager because he was talking in another meeting, but it was different. Then when Christian told me, I am with him and I was super clear, and David Sanchez came to me, he told me, I have the feedback that Martin just gave you. I said, no, this is not the feedback that I need, but if you would like to talk with me, let's book 30 minutes and I'm going to speak with him next week. So, but at least it came in the opposite direction. All the people were aligned with What you thought and also what I think. Martic is on top of Martic, not us, okay?

Me: Yeah. Thank you.

David Matellano Criado: You're like a man.

Me: David.

David Matellano Criado: Perfect. So we will get to.

Me: Have a great afternoon. Bye.

David Matellano Criado: Bye.
