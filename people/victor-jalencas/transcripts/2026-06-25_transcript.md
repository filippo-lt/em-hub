# 1:1 Transcript — Victor / Filippo — 2026-06-25

**Participants:** Filippo Tosetto, Victor Jalencas
**Date:** 2026-06-25

> Note: auto-transcribed; some names/terms are garbled (e.g. "market kit" = Martech SDK, "iMod Android" = iMote Android, "matiano" = likely Mateo, "catala/katala" = David Catalá, "VHS luck"/"via chas love" = the iMote Android dev to loop in).

---

Me: Hello.
Them: Hello. Good morning. Sorry for being late.
Me: No worries at all.
Them: Okay. How are you? Did you enjoy the. The holiday?
Me: I wish. I mean it's summer so in a day like yesterday what you do is just go out and do activities and stuff. It's 37 38 degrees what do you want to do is just stay home. Nothing honestly. But yeah it was arresting day.
Them: Oh. Good. It's fair enough.
Me: It was good it was good what about you?
Them: Well, was it the same? It was also the birthday of my father-in-law. So we got to celebrate.
Me: Okay. Nice. I'm happy because tomorrow is already Friday and then it's weekend again so I kind of need a bit of holiday to be honest. It's almost one year that I'm working at Leadtech.
Them: Oh, is there now? Wow.
Me: Yeah it's 18th of August.
Them: And I've been doing it so far, or how is it going?
Me: Let's say that. It feels way longer because so many things has happened. And you know the idea of I've always worked for smaller companies so the idea for me of joining as a bigger company was to you know slow down the pace and take things slowly it's exactly the opposite.
Them: Yeah, because we're a small company in the end.
Me: Yeah.
Them: But we want to do a lot of things.
Me: Yes.
Them: We want to in China, we want to sell the company. We want to acquire smaller companies. It's. It's all going to be everywhere and do everything.
Me: And do it yesterday not tomorrow.
Them: Yeah. That's the important thing.
Me: It's fine it's fine I like it it's it's very. You never get bored let's put it like this. Interesting. Victor I have two topics for you the first one is obviously the big one which is the Martech SDK just to check up a bit on you and then I have a proposal as well so just checking up. How things are moving forward with the Android version.
Them: So I did an integration successfully with. Remote and I spent a lot of time verifying. Because at first I thought or sometimes at some point I thought the amplitude had stopped working, but it just reports late. And the connections appear later. So I was. I was like, oh, I don't. I don't understand. I have connections from yesterday, but not from today. And then later during the day period. And I was, oh, I was debugging for nothing. But it helped me. See possible improvements and things like this. Because I was trying to find. Problems and so on. And I think I tested it well enough. And I think it's really bad. I think also that it would benefit from, from more ice. On it, especially since Android is not my, my home tar.
Me: Do you so the guy working in iMot android is pretty skilled. Do you think involving him would help a bit.
Them: Yeah, yeah. Yeah. If you could review the, the code and the integration, that would be perfect.
Me: If you send me the PR I will create a three ways chat and I will involve this guy. Okay. Where is the have you sent.
Them: I'm more tundra repository.
Me: Me. There apps. I mode I mod Android yes.
Them: Right. I'm effectively.
Me: I don't see any PR.
Them: Oh, maybe. Maybe I just pushed the branch. Let me check.
Me: Integration there is a branch yes.
Them: Oh, I didn't create the p. I just pushed it. My bad. I thought I had, I had created it.
Me: Okay. Yeah whenever you will you you can create the PR I wolf this guy VHS luck. And I'll I'll introduce him to what we're doing and I'll ask him to do a review as we did with shoutun from that list. I think that will put us in a very good position. And most likely now that we also have android. Then we can do the presentation the famous presentation that we haven't done yet I was chatting with the other engineers managers and the reality of thing is that this is this presentation is more for product people because we know already what this is and what it will bring us. So I will try to involve the product people I have an alignment with Jorge and Fernando this afternoon so we'll mention this to them.
Them: Okay.
Me: Let me take a note. Okay. And then obviously there's the all. I always forget the name.
Them: The name of, of the.
Me: Technology technology of the programming language.
Them: Fifth flutter.
Me: Flutter sorry flutter my brain. Yeah it doesn't exist for me.
Them: Just some, some blue coat.
Me: Do you think we should involve maybe katala have a chat with him about this. Or we want to spin it up by yourself what do you want to do.
Them: If only to, to have a confirmation that this is the best approach to do it in art. And also because otherwise he, I don't want him to be left out. And then later when we need him, he will be with, ah, you should have asked me, guys.
Me: Because I end up brief conversation with him about exactly this topic last week in a bigger chat so it wasn't a one to one and we briefly touch this point. And he said that. In his applications it doesn't really need a market kit. But I explained the reason so it's not we trust this code base because it's internal but we also have external apps today in m a for instance but also the fact that. Future development will be hidden. And it doesn't need to to do it themselves. So probably involving him in a conversation can help. Let me set it up let me set it up. Okay. Last point and this is a proposal for you. I don't know the roadmap for the market kit at least the iOS version. But I would like to have. Vlad to start to get his hands dirty a bit in this topic. Two possibilities here first one will be to have him to integrate it in AI design for instance which is not yet integrated and now that we have the Android version probably having both iOS and other could be a good idea. Second and this is more to discuss between me and you is do you think having someone else helping to improve the SDK itself can help. Okay. Okay. Let me first talk to matiano see whatever he has in mind and then on top to Vlad and then we can probably start to. Give him a few tasks. So we can we can keep up these kind of things because I want him to start to be a bit more horizontal because today is focused only on one app and he's doing the advisory for another app. By having him involved in much bigger scope like the market kit can help a bit. I think. Nice we can align once can kickstart this but I think the first step would be to get him to integrate this tool in AI design. So yes a broader understanding of the tool itself.
Them: Makes sense.
Me: Nice. Anything else on your end for market kit.
Them: No, just the long list of, of. Improvements that Martech wants that are in the roadmap issue or wiki page. I just need to review and see the feasibility. And what brings more impact first. So I also, I probably need to add some clarifying questions. Because. I, I still, there's still a lot of things I don't know how attribution works. And, and how they want their data to be organized and so on.
Me: I'm thinking what's the best way to do this? Because if it were for Martech. There will be a full team working on this tool. But we need to also understand. What is actually needed here. Because they have. Very much marketing driven. The way they work which means let's try everything let's throw the spaghetti in the wall and see what sticks pretty much. Which is. The other way that we tend to work in engineering obviously. So we need to find. A bit of a balance here. Okay. So am I writing understanding that this roadmap that you're talking about is the issue 38 that you open time ago.
Them: I think so. Yeah, 38 already. Issues. Yeah, of course, because the, the numbers go with. With the pull request as well. Okay. Yeah, it is one. And all of the event that, that they added. A lot of all of this is. AI is locked. So they just explain what they want, and then someone does the actual English competition.
Me: Yeah. Yeah that's how I'm spending my days nowaday. To read AI slope coming from product and say nope. Okay okay okay. Try to understand what's the best way to move forward with this is. I'm sure that in all these requests from them. Some of them don't make sense or we can skip or market is not the right place.
Them: Yeah, I need to, I need to start. I just, I just did a scheme, but I need to start. Like, digging in. Now I will, I will finish creating the. The pull request. And then I have a certificate that needs the newing. I had. A lot bucket for this after this call, but then there's this call that Apple just.
Me: Oh.
Them: Came this morning. And I think I will, I will at least get this started. And after that, I will get to this.
Me: I don't have time. To do that today. Should I go to the apple one?
Them: It's, it's a, it's a summary of that, that this is. There should be nothing new except they just highlight on what they would like us to, to. Work on. Maybe.
Me: I'm probably not gonna. Count no I need to push forward a lot of other things okay Victor I'm gonna go through that tentative roadmap as well and trying to see if there is a bit of sense in it. But for me the important thing now. For you to complete the Android version. If you could move forward that PR that Andre and his team opened. The iOS 1. So that we can kickstart the integration in a lot of other apps so that for me is the priority and then all these roadmap will come somehow. I will also try to organize a meeting with catala regarding the flutter version just to see what he thinks is the best way forward. Okay. And there's so much work in this tool that. We really need a team or more eyes on this. Okay. Okay. I have a second topic for you. Which is. Chat ultra. Android. There was a chat the other day and you say oh let's align later.
Them: Okay. So the thing is. We recently activated the app check or whatever is called for Android Integrity. And since then, sara cannot test because she is not working with the bug wheels. She's working with release bills that just happened to. Well, actually, they don't want. They don't point to development because Tesla development environment. If there was, we could disable integer checks on development. But there's. Only.
Me: There is no development environment it's just one environment.
Them: Yes.
Me: They just work on production.
Them: Yes. We test on production. We develop on production. So the, the long-term solution is. Yeah, let's create the development environment and let's test there. Meanwhile, we could do the things we could build the releases. For the back instead of for production. I mean, for lease. So that she could have debug token, but that's anyway cumbersome because for everywhere we will need to add it to the list of, of hashes. The other thing, what we are doing now is taking the aib, the bundle that, that bill produces and re-uploading it to Play store for the, to the internal testing track.
Me: Now.
Them: So that you can install it on her, on her device. Long-term solution or, or midterm solution is to modify because I had to modify it so that instead of an apk, it will produce the, the bundle because there's two different ways of packing packages, of packing apps in Android. Long term or, or mid conservation would be to have that workflow upload directly to the internal testing track. While we don't have the development environment.
Me: Is this something that can be done through code magic.
Them: Yes. It needs to be done. It's just changing the, the publishing step and, and copying it from the release from the production one. But instead of the production track, the internal testing track, it's like. I copy that block and change one line. It's easy.
Me: I can do it I can do it so.
Them: Yeah. Let me, let me, let me show the. Let me share my screen and show it to you. So I cannot make this. So the. Under the distribution, this one, instead of uploading to firebase here in, in the publishing phase. We just copy the distribution one. Which is this. We will play. But instead of track production, we put track internal. And that's it.
Me: Got it? Should be pretty straightforward.
Them: Yeah. And since it will be downloaded from the App Store. Sorry, the Play Store, they will have the integrity checks. Passing.
Me: Internal okay so and this will. Automatically add the build to Google Play and distribute it for internal testing so no need to do. Everything else.
Them: Yeah.
Me: Okay.
Them: And she's already in the list of testers, so she should. Check the Play Store and it should appear.
Me: So because I don't know the future of this app so I don't want to spend too much time creating the split environment and do everything in a clean way I can do this in 10 minutes no problem okay.
Them: Yeah, I also could, but it's one of the things that I never get to it. Sorry.
Me: Victor I focus on our tech kick please don't worry. I'm handling m a the best that I can. And for me they are not a priority. So they can wait.
Them: Okay. You mentioned that you don't know the feature, but I thought chatbot was, was doing money.
Me: Chatbot is doing money I don't know the future meaning. Do we want to invest engineering time on it? Or do we want to pass it to the next team? That's what I'm trying to figure out because after conversation with matiano last week that launches slash m a will focus on only two apps. I need to understand better because there's miscommunication between departments here and I receive different signals from product so I need to understand and align with them because their narrative is completely the opposite of ours.
Them: Yeah. Some of these apps make money, but they realized that they don't make enough money as. To, to have a good return on investment. So the acquisition cost is, is higher than the lifetime value.
Me: If you put a team on it. That cost 30 40 50k a month. If it doesn't pay off what's the point on keep running these apps? But this is a bigger conversation and again I don't think there is an alignment yet between engineering and product in that sense and not at our level at a higher level so I need them to decide. But anyway. Okay this is very good for me. Chat ultra we discussed market we discussed. Set up a call with catalog. Check the roadmap format the kit involve Vlad. I think I don't have anything else.
Them: I don't have anything either.
Me: That case Victor. Have a great day.
Them: You too.
Me: And in the moment you create that PR involve me and I involve via chas love so we can have a discussion regarding the Android integration.
Them: Okay.
Me: Thank you so much have a good day. Bye bye.
