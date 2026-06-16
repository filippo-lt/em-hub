Jun 15, 2026

## Andrey / Filippo \- Weekly 1:1 \- Transcript

### 00:01:19

**Filippo Tosetto:** Hello. Hello. Why is my face off center? Okay. Good morning, Andre.

**Andrey Marinov:** Good morning.

**Filippo Tosetto:** How are you doing?

**Andrey Marinov:** Doing well with you.

**Filippo Tosetto:** I'm uh good.

**Andrey Marinov:** How was the time off to

**Filippo Tosetto:** I'm always good. Always good.

**Andrey Marinov:** here?

**Filippo Tosetto:** I was uh I was at a wedding on Thursday. Yes.

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** and uh Italian weddings.

**Andrey Marinov:** Good.

**Filippo Tosetto:** We started No, it's good.

**Andrey Marinov:** Bad.

**Filippo Tosetto:** Started eating at around 12\. We finished around 900 p.m.

**Andrey Marinov:** Oh, that's quick.

**Filippo Tosetto:** What do you mean that's quick?

**Andrey Marinov:** Well, here usually if you start at like 6, it goes until like 2:00

**Filippo Tosetto:** Okay.

**Andrey Marinov:** a.m.

**Filippo Tosetto:** Okay. Yeah. All right. Good. Nice.

**Andrey Marinov:** Yeah. I mean, a lot of a lot of people leave in the meantime, but

**Filippo Tosetto:** Yeah. Yeah. Yeah. Same same for us.

**Andrey Marinov:** still.

### 00:02:21

**Filippo Tosetto:** Same for us. But no, um time off is always good. Uh you're going to have some time off from Friday, right?

**Andrey Marinov:** Yes.

**Filippo Tosetto:** Nice.

**Andrey Marinov:** Going to Greece to the beach.

**Filippo Tosetto:** Where exactly.

**Andrey Marinov:** Uh, Nikiti in Hokiki.

**Filippo Tosetto:** Okay. No, I've never been there.

**Andrey Marinov:** I agree. It's uh in the north part.

**Filippo Tosetto:** I've

**Andrey Marinov:** Uh since it's so close,

**Filippo Tosetto:** been

**Andrey Marinov:** we usually drive there.

**Filippo Tosetto:** fair point. Nice.

**Andrey Marinov:** Oh,

**Filippo Tosetto:** Now I usually go to the islands. Um last time I was in Cit was super nice. Cit is very very nice actually. Really enjoy that. But yeah, you need you No,

**Andrey Marinov:** I don't

**Filippo Tosetto:** it's huge.

**Andrey Marinov:** think

**Filippo Tosetto:** It's it's a huge island. You you take hours to go from one side to the other.

**Andrey Marinov:** I usually focus around this area over here.

**Filippo Tosetto:** Yeah. Nice.

**Andrey Marinov:** And this is where I'm

### 00:03:19

**Filippo Tosetto:** Okay.

**Andrey Marinov:** going.

**Filippo Tosetto:** Okay. With all the family.

**Andrey Marinov:** Yeah, everyone. Even the two moon

**Filippo Tosetto:** Nice. Good.

**Andrey Marinov:** fold.

**Filippo Tosetto:** You deserve a bit of a of a rest. And I guess your wife deserve it more than you.

**Andrey Marinov:** Oh, traveling with two kids. You're not going on a vacation. you're going on a

**Filippo Tosetto:** Okay.

**Andrey Marinov:** trip.

**Filippo Tosetto:** Okay. That's a good definition. Yes. Makes sense.

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** I was last

**Andrey Marinov:** Uh so pretty good.

**Filippo Tosetto:** week.

**Andrey Marinov:** I was I managed to uh make a lot of progress. I think we I covered the the phases as much as I can. I made some progress on the parapet side, but I still need to figure out how to test that and make sure that it works properly because I don't trust it. Uh, and what it did uh and then I tried to get up the deployment to work, but we ran across those issues.

### 00:04:26

**Andrey Marinov:** Uh, message Julian. Uh, he's obviously going to work through that. uh so he's going to handle the deployment and yeah the outstanding things for that deployment setting up uh a lot of secrets there basically I I need to plug in a lot of secrets everywhere so that uh we can make sure that the functionality works properly I did check out the register and signing in and those are fine uh and it's pretty plug and play and yeah that's that's about the state of it need

**Filippo Tosetto:** Nice.

**Andrey Marinov:** decisions design uh the lookup API keys and that sort of

**Filippo Tosetto:** Yeah. Yeah. Yeah. I know. I know everything um about those parts.

**Andrey Marinov:** thing

**Filippo Tosetto:** But let's say that in one week you progress more than I expected, which is uh very good in my opinion. Um I think you're doing very well with this web project considering we don't know anything about

**Andrey Marinov:** I I don't know.

**Filippo Tosetto:** web.

**Andrey Marinov:** I might be doing it very well or I might not.

### 00:05:42

**Andrey Marinov:** I I have no way of

**Filippo Tosetto:** Yes, I know. I know.

**Andrey Marinov:** knowing.

