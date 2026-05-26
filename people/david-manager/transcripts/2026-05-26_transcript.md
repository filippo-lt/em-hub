Meeting Title: Filippo / David - Weekly 1:1
Date: May 26
Meeting participants: Filippo Tosetto, David Matellano

Transcript:
 
Them: Hello.  
Me: Good afternoon.  
Them: How are you, Filippo?  
Me: I'm good just checking your message. Do you have a document with all the projects Jira boards? So a list of our Jira boards. No, we don't. But we can create it. It's fine.  
Them: Have a look. I am trying to have all this information, and I reached the point that I have 150, more or less data projects. Which are the total one of them. So I have the same information previously done before. Nothing and nothing which one has the good ones in order to have information on my side. It's not a hurry. I will create the document, but I didn't know if there was imaging that you maybe have already something like this.  
Me: Now because obviously I have way less projects than you. So I just saved them in the Jira board and I'm fine with that.  
Them: Don't worry. Now I will create the leaves and then I will ask you if you put live. Can you put the links? So I put projects, you put the links and I updated everything for six months and at least you have a control of it. Filo, how is your house?  
Me: It's going to be an interesting summer. Let's put it like this.  
Them: Summer? But you also, you have already signed the contract, the promise contract.  
Me: Yeah, no, no, no, no, no, no. But so the first part of the summer is going to be about signing contracts and mortgages and banks and lows and all of that. The second part of the summer is about dealing with the constructor company that comes in and.  
Them: Okay. Okay. Okay. Okay. Okay. Okay. Now I totally understood.  
Me: Yes.  
Them: Good luck.  
Me: Yes. Thank you. Thank you. Everyone says exactly that great. You have a new house. Good luck. Yes.  
Them: Well, in two years, you will be better.  
Me: We are very. Optimist. Because we think about Christmas. Christmas is going to be in the new house.  
Them: It's a, it's a big reformation or just.  
Me: No,  
Them: Like painting and that's it.  
Me: It's something more than that. Because if it was painting, put down a wall, build a couple of new worlds, renew all the floors.  
Them: You're putting down walls.  
Me: Put down all the furniture, redo two bathrooms. Yeah, it's going to take a while.  
Them: No, but Christmas is not crazy. But do not be savvy if you are there for, for holy week of the next year. It's, it's a kind of expectations. You need to push for Christmas, you need to expect for that today.  
Me: Yes. Exactly. Exactly, exactly. Oh man, how's it going David?  
Them: Okay. It's been fun. I, I was in a, in a, in a, in a within this weekend. One of my friends was in, got married.  
Me: Oh, nice.  
Them: So it was a very nice weekend. We went to Madrid, going party. Also yesterday I was like kind of, I'll do, I, I did my IRAs. So everything is more or less okay. Well, read the iris, the, the carna, the rent, the taxes. I did my taxes, so now I need to go to the contab list in order to check everything because I am kind of this kind of magnetic person that I'm afraid of the IRS. So I prefer to go to a Portuguese. Again. I've been living here for 10 years, but I prefer to go to an accountant to check everything before sending it. But yesterday was like, okay, two hours of my life. Filling all the gas because, again, these kind of things that account you need.  
Me: Yes.  
Them: Filippo, let's go with the agenda.  
Me: Yes. Let's do it. So first point typey and chat AI, I know that we've been closing it. I've also talked to product. So they are doing their part in that.  
Them: Nice.  
Me: And also when I mentioned that they come back to me and say, what about goya mirage?  
Them: Okay, but, but do we have a, do we have something ticket, something that we, we can catch here or just the, the, the word that was Antonio and.  
Me: It's just a word for now. It's just a word what they are doing on their end is to check all the accounts that they have open for this application and they are closing them. I'm going to meet both of them tomorrow. I'm going to ask for an update and probably I'm going to put down some dates to have some clear picture of this.  
Them: Okay. Thank you. I'm going to rewrite this for the next meeting because I would like, I would like to be sure that we close everything and we don't have this kind of backdoors open. Okay.  
Me: Absolutely. Good idea.  
Them: Regarding gojan miras, I don't know. What did it tell you?  
Me: No, no, great idea. What about these other two apps? Goya Mirage that we have. Are we benching them? Are we killing them? Are we closing them? Because today they're still alive. And there is some spending there.  
Them: I don't know. I don't have info. Do you want it? So did they say something to you or not?  
Me: Nothing specific. It was more a question what do we want to do with this?  
Them: I would. Point. I don't have data. What do I want to do? I would like to close them since they are not doing a lot of money. But they don't know if they are doing any. How can we know if they are making money Revenue cut?  
Me: I haven't got this the only way.  
Them: Do you have access?  
Me: Yeah?  
Them: Let me.  
Me: So goya, goya, goya, go.  
Them: Show they have access. Should we still have this, this, this, these actors that is for all the people, or if you can share your screen.  
Me: Yes this morning. They activated my personal account. I still have to activate it myself. So after that I will. Do it. Okay, this is goya. 3k. Monthly.  
Them: Is welcome. The thing is how, and we are spending less than 3K. Let me open the expensive. And expensive sheet is goya. We are spending 25.  
Me: Let's keep it.  
Them: The maths are there for me. Let's keep it. And mirage.  
Me: Mirage. 8k. Okay. Problem solved.  
Them: Accounts. So again, for me. They are paying accounts. We are not running into a big travel with them. I prefer to keep them if you don't mind.  
Me: Yeah? Absolutely no no I never checked the data but with these numbers. We're spending we are getting much less for apps that we are maintaining today.  
Them: So m a.  
Me: This is the core of this discussion because every week I come to you with a bit more information regarding this. First what I'm doing is every week I'm taking one of the application and I'm doing some sort of security review. And in general it's more like a scorecard is the code base good bad what's state blah blah blah blah. Two weeks ago chat ultra the reality of things is that the code is good for the upside. You can clearly see a point in time where connecttino stopped working on that app and yeah.  
Them: Sadly. Yeah.  
Me: The app itself it's okay. The guys are maintaining it not great but chat ultra is okay so nothing to worry about also there is a product they are preparing roadmap so we can put certain resources on top so good. But this week I open pdf editor and I uncover a big big mess. Big mess because we are leaking two API keys inside the application which is bad. But worst of all for me is a gdpr breach that we have. And it's a big bridge because what's happening is long story short. The user can preview their documents like the docs, the excel etc from the app. But the app doesn't preview them locally they upload it to a public repository. And then from there they get a URL that is displayed in out from a web page which means that the documents are in a public repository my personal document my ID my taxes everything are in a public space that everyone can access that. Which.  
Them: What kind of public?  
Me: Is if you have a URL or if you know how to find this URL.  
Them: That is open?  
Me: No it's not fire store it's not far so it's a third party tool that we are using don't ask why they are doing this and it's a big big flag we are against gdpr in three or five points. It's very bad.  
Them: Okay, so have you informed the product?  
Me: Product stop releases and I told them this is not about only stopping or hiding the features is about fixing this as soon as possible meaning that they can we need to rotate api keys and we need to solve the gdpr issue.  
Them: Okay.  
Me: To make you aware of the situation there but product we saw in this team know about this. Nice.  
Them: This is what it is. So we need to change them. We need. Okay.  
Me: David Q2 exploration Q3 start to work on a plan. But on the plus side I had a great conversation with Rezo last week we have a weekly one-to-one me and him it presents me his plans he talked to Christian shows me his vision and for the future we have a good plan. Which is we want to build ups internally we are going to start to work on an internal. Library of components because on the product side they start to think in that direction so if they want to work on a design system as well so we can start to work even though we don't have any new app we can start to work on these components so that we are going to be ready to build faster so very happy about that.  
Them: Nice.  
Me: So the the future is bright but we need to deal with the present.  
Them: The body is the present. The good is the future. The ugly is there is the same.  
Me: So yeah I'm going to try to find the solution here but I told whether the situation is not good this guy literally they have no idea what they are doing.  
Them: Just to provide an example. Last week we saved one resource on the website. On the upside. That, one of the guys that was leaving, he was moved to video app because Andre required.  
Me: Yeah was my idea yes.  
Them: So. The thing is, if you would like to send people to there. I am open to it.  
Me: I'm working on a plan.  
Them: Okay.  
Me: But I don't want to start to give away for free resources if there is no reason to do it.  
Them: Start to give away resources. What do you mean? The money resources or the other resources?  
Me: Now if I start to say okay we can hire externals we can put externals on top of m a apps for free. It's not going to solve one of the issues that we have today which is we keep a live applications that don't have any reasons to exist.  
Them: For example, it's not black and white. It's like maybe you would like to save chate.  
Me: Correct.  
Them: Because we do know that in the, in this case. So if you would like to go. Kind of faster, if you would like to do something during June. With this app or another one, we can do it. Okay. So we don't need to wait until the start of Q3 or it doesn't mean that at the beginning of July we can do all the changes now. So, so if you will see something that, that we can do in June. Regarding, for example, you will tell the ones that are providing more money. Let's do it. Okay.  
Me: So the only one that is providing money is ultra the only thing I asked product is can you provide a roadmap so I know what kind of resources to put on top so for me as soon as I have a roadmap I can start to think about resource and I will request them to you. Yes so Christian want to launch a website version of truth seeker. Great idea. I don't have resources to put on top of this. Do we have web resources we can use?  
Them: Let's. Yes, we have. But let's rephrase this. I remember we saying we do have resources. The thing is, we don't, we need prioritization.  
Me: Okay.  
Them: Why do I say we do have resources? We have all the money people. Maybe they are not the best, but they are resources.  
Me: M a.  
Them: Yeah. I do. Let me do first of all, let me read the book and then we phrase the reality. Okay. But are there resources? For sure. Yeah. We have the money resources. We can try it. We don't think that is good idea, but they are, they are there. Also, you do have two suburb Engineers which are lab and Andre. Both of them can be as, can be attached to this project. It's a website check this, this decision. So that is not a matter of resources. It's a matter of political matter. We need the prioritization correctly of this website.  
Me: But would like to have one of my software engineers but they are not free they are busy with other projects.  
Them: So actually needs to speak with weo in order to say, okay, we are going to maybe. So we, we can do this. Also, we have, and, and now, yes, we can have a web resource and we need to align the gal in this. Okay. But it's important to, to also, in the same way that you, you mentioned, I don't want to put the external resources because I, I like them to provide me roadmap is also to have this conversation with self and say also we don't have the external resources that we have attached to the apps. We have an external resolution office AI, we have listed resources of the tools, we have the step research. That then we need to check. Prioritization or roadmap plus in the skiffs of the people. Okay. The other day, if you would like to ask for web resources, I do have people on the web teams that I can move. We need to have this alignment. We will, we will take between 15 days and one month in order to move the people. And this people is not like durvan. Okay. We might need to go closer to them in order to the, the training in order to release websites, which I believe that is going to be open to if we would like to do it, okay, as well as we did with youl and we have done with other developers that we have here. So. What framework do you prefer?  
Me: Explain a bit better so we have internal web resources. That could work on this specific project or in general.  
Them: I have a bunch of what. So I don't know if you, if you know how many people do we have on the website. But on the website we have. Too much people. So in QR, we have this, the blues are front ends and the other color is, is backends in CV the same. And in real we have a crazy amount of sheet of people. Okay. I myself are working on this because also in the PDF side, for example, we have a lot of sources and running inside, we have a lot of other sources. So step by step, we are doing the same as we are doing in apps. We are reducing the external teams in order to move the internal teams as they are learning more regularly in artificial intelligence. But also. I can ask Twitter. Hey, I need one guy because he knows that he has a lot of people and I'm kind of solving myself a problem regarding that providing people the value what they are going to. So if you want. I can make a movement of one of the web resources to your team and it will be permanent to keep it forever and you have one resource more with you as whatever you want or it can be temporary. I offer this also to buy a catalog.  
Me: This is very good. And just to understand are these people only skilled on websites or also backend?  
Them: There are only. Thick.  
Me: All Leadtech what do you mean?  
Them: All Leadtech, they were backend developer. Web developer, I believe they are very attached to a technology. There are people that need investment. But this, these people that I would like to invest on their investment, they are doing investment on the website. So their teams are working with them, but they are always cool. You haven't been with a lot of contact with all Leadtech. These people, it's people that has been on the company for three to five or more years. These people is people that has been, like, comfortable in the company with a kind of salary that it's okay based on the previous written of Leadtech. And there is a lot of frustration in few of them. There are projects where people have better, better scores than the others. Also, you can say that on forwards if you want. Okay. Here is or the people that right now have on my mind. For example, I can put you example. This guy, Victor solar, robin is, is doing a lot of changes in PDF and he's more comfortable working with a glance that we him. The, the Leadtech side would like to have him without any kind of issue. Also, it likes heat and he do have any kind of issue moving to another project. So for me, this is a good candidate in order to move front end developer. I don't know if you would like to check with him. Also on the QR website. We have people idea here. And please keep this information with you because it's a risky information. Okay. The idea here is to reduce two to three developers, moving them to a chat or maybe to PDF, too. In the same way, I can take one. But here we need to align the lines. Okay. Because I can ask for the resource. It's not going to be for tomorrow. It's something that can happen during June if I align with it. Or.  
Me: Thank you for for this. It's a very interesting.  
Them: Maybe there's nothing that I need to comment on Thursday with all of you because I spoke with this regarding catalan spoke with you also to private visibility.  
Me: It will cover a gap that I have in my team today. Having someone like this but as you are mentioning these people are not durban no no one is dual band come on.  
Them: Now, but they are not like UL or maybe. I don't know if they are like youl, the guy that is currently the web iOS developer that has been wind durban. With. They are not people. They are. I believe that they got, they would like to change and if they are put, if we put them in a good environment, they are going to play the ball very well. But the thing is. We are going to face when these kind of things is like you would like to have the, the challenge and then we will need to have the uncomfortable meeting because you're going to do a kind of interview with an internal resource. So it's something that we also need to check with him or with hair on the other side, this change who is going to be open. I don't know. There are several things. So you have this option if you want also for sure, you can go with black and Ray. And this is a discussion with the webinar prioritization.  
Me: Okay let's select this let me think a bit about it pros and cons of this challenge because it can be a challenge and I'll come back to you but thank you very good idea okay nice.  
Them: Nice. Another point regarding M new purchase updated. Today we have a meeting in the committee and I ask regarding the two purchases that are closer in the social network or the social one of Alex and the style. Okay. Regarding the social one, the idea here is to hire to Alex, but not to purchase the app.  
Me: Okay.  
Them: So it's a good point. We part we hired and approved my manager that is nice. We have put it in one team. I don't know where we will then. We put developers by the thing is we, we do not need to do any kind of integration. He's open to come back to Spain. So it's nice. No issue in our site. It was nice. The garden style. We like it right now. They are going to open the conversation with januka, which is the CFO of the group in order to do the deal. If it runs well, the idea is to do due diligence. Like, because this is aperture, not all the app we are purchasing the, I don't have to say the company, but at least the app. So it's a package with the whole people. So I made asks more meetings with them in order to say, guys, we need to open up the box. You need to do an inventory. You need to do everything. So put with more details to know what we are purchasing.  
Me: The team.  
Them: And that's it. But it's looking well. That's it. And I believe that it's nice.  
Me: My impression of the guy is very very very skilled they believe in the product I like them so yeah for me it's it's a good move economically speaking I have no no visibility.  
Them: They were talking about. 2000 case. 200ks. Which is a very good price.  
Me: Okay. It is.  
Them: For everything. The thing is, then we need to maintain their salaries, which is around 2K 2200 case also per year. So again, we are.  
Me: How many people.  
Them: This mic. Well, I don't know if I can share with you, so I never ask. I never asked answer you this question. Already because then we are doing with due diligence and all these kind of things. But they are eight people.  
Me: Okay okay. Yeah okay.  
Them: So bitto, which is the product manager that we met, Alessandro. No, we don't know. Giacomo, the technique AI. We also know him. Alessandro. He was also on the call. Daniel d, which was the, the, the front end developer and haniska. It was so agree that we met all of them. They are to that to that engineered in terms of, I don't know, I don't have the names. These are more or less a total cost of. 200,000 per year.  
Me: 200,000. Yes.  
Them: But I believe that this is just salaries, not the total cost. This is really, I prefer to purchase this like another helicano. So.  
Me: But big time. Big time if you need me I mean I'm in Milan I can meet them in person if that's the case during the due diligence anything.  
Them: Good point. I don't know. So first of all, Liz and Luca and the money talks. And then after me talk, we will go with more details that it needs. Okay.  
Me: Okay sounds great. Nice.  
Them: Andrea tokens.  
Me: Yes so very interesting conversation from Andre so Andre as you know. Has been always pushing for AI things today what is he doing? To give you visibility from a product perspective. Screen mirroring is working on the famous library and. Is using AI to help him debug all the issues that we have with connectivity to all the different TVs. This is. These apps never worked before that's the reality of things and now Andre is making them work.  
Them: Weird. O.  
Me: So these are very very.  
Them: Now we need to see if we are making more money because this is a fun fact.  
Me: Hard. Correct but that's a fun that's an interesting part for me so he has been using a lot of tokens for this kind of things. Is using very smart models. Because it requires a lot of thinking. On the other end is also working on iMode. There is another conversation regarding iMode but let's skip it but in there is not using smart models because the changes are very minimal so is using this kind of thinking on how to use them. Is buying his own subscription for chat GPT. And yes let me explain.  
Them: But, but let's go with, with cars or he can burn the tokens that he want.  
Me: David it will burn the token and already did in three days. We did.  
Them: The normal plan plus in the 350.  
Me: Yes so we did a simple math of the 200 the $200 of his personal chat GPT account. And the amount of token that is spent this month. Is an equivalent in token of 3500 dollars.  
Them: This is the conversation of the market. This is why Microsoft ran out of cloud and all these kind of things.  
Me: Yes. Yes. So and and it was open about this so it's not that Andre is no no it's very open about this it's like. Okay I could burn through all this roadmap we were looking at iMode in a week. But that means I need way more tokens. This is the conversation this is for me very interesting.  
Them: I don't, I don't have the answer. And this is the interesting conversation.  
Me: No no. There is no answer here but it's more like okay I have a guy that is actually doing a lot of work but this is the spending.  
Them: It's.  
Me: 3500 dollars in tokens. And is working on two apps and this providing value is the company willing to keep going this way add more are less it's not about Andre is a general conversation this.  
Them: Also a general conversation. The problem here is the scale. Okay. Because last month we spent on top of all the courses expanding. So we have a budget in cursor and then we go 3,000 more 3,000 3,000 more on top of that. So we are checking that we are, we are, this is why cursor was fixed. This is one last week on the people. I still have money until, but we reached there because there is a common pool. And we reach the limit. And, and every time that we talk with a new company, also with kilo, what is happening nowadays in kilo is like, okay, we are going to agreement and we said that and suddenly there is a common pool. And we said, no, no, no, no, no, no, no. We want developer pool. So we know, we do know in which developer we are topping up. And they said, yeah, you know, we, we discard this. There are more three pools for, for the whole companies. Like guys. So all the, they know because if they put a common pole, you are, you're going to have the greedy person. And because it's the money of every, of everyone. So I don't know. So, so, so. And I also ask, and why don't we go with individual license for all of them? And there are also cons. So the currencies are that we are having discounts in order to go with the group. We don't have any kind of control when we go with individual license. So, so, so we are right now we are still answering this question. The point here is. In order to have a business case, we need to know if it is worth it or not. You need to know how much money are you doing by those features. And this is impossible nowadays. So we can face it in the approach of it is an expanding of this project. And the project has enough p l to cover this. Yes, we have. The point here is how can do it this at scale? And what the issue with the scale? And there is one in that we have few people. But in the website they have, as you saw. A lot of people. So. I don't, I don't have an answer. This is something that we are trying to discover. But thank you very much. I think you see fan base having his own license. We need to open a license for heat. We need to ask for a cloud license of a chip GPT license inside of the company. He's not going to pay by himself. Come on.  
Me: I'm giving you visibility on what's happening because you need the information.  
Them: Ask for him for it. What does he like more? What does he like more? The chat GPT or the.  
Me: I yes yeah it uses codex chat BT yes.  
Them: So open a ticket in order to ask for a license for him and I will approve it.  
Me: A personal license.  
Them: And.  
Me: That's a problem. Personal license are $200.  
Them: There are the personal answers here. There are a lot of all the people is asking for his personal license of cloud. They are, they are dealing with the cloud person, not personals. It's like the company is paying for a license for this person. So he can ask for it right now. We are writing the web writing a governance document where we say it. We are going to have the tools for developers and then each department is going to have one cloud, one GPT in order to have a common access.  
Me: Okay.  
Them: Also, I can create mine. I can employ him the access. Okay, let me do one thing. Let me ask, how can I ask for the, the department license of chat GPT.  
Me: But my question is is this. Both as a personal license because in that one with $200 you have tons of tokens if it's a.  
Them: That is the point. It's if I, I need to check.  
Me: Company.  
Them: So. I'm going to check this with our phone. So I would like to request the common license of chat GPT for my team. Since I can do it. F I ask for this. What kind of this is a, it's a max plan of chat GPT. Yes. How can I share this with the people? So something that is going to be important. Yeah. So I take it, I bring you the keys and, and they can go inside and burn all the tokens. At least we provide. We need to solve this issue of Andreo. Thank you very much. First of all, thank you very much to Andre. We are grateful for having him. But then now we need to, to do something, or at least to try to do something.  
Me: Son okay.  
Them: Okay.  
Me: Yes I'm providing as much visibility as possible because I know it's hard.  
Them: Thank you very much. So, like, I tried to do something else on my side in order to bring more tools to Andre. Okay. Probably 10 roadmaps.  
Me: Which brings us to the next question which is so this morning Andrea is like yeah I've done I've done this this and this and that also done the MVP and all of that for product there is a problem I'm burning through all my tokens and I okay Andre so let's look at this roadmap first of all what is providing actual value. So that blue line. It's 90% 50 50% done already in two days.  
Them: So estimation. Not the best, but okay. I can live with this. I'm happy also.  
Me: It's an estimation done. With the information that I receive we receive from product.  
Them: It's okay.  
Me: Yeah I know I know I know what you mean. But then. The conversation goes back to product okay we provided the MVP what do you want to do with this? There is no plan there is no roadmap is let's keep the developers busy. So on one end a guy burning tokens. To do busy work that is not providing value so I was okay Herman which is the pill. Is this providing value I need to know you you shouldn't come to me asking what should we do with this MVP you asked for it do something with it you know so we are spending money to create this but you probably need to provide the value we cannot decide for you.  
Them: What does David m to say?  
Me: I haven't talked to him yet.  
Them: Is the. Guy?  
Me: Right I will talk to him.  
Them: Because when, so, so there is a good and bad thing regarding of our problem. Yes. Our broad managers are business, not product. See what it is. At least he's someone on the vertical that is taking care of the money. So, David. And I know because he's doing like websites in, in another app. So in qw, he was doing website. Let's start doing websites. Place the value of iMode. And just play the whole story. I have a guide which is burning tokens. It's a little bit faster. At the end of the day, we are not providing value. Do we have a business case in order to invest all these tokens? Plus the salaries plus everything on top of this? Pro manages are the keys. At least from my point of view, because they are the, the, the content money. So it's the same in Android.  
Me: Now Android not yet Android we have an external that is but even here yeah the rest of the roadmap should come today. I need to find a way to control the resources. Let me explain a bit better. Today. We give the resources give the resources to product they feel the time of the resource without any reasoning.  
Them: Do you know.  
Me: Yes yes yes yes that one yes yes.  
Them: So this is the issue. We have an orientation and the proof that we have is the reflector organization. And since we have developers there, product is filling with stupid features.  
Me: I could use this developer that I have in iMode Android for other things I have plenty of work for him.  
Them: Whether you want to put him.  
Me: It doesn't matter today where I want to put him.  
Them: No, but, but I have seen in several companies and every time that they ask with people, it's kind of the same product.  
Me: But.  
Them: I think he had is the incentive of products are not correct. The incentives of the product guys that I would like to survive. I would like to have my team. I don't care whatever. So the product manager is not the product owner is not going to say never, never, never. You can put the resources away. Because if the problem manager doesn't have the resource, he's going to say, okay, and now. What I'm doing. Manager has a kind of better incentive. In this case, why, why I'm thinking this and I don't know if it is going to work and this is, this is why I'm asking you to talk with the, with the other guys. The point open is David martos is with qi and i. Rthos is just over here. But you can say trade martyr in the same way. Maybe we can help on QR with this resource. Because David, you have a pool of people. So here there is a market here. There is survival. No, sorry. Here there are survival. Well, kind of. Because also her bank, we are is in both of them. But David Marto must have the business vision. So David or, or we are more money here. I think it's the money that we are now relevant. It's the money of the developer. But we have fast in other places. Or if you would like to have CD2 guys, is David, we don't have any kind of problem with martos. I am going to take the resource out and I'm going to put this developer outside here. Because it's not worth it for me and I'm going to ask to the sponsorship of Matellan. O. So you have this, this, this, this, these buttons in order to press. This, this is what I've done with Christian. Christian. I don't see roadmap. I'm going to take one resource and you have seen it during the time. Thing is every time that I do it, I don't have the same visibility that you have. So the thing is, if you would like to face this, my recommendation is to, to with her man, talk with David martos. If not, I go. If you don't want to talk, I can do it by myself. But the best approach for me talk with David martos, because this is the way that we scale up.  
Me: Yeah. Yeah I don't want you to get involved yet for me it's just a beginning first conversation but I want the conversation to move in that direction we have a pool of resources we move them based on the needs not just to fill their time.  
Them: This is a good point moving into families approach. Right now we have developers per app and you have your applications and the conversation against product is hard. And you are, you are restricted to the product owners. Since we are moving in a way that you are better positioned regarding the product managers because you are with launches with software wash and you know the resources of Filippo was and you are with the market in this case, you need to share with David. But I'm what is going to be with David catalytic in the future. So the idea here is you got to do this pretty well with serverless. We are having a stupid situation here because we have the resources. I know that you haven't, you know that we haven't and we are not doing any best approach. The idea is to put this conversation with the other verticals. The thing is. Right now with I mode there is this special case. Because we need to move it to growth. Maybe it's a competition that we need to postpone. And I leave this up to you. Because there is nothing we can use the resource in order to put better eye mode to deliver it better to the big catala. So you don't need to do it if you don't have the space needed if you want with with the vertical martos. But you need to do it in launches and money.  
Me: I have more control there for the reason you just explained and there's something we already started.  
Them: But this is why we are moving the teams and this is why the change that we have been and never is going to fit 100%. But in this case, if you would like to wait, it's okay. At least.  
Me: The toyst is in good shape we are implementing what's the name parapet AI design we are implementing parapet.  
Them: Regarding roadmap. The roadmaps are healthy. Screen mirroring.  
Me: Screen we are slow but we are okay. This is a mess it's a very bad mess it's not reflected on.  
Them: It doesn't look like my mess.  
Me: This.  
Them: It doesn't.  
Me: The way the fact that we have a roadmap doesn't mean we have a good team. The PO has been removed is still there annoying the people it's a very tough conversation but unhandling that.  
Them: Happen with this guy. I'm curious.  
Me: It's the usual you call it survival. But for me it's when when you start to blame the other teams for your inability to do your job I get really upset. So unhandling that part of the conversation.  
Them: But if you went to live or not.  
Me: He will be living at the end of the week. Leave the team the team.  
Them: Is going to be.  
Me: Is in m a.  
Them: Okay. What? Did you said to YouTube? Who was to put this guy out of the company and I do know that right now is not the problem because of the union.  
Me: It's no easy it's not easy conversation but I will.  
Them: If you, I, I don't have any kind of troubles. What is happening with this guy?  
Me: No don't worry I'll handle it on my end and if I see the conversation I'll involve you but yeah.  
Them: Because this has happened with Carlos. The mas converting into the thrust of the product.  
Me: Great.  
Them: And they are putting there the resources that are not working well in any place. And I'm living okay until the end of the junior, whatever, whatever. The thing is, I would like to someone said in private guys, we have this in Q3 will resolve. If it is happening, I will do not ask more.  
Me: I'm going to drop a bomb that we're going carlos and the face AIPO are working together on the PDF editor. App.  
Them: Do you want to speak with Christian regarding these two guys?  
Me: It's okay I'm just entering the project so I want to see how things are moving.  
Them: No, but the thing is you're entering the project, but I do have the background of carlos and you have the background of this guy. And since they have been moved to m a doesn't mean that they have a clear paper. No, no, they have their past, they have their backlog on their shoulders. So I don't want to repeat the same issue. If you want, I can speak with Christian. Please, can you provide me while regarding these two people because they have been, we have facing issues with them and I do know that we can remove anything because the union, we need to waive at least. I would like to know what they are going to in Q3.  
Me: Give me a couple weeks.  
Them: Okay.  
Me: Let me do the proper process from my level and grow up.  
Them: Okay. Regarding the pros and road map, I am asking also the, the, the data boards in order to check if everything is on jira and if everything is on dealer, we don't need to update the document or I don't know if we will need to delete the document. So this is why I'm asking there. So is the same having different tabs or having one gita after one jira, which are going to make our life easier because it's just one document.  
Me: Yeah.  
Them: Field.  
Me: So how I work with my product people is we go to jira we check the timeline there and then we report it in the spreadsheet that you check.  
Them: That is the point. Maria here is to remove your destruction to the spreadsheet. Okay, this is why I'm going to ask for links monthly metrics of the forward, whatever. So. Metrics of forward. Let me check people on your side that is under seven.  
Me: There's only one which is.  
Them: These guys.  
Me: Exactly. The vid I don't know what to say regarding forward because this guy is doing good work is producing PRs it's producing code.  
Them: Okay. On your side, nothing else. No, this guy. This is sign up, I believe. Yeah. China apps.  
Me: Not mine.  
Them: And this is.  
Me: Not mine.  
Them: I don't know. Okay. So. North question. I have a curiosity question on my side. Which is the following. Asking for feedback, not on whatever. Her man, the PO, one of the POs on your side is called herman. It was kind of stupid, but it's okay. So. He provided feedback and everything. Everything is, it's, it's, it's, it's stupid layer on top of a stupid player. So her man informed to have in the retros one per month instead of every 15 days.  
Me: Okay.  
Them: Which I say, okay, if we need to, if, if I need to check these kind of things on my side, this means that the north is too much strong. So, guys, I don't care if you would like to do every 15 days or one month. It's all right. So, so if you Filippo previously, it's okay. No issues on, on regarding norm. The other way around is. But launches is kind of a wild west. So having 15 days retro, it's kind of all right. So did you receive also this feedback? Is everything also right?  
Me: Wait wait. Wait wait wait. It launches north is implemented pretty well we have retros every 15 days.  
Them: I know, I know. The thing is, my question here is.  
Me: We.  
Them: Don't you have information enough since it's wild west launches and not, not regarding north is because lunch is okay because of probably plants. It's not because I was. So since lunches is lunches, as you mentioned, face AI, the guy that. We have enough material to talk about every, every, every Sprint.  
Me: Oh yes we are we are.  
Them: Okay. So, so we have enough material to talk every 15 days. So herman may be having a lot of meetings. I don't know. I'm trying to guess.  
Me: But her. Man David herman is in growth in iMode.  
Them: Apologize. I have asked to you because of iMode. So same question for iMode. So don't we have enough material every 15 days to talk with her mantra in what?  
Me: Considering. No because the guy that is going to be Andre and the android guy and there is no much to talk about.  
Them: So the thing is, if you would like to do 15 days. If you need an email which I say, okay, send me an email. I don't think that is required, but that's to provide. So North is flexible. Okay. So if you would like to do.  
Me: But this is the first time I hear this is this is something new to me what is this.  
Them: I know. Don't worry. Now, the thing is, if you remember, we are recollecting feedback regarding the north. In that is understanding of people is complaining and these kind of things. So one of the things that came to me from this, from carman and it was come through directly through David, because like we need to, to check this, the, this exception. I said, okay, what is exception? I need to set up the, the, the reading of the, of the review. In this group, we are not here to, to do this. Guys, if the people wants to do every 15 days, let's do them. If the people want to do every week, let's do them. If the people want to do it every month, I kind of. Okay, this is, this is under this responsibility for me. It's okay. Now what we need to prove the, the, the, the, the check and you have my check, but I don't want to lose time in this kind of position. But then I say, okay, but let me wait. Also, I would like to check. So the first thing, her mandate has to do. It's okay if he's just probably knew the feedback from the top down and it's completely normal. He's talking regarding his line report management. But again, the point here is if you see this kind of changes with a small, feel free to do them. Okay. If you would like to inform me, it's okay if you don't want from installs. Okay. The reviewers and these kind of things. Or, for example, if there is one week with, with no planning requirement, another week that we need to refinements, I leave this up to you. Okay.  
Me: I'm sorry. But. This is pretty. You know going to bother you for this thing hey this week we're not going to go with brand name.  
Them: No, but this is the fun fact. The fun fact, the fun fact is that you understand that they have not a race, something that you can keep between the team and that seat and it's completely normal. But suddenly it pop up on the, on the committee meeting when you need to check this and we have a conversation regarding having the, it's stupid. Okay. I say it's a stupid layer on top of stupid level. Do nothing regarding this. At least you, you can Vlog with me again. But if you see in the future that you need this kind of flexibility in Filippo, it's all right. Okay. The north, it shall be nice to have good year awards, good flows. But for these kind of things, if you would also recommend to put it to write down on the documentation is recommendable to have a read through every 15 days or at most one month. But again, there are things that still are, are kind of hard regarding the, the processes.  
Me: Because. Dav. Id it has happened in the past that we skipped one retro or not but the normal let's say that in general we follow the rules but then I'm not going to bother you with this the only point that I that we discuss me and you was about face AI because we were doing we are doing all this testing but that's normal I should come to you David the metrics for face AI are all gone.  
Them: But this is different. And, and what is the point? You understand correctly in the. Sorry, I, I had this conversation right now. The people is super sensitive regarding the union, and I wanted to check with you if everything is all right. So that's, that's Filippo. Martech is SDK. How is going?  
Me: Okay okay. Yes right it's live in phase AI the version one I mean the one with all the amplitude stuff we are going to release tattooist this week. And version one of the SDK is live itself so on my end I would say after we put live.twist and we get some data just to make sure that the data is okay. We are good to go. On my end I prepared an email I ran it through Victor because because yes.  
Them: Nice?  
Me: What I told Victor is. As of today I do not have this the capacity to create a proper presentation for this you know a big presentation with everyone involved so I was trying to understand from him how he wants to do this it could be purely technical.  
Them: For me, it's more feature. Feature. So what does include what, why is this helping your life? And that's it. If you would like to make a videos and then with the, with the email for me, it's all right. But let's also check what David Sanchez wants. He would like to do something big. That is the point. Try to do something. Okay. If it is a problem, let's, let's go with the video. Don't buy your ambitrant. That's it.  
Me: David sanch want to have her man castillo in in in the meeting you know.  
Them: Can I talk to him and say, David, let, let, let first start. If you want, I can talk to him to David. Sanctio. You're trying to do something huge for something that is nowadays. Small. Don't you want to do this with her man when you have all of them? Right now we just want to. Hook the pro side in order to, to, to speed up the development.  
Me: Exactly.  
Them: Do you want to speak with him?  
Me: Now let me do let me do the the usual process let me get this up out of it yeah yeah yeah yeah yeah.  
Them: But in a good way, I'm not telling the.  
Me: What I want to go to David Sanchez is hey I have an email we were thinking about creating a video to attach the email. What do you think see what it comes back with because one month ago when we talked about this he wanted to do a big presentation slow down we don't even have version one of this tool.  
Them: Having the good, the, the, the having herman on the call, but when we have all the applications.  
Me: I said herman it never asked for her mom by the way it was just me to shoot me yeah I know I know I know yeah so that is good what else let me share a couple of things regarding hiring we have two good candidates in the pipeline.  
Them: But he might. Have one interview on Thursday.  
Me: We'll let you.  
Them: Or Leadio video.  
Me: Very good guy really really nice that is the one third one just came out of the interview right now still go need to go through the second stage so let's see so I will keep these two they are very equal for now let's see how they go and then we take a decision Leadio is iOS focused these are the guy that interviewed today is Android focus very interesting let's see let's see.  
Them: This is what I said regarding the, the now you need to decide the, the flavors of your teams and again, think about also the web option. Okay. An important point, it's not a hurry. There will be web resources until the end of the year for sure. Right now, what we are working is we are going to keep up the people. We are going to provide trainings. We are going, we have a space enough in a chat plus PDF to move the people to one team to another. But also an opportunity to you, Andre and to David catello to say maybe I would like to strongify my team. But the point is you need to train this person also. So it is going to have, it needs to have more work on your side in the one on one and the manager approach.  
Me: Yeah it makes sense.  
Them: Which are related to is nice. It's not bad. This is work is better than others.  
Me: Yeah no it's. It it's it's an interesting challenge so nice let me let me think about it.  
Them: Perfecto, something that's on your side.  
Me: That's it for me.  
Them: So for my side. So if you don't mind, I'm going to leave because you have a meeting regarding Master card. I see that we have on web. I would like to prepare.  
Me: Thank you so much David have a great day.  
Them: Thank you very much. Bye bye. You too.  
Me: Bye bye. 