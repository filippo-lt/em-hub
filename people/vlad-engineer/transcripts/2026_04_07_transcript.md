Apr 7, 2026

## Vlad / Filippo \- Weekly 1:1

Invited [Filippo Tosetto](mailto:filippo.tosetto@leadtech.com) [Vladyslav Krut](mailto:vladyslav.krut@leadtech.com)

Attachments [Vlad / Filippo - Weekly 1:1](https://www.google.com/calendar/event?eid=M2Rjazdnczk1M2V0ODVtOWo0cWwyOHBtMHJfMjAyNjA0MDZUMTIwMDAwWiBmaWxpcHBvLnRvc2V0dG9AbGVhZHRlY2guY29t) [Vlad / Filippo - 1to1](https://docs.google.com/document/d/1YDkXYSVCzPasVeyozvrdZ6jLWEEXjlOdggOTsQynhgQ/edit?tab=t.0) 

Meeting records [Transcript](?tab=t.80ne6ma3e9cn) 

### Summary

Initial personal updates and a review of CI/Periphery integration led to a discussion regarding workflow improvements and future feature delivery goals.

**Discussed CI/Periphery Integration**  
CI/Periphery integration required about 30 iterations due to unhelpful AI configuration settings but successfully added a 2-step approval process for PRs. The decision was made to rewrite the current CI flow from scratch to eliminate redundant build jobs and improve caching.

**Planning Feature Delivery Workflow**  
The next phase of work is split between delivering new features and adding unit tests, with priority on feature tickets to reduce context switching. The long-term goal is for the developer to manage 2 applications, Face AI and AI Design, by the end of May.

**Refining UI Development Strategy**  
The goal for the week is to deliver 3 UI-focused user stories and refine the UI feature development workflow for increased proficiency next week. It was agreed that design references, such as Figma screenshots, should be stored in the repository to act as a source of truth for both humans and AI.

### Details

* **Personal Update and Car Accident**: Vladyslav Krut shared that they were in a car accident over the weekend, confirming that only the vehicles were damaged and all people involved were unharmed. They described the ensuing difficulty dealing with the insurance company, which only provided support in Spanish, limiting their ability to communicate effectively despite having an expensive car insurance policy for expatriates ([00:00:00](?tab=t.80ne6ma3e9cn#heading=h.eko4tknxynqn)) ([00:03:44](?tab=t.80ne6ma3e9cn#heading=h.v2alp7co6xdb)). Filippo Tosetto expressed sympathy and noted that the slow and painful insurance process is due to significant economic interests involved ([00:02:23](?tab=t.80ne6ma3e9cn#heading=h.byafhyyv1r3t)).

* **Insurance and Driving License Challenges**: The discussion covered the cost of car insurance, which is mandatory, and the perceived inefficiency of some policies that cover little, despite high annual costs for Vladyslav Krut ([00:03:44](?tab=t.80ne6ma3e9cn#heading=h.v2alp7co6xdb)). They also noted that their Ukrainian driver's license has expired, and while legally usable until they receive their Spanish residency status, it prevents them from renting cars, meaning they will eventually need to attend driving school in Spain ([00:04:54](?tab=t.80ne6ma3e9cn#heading=h.pvw9ch1dhoxh)).

* **Long Weekend Summary**: Aside from the car accident inconvenience, Vladyslav Krut reported having a nice and relaxing long weekend where they met friends and celebrated Easter, which they may celebrate twice due to the different dates in Ukraine. Filippo Tosetto also had a pleasant weekend, spending time outdoors with their dogs, while Vladyslav Krut's dog briefly stole a piece of Pasco bread ([00:06:03](?tab=t.80ne6ma3e9cn#heading=h.orqfx5nrpubh)).

* **Review of Last Week's CI/Periphery Integration**: Vladyslav Krut summarized their work from the previous week, noting they completed the planned tasks, including periphery integration that required late-night Continuous Integration (CI) work. They explained that the process involved about 30 iterations because the AI was unhelpful with the configuration settings, though they successfully added a two-step approval process for Pull Requests (PRs) ([00:08:43](?tab=t.80ne6ma3e9cn#heading=h.2xiuge9ibqh3)).

* **Proposed CI Workflow Improvements**: Vladyslav Krut expressed concerns about the current CI flow, particularly the redundancy of having two separate build jobs (PR required and PR optional) that do not reuse caches. They indicated that they might delete the second build job and completely rewrite the CI flow from scratch, which Filippo Tosetto encouraged them to do, noting that they have the autonomy to change the current system ([00:09:46](?tab=t.80ne6ma3e9cn#heading=h.yplm468ea5tb)).

* **Next Phase: Feature Delivery and Unit Tests**: With the initial integration phase complete, the agreed-upon plan is for Vladyslav Krut to begin part-time work on delivering new features and part-time coverage of existing flows with unit tests and specifications ([00:11:04](?tab=t.80ne6ma3e9cn#heading=h.dfzgu4es2asf)). Vladyslav Krut intends to prioritize working on tickets first and use leftover time for writing tests, believing that splitting time 50/50 would cause too much context switching ([00:18:41](?tab=t.80ne6ma3e9cn#heading=h.ehdblqh7pz5l)).

* **Challenges with UI Feature Delivery**: Filippo Tosetto expressed curiosity about Vladyslav Krut's feature delivery results, specifically noting that their own experiments with AI workflows for UI work have not yielded positive outcomes, unlike for business logic features. Vladyslav Krut noted that current user stories, often based on the "Norse project format," are difficult for AI to process, suggesting that manually feeding design screenshots from Figma would be a faster way to work than spending weeks preparing detailed user stories ([00:13:24](?tab=t.80ne6ma3e9cn#heading=h.6jdl8lyv8pka)).

* **Workflow Goal: Sustaining Two Applications**: Filippo Tosetto established a clear long-term goal for Vladyslav Krut to take over the development of Face AI and eventually an additional app, AI Design, by the end of May ([00:16:12](?tab=t.80ne6ma3e9cn#heading=h.3g8bv6fxrmm1)). They proposed a workflow iteration where Vladyslav Krut uses a single Jira epic to generate their own user stories and specifications with AI, thereby eliminating the need for extensive product team scaffolding ([00:17:25](?tab=t.80ne6ma3e9cn#heading=h.txoig1cjspjd)).

* **Week's Goal: Feature Delivery and Workflow Refinement**: To start the new phase, Filippo Tosetto directed Vladyslav Krut to deliver three UI-focused user stories from the editor screen epic and concurrently refine the workflow for developing UI features. The expectation is that by taking time this week to refine the workflow while delivering features, Vladyslav Krut will be able to work much more proficiently starting next week ([00:25:41](?tab=t.80ne6ma3e9cn#heading=h.urqkhg1mg30f)) ([00:31:44](?tab=t.80ne6ma3e9cn#heading=h.ban86vcagnx8)).

* **Proposal for Storing Design References in Repository**: To address the frequent problem of design-to-implementation mismatch, Vladyslav Krut proposed storing Figma screenshots or other visual references locally in the repository to act as a source of truth for both humans and AI ([00:33:01](?tab=t.80ne6ma3e9cn#heading=h.9nxjjeevk0x6)). Filippo Tosetto agreed that this is a good idea that complements feature-based development and helps maintain a history of design changes ([00:34:32](?tab=t.80ne6ma3e9cn#heading=h.bfxdfm4dj9yx)).

* **Future Workflow Focus on Specifications**: The participants agreed that for future new features, they should start by defining clear specifications before implementation ([00:30:35](?tab=t.80ne6ma3e9cn#heading=h.ivc615kq41v6)). Vladyslav Krut stressed that the current focus should be on building a source of truth and exploring the UI development workflow, possibly trusting the AI to build the view completely unless logic changes, rather than covering existing flows with specs ([00:27:49](?tab=t.80ne6ma3e9cn#heading=h.awe76by3s2rq)) ([00:31:44](?tab=t.80ne6ma3e9cn#heading=h.ban86vcagnx8)).

* **Roadmap Overview and Alignment**: Filippo Tosetto provided Vladyslav Krut with an overview of the company's 3-month roadmap, emphasizing that this document gives C-level visibility into delivery commitments and allows for capacity planning ([00:39:27](?tab=t.80ne6ma3e9cn#heading=h.bsby75rr37ai)) ([00:44:29](?tab=t.80ne6ma3e9cn#heading=h.fge41up5qbvl)). Vladyslav Krut was asked to be the "eyes and ears" on the Face AI team to provide early warnings if expected delivery dates, such as the library redesign, are at risk of delay ([00:43:16](?tab=t.80ne6ma3e9cn#heading=h.2v1frw8lsa5u)).

* **Roadmap and Future Role Planning**: The roadmap visibility is intended to allow Vladyslav Krut to plan their work effectively, especially as they transition to covering the work of two developers by the end of May. Filippo Tosetto explained that delivering according to the existing roadmap expectations will be a key achievement for Vladyslav Krut in their increasing responsibility, providing a benchmark for success ([00:45:46](?tab=t.80ne6ma3e9cn#heading=h.xb6h8l8wlanh)).

### Suggested next steps

- [ ] \[Vladyslav Krut\] Coordinate Sprint Stories: Talk to Anton about delivering 3 specific user stories for the editor screen and 2 modules during this sprint.

- [ ] \[Vladyslav Krut\] Implement Figma Storage: Explore and implement the workflow to store Figma reference images and structural design data locally in the repository.

- [ ] \[Vladyslav Krut\] Report Roadmap Status: Monitor team delivery status and report potential delays or issues to Filippo Tosetto, specifically concerning roadmap items like the Library Screen Redesign.

*You should review Gemini's notes to make sure they're accurate. [Get tips and learn how Gemini takes notes](https://support.google.com/meet/answer/14754931)*

*Please provide feedback about using Gemini to take notes in a [short survey.](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=9Tk70zQ7_MxlgjWcn3mADxITOAIIigIgABgDCA&detailid=standard)*