**Filippo Tosetto:** I know a bit of web development and in my opinion it's you know what I think is that web development is just much much easier than app because you can add a lot of tests and uh unit test but also end to end test so well it works

**Andrey Marinov:** Yeah,

**Filippo Tosetto:** so I'm doing

**Andrey Marinov:** it's so much easier because it was like, "Oh yeah, I'm going to need all of the Parapat information and I looked around the the parapat stuff and I found one of the things it wanted, but I couldn't find the rest of it." And I was like, "Okay, here's here's the website. Figure it out." and he managed to figure it out.

**Filippo Tosetto:** Yeah. Yeah. Nice. Nice. Thank you. Uh yes.

**Andrey Marinov:** Allegedly,

**Filippo Tosetto:** So the plan for me for this is this week is mainly wiring all the things up pretty much. So as you mentioned all the missing API keys for the phone lookup service regarding parapet I've noticed that you already configured everything.

### 00:06:49

**Andrey Marinov:** I only have access to development. So nothing from production and uh yeah

**Filippo Tosetto:** Yep.

**Andrey Marinov:** it should be configured.

**Filippo Tosetto:** Yeah. So, it's just a matter of seeing if tokens are actually Yeah.

**Andrey Marinov:** It works

**Filippo Tosetto:** But okay,

**Andrey Marinov:** now.

**Filippo Tosetto:** we can do that throughout this week. And then um authentication, you said it works

**Andrey Marinov:** Yeah. Tested that. Managed to log in.

**Filippo Tosetto:** fine.

**Andrey Marinov:** uh fixed an issue because after you log in, it still says login. So, it now takes into account your authentication state and it says log out instead.

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** Uh but

**Filippo Tosetto:** Okay. Nice. And I guess we also need Stripe,

**Andrey Marinov:** yeah,

**Filippo Tosetto:** but I think that part can wait. Uh let's do everything else first and the payment after holidays, I would say. Um okay. Uh, also in terms of product, there are a lot of epics ready that I'm going to go through because I don't trust product people at all and already bounce back a few things because they are not really reading what the AI is spitting out.

### 00:08:10

**Filippo Tosetto:** Yeah. Yeah. That's uh my the problem with AI that you can use

**Andrey Marinov:** Hold

**Filippo Tosetto:** it properly or just just approve everything.

**Andrey Marinov:** me.

**Filippo Tosetto:** Let's see. Okay. Nice. Um, anything specific you will need from me beside pushing to get this API

**Andrey Marinov:** Uh let me just check through real quick.

**Filippo Tosetto:** keys.

**Andrey Marinov:** Uh secret manager and runtime environment. That'll be interesting to see how we set that up with Julian. I did ask last week but don't think he responded about us getting the uh secret manager secrets create permission uh because we need to plug in the the Firebase admin runtime configuration the parapet stuff the keys when we get them uh so we probably need to do that uh for parapet there's some other things like building project logical product offering entitlements and strip price mapping, that sort of thing, but I'm not 100% sure what to put in. And yeah, things like price, trial, price, if there's a trial, trial length, um billing

**Filippo Tosetto:** So sorry if I go

### 00:09:38

**Andrey Marinov:** cadences.

**Filippo Tosetto:** here I see you created this guy and and then if I go to app

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** setup I see why did you put no authentication? third

**Andrey Marinov:** I don't remember. Uh can you uh yeah because all there was only anonymous plus identity and I didn't want to put in anonymous wasn't sure on that yet as well.

**Filippo Tosetto:** per.

**Andrey Marinov:** So that's that's something we can tweak.

**Filippo Tosetto:** Oh, your project owns identity and session. So, okay. So,

**Andrey Marinov:** All right.

**Filippo Tosetto:** the project the web project Yeah.

**Andrey Marinov:** It was because Firebase handles

**Filippo Tosetto:** And then the quarter limits.

**Andrey Marinov:** that.

**Filippo Tosetto:** This is like what apps you don't care. Tokens is about tokens. It's like apps.

**Andrey Marinov:** Put in the phone lookup tokens in

**Filippo Tosetto:** Okay.

**Andrey Marinov:** here.

**Filippo Tosetto:** Nice. Uh this is something that we need to discuss with product. How do you want to handle um credits and tokens?

**Andrey Marinov:** I

**Filippo Tosetto:** But this is an easiest configuration.

### 00:10:51

**Andrey Marinov:** don't

**Filippo Tosetto:** Oh. Oh, I see. So, entitlements, products,

**Andrey Marinov:** like we will have monthly,

**Filippo Tosetto:** offering,

**Andrey Marinov:** six months, a year, that sort of thing.

**Filippo Tosetto:** but um probably this is coming from Stripe.

**Andrey Marinov:** Uh the billing. Yeah.

**Filippo Tosetto:** Okay.

**Andrey Marinov:** We need Stripe setup credentials, things like that.

**Filippo Tosetto:** Do we really need to? Well, I'm going to ask um Durban about all of these parts because

**Andrey Marinov:** Yeah,

**Filippo Tosetto:** in apps everything comes for free because you connect to revenue cat and so entitlements products.

