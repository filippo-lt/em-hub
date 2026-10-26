# Transcript — Victor 1:1 — 2026-09-18

> Source: Granola "Víctor / Filippo - Weekly 1to1", 18 Sep 2026 11:00 CET (id `2e59c0ac-7426-414b-b467-d88043203596`).
> Raw ASR, lightly formatted only (speaker labels normalised, blank lines removed). No wording changed.
> `Microphone` = Filippo · `System audio (Víctor Jalencas)` = Victor.

---

**Filippo:** Hello.
**Victor:** Hello?
**Filippo:** Again.
**Victor:** Lord.
**Victor:** Just as as I was hanging up the previous call came the guy for to to look at the the roof. We have a diagnostic We have a a we we know the fix. I know it's just a matter of getting a slot in his busy calendar.
**Filippo:** It feels like my life.
**Victor:** And I just now, I came from
**Filippo:** Good.
**Victor:** from talking with him.
**Filippo:** Good luck.
**Victor:** Yeah.
**Filippo:** Is it gonna be costly? Expensive?
**Victor:** I don't think it will be too costly. It's more a matter of yeah, It's it's well, we have, like, a a false or a fake what's the name?
**Filippo:** Yeah.
**Victor:** Like, half pipe or or sink, but it's not outside the roof. For some reason, it's it's on over the lip of the roof,
**Filippo:** Okay.
**Victor:** made with with fake tiles I mean, I have I have I I cannot sit. I I I but I have a another portion of of
**Filippo:** Yeah.
**Victor:** overextending cross section where I that I can look from inside the house. I I will make pictures someday to
**Filippo:** Okay.
**Victor:** to explain it because it's yeah.
**Filippo:** Okay.
**Victor:** Anyway, But the fix is, yeah, is extend the actual roof tiles the edge of the of the of the wall.
**Victor:** To the the street.
**Filippo:** Right.
**Filippo:** It's very technical, and I have no clue how to do this. It's manual work.
**Victor:** Yeah. I need And and for me, it would be super risky because, yeah, you're on top of of of the roof rooftop, and it's, like, two It's it's it's two two floors.
**Victor:** Eye.
**Victor:** So I could not even
**Filippo:** No.
**Victor:** concentrate And on the other side of the of the of the roof, which is not broken for now, There's, like, even two two more floors.
**Victor:** Because it's a a it's it's different levels on on each street.
**Victor:** So that will be I I would need to be tied up
**Filippo:** Please don't.
**Victor:** three different ways.
**Filippo:** Please don't.
**Victor:** I just I just just looking just imagine it, I get cold feet.
**Filippo:** Yeah. I can imagine. Come on.
**Filippo:** Victor, it was a bit of a crazy week for me.
**Victor:** Oh,
**Filippo:** And just to let you know what's happening is that pretty much, they are preparing for the sale of the company, as you know.
**Filippo:** And so there is a lot of initiatives that are horizontal to pretty much all the products of the apps, etcetera.
**Filippo:** And, it's, it's all related to security, ISO 2,000, whatever, compliancy.
**Filippo:** So there's a lot of things that on one end, it's actually great that they are coming up, On the other end is a so many things, so many so many bad decisions that have been made while building our product.
**Filippo:** That I have no clue where to start.
**Victor:** Yeah. And they went in yesterday.
**Filippo:** Honestly.
**Filippo:** Yeah.
**Filippo:** Yeah. That's the whole thing. That's the whole thing.
**Filippo:** Plus, my problem is as we are tackling problem small problem by small problem, I have these huge reports of things to fix.
**Filippo:** So should I unleash the old thing in the end of security so they are gonna get extremely worried, and we need to spend the next three months just to fix every findings? Or should they just focus or reveal that portion that they are asking for? Hard
**Victor:** It's hard because you could be accused of negligence or of hiding yeah.
**Filippo:** So I'm I'm trying to balance this to avoid creating panic.
**Filippo:** But to also flag what must be fixed as soon as possible.
**Filippo:** Anyway, that's it. That's so that's my my week summarized, and I guess this is gonna be the next few weeks as well.
**Victor:** Do do you know if they have a prospective buyer already? Or
**Filippo:** Because no. No. No. No. I know that
**Victor:** not yet? Okay.
**Filippo:** They want to get certified ISO whatever.
**Filippo:** But this is not because someone asked for it. It's because it will increase the value of the company.
**Filippo:** And, so what's happening is that, we are running this initiative alongside security. The we are providing them information. They will come back to us saying yes. Yes. No. No. Yes. Yes.
**Filippo:** And then we need, obviously, to act on that. And the far as I understand, by the end of this year, we're gonna run a sort of simulation So someone is gonna simulate the actual process to see if we have holes or not.
**Filippo:** Then we will need to fix them before the actual, I guess, agent will come in and start to perform this evaluation.
**Victor:** So
**Filippo:** To to give us this verification.
**Victor:** Penetration testing with a red team and so on.
**Filippo:** I have no idea.
**Filippo:** I I I don't think it's that. It's more about there's sort of yes. It's an audit. There's a huge checklist, and I doubt the the agent will go through each one item. It will pick and choose and try that.
**Filippo:** Because otherwise, it's gonna take months So that that is what's happening in my end.
**Victor:** Mhmm.
**Filippo:** And the the Goya Mirage work that you started to do is part of this somehow.
**Filippo:** Because two two reasons.
**Filippo:** On one end, there is all this part, but also, security started to use AI.
**Filippo:** To do their penetration testing and all the security testing, and AI is flagging quite a few things here and there.
**Filippo:** And one of the things that they flagged is the Firestore openness that we have in some of the apps.
**Victor:** Mhmm.
**Filippo:** Hence why you're working that.
**Filippo:** And before we jump on your, status update on that sense, the the the the point here is that we need to fix those breaches in Firestore.
**Filippo:** But we don't need to fix the whole app.
**Filippo:** And this is the balancing act Are we making sure the app is solid on the percent, or we just fixing the small part that has been flagged?
**Victor:** Goya is in a slightly better shape.
**Filippo:** Okay.
**Victor:** But we are lacking competitive environment to test with.
**Victor:** We we don't have a way to deploy the should we need to update cloud functions, which I don't know yet? But the cloud functions may need updating to adapt to the to the new
**Filippo:** Yeah.
**Victor:** lack of openness.
**Victor:** And There's no there's no currently working way of deploying them to to the dev environment. I don't think it it will be more more complicated, but apparently, we were deploying still to a brand by a cloud server or cloud
**Filippo:** But that's for dev. But that's for dev.
**Victor:** environment.
**Victor:** So we can we should fix production, but without the safety net of having rehearsed it before on on an environment which doesn't affect users. So if we close it a bit too much, if we need to update the app to work with the new Huddl environment.
**Victor:** Meanwhile, in the one the the current users will see that the app is not working.
**Victor:** That's the risk.
**Filippo:** Okay.
**Victor:** That we we cannot know in advance until we try.
**Filippo:** What what are we blocking? What is the the the possible so the data that we have there, which points I'm just gonna open Firestore now.
**Victor:** Yeah.
**Filippo:** Because
**Victor:** So Faster has essentially
**Filippo:** Because it's gonna be easier
**Victor:** grew up themes and styles and and what is shown as suggestions and and ideas.
**Victor:** In the carousel or whatever.
**Victor:** This is configuration, but it's configuration with images and with
**Filippo:** Yeah. All this get inspired parts
**Victor:** yeah.
**Filippo:** Etcetera. Okay.
**Victor:** Then there's the rate the app. I think this is I I don't think this is serving any useful purpose.
**Victor:** Because it's it's when you have this sweet point, you're the user, hey. Would you like the app? And if they point if they four or five stars, then they redirect them to the App Store.
**Victor:** So that that, they can emit the same rating again, but we don't know if they're fooling us.
**Victor:** If not, well, it just started here. But I don't know if any PO is actually looking
**Filippo:** Definitely not.
**Victor:** at the comments or this.
**Filippo:** No.
**Victor:** So we have a a few tables that are, like, the contact us that are not in not in use.
**Victor:** Things like this. But mostly, what you have here that affects the the experience of the users is all of this configuration about themes and suggestions and so on. And the API keys that the cloud functions use.
**Victor:** So it's not using directly by the app. It's using them directly because they go through the
**Filippo:** But
**Victor:** gateway.
**Filippo:** Are we sure that these are still used? Because I remember when we did the the brain buyer purge.
**Filippo:** We spent couple of days in our war room and we sort of remove all of this
**Victor:** The key is you in? Or what?
**Filippo:** The API keys But this is more this is a year ago. So
**Victor:** Well, the
**Filippo:** My
**Victor:** the mean, I I didn't do it directly. The agent did it for me.
**Victor:** He checked it to deploy it. He checked it to deploy it cloud functions.
**Victor:** The code.
**Victor:** Because it's essentially Node. Js.
**Victor:** And it was using those keys to to make the request to whatever services we use.
**Victor:** For for image generation.
**Victor:** Stability and I don't know what the names. But they are in use.
**Victor:** The app does not use them, but
**Filippo:** Got it.
**Victor:** the the back end uses the thing is that the app and the back end use the same database.
**Filippo:** Yeah.
**Victor:** I would have kept it isolated.
**Victor:** But not my design.
**Filippo:** Okay. So here's how I see this.
**Filippo:** All the get inspired or all the data that needs to be read by the app.
**Filippo:** We can somehow create a rule that this data is literally a rule here.
**Filippo:** That these data points can be read. So it is pretty straightforward to do.
**Victor:** Yeah. I I have I have the the rules written already.
**Victor:** I'm I'm applying them bit by bit, but
**Filippo:** Yep.
**Victor:** in Milash. But not here because
**Filippo:** Yeah. Yeah. No. Fair point.
**Victor:** didn't want to touch production
**Filippo:** Then what else? We have the rate app It's a right operation
**Victor:** Yeah. It's it's direct only.
**Filippo:** From the app.
**Filippo:** To
**Victor:** App doesn't ever read.
**Filippo:** And, also, do we actually care? But we need to enforce this through a rule, The
**Victor:** More importantly,
**Filippo:** Exactly.
**Victor:** we also have the quota system, the quota the tokens and so on.
**Victor:** And this needs to be hardened so that no one can just so right now, anyone can read the need of any other users. So they can impersonate them and start making requests and so on.
**Filippo:** I think And how do you are done this?
**Victor:** I don't I don't remember what was the action mechanism.
**Victor:** I think well, one of the solutions needed modification in the code.
**Victor:** Because in addition to writing the so right now, they are so right now, they are, filtered by revenue category.
**Victor:** So you will need to know the revenue category of any other user to get access to it. I think that's the gist of it.
**Victor:** But, there's no way if you guys hit, you could you could read it.
**Victor:** I think.
**Victor:** So they wanted to use the Firebase and Remus ID, as a key so that so that the rule can know can say, okay.
**Victor:** Only only the the rows that have your UUID are the ones that you can or write.
**Victor:** But for doing that, we need to modify the app.
**Victor:** So to also well, I think, to also modify to also write the UUID column.
**Filippo:** So these are the rules that I created for chat.
**Filippo:** And what they say is to check if a user but this is how the data is actually stored.
**Filippo:** So only the person that created a data point can read it.
**Victor:** Yeah. But we are lacking this this column or this
**Filippo:** And
**Victor:** property in the in Goya.
**Victor:** The the it's not written.
**Victor:** The the rest data you
**Filippo:** So it
**Victor:** The Dress data UID does not exist in in
**Filippo:** Yeah.
**Victor:** in the items.
**Filippo:** I know.
**Victor:** I don't know if if it can be written automatically by the back end without modifying the app.
**Filippo:** But
**Victor:** I'm
**Filippo:** How does the app identify which data point to to read?
**Victor:** By By by keying on the revenue tech ID.
**Filippo:** So is revenue cut ID the actual key?
**Victor:** I think so. Yeah.
**Victor:** I think
**Filippo:** So you cannot write a rule a faster rule, that match that.
**Victor:** I not sure about this point.
**Victor:** I checked this at the beginning of of the month. I I have forgot to
**Filippo:** No.
**Filippo:** No. It's a query, and you can't do it.
**Victor:** what what's the
**Filippo:** So what needs to happen in the app? Because this needs to happen in the app.
**Filippo:** I'm assuming, because the app reads directly the quota.
**Filippo:** From Firestore.
**Filippo:** Is that you need to
**Victor:** I think I need
**Filippo:** What do you need to do?
**Victor:** I think I need to include or or the thing is since the right operation is handled, I think, That's the part I'm not sure if it's handled by a cloud function.
**Victor:** Or directly by the app.
**Victor:** But I don't know if we can if we can modify the query or the schema.
**Victor:** Somehow so that the UID is automatically taken and and use it as a value.
**Victor:** I'm I'm afraid we need to modify the app to to also include it in the in the set of the Nope.
**Filippo:** Is this retroactive? But that but that's my point.
**Victor:** Yeah. That would be
**Filippo:** So today, the data is not secure.
**Filippo:** Because there is no way we can set some rules that makes this secure.
**Filippo:** The only way is to modify the schema and consequently modify the code of the app so that it complies with its new schema.
**Filippo:** But that leaves the fact that all the data that has already been written is not safe.
**Victor:** Correct.
**Victor:** We we don't know I mean, we know who it belongs to because we have the revenue category.
**Victor:** So long long term, we would need to to trust that whoever is asking for a specific UUID is the legitimate owner of of that of that revenue cut ID, I mean.
**Victor:** Before we can enforce it at at the fire risk level.
**Victor:** I'm a bit green on the details of how all of this work.
**Filippo:** It it's it's a bit fuzzy as well for me, but the more I think about it, the more I think I'm I'm to consider if it's worth your time.
**Filippo:** Because it's not let's write the rules in Firestore
**Victor:** Hello?
**Filippo:** Hello? Can you hear me? All good? All good? Victor?
**Victor:** Yeah. For for our end, you you disappeared. Yeah.
**Filippo:** My point here is it's not only enforcing the rules in here.
**Filippo:** It's also modifying that they code of the app.
**Filippo:** But these two action and obviously, to the API keys to to change how the back end risk.
**Filippo:** But what I'm understanding here is that not all of this will not solve the historical data problem.
**Filippo:** The historical data will stay as it is today.
**Victor:** Yeah.
**Victor:** Historical data, we just need to we just need to use the the quotas.
**Victor:** And I think that can be refreshed I mean, we could I think we could recreate it.
**Victor:** For new users.
**Victor:** Or new users.
**Victor:** Users with an updated app.
**Filippo:** Sounds to me a lot of work.
**Victor:** It is.
**Filippo:** Is it worth it?
**Victor:** I I don't know how much how to how to evaluate this because I I I don't know if the app one one thing is knowing how much it makes, but if we discount the amplitude licenses, the Google Cloud cost and so on, I know how much is actually benefit
**Filippo:** I'm thinking
**Victor:** to pay for each
**Filippo:** I'm thinking ahead here.
**Victor:** Yeah.
**Filippo:** So let's say that you're gonna take we're gonna remove everything else from your plate.
**Filippo:** You're gonna close in a room for the next week and you're gonna solve one up.
**Filippo:** So for two apps, it's gonna take two weeks.
**Filippo:** To solve the Firestore issue.
**Filippo:** But and going back to the the beginning of this conversation, there's a lot of other initiatives coming in from security.
**Filippo:** So tomorrow, there's gonna be another point that we need to fix.
**Filippo:** And then another one, and then another one, until we comply with ISO and everything else.
**Filippo:** So I'm wondering is it worth spending Victor's time in the zombie apps?
**Victor:** Okay.
**Victor:** Taking into that that we need to deal with other issues.
**Victor:** I would say, it it it starts making sense to to close the apps.
**Victor:** And it's one less thing on our plate, And we this allows us to focus on other things because the real fix for this will be start using para among other things.
**Victor:** The long term one. No? But I think we want to invest long term in these apps anymore.
**Filippo:** You know?
**Victor:** I And apps are doing essentially the same thing with different UIs.
**Victor:** And eventually, even because as I told you, Mirage is a is a maze of UI dead ends.
**Victor:** And also, long term, it would be better to to start using and in device models.
**Victor:** To do the easy or the
**Filippo:** Yeah. Yeah.
**Victor:** and, eventually, these apps will need also updating for iPhone two.
**Filippo:** But that's my point.
**Victor:** So it's it's a
**Filippo:** So
**Victor:** It's a it's a lot of work for little benefit, I think.
**Filippo:** Okay. And this is gonna open up another conversation that we are having with Matiano. And I don't know if you heard about the sandwich.
**Filippo:** No. Okay.
**Victor:** The sandwich The shit sandwich. No. What is that?
**Filippo:** No. No. No. No. No. No. No. No.
**Filippo:** So what's happening is that, we are reducing investment in apps.
**Filippo:** And we are focusing on a core set of apps.
**Filippo:** And we already defined this score, and Goya and Mirage are not part of this.
**Filippo:** Goya and Mirage are a sort of second tier apps.
**Filippo:** Which are called
**Victor:** Yeah. Yeah. That
**Filippo:** Are called zombie apps, meaning that they exist,
**Victor:** I I I knew what it is.
**Filippo:** They exist. No one will take care of them because there is no need for.
**Filippo:** But they are making a little amount of money, so there is no point of removing them.
**Filippo:** And then there's the dead ops.
**Filippo:** Starting to wonder if Goh and Mirage should move to the dead ops considering the amount of time that we we need to spend. And I'm not talking about improving them to make sure that they're working
**Victor:** Yeah.
**Filippo:** IPhone Duo.
**Filippo:** I'm talking about basic security here.
**Victor:** Just to make them work with the hardened back end.
**Victor:** It's work.
**Victor:** And it hardly justifies itself.
**Filippo:** Great.
**Victor:** So it may be better spending the time planning the closure because eventually it will arrive.
**Victor:** So that we can focus on on the core and the tier one apps.
**Victor:** I mean, this cannot remain a zombie because they need updating, and we will not pass the so audits with in in their current state.
**Victor:** So it's not just it's they're not zombie apps. They cannot remain as zombies.
**Victor:** They need to work.
**Victor:** If they're not making enough money to
**Filippo:** No.
**Victor:** justify the the the time, then
**Filippo:** I mean, I have a list of things to to to work on a lot of other apps.
**Filippo:** That are that have an active team working on them.
**Filippo:** And that will require time.
**Filippo:** If only half of these items will be somehow affecting Goya Mirage, You're gonna spend the next three months working on them.
**Victor:** So
**Filippo:** Which we don't want, obviously.
**Victor:** no. No. No. And if if we cannot I mean, if if we need to spend time on on on many apps, it needs to be tier one.
**Victor:** I
**Filippo:** Agree.
**Filippo:** Here's what I'm
**Victor:** And given My opinion. Even that we cannot justify working on them, Let's and we cannot leave them in the current state.
**Victor:** I I'd rather close them and inform you. I don't know how how you close an app and inform users that I mean, I I've received the emails, but usually, it was apps that I was not using actively, and I was not a subscriber anyway.
**Filippo:** How does it work
**Victor:** So I don't come
**Filippo:** It's pretty straightforward, meaning that you remove them from the store.
**Filippo:** And, they're running subscriptions will keep running until they expire.
**Filippo:** And that's it.
**Victor:** Okay.
**Victor:** What if someone has a yearly subscription Do we need to keep the back end working for a year? Or can we refund
**Filippo:** This is a big company decision.
**Victor:** those users?
**Filippo:** Okay. Let's select this.
**Filippo:** I'm going to talk to Matiano about this and I totally agree. The best way here is to close this.
**Filippo:** Right now.
**Filippo:** And to use the time to make sure that we are closing them in the proper way.
**Filippo:** Why do we decided that? Because today, we have two.
**Filippo:** We have a depth back end that is not being deployed by us, and it's not our servers somehow.
**Victor:** Mean, the the yeah. The dev the dev environment. Correct.
**Filippo:** Yeah.
**Filippo:** We need to modify the back end to comply to these rules
**Victor:** Mhmm.
**Victor:** Is the relatively easy part because
**Filippo:** Sure.
**Victor:** we own the deployment.
**Victor:** Mhmm.
**Filippo:** It's work.
**Filippo:** And even if to make sure that the full process is actually working fine, it will at least require one day.
**Filippo:** Let's be honest. Just to make sure that everything works, that we are okay, and everything So that's part. And then there's the Firestore enforcement and, actually, the app update first.
**Filippo:** So the app will write and read the schema in a correct way, and then the first two rules.
**Victor:** Yeah.
**Filippo:** Enforcements.
**Victor:** Yeah. Which is needed because Which is needed because the quota system relies on the openness.
**Victor:** And as soon as we close it down I mean, cannot close it down without modifying the app.
**Victor:** To send the right UID every time.
**Victor:** This means, yeah, making a new release and needing to keep the back end open I mean, in secure until most users have updated. Otherwise, breaking the the user. I mean, we could make a false update, whatever, but we need to to keep it running for them.
**Victor:** Still.
**Filippo:** And, obviously, this is for both apps.
**Victor:** Yes.
**Victor:** Yes.
**Filippo:** Great.
**Filippo:** Gonna talk to Matteo Anno and decide about the future.
**Filippo:** He may come back and say, no, guys.
**Filippo:** Work on this.
**Victor:** Okay. I I started up adding some products yesterday, but I wasn't yet in the quota part.
**Victor:** And I was only in the environment.
**Filippo:** Yeah. But, Victor, for me, Yeah. But, Victor, for me, the the the rules that we can add today are the safest one because it's just about, you know, the the the reading part of the data.
**Filippo:** And you can even the the app what's the name? The rating part. It's it's it's easy.
**Victor:** Go ahead,
**Filippo:** The hard part here is the the quota.
**Filippo:** There's no way around it. We need to modify the app.
**Filippo:** We need to touch the code of the app.
**Filippo:** Okay.
**Victor:** Yeah. My I the the last time I thought to, he wasn't even considering a week perhaps just one day.
**Filippo:** No.
**Victor:** So so even even less
**Filippo:** No. This is too much.
**Victor:** less justified to working
**Filippo:** No.
**Victor:** them.
**Filippo:** And you already spent a few days on this.
**Filippo:** So okay.
**Filippo:** Nice. Thank you, Victor, for this. It's
**Victor:** So
**Filippo:** It's important.
**Victor:** until you you unless you tell me otherwise, I stick with Martech.
**Victor:** On on the release.
**Filippo:** So
**Victor:** I was going to do that first and later
**Filippo:** Yes,
**Victor:** keep working on Mirage. But for now, I don't work anymore in Mirage.
**Filippo:** I will say let's park this for now until the
**Victor:** Okay.
**Filippo:** To Matiano, and I have yes or no.
**Filippo:** I'm gonna push for a no so to close the apps.
**Filippo:** Because I need to start you to start to get involved in IMOT, obviously.
**Filippo:** So considering the amount of, responsibilities that you have, in my head, I have the following split.
**Filippo:** Weekly,
**Victor:** Mhmm.
**Filippo:** And this obviously varies depending on on your workload.
**Filippo:** 10 to 15% of your time should be somehow invested in horizontal initiatives.
**Filippo:** Certificates expiring, anything that is horizontal and that is your staff engineer kind of role, requiring.
**Filippo:** The remaining 40 the remaining 80% split 4040% in, I mode.
**Victor:** Mhmm.
**Filippo:** And the Martech SDK.
**Filippo:** What do you think?
**Victor:** I'm fine with whatever proportion.
**Victor:** You know, whether the needs of of and and, Marty, they came in I I I more or less know the road map for Martech.
**Victor:** And what Martech wants to do afterward and all of the ideas they have.
**Victor:** I'm not too sure about IMO. I know that there's the web part, and I don't know if there's any security concerns for remote or it's use of Firestore.
**Victor:** No idea? I haven't checked.
**Victor:** And I know that there's this idea of wrapping the the common TV foundation library
**Filippo:** Okay.
**Victor:** and I don't I don't know any more details about. It's also
**Filippo:** Okay.
**Victor:** I don't know how to how to allocate time to it.
**Filippo:** Okay. Let me, it's one of my points.
**Filippo:** Because I wanted to start to talk about IMO to you.
**Filippo:** First of all, I set up conversation with Andre next next week.
**Filippo:** And he's gonna be the first I think gonna be a few of them because you need to to start to align with what he's doing.
**Filippo:** Let's go from the high level down to a bit more narrow and bit more in details. IMO is an app that is making between 1,500,000 to 2 millions per month.
**Victor:** What?
**Filippo:** I iOS.
**Victor:** No.
**Filippo:** You didn't know.
**Victor:** No way. But it's a really?
**Filippo:** Okay.
**Filippo:** We do like this.
**Filippo:** Let me do like this.
**Victor:** Yeah. I
**Victor:** I mean, I only heard about this numbers in the quarterly report, and I think it's we only made one this year.
**Victor:** And I don't even, like, I don't even wow.
**Filippo:** Yeah.
**Filippo:** This is the number for the last
**Victor:** It
**Filippo:** The MRR, monthly recurring revenue.
**Victor:** It's it's been a while since I logged into to revenue cut to check numbers. At first, I was curious, but then
**Filippo:** And
**Victor:** I just lost interest.
**Victor:** But I I I didn't know I I I was making that much at least during year, I doubt it was making that much. But I don't know.
**Victor:** I I knew about the easy and
**Filippo:** I
**Victor:** and so on, which are cash cows, but
**Filippo:** I mode
**Victor:** wow,
**Filippo:** Is the the in the first three months, I got the performance that we projected for 2027.
**Filippo:** In the first three months of this year.
**Filippo:** Said that,
**Victor:** So now the 4,000 I mean, the €4,000 that Goya or Meiji was doing, it's it's it's
**Filippo:** You see why I need you to start to get involved with the iMode?
**Victor:** Oh, yeah. Yeah. Yeah. Yeah.
**Victor:** If we can extract more more revenue from it, let's
**Filippo:** Okay.
**Victor:** yeah, let's do it.
**Filippo:** The good the the the the funny thing about IMOD is that as a product, we don't have to do anything else.
**Filippo:** It's complete product because from a product perspective, there is nothing else lad.
**Filippo:** It's a remote control, that connects your smart TV and we have a a list of models that we support.
**Filippo:** Okay? So this is it.
**Filippo:** From a a product perspective.
**Filippo:** What can be asked to be done is add a new model TV Amazon released a new stick for a different type of TV.
**Filippo:** We need to add that.
**Filippo:** And that requires some work. I'll I'll explain how to do these kind of things later.
**Victor:** Mhmm.
**Filippo:** But to go back to the road map for IMOTE, we just work on marketing related, features.
**Filippo:** So improving conversion, improving retention, and these kind of things. Or there is a new tool that like Braze these kind of things.
**Filippo:** So the reason why I pushed to get iMode to get the the market kit is because everything can be driven by the market kit, and the work in the IMO top itself.
**Filippo:** Is coming for free.
**Victor:** Mhmm.
**Filippo:** Terms of road map, what they want to do is to start to move and to try to get traction over other platforms.
**Filippo:** Meaning web.
**Filippo:** From an app perspective, terms of feature parity, iMultiOS and Android are pretty much the same today.
**Filippo:** So there is not much work to do there.
**Filippo:** But they want to start to add this website.
**Filippo:** Why? Because they want to try to bring in people from other media.
**Filippo:** Pretty much.
**Filippo:** So there are the the road map for the web is I I managed to to convince them to split it into three parts.
**Filippo:** The first one is new landing page.
**Filippo:** Simple landing page. Today's landing page is a template that is pretty terrible. So we are working with Andre on a new landing page, which is a proper website with all the links and the explanation, nice, fancy graphic, and everything else.
**Filippo:** This is step one.
**Filippo:** Step two that I managed to convince them to move forward with is gonna be a sort of web to app.
**Filippo:** Experience.
**Filippo:** Meaning that, a user gets driven to the website completes the quiz, you know, the the usual quiz that you have on the web.
**Filippo:** From your mobile. You pay on web and you get redirected in mobile, and you redeem your, subscription on the mobile.
**Filippo:** This would be phase two.
**Filippo:** This is something that you have to work on.
**Filippo:** And we can discuss on how to do this. Are we gonna use parapet? Are we not gonna use parapet? Are we using revenue cut? We can discuss about it.
**Filippo:** The third step I want to block, but I I'm I'm trying.
**Filippo:** Is that they want to build a sort of service to sell to the user on web.
**Filippo:** It's a freaking remote control. What do you want to sell?
**Victor:** A service to sell, but what service
**Filippo:** Correct.
**Victor:** Yeah. The the the electronic programming guide and so on.
**Filippo:** Correct. So they had the running around with this TV guide, pretty much. It's a TV guide.
**Filippo:** To be implemented first in the app and then this and then that. So we gave them a prototype still in May Never received feedback on it.
**Filippo:** So there is a branch of the app with this prototyping
**Victor:** Yeah.
**Filippo:** No through.
**Filippo:** Now they want to move this to web.
**Filippo:** To get an excuse to build the website.
**Filippo:** So my reasoning is, guys, let's do the web two apart.
**Filippo:** If we get traction, we move to the final stage, which is the TV guide. If not, why investing so much resources to build that thing
**Victor:** Yeah. Also,
**Filippo:** Being any users?
**Victor:** TV guides are not really every every station has its own format.
**Victor:** It's sort of each country, well, has its own stations, and then so you have to detect where the user is or what he's trying to see.
**Victor:** And then sometimes you have to work around geofencing, but that's that's a side of the thing. But, also, yeah, you need a lot of maintenance because this one must change from one day to the other or they add channels or it's it's a pain in the other. It's too too working too much work and too little
**Filippo:** Reward.
**Victor:** Yeah.
**Filippo:** But that's my point. So this is the road map for iMode.
**Filippo:** It's very high level.
**Filippo:** But that's pretty much it. So there is no constant work as in other apps.
**Filippo:** The the majority of the work that we have in India app is coming from and martech.
**Filippo:** And there are other ways to make money.
**Filippo:** But that's it.
**Victor:** Martina mentioned expanding the functionality to also cover smart houses, the motives, and so on.
**Victor:** It's a bit different region.
**Filippo:** No one ever mentioned this.
**Victor:** I I
**Filippo:** No one ever mentioned this.
**Victor:** okay. And then how much we make with the ads? You know?
**Filippo:** No.
**Victor:** You know, there's a banner on at the bottom
**Filippo:** Not much.
**Filippo:** Not much.
**Filippo:** But it's a revenue stream.
**Victor:** Okay.
**Victor:** Why why, Caleb? No. I well, it it would improve the the user experience with hookers.
**Victor:** And can we do something to to work better with certain TV models? I tried it with mine, which is a new model.
**Victor:** With a lot of functionalities.
**Victor:** And I noticed that I can invoke the apps on the smart TV from the from the phone.
**Filippo:** Yep.
**Victor:** But it only comes with the standard apps, Netflix, Prime, so on, and some apps that I don't use or they're not available in in my country. And then the apps that I have on the TV like a regional TV station and so on, to to watch content on demand.
**Victor:** It's it's not available.
**Victor:** Because the app doesn't know about it. So we somehow I don't know if the TV is supported, but make a process of discovery, or try to incorporate more apps
**Filippo:** So
**Victor:** to the roster?
**Filippo:** And this is where
**Victor:** Or launch
**Filippo:** This is where we we need to start to talk to Andre.
**Filippo:** Let me explain here what happened. Andre built this, so before Andre started to work on the project, we were using third party libraries to connect to all the TVs.
**Filippo:** With all the problems related to this because most of the libraries were not
**Victor:** No. No. I I I I was
**Filippo:** Updated. They were five, six years
**Victor:** looking into that at some point. Yes.
**Filippo:** So, Andre, what he did was to build what he calls TB Foundation Kit, which is pretty much a library, internal library that actually supplies all the functionalities of those third party libraries.
**Filippo:** Were adding.
**Filippo:** Where are we at? We are in a good position but it's a rolling test.
**Filippo:** Meaning that there are a lot of things that needs to be constantly checking.
**Filippo:** And this is not live yet.
**Filippo:** So I asked Andre to make sure this goes live before he leaves.
**Filippo:** But, again, next week, we're gonna sit down, and this is gonna start to explain a bit more into details these kind of things.
**Filippo:** Did we want to build this? Because this library will be used also in screen mirroring.
**Filippo:** And screen mirroring is one of the app that we're gonna keep alive.
**Filippo:** Again, I'm not foreseeing any road map there similar to iMode.
**Filippo:** Very little improvements.
**Filippo:** But once we have the Martech kit working, the TB Foundation kit working is a matter of maintaining the libraries and the should get everything for free.
**Filippo:** So that's the work for the market kit.
**Filippo:** For the iMode. Sorry. No Martech.
**Victor:** Okay.
**Victor:** So we want to keep this foundation kit in the same manner that we do market kit package that you reference.
**Filippo:** Yes.
**Victor:** Yeah.
**Victor:** And then it gets the functionality and so on.
**Filippo:** Yes.
**Filippo:** Yes.
**Victor:** Even if even if only two apps use it, but we have a working model for how to later package functionality that is more common across apps such as Firebase,
**Filippo:** Yep.
**Victor:** eventually, Parapets or logins or whatever.
**Filippo:** Yep.
**Filippo:** That's the idea. Yeah.
**Filippo:** I want you to sit down with Andre and ask him 1,000,000 questions because Andre is not really great at conveying information and doing handovers, so we may need to start now get some information. You do some research. You
**Victor:** Okay.
**Filippo:** Discover that you're missing some other information, and and keep in a loop.
**Filippo:** For instance, I know that he has quite a few automation built.
**Filippo:** Automatic Jira ticketing coming from Crushlytics crashes and fixes and everything else. So this is something that needs to be discovered.
**Victor:** Alright.
**Filippo:** And that's iMode.
**Filippo:** Last one is the Martech SDK and what's happening there.
**Filippo:** You already explained that today you want to you're gonna release the four point o with with race.
**Filippo:** Which is great.
**Filippo:** I'm gonna push to get the Martech pack in a good position by next week.
**Filippo:** What is preventing us to release at 1.0?
**Victor:** Don't know what, functionality we are lacking compared to iOS.
**Victor:** Because I I know that there were some gaps that Slava was closing, And then, ideally, we would like to not only keep feature parity, but architected parity for the sake of Platter. So I had I had this prompt that made the analysis back in the day. We could run it at any
**Filippo:** For the sake of flutter. Okay.
**Filippo:** No. I'm I'm listening. I'm just searching for a file.
**Victor:** Okay.
**Filippo:** Gone. Gone.
**Victor:** Okay. So
**Victor:** prevent this prompt and and and update the analysis to detect
**Victor:** things that are not quite the same or things that we have
**Victor:** other things and and
**Victor:** for example, brace.
**Victor:** And that is why we'll need to catch up on.
**Victor:** And vice versa,
**Victor:** if there's something that he added that we
**Filippo:** You're lacking
**Victor:** missed, we also want to to know about it.
**Victor:** Either to remove it it's not unusual or add it to us to our to our admin.
**Victor:** Because it's generally useful and and we want to The idea is to
**Victor:** keep the
**Victor:** Flutter code as simple as possible and avoid if iOS do this and if Android do that.
**Victor:** If we have the same methods and the same objects named the same in any in all places, the the floater code, they will be much, much simpler.
**Filippo:** I'm I'm looking at this.
**Filippo:** So we are still in this specific state. I mean, beside the version we changed, AI design Vlad finally started.
**Filippo:** Chat Ultra is gonna be the only big flatter one that we need to somehow get the Martech kit on.
**Filippo:** Because this is a zombie app.
**Filippo:** If we have the Martech SDK on, we can update it and shouldn't be a big problem.
**[unattributed]:** Fine.
**Filippo:** But what about these other apps?
**Victor:** These are the apps we need to remove their current apps flyer amplitude well, amplitude partly.
**Victor:** Well, yeah, they haven't they haven't tracking don't know if they use TikTok at all.
**Victor:** Whatever they use, they they will need to remove it.
**Victor:** On behalf of the new implementations in in MarketKit.
**Victor:** Or Market, yeah, in Flutter in the Flutter Market.
**Victor:** And It may happen as with some apps that we have seen that they're not market guidelines compliant.
**Victor:** And maybe they're doing something extra that Martech SDK does not do yet, but they want to to they need it.
**Filippo:** Yeah.
**Victor:** For pure reasons or because they think it's useful, then we will need to provide that functionality either in the SDK or custom in the app, one custom.
**Filippo:** Yeah.
**Victor:** Keep it somehow, but the the custom code in the app needs to rely on Multic SDK instead of calling the SDKs directly.
**Victor:** And for example, Braze and so on, I don't I don't know if they're using it. I don't think so because I've only found two two keys for for
**Filippo:** No. The idea
**Victor:** raising in the
**Filippo:** The idea is to deploy this to all the apps.
**Filippo:** Braze.
**Filippo:** So having it in the market kit is gonna solve this problem.
**Filippo:** But, again, we need the Flutter to be version of this library to be ready. Okay.
**Filippo:** Well, the good news is that this is that and most likely, these are gonna be dead as well.
**Victor:** How
**Victor:** how feasible is it to have some flutter
**Victor:** developer consulting
**[unattributed]:** Us say, couple of hours a week to to check
**Victor:** if what way because neither Vlad or me have experience with Flutter.
**Victor:** To see what we're
**Victor:** doing makes sense or not.
**Victor:** Or if we
**Filippo:** Well, the good news is that we have
**Victor:** could improve it somehow.
**Filippo:** Internal Flutter developers.
**Filippo:** That's great.
**Filippo:** Can use them.
**Filippo:** So I'm gonna ask David Catala if you could point a name that we could ask for advices.
**Filippo:** Yeah. Something like that. Yeah.
**Victor:** Or even
**Victor:** call it. You know? Something that because I will be going blind And then later, if if we realize that we need to do something differently too late,
**Filippo:** Yeah.
**Filippo:** Yeah.
**Victor:** it's going to be more more more effort.
**Filippo:** So Victor if you were to put down a timeline on this, Release Martech Kit four point o.
**Filippo:** Today.
**Filippo:** Release Marteck pack one point o next week.
**Filippo:** Making sure there is feature parity, obviously, And then you're gonna start to work on the Martech flutter wrapper.
**Filippo:** Let's call it.
**Filippo:** In your head, how long would it take to get this?
**Victor:** I think
**Filippo:** Ready?
**Victor:** Think since most of it is automatic because we're not writing the code We just wrapping it or calling it.
**Victor:** Think the troublesome part will be the unit.
**Victor:** Because Flutter has so many conventions that are different at least from iOS. So I need to to learn about them.
**Victor:** The rest is for example, I don't I don't foresee the actual event tracking.
**Victor:** To be much much complicated because you're just calling an event.
**Filippo:** Yeah.
**Victor:** But unique part is is going to be the where where the hard part is?
**Filippo:** Yeah.
**Victor:** To adapt what we have now so that it's callable from from Flutter at the right
**Filippo:** Yeah.
**Victor:** moments.
**Victor:** So once we solve this problem, the rest is is downhill, I think.
**Victor:** Packaging and and this will be done by the AI. So I don't don't care too much.
**Victor:** And then testing it in chat ultra.
**Victor:** Yeah. I think removing the calls would be yeah. As I said, the
**Filippo:** Yeah.
**Victor:** the technical part is the they need to start up.
**Victor:** So I would say maybe three, four days to figure this out.
**Victor:** And let's say a couple of days for the packaging itself.
**Victor:** Because I said it's it's just wrapping existing code.
**Victor:** Just need to translate and
**Filippo:** I'm
**Victor:** it at the right Instead of calling the SDK, we call our
**Filippo:** I'm gonna aim to get this
**Victor:** thing.
**Filippo:** Done by mid October.
**Filippo:** Think yeah.
**Filippo:** Like, fifteenth of sixteenth of October to get the first beta version out.
**Filippo:** And to start the integration into the chat, chat tool drop.
**Filippo:** Okay.
**Filippo:** Let's, let's try to to stick to this deadline as much as possible.
**Filippo:** But, again, Marty Kitt is now solid for now.
**Filippo:** Is a matter of getting Slava too.
**Filippo:** Close it.
**Filippo:** And I think it's almost there.
**Filippo:** And then again, David Catala will be back. I'm gonna ask for, for someone, a name, that we can use this person to help us out.
**Filippo:** But as you said, in a week or so, we should be able to get a first version out.
**Filippo:** Sounds good? Sounds good. K.
**Filippo:** Week what else? Oh, iPhone do screenshot. Your point. Yes.
**Victor:** Remember that, Martin, was they start testing it and testing an update.
**Victor:** Apple released x code 27.2.
**Filippo:** I noticed
**Victor:** Which does not include this functionality.
**Victor:** We're waiting for point one which I guess it's the edge version, the like, in some distributions.
**Victor:** The the old one is
**Victor:** the
**Victor:** limit. Anyway, so so far, not updates. What I've been trading in developer forms and so on is that it's not
**Victor:** going to be as
**Victor:** easy as moving from
**Victor:** I remember it was, to flat design or or or
**Filippo:** Yep.
**Victor:** looking look at
**Victor:** glass and so on. It's you have to consider a lot of new ways to interact with with the app.
**Filippo:** Yeah.
**Victor:** Or within my so screenshots is easy once we once Apple releases 27.1 in the new simulator.
**Victor:** Making a good adaptation not so much.
**Victor:** But that's that comes afterward.
**Victor:** But
**Victor:** just so that you are aware.
**Filippo:** So
**Victor:** And
**Victor:** I that's that's the thing that I forgot to
**Victor:** mention.
**Victor:** If we keep Goya and Midaj and Life or Zombie, we need to eventually come for this.
**Victor:** Or they will become non relevant.
**Victor:** In
**Victor:** in the store.
**Filippo:** Matiano is gonna meet Apple the thirtieth in the office. Actually, no. Matiana is not gonna be in the office, but there's gonna be the the airport people in the office. What he wants to do is to go there with a plan.
**Filippo:** Not a fix, a plan.
**Filippo:** Which means show them a video slash screenshots.
**Filippo:** On how the major apps are behaving with the the new screen.
**Filippo:** And to be fair, I think you can do this using the simulator that you have in code right now because there's a sort of simulator that you can use to to enlarge or or kind of, change size.
**Filippo:** That is enough to prove how an app will look into the two screen, sizes that that the Duo has.
**Filippo:** So my question to you would be, would you be able to provide those two screenshots or even a video showing how enlarging the the the the simulator
**Victor:** Yeah.
**Filippo:** Will affect the app.
**Victor:** Yeah. You're right. The the resizable functionality is already there.
**Victor:** For mostly for iPhone mirroring.
**Victor:** I may need to convince Xcode that I'm not in Europe.
**Victor:** To use, like, for memory or or maybe the simulator doesn't care.
**Filippo:** But it does work for me, by the way,
**Victor:** Okay.
**Filippo:** Works for me.
**Victor:** I I did yeah, I did something to, actually, to enable the image playground. For example, the the seat intelligence or whatever it's called now.
**Victor:** But for mirroring, it still was not launchable.
**Filippo:** You
**Victor:** Does it lunch for you? I mean,
**Filippo:** It does.
**Victor:** I think I said it I said my environment for for United States, but maybe that's not enough. I know.
**Filippo:** I tried
**Victor:** I can I can
**Filippo:** I may be wrong.
**Victor:** keep trying? I did not try not enough because
**Filippo:** Yeah. Yeah. No. Clear. Clear.
**Victor:** I did not care enough.
**Victor:** For for this.
**Victor:** And still, the resizable thing is not the whole story.
**Victor:** Because now you can put the app, like, in alpha to the state and and put it, like,
**Filippo:** Yeah.
**Victor:** a standard piece or, a timepiece
**Filippo:** Yeah.
**Victor:** So all of these modes I will I don't know.
**Victor:** Guessing they will not work out of the works. I mean no. That's not the that's
**Filippo:** That's
**Victor:** that's a sure bet.
**Filippo:** That that that's sure.
**Victor:** But that's that's what Apple will ask about.
**Victor:** Even if the it doesn't make sense for some of our apps. Yeah. Like,
**Filippo:** So
**Victor:** yeah.
**Filippo:** The the important thing for us is to show that we care by saying, hey. Look. We are already starting to think about how to improve this.
**Filippo:** But the reality of thing is that we need a full product team involved in this.
**Filippo:** Because we need a designer to think about what's gonna happen, as you said, in different modes, It's not about a developer going there and say, okay. Fix No. It's not about constraint or or auto layout.
**Filippo:** It's much more complex. It's a proper product decision here.
**Victor:** Yeah.
**Filippo:** So
**Victor:** And it is his last photo app We need to support the new Apple Pencil.
**Victor:** Because it's it's a natural interaction with with the designer and image to
**Filippo:** Yep.
**Victor:** to just
**Filippo:** Yep.
**Victor:** draw.
**Victor:** Or or even to to drag things.
**Filippo:** Okay. Let's select this because I really need to jump on the next meeting. Today's some it's a Monday pretty much for me.
**Filippo:** I want to do a recap quickly.
**Filippo:** Go ahead, Mirage. Let's stop here. I'm gonna talk to Matayano.
**Filippo:** And see if it is okay for us to start to sunset this up.
**Filippo:** In that case, we are gonna come up with a plan on how to sunset them.
**Filippo:** Martech SDK, Martech kit release, today, the four point o with Braze, integrated. Martech pack, we know that next week, it's gonna be released I'm gonna push forward 1.0 with the good documentation and Braze integrated.
**Filippo:** Eye mode Start to talk to Andre next week.
**Filippo:** About how everything is working. I will meet with David Martos, which is gonna be which is the PM
**Victor:** And
**Filippo:** Is gonna be the sole product person working on the app. I will meet him next week.
**Filippo:** On Tuesday. So I will have a proper overview of the road map, and I'm gonna share it with you once I meet him. And last point, the iPhone Duo if you could provide screenshots or video on how iMode behaves today in a resizable screen.
**Filippo:** That would be great.
**Filippo:** That's it.
**Victor:** Okay.
**Victor:** Will let me write it down.
**Victor:** I mean, the the IMO thing.
**Filippo:** I'm gonna write your message now with everything
**Victor:** Perfect then.
**Filippo:** So that Victor.
**Victor:** Mhmm.
**Filippo:** You so much.
**Filippo:** Anything that I can help that we haven't mentioned yet?
**Victor:** No.
**Victor:** That's it.
**Victor:** I guess you're aware that next Friday is also PTO.
**Filippo:** It's Thursday.
**Victor:** Or oh, Thursday. Yeah.
**Filippo:** It's Thursday.
**Victor:** Yeah. That works. That's yeah.
**Filippo:** I know. I know. I know. I know. I know.
**Victor:** Thursday. You're right.
**Victor:** So you're you're
**Filippo:** Yeah.
**Victor:** more than I am.
**Filippo:** Victor, I'm try I'm gonna try to to be be, more, open with the deadlines and everything, try to give you proper dates.
**Filippo:** But as you can see, things are evolving every minute. So I'm I'm gonna try to
**Victor:** K.
**Victor:** Alright.
**Filippo:** To be as as strict as possible.
**Victor:** You too.
**Filippo:** Have a great weekend.
**Filippo:** Speak soon.
**Victor:** Pressed.
**Filippo:** Bye bye.
**Victor:** Cheers.