**Andrey Marinov:** we don't have anything.

**Filippo Tosetto:** No, no, not in web. No, no. That's why we use stripe.

**Andrey Marinov:** Maybe let's let's open the other ones. If you go to to web projects and see like PDF stuff. Oh, maybe gather one because it has subscribers.

**Filippo Tosetto:** Cosmic PDF. Okay. I can see stripe here.

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** Okay. So that is something. Okay. Configured offerings.

### 00:12:12

**Andrey Marinov:** Where is the default monthly one?

**Filippo Tosetto:** Okay.

**Andrey Marinov:** Maybe that's

**Filippo Tosetto:** Oh, these are the different products and entitlements. Okay, so it's an interface similar to revenue cat. I will play around with it or this week or the week you're off so that when you're back, we can get this sorted.

**Andrey Marinov:** Oh, it's basically what do we want uh people to have at what price, at what period, that sort of thing.

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** But I don't know what we want.

**Filippo Tosetto:** Web hook. Okay. Need to understand that part and no plugins. So if I go to webbook.

**Andrey Marinov:** Oh, we don't have anything

**Filippo Tosetto:** Oh,

**Andrey Marinov:** yet.

**Filippo Tosetto:** got it. Interesting. This is going to be fun. Okay. Um I'm going to uh let's do everything else first. deployment, the phone lookup API keys and uh the Yeah,

**Andrey Marinov:** just past the stuff we

**Filippo Tosetto:** thank you.

**Andrey Marinov:** need.

**Filippo Tosetto:** Wow. Okay. Okay.

### 00:14:00

**Filippo Tosetto:** Okay.

**Andrey Marinov:** So dev deploy that's Julian he handles that uh secret manager the things where we set up all of the secrets parad stuff what we just discussed

**Filippo Tosetto:** Yeah. Yeah.

**Andrey Marinov:** pricing pricing of the stuff that we just just discussed uh the phone lookup uh we need to plug in

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** keys that sort of thing in here for the phone look up and then the

**Filippo Tosetto:** Okay. Sounds good to me. Not a problem.

**Andrey Marinov:** design

**Filippo Tosetto:** Um, as I said, this week is probably going to be mostly wiring thing up and testing that what we have till now it's working and when you are back from your holiday uh hopefully we're going to have a design first of all and we can move forward with more like visual stuff. But my opinion the core log business logic it's already there. It's just a matter of making sure it works as expected.

**Andrey Marinov:** I think so. Let's

**Filippo Tosetto:** Um, let's see. Let's see. Uh,

### 00:15:03

**Andrey Marinov:** see.

**Filippo Tosetto:** I'm as curious as you about all of this. By the way, uh, I have a question which is, how do you find this way of working with tons of documentation and this report? What do you think?

**Andrey Marinov:** Uh, I like it because like we can uh see where we at, what needs what's outstanding, what needs to get done. Makes it a lot easier on the agents as well. So yeah,

**Filippo Tosetto:** How do you wire it up with the agents? That's me. I'm trying to understand the

**Andrey Marinov:** I give it the the GitHub uh repo and tell it to go read through it

**Filippo Tosetto:** workflow.

**Andrey Marinov:** and based on that in the beginning I put in the the highest uh uh thinking possible and told it uh to come up with a plan. Based on that I copy pasted all of our chats that we were having in the chat so that it can because there were new things in there as well so that it can know what we discussed in there as well and then it came out with a plan and I told it okay uh think of five different things that we haven't covered or we haven't thought of and it starts like spitting some things out and uh whatever made sense I put in there And uh yeah that's that's basically what it did.

### 00:16:32

**Andrey Marinov:** It came in came in with a plan. I told it to break that plan into different phases so that uh we would have an iteration with every APR and like things that to work on. It did that as well and then it just lowered the thinking and then started implementing. And by the way,

**Filippo Tosetto:** Nice.

**Andrey Marinov:** this is like the the site.

**Filippo Tosetto:** Oh

**Andrey Marinov:** Put in a number uh search just search history.

**Filippo Tosetto:** no.

**Andrey Marinov:** There's rendering here at the bottom history. I haven't used history anything account is just sign

**Filippo Tosetto:** Well,

**Andrey Marinov:** uh which is one. Yeah. But then you can go in you can register or continue with Google.

**Filippo Tosetto:** that's

**Andrey Marinov:** I'm not sure if you see the popup, but I pressed continue with Google and I'm now signed in

**Filippo Tosetto:** nice.

**Andrey Marinov:** again.

**Filippo Tosetto:** Okay. And obviously phone lookup doesn't work because we don't have APIs.

**Andrey Marinov:** Yeah, but this is the UI when we do have it.

**Filippo Tosetto:** But Okay,

### 00:17:43

**Andrey Marinov:** Yes.

**Filippo Tosetto:** it's a starting point. Nice. Um, do you write so not you the agents do you ask to write tests and end to end tests in general?

**Andrey Marinov:** Yeah. Yeah.

**Filippo Tosetto:** Nice. Nice.

**Andrey Marinov:** And you also plugged in uh playright test. So we do those as well.

**Filippo Tosetto:** Yeah. Yeah, I put that. um just coping around with what other people are doing around uh the company. Uh but this is very good.

**Andrey Marinov:** It's

**Filippo Tosetto:** Uh I I actually run it last week uh just to to make sure I knew

**Andrey Marinov:** always

**Filippo Tosetto:** what was happening and it works. Nice.

**Andrey Marinov:** uh there's a lot of these messages here about things that we've discussed that uh for example for EU, UK and Swiss numbers and this sort of thing that we'll figure out with the design but

**Filippo Tosetto:** That's that's on product people. I flagged everything and they need to take care of it. I'm not I cannot take that decision for them.

### 00:19:07

**Filippo Tosetto:** Okay, Andre, thank you so much. Um, very very good. Um, I like the workflow, the the five things we haven't thought about. I'm going to use that. Um, if you are okay, I will keep improving that documentation based on the information we're going to get throughout uh the conversation with product so that we keep everything centralized somewhere. 96\.

**Andrey Marinov:** And today I just had something. This is most on my side

**Filippo Tosetto:** I let you know of any

**Andrey Marinov:** now.

**Filippo Tosetto:** advances.

**Andrey Marinov:** I guess he's having a tough couple of

**Filippo Tosetto:** Nice.

**Andrey Marinov:** weeks.

**Filippo Tosetto:** Okay, sounds good. Good. I like movement. Um, last Monday you guys released Screamy Ring with TV Foundation

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** Kit.

**Andrey Marinov:** Uh, and it's working suspiciously well.

**Filippo Tosetto:** I've never seen Miguel so happy in my life.

**Andrey Marinov:** 11 cuz I was checking

**Filippo Tosetto:** Yeah, he was super

**Andrey Marinov:** like uh the latest one uh I don't know where it

**Filippo Tosetto:** happy.

**Andrey Marinov:** says healthy release.

### 00:20:52

**Andrey Marinov:** Haven't checked that today. That's weird.

**Filippo Tosetto:** Okay. Do we have any users?

**Andrey Marinov:** Uh, it's going to be right because I was looking at one one zero and it says 98% 98% crash free.

**Filippo Tosetto:** There's only one

**Andrey Marinov:** Go to monitor.

**Filippo Tosetto:** crash.

**Andrey Marinov:** Ah, I I already fixed that one. Uh the other ones were actually Oh no. Yeah, I uh plugged that in and I fixed it. It's uh we haven't released it obviously, but that's been taken care of. But to active users since I'm looking at 24

**Filippo Tosetto:** Nice.

**Andrey Marinov:** hours,

**Filippo Tosetto:** Okay.

**Andrey Marinov:** it wouldn't work. Uh so that is that just one. Yeah. So it's these two crashes. I've addressed them uh were created in Jira. So that's good. But if we go into non fatals, which is what tells us whether there are any issues when they try to connect and that sort of thing. Uh there was some something from revenue cat that I looked at and uh it's more of a uh it's an okay warning that we should ignore.

### 00:22:27

**Andrey Marinov:** So I've ignored that as well. But suspiciously there's like no we failed to cast to a certain TV because those should come up here as well.

**Filippo Tosetto:** Why you say

**Andrey Marinov:** Oh,

**Filippo Tosetto:** suspiciously?

**Andrey Marinov:** it can be 100%. I mean it's it's got to be at least someone out there. can

**Filippo Tosetto:** Do you do you connect Have you connected stuff to amplitude as well?

**Andrey Marinov:** connect. I don't have access on amplitude.

**Filippo Tosetto:** What?

**Andrey Marinov:** Yeah, when I go in there, um, mode, I have to turn off my think that prevents me from loading ads. One second.

**Filippo Tosetto:** For me, these few applications are very weird in terms of user

**Andrey Marinov:** They sure

**Filippo Tosetto:** base.

**Andrey Marinov:** are. Do you have access to amplitude?

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** I'm going to leave this to be able to turn off my

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** protections.

**Filippo Tosetto:** Uh are you logging anything specific regarding um connection in

**Andrey Marinov:** I'm logging everything on amplitude.

**Filippo Tosetto:** amplitude in amplitude as well.

### 00:24:30

**Andrey Marinov:** No, it's just in Firebase.

**Filippo Tosetto:** Okay.

**Andrey Marinov:** Okay, I cancel it now. Need some time to figure out why that is.

**Filippo Tosetto:** Well, I have some data point cast photofunnel start cast. Yeah.

**Andrey Marinov:** 60%.

**Filippo Tosetto:** And video is very low.

**Andrey Marinov:** Now, is that on 1.1

**Filippo Tosetto:** And this is uh we can filter

**Andrey Marinov:** or

**Filippo Tosetto:** by version. Where is it? Filter by Okay.

**Andrey Marinov:** So number

**Filippo Tosetto:** 73\. Let me go to the other. Can I filter? No,

**Andrey Marinov:** Thanks.

**Filippo Tosetto:** not from here. Uh where is it? Uh video. Buy Android. We don't have Android. Need to buy version.

**Andrey Marinov:** That's not

**Filippo Tosetto:** That's still pretty

**Andrey Marinov:** good.

**Filippo Tosetto:** low.

**Andrey Marinov:** Well,

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** that's weird. I should be able to get the logs on our base. Maybe they're not working now. Take a look.

**Filippo Tosetto:** Oh, we also have the web part.

### 00:26:21

**Filippo Tosetto:** Direct accesses or no direct accesses. What's the difference?

**Andrey Marinov:** I I don't know either maybe the thing where you put in the URL or the thing where we navigate you to it.

**Filippo Tosetto:** Yeah, slightly higher, but it's only 38 users overall in the last 30 days. So,

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** it's not really something specific.

**Andrey Marinov:** So, I guess it my logging doesn't work. I'll have to take a look at this and the logging and see why that is.

**Filippo Tosetto:** Okay. Yeah. This is the data that I have.

**Andrey Marinov:** Is there a way you can check whether maybe invite members at the top right and invite me?

**Filippo Tosetto:** Uh I need to do you have access to amplitude? Let me see.

**Andrey Marinov:** I do. Yeah.

**Filippo Tosetto:** And uh Oh, you

**Andrey Marinov:** Yep,

**Filippo Tosetto:** do.

**Andrey Marinov:** I have access to the team, but the team is empty for me.

**Filippo Tosetto:** Uh, Andre, Andre, Andre, search name our email. Here you go. Manage project success.

### 00:28:08

**Filippo Tosetto:** This is stupid. Why don't you have access to this things screaming member member? Maybe I note as well.

**Andrey Marinov:** I want to be nice. Okay,

**Filippo Tosetto:** Okay.

**Andrey Marinov:** to load things now. And also take a look at how the funnels are set up because that doesn't mean much. Maybe we're not tracking the right thing. Yeah,

**Filippo Tosetto:** That could also

**Andrey Marinov:** for me it's uh it's like this

**Filippo Tosetto:** be.

**Andrey Marinov:** uh should be do you have this thing in your now?

**Filippo Tosetto:** Can you try to open that one?

**Andrey Marinov:** Okay, it's not I have another website, I guess.

**Filippo Tosetto:** Yeah, you can see

**Andrey Marinov:** Oh,

**Filippo Tosetto:** it.

**Andrey Marinov:** yeah. Yeah, it's dashboard. Yeah, I had a different company here. Okay, great.

**Filippo Tosetto:** Nice. You have also access to both staging and production. So you can do all your tests.

**Andrey Marinov:** No,

**Filippo Tosetto:** Good, good, good.

**Andrey Marinov:** right.

**Filippo Tosetto:** Um, Andre, I want to talk to you about

### 00:30:20

**Andrey Marinov:** Yes.

**Filippo Tosetto:** IMOD.

**Andrey Marinov:** uh for that we are starting to figure out how to uh support the the tiered subscriptions. Uh basically today we were talking about whether there's a way from Super Bowl to uh figure out whether uh people are on the current subscription that's not tiered so we can keep them there and how to go implement the tiered subscription. And I think that Carman is mostly going to be figuring that out today uh this week with Sophia Stephania. Stephania, I forgot the name.

**Filippo Tosetto:** Okay. The the person.

**Andrey Marinov:** Uh Stephania.

**Filippo Tosetto:** Yes.

**Andrey Marinov:** Uh and yeah, we'll probably have more when I come back,

**Filippo Tosetto:** Okay.

**Andrey Marinov:** but that's like a priority to do.

**Filippo Tosetto:** Yeah. It was talking. He was asking me to have a look at this pro plus monetization from an implementation point of view. What do you actually need to do? Because for me it's a bit confusing what they want to

**Andrey Marinov:** uh set up like a tiered way,

### 00:31:30

**Filippo Tosetto:** do.

**Andrey Marinov:** a tiered subscription. And then the tricky part is figuring out who's currently on the subscription where it's not tiered so that we don't mess with those guys. And then any future users need to be on the tier

**Filippo Tosetto:** Oh,

**Andrey Marinov:** subscription because the other guys have paid.

**Filippo Tosetto:** can it be as simple as version check?

**Andrey Marinov:** Uh no because uh that comes from super wall and revenue cat and those are like version agnostic

**Filippo Tosetto:** No.

**Andrey Marinov:** and they think they can maybe do it through super wall. Maybe super wall can do that for us but they're not sure. So they're checking

**Filippo Tosetto:** Why what about doing it through revenue cat um entitlements?

**Andrey Marinov:** Uh I've we can do that through revenue cat but we need still to uh show the right pay walls for people and that comes through super

**Filippo Tosetto:** Yeah,

**Andrey Marinov:** wall.

**Filippo Tosetto:** that's true because we use Super Bowl and Super Bowl is stupid. You're right.

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** I hate Super Bowl. Okay, so it's not even a matter of implementation in your case here because the implementation part is pretty straightforward.

### 00:33:06

**Filippo Tosetto:** Okay,

**Andrey Marinov:** No.

**Filippo Tosetto:** because my suggestion was, hey, uh, considering the web is under control, why don't you focus on IM mode so you get a build out before you leave? But it's not under your control.

**Andrey Marinov:** They don't know about that. Yeah. Oh, look at screen mirroring.

**Filippo Tosetto:** It's not under you. Uh, whatever you you feel you have the the time to do, I mean, you are I trust you. I honestly trust you. I see that you move freely in between things. So I'm not I'm not going to direct you uh because uh you're able to do that. Uh that case I'm going to try to unlock you in in the web part as soon as possible so we can move

**Andrey Marinov:** Okay,

**Filippo Tosetto:** forward. Okay, sounds good.

**Andrey Marinov:** down.

**Filippo Tosetto:** Um question regarding IMO Android. How is it going there?

**Andrey Marinov:** Uh still basically the same thing where uh they're nailing down uh things to to nail down on the performance side and trying to figure out like uh the road map and future development things.

### 00:34:13

**Andrey Marinov:** still talking about ads and Tik Tok SDK integration. So no, not much progress there. Uh they're doing some maybe testing on the super site on Android.

**Filippo Tosetto:** Do you think it's worth for for them to focus on a similar work that you're doing with the foundation kit?

**Andrey Marinov:** Um, I don't know a lot about the connect SDK on Android, but the performance thing, I think that's part of it.

**Filippo Tosetto:** Okay. My

**Andrey Marinov:** Also, it maybe doesn't make as much sense because we don't have like screen mirroring Android.

**Filippo Tosetto:** perception

**Andrey Marinov:** So it doesn't make sense to extract it for now. And if it works currently, best thing would be to tweak it to work better.

**Filippo Tosetto:** I'm going to investigate products if they want to build a screen mirroring Android version in the future because in that case we can save some time and go down with uh that on the but you know this

**Andrey Marinov:** not the case then. Yeah.

**Filippo Tosetto:** company they take decisions on a dayto-day basis.

**Andrey Marinov:** Yeah.

### 00:35:40

**Andrey Marinov:** Oh, and on multi they also wanted to have like an AB testing uh have the non-tiered version for some people and then the tiered version for other people. So, we'll be doing that as well and see whether we get more money the tiered version.

**Filippo Tosetto:** AB tests for current state and tier version and then the tier version is split. the subscriptions in through three

**Andrey Marinov:** Yeah,

**Filippo Tosetto:** tiers.

**Andrey Marinov:** basically leave the app as it is right now and then as a B test at the tiered

**Filippo Tosetto:** Okay.

**Andrey Marinov:** version

**Filippo Tosetto:** And the tier version is like today, but they add one more tier on top of it. It's like the pro subscription with the skins that no one cares

**Andrey Marinov:** with the skins Yeah.

**Filippo Tosetto:** about. All right,

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** sounds good to me. Foundation kit on IM mode TV foundation

**Andrey Marinov:** I have a PR for that.

**Filippo Tosetto:** kit.

**Andrey Marinov:** Uh I need to do a lot of testing basically. But from the screen mirroring side it should work cuz connect discovering connectness moves toward to work there.

### 00:36:57

**Andrey Marinov:** Uh so maybe that's something we can focus on this week.

**Filippo Tosetto:** Yeah. Yeah.

**Andrey Marinov:** Push that

**Filippo Tosetto:** Yeah. Push that out.

**Andrey Marinov:** out.

**Filippo Tosetto:** So I can uh write a nice email to everyone and everyone is happy because we are making progress and it's noise that we like to to keep um up. Yeah, I like that.

**Andrey Marinov:** Yeah,

**Filippo Tosetto:** I like that. Let's do that.

**Andrey Marinov:** I'll message

**Filippo Tosetto:** Okay. Nice,

**Andrey Marinov:** her.

**Filippo Tosetto:** nice, nice, nice. Okay. Uh what else, Andre?

**Andrey Marinov:** You no kill code for me or I guess anyone.

**Filippo Tosetto:** Say again.

**Andrey Marinov:** uh Q code the the

**Filippo Tosetto:** Oh, kilo code talked to to Durban last week.

**Andrey Marinov:** tokens.

**Filippo Tosetto:** Uh common is slightly stuck at the moment because Hilo code promised us something which is being able to uh provide tokens to each developer. They promised that they can do it but now they can't. So they have a pool of tokens for the whole company which is the usual thing that we don't want

### 00:38:10

**Andrey Marinov:** Interesting.

**Filippo Tosetto:** because Andre may need way more tokens than Vlad but Vlad will steal tokens from Andre so it doesn't really do what we want to do. So we are trying to get our way around all of this basically. I'll keep you up to date, but we are sort of a an impass moment uh with this AI token situation and hopefully we're going to get sorted very very soon.

**Andrey Marinov:** Okay. Well, I'll be off next week, so

**Filippo Tosetto:** Yeah,

**Andrey Marinov:** fine.

**Filippo Tosetto:** to be honest, Andre, I think you are moving very very well. Um, and the fact that yes, you are handling two different projects, but I notice even though he's making more money, he has way less road map. So, I'm I'm I'm okay with that. Um, how do you feel about it? You feel stressed or

**Andrey Marinov:** Uh, no. It's I'm mostly blocked everywhere,

**Filippo Tosetto:** So, that's my

**Andrey Marinov:** but I'm also out of tokens.

**Filippo Tosetto:** point.

**Andrey Marinov:** So, I know I have 80% left until

### 00:39:25

**Filippo Tosetto:** Yes.

**Andrey Marinov:** Thursday.

**Filippo Tosetto:** 80% left until Thursday.

**Andrey Marinov:** 18\.

**Filippo Tosetto:** What about that thing you sent over during the weekend?

**Andrey Marinov:** I do have one reset,

**Filippo Tosetto:** The reset.

**Andrey Marinov:** but I'm like pocketing it for now for

**Filippo Tosetto:** Yeah. Yeah. Pocket. Yeah. Yeah.

**Andrey Marinov:** tough times,

**Filippo Tosetto:** No need.

**Andrey Marinov:** crisises, that sort of thing.

**Filippo Tosetto:** But are you maxing out cursor at least?

**Andrey Marinov:** uh it was refusing to for me to use any of the cool models last week. So guess so. I don't know. It said everything above like Opus 4.1 was

**Filippo Tosetto:** Why?

**Andrey Marinov:** paid max model and gave me an error and all the

**Filippo Tosetto:** So you can't

**Andrey Marinov:** cool 12 GPTs as well. I only get like 5.3 GP

**Filippo Tosetto:** Wait, what?

**Andrey Marinov:** and that was last week inside that amount of extra

**Filippo Tosetto:** So

**Andrey Marinov:** usage.

**Filippo Tosetto:** uh so sorry, let me show still. I can Can you see oppus 4.8?

### 00:41:03

**Andrey Marinov:** Yep.

**Filippo Tosetto:** Uh,

**Andrey Marinov:** No, you you put in CEX put in uh GPD. Yeah. Max only.

**Filippo Tosetto:** but I can use Max.

**Andrey Marinov:** Uh for me it says currently let me send you a

**Filippo Tosetto:** So if I use max mode,

**Andrey Marinov:** screenshot.

**Filippo Tosetto:** I can use GPD5.

**Andrey Marinov:** I've used a,03 requests out of a thousand requests.

**Filippo Tosetto:** Oopsies. Wait. So if we check So if you check your usage, how are you doing here?

**Andrey Marinov:** Uh there's some still some money left. Is that a team based money? No, it's not.

**Filippo Tosetto:** This

**Andrey Marinov:** Yeah. Uh let me share.

**Filippo Tosetto:** one

**Andrey Marinov:** Where did that go? You're doing better.

**Filippo Tosetto:** Yeah, but I'm not really doing anything here. I'm not really coding.

**Andrey Marinov:** So I'm I'm a thousand out of a thousand and I have like 200 left.

**Filippo Tosetto:** Oh,

**Andrey Marinov:** I don't know what on demand usage is now.

**Filippo Tosetto:** got it.

**Andrey Marinov:** But yeah, I'm now using 5.2 too and Kimmy

### 00:42:44

**Filippo Tosetto:** Okay.

**Andrey Marinov:** because those are the ones that work for me and

**Filippo Tosetto:** That king is total rubbish.

**Andrey Marinov:** ever.

**Filippo Tosetto:** Yeah. Uh that that error is pretty interesting. Vlad has been reporting the same and not only you two guys. So you see that number $350 that you have.

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** Well, that's not real.

**Andrey Marinov:** I think so.

**Filippo Tosetto:** Apparently we we discovered that is there is a pool of money which is

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** companywide and uh it doesn't really correspond out 350 per person but it's a cumulative one. So it's it's fake and so we are fighting with cursor for that reason

**Andrey Marinov:** Yeah, I

**Filippo Tosetto:** because it's like fake in case you're promising we can use 350 each but it's not like that but yeah that's um that's reality of things and we are trying to get things moving in this area because you guys

**Andrey Marinov:** Yeah. So, I guess I'm maxed out then.

**Filippo Tosetto:** can yeah you are you're literally maxed out uh kilo we are stuck just use whatever you can.

### 00:44:09

**Filippo Tosetto:** And uh Matiana is back from holiday. So I'm going to press in to to get us something because because you can't move forward into projects if you don't have tokens. As easy as that.

**Andrey Marinov:** Damn it.

**Filippo Tosetto:** Uh on the other end, I don't know if you heard, but Fable 5 is blocked in

**Andrey Marinov:** I saw Yeah,

**Filippo Tosetto:** Europe.

**Andrey Marinov:** that's very sad. But apparently it's very expensive. So

**Filippo Tosetto:** But the reason why is because the US government blocked it

**Andrey Marinov:** yeah.

**Filippo Tosetto:** because of jailbreak reasons. And Antropic is like what? There is no jailbreak. every single model can be jbreed and

**Andrey Marinov:** Apparently, Amazon snitched on them.

**Filippo Tosetto:** uh

**Andrey Marinov:** It's weird because Amazon owns part of the

**Filippo Tosetto:** yeah

**Andrey Marinov:** company. They know best.

**Filippo Tosetto:** they know better how to deal with all of this

**Andrey Marinov:** It's rather sad because they can choose to like rip out any model at any time for

**Filippo Tosetto:** really

**Andrey Marinov:** Europeans.

**Filippo Tosetto:** it's well we haven't actually talked about WW WDC and the fact that Apple Intelligence will now be available in Europe.

### 00:45:27

**Andrey Marinov:** Yeah, that's also very sad. Well, for now, they'll probably figure something out because it's also not available in China and this next iOS release will be, hey, look at our new release. Uh, the US gets new Siri and everyone else gets nothing. How will they sell that? How will they sell codes with nothing?

**Filippo Tosetto:** No idea. No idea,

**Andrey Marinov:** If there's nothing else in the OS itself,

**Filippo Tosetto:** honestly.

**Andrey Marinov:** there's no like big features or anything. Why

**Filippo Tosetto:** No, no, exactly.

**Andrey Marinov:** update?

**Filippo Tosetto:** It's Well, let's see. Let's see what's going to happen. Okay, Andre, anything

**Andrey Marinov:** Uh, nope.

**Filippo Tosetto:** else?

**Andrey Marinov:** There probably will be some things to update for WWDC for September with apparently the big iPhone default is coming based on things. Uh so maybe touching up the UI to be more responsive to aspect ratios. I don't know if you watch any of the videos, but it was very funny because they said you can uh screen mirror your phone on your Mac and when you do that, you can like uh pull it and make it wider and responds to aspect ratio.

### 00:46:48

**Andrey Marinov:** So, make sure you go in and support that. Wink wink. It was very funny.

**Filippo Tosetto:** Okay, but this is good to know. So, probably we should put it in the in the works for second half of July.

**Andrey Marinov:** Yeah.

**Filippo Tosetto:** Um, yeah, I wouldn't bother to do things now considering that they will change the APIs at least five times

**Andrey Marinov:** No.

**Filippo Tosetto:** before end of July. Um, have you been uh accepted to that?

**Andrey Marinov:** Yes, I'm going to that. Not sure when it was, but yes,

**Filippo Tosetto:** Yeah,

**Andrey Marinov:** I am.

**Filippo Tosetto:** it's next Thursday.

**Andrey Marinov:** Oh, that sucks.

**Filippo Tosetto:** You're No,

**Andrey Marinov:** But okay.

**Filippo Tosetto:** it's the Sorry. Sorry. No, it's the 25th of June. You You should be back. Are you back?

**Andrey Marinov:** No, but I can still access it.

**Filippo Tosetto:** No, you're not.

**Andrey Marinov:** Access it, I think. Can I?

**Filippo Tosetto:** Yeah,

**Andrey Marinov:** It doesn't need my latte

**Filippo Tosetto:** I think so.

### 00:47:43

**Andrey Marinov:** account.

**Filippo Tosetto:** No, also it's from 9:30 a.m. until 11:30 p.m. The f\*\*\* is this?

**Andrey Marinov:** It'll also be very interesting because they have nothing to talk to us about outside of the the series stuff. Like that's the big thing they want to promote to developers. Integrate with the Siri thing. Use AI. We can't use that

**Filippo Tosetto:** No, we can't.

**Andrey Marinov:** because is it a it's just for the company, right? It's not like a uh

**Filippo Tosetto:** What do you

**Andrey Marinov:** the event that they're doing is it uh is

**Filippo Tosetto:** mean?

**Andrey Marinov:** it for our company or is it for like um

**Filippo Tosetto:** Oh, I have no clue.

**Andrey Marinov:** is it for cool beyond like like when did when they did

**Filippo Tosetto:** I have no clue.

**Andrey Marinov:** the yeah the model stuff in the other

**Filippo Tosetto:** Yeah, the other two. I don't know. I'm going to check.

**Andrey Marinov:** because it's again with

**Filippo Tosetto:** I'm going to check. Yeah. So,

**Andrey Marinov:** WebEx.

**Filippo Tosetto:** I'm assuming is for us because otherwise if it was worldwide would be well WWC videos, they are public. Go and check them.

**Andrey Marinov:** Yeah. Well, again, that makes it very weird because hey, you have this API, but you can't even test it.

**Filippo Tosetto:** But you know that all of that is available on Mac.

**Andrey Marinov:** Uh yeah, I think so.

**Filippo Tosetto:** Yeah, it is.

**Andrey Marinov:** Is there another gatekeeper?

**Filippo Tosetto:** It's just not available on iOS.

**Andrey Marinov:** Yeah,

**Filippo Tosetto:** Yeah.

**Andrey Marinov:** guess that's how we'll

**Filippo Tosetto:** Doesn't make sense. Exactly. All right,

**Andrey Marinov:** test.

**Filippo Tosetto:** Andre. Thank you so much. I'll keep you up to date uh on uh all the things that we are missing so we can move forward at least with testing web. Nice. Thank you so much.

**Andrey Marinov:** That's on.

**Filippo Tosetto:** Have a good day.

**Andrey Marinov:** Bye-bye.

**Filippo Tosetto:** Bye-bye.

### Transcription ended after 00:49:58

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*