# Session record — 2026-09-19

This is a snapshot for Isaac to read offline. It has two parts: a record of what happened in this session (below), and a copy of the approved plan (`ROADMAP.md` as of today, after the divider). The copy of the plan in the project is the authoritative version. If the two ever differ, the project version wins.

---

## What we did, in order

**1. Mac setup.** You cloned the repo on the MacBook. The steps that made it work:
- Use `python3` to create the venv on macOS: `python3 -m venv venv`, then `source venv/bin/activate`, then `pip install -r requirements.txt`.
- The pip version warning is harmless.
- In VS Code, select the interpreter under `./venv`.
- Set the git identity for this repo only (`git config user.name` and `git config user.email`). `git log -1` shows the name and email you used on the PC.
- `python app.py` runs the app. Your `.gitignore` covers `venv/`, `__pycache__/`, `*.db`, `.env` and `.pytest_cache/`.
- The local `instance/practice.db` is per machine, so the Mac starts with an empty database.

**2. The Reddit thread.** You shared a post from someone who graduated with no internship and applied for a year without success, plus comments about open source and about projects. My read:
- Most comments were anecdotes with a handful of upvotes, so they were not a reason to rewrite the sequencing.
- The one useful comment described the mechanism: interviewers want to see whether you can explain the logic behind your project. That is why you are writing practice-tracker yourself.
- The thread's real lesson is timing: get real experience before graduating, not after.
- The "AI something" comment was one line with no detail. Use real job postings as evidence at the December checkpoint.

**3. Repo review** (read-only on your Mac).
- The tracker was far ahead of the old README and roadmap: all routes, edit, delete, growing retest intervals, four templates, a 181-line stylesheet, and passing tests.
- Git history: 8 commits from Sept 16 to Sept 18. The old roadmap targeted "routes and `is_retest_due()` by mid-December" even though the dashboard, add and retest routes were already committed by the morning of Sept 17.
- Design strength: `logic.py` is pure and takes `today` as an argument, so it is testable.
- Gaps, all unhappy-path: a blank date crashes the add route, refreshing after a save duplicates the row, delete has no confirmation, `is_retest_due()` subtracts from a `None` default, and retest status is derived in two places.

**4. Roadmap critique.** The old roadmap was wrong on day one, not just outdated:
- it was written from a README that predated the routes;
- it held applications until winter, contradicting both the recruiting calendar and your agreed plan;
- it assumed weekday-only 45–90 minute sessions;
- it left out the larger project.

**5. Research** (sources below).
- UC Davis fall classes start Sept 23. Instruction ends Dec 4, finals are Dec 7–11, and winter begins Jan 4, 2027.
- The UC Davis Fall Career Fair is Oct 14 (in person). The tech career fair is tentatively Jan 21.
- Summer 2027 internship recruiting runs in waves: main wave late July–September, second wave October–January, backfill January–March. Applying in late September or October is still viable. This is a third-party guide.

**6. Analysis passes.**
- Time: Sept 23 to Dec 11 is about 11 weeks. At 1–2 hours a day that is about 120 nominal hours, or about 100 after midterms, Thanksgiving and finals.
- Fundamentals: Stack, Sliding Window and Binary Search are about 20 problems, or 25 hours. With Trapping Rain Water and the retests, that is about 30 hours. That is the floor, and it leaves slack. Linked Lists and Trees add about 30 more hours at a slower pace.
- Tracker: about 40–45 hours fits robustness plus the README (8–10), deploy prep (about 5), and Terraform/Azure (20–25), with little slack.
- Whole horizon: 21 months at 1–2 hours a day is about 950 hours.
- GPA arithmetic: your Davis GPA counts only Davis units. If the two classes were about 8 units, one 12-unit quarter around 3.5 gives about 2.9, and two such quarters give about 3.1. You are at the 2.0 line for good standing and graduation, so treat school as a floor to protect. Confirm major requirements with an advisor.

**7. Your corrections.**
- The CTI/CodeDay internships were real, paid and mentored, not a training program. My earlier wording came from an older note and was wrong.
- The caretaking role is the main reason for the gap from when your resume activity ended until this summer.
- Your Davis GPA is 2.0.
- You do not remember what the internship work involved. Your blog posts are on your home PC.
- You are not under financial pressure right after graduation.
- Your panic comes from the resume and from not knowing if you are good enough, not from rejection or interviews.
- You will spend at least 1–2 hours a day regardless of your courses.
- You have no larger-project idea yet, and you want it ambitious and provably yours.

**8. Decisions made.**
- The old plan documents no longer bind us. Claude owns the plan, built from your background and the evidence.
- There is one plan document with a handoff section, and it changes only at checkpoints or on evidence.
- Applications start now as a light standing thread.
- The tracker gets deployed this fall if possible.
- Confidence is built from measured evidence: a scoreboard, timed sets, monthly mock interviews, explain-back checks and outside review.

## What changed on disk and in the project

- **Project docs:** `ROADMAP.md` was rewritten as the single plan with a handoff section. `PROGRESS.md` now has the cold-retest queue, a tracker milestone log, a weekly scoreboard table, and an "Up next" list. The project `README.md` was updated earlier today.
- **Your repo:** `README.md` was updated in the practice-tracker repo. It is uncommitted. Suggested commit message: `Update README: Phase 1 complete, add macOS setup and How-it-works prompts`. Edit it before you push.
- **Stale file:** my git commands left a stale `.git/index.lock`. I renamed it to `.git/index.lock.stale-from-claude`, and you can delete it. I stopped running git in your repo after that.
- **Not synced:** the `fall` repo copies of `ROADMAP.md` and `PROGRESS.md` on your PC are now older than the project versions.

## Things I got wrong today (so you can weigh my judgment)

- I called your Group Anagrams and 3Sum retests overdue. You had deferred them on Sept 18 on purpose.
- I wrote "training program" for your internships. They were real, paid internships.

## What I can and cannot promise about continuity

- I cannot promise that this chat will be fully available to me, or that I will process all of it clearly, days from now. Long conversations can be compressed, and details can blur.
- The project's `ROADMAP.md` (with its handoff section) and `PROGRESS.md` are the safeguard. They live in the project, not just in this chat.
- When you come back, start by asking me to read the Handoff section of `ROADMAP.md`. I will do that first either way.
- Any session, this one or another, that changes the plan should log the change in section 12 of `ROADMAP.md` with the reason.

## Sources

- [UC Davis academic calendar 2026–27](https://acadcalendar.com/uc-davis-academic-calendar/)
- [UC Davis career fairs (Career Center)](https://careercenter.ucdavis.edu/career-center-services/career-fairs)
- [Summer 2027 SWE internship timeline (PracHub)](https://prachub.com/resources/when-do-summer-2027-swe-internships-open-oa-waves-rolling-recruiting-and-deadlines)

---

# The approved plan (snapshot of ROADMAP.md, 2026-09-19)

# Roadmap — Isaac's Plan to Post-Grad Readiness

**Version:** 2026-09-19. Rebuilt from scratch at Isaac's request and approved by him the same day. It supersedes every earlier version of this document, which were built from a stale README and from each other.

This is the single source of truth for the plan. `PROGRESS.md` logs what happened. `README.md` describes the practice-tracker app. Nothing else should hold a competing plan.

---

## 0. HANDOFF — read this first, rewrite it last

**Last updated:** 2026-09-19, end of the session that built this plan.

**Where things stand.**
- Fall classes start Sept 23. Isaac commits to 1–2 hours a day, every day, regardless of coursework.
- Fundamentals: about 11 LeetCode problems done. Trapping Rain Water unsolved. Group Anagrams and 3Sum retests deferred on purpose on Sept 18.
- practice-tracker: local Flask/SQLite app complete beyond original v1 scope, 8 commits (Sept 16–18), tests pass. Not yet robust, not deployed, README "How it works" not yet written.
- Uncommitted in the tracker repo: an updated `README.md` (status, features, macOS setup, "How it works" prompts). Suggested commit message: `Update README: Phase 1 complete, add macOS setup and How-it-works prompts`. Isaac edits it before pushing.
- Housekeeping: `.git/index.lock.stale-from-claude` in the tracker repo is an empty leftover from a session and can be deleted.

**Next actions, in order.**
1. Tracker robustness, with a walk-through first and Isaac writing the fix:
   - blank date crashes the add route (`date.fromisoformat('')`);
   - the add route re-renders after POST, so a refresh creates a duplicate row (Post/Redirect/Get);
   - `is_retest_due()` defaults `today=None` and then subtracts from it;
   - delete has no confirmation.
2. Isaac starts the README "How it works" section with the dashboard flow, in his own words.
3. Resume: add the practice-tracker, complete the Handshake profile, register for the Oct 14 Fall Career Fair.
4. Isaac sends the CTI/CodeDay blog posts from his home PC. He then writes 3–4 internship stories in his own words and is quizzed on them.
5. Sept 23 onward: Group Anagrams and 3Sum retests cold, then Trapping Rain Water, then Stack.
6. About Sept 26: timed baseline of three unseen problems in 75 minutes. Claude picks them, and the score goes in the scoreboard.
7. About Sept 28: applications start, 2–3 a week, each logged.
8. By Oct 5: Isaac messages one or two CTI/CodeDay mentors (resume feedback, referrals).
9. Before deploy work: confirm the Azure for Students subscription is active. Also confirm the major's GPA requirements with an advisor, and what resume reviews the UC Davis career center offers.
10. Sync the `fall` repo copies of `ROADMAP.md` and `PROGRESS.md` with these project versions.

**Waiting on Isaac.** The CTI blog posts. Whether he has a larger-project idea yet (not needed until about Feb).

**Not-fully-grasped list (revisit later, same idea as the cold-retest habit).** Post/Redirect/Get; how retest status is derived in two places (`logic.py` and the `dashboard.html` if/elif chain); the hashmap-of-lists mechanic from Group Anagrams; the "advance the smaller side" invariant for Trapping Rain Water.

**Rules for the next session.**
1. Read this section, then ask Isaac what changed since the date above.
2. If the device link is up, check the tracker repo's `git log` and update the picture of where things stand.
3. Do the work. Log results in `PROGRESS.md`.
4. Before ending, rewrite this section: where things stand, next actions, waiting-on, and the not-grasped list.
5. Do not change the plan except at a checkpoint or on evidence, and log the change in section 12.

---

## 1. How to work with Isaac

- Give direct feedback with no filler reassurance. Genuine praise is fine when it is earned.
- Give hints and scaffolding, not finished code, even when he asks. The exception is a small mechanical change identical to a pattern he has already built himself.
- Explain how each piece connects across files before he has to ask. He wants to explain the project in an interview. That standard is not to be dropped for speed.
- Use short, single-idea sentences with checkpoints. Ground explanations in his real files and variable names, and name the file when switching files.
- For an unfamiliar domain, give a plain-language vocabulary briefing first. Separate what is essential now from what can wait, and keep the not-grasped list.
- Quiz him rather than asking him to pick his own starting point.
- Flag good GitHub push points with a commit message he can edit.
- The highest care goes to planning and direction decisions.
- If he is frustrated about pace, look at the evidence and give a straight answer. Do not manage his mood.

---

## 2. Background (corrected by Isaac, 2026-09-19)

- 5th-year CS student at UC Davis, transferred after 3 years at DVC. Target graduation: June 2028, end of 6th year, 6 quarters remaining.
- DVC: Associate of Arts in CS, Physics and Math, 4.0 GPA. His last year there was mostly math and physics.
- Fall 2025 was his only Davis quarter so far: two classes, both C's, so his Davis GPA is 2.0. He was the primary family caretaker at the time. That role also accounts for the gap from when his resume activity ended (2025) until this summer. It has ended.
- He chose a lighter load for two years so he could build things outside class. He could have finished in one more year by loading up, and he is unsure it was the right call. He is not overly worried about GPA but is not neglecting school.
- Before September 2026 he had gone about 3 years without independent coding and had not used an IDE properly in years. He learned C++ first and is now much more comfortable in Python. He had no database or web-dev background.
- Experience: the Open Energy Dashboard micro-internship (Oct–Dec 2023, Mocha tests for API endpoints) and the OJS internship (Jun–Aug 2024). Both were real, paid internships coordinated by CTI and CodeDay, with formal mentors and reporting. The OJS work produced a standalone Terraform configuration for Azure that was never verified end to end because his subscription expired. It was not a merged upstream contribution, and it must be described exactly that way. He also has the Skintelligence hackathon project and CTI Accelerate (2023–2025).
- He cannot currently explain the internship work without re-reading it. His blog posts documenting it are on his home PC.
- Setup: usually a Windows PC, a MacBook now. Repos: `fall` (LeetCode, private) and `practice-tracker`. He has Azure for Students credits.
- Not under pressure to take the first offer after graduation. Family support is available if he needs it.

## 3. Goals and constraints

- Be a competitive SWE candidate by graduation, stronger than typical peers.
- Floor: any CS-adjacent role using the degree, at roughly $70–80k or more, Bay Area or open geography. Data analyst, QA, support engineering, IT and research-adjacent roles all count as real entry points.
- His core fear is graduating with no job, not missing a prestige role.
- A Summer 2027 internship is the ideal, but he accepts it may not happen. The fallbacks are off-cycle internships, building, and open source.
- Later: a larger, ambitious project with real impact (criteria in section 9), and a real open-source PR to a smaller project.
- What he wants to feel: some confidence and belief while applying, not panic. His panic comes from the resume and from not knowing if he is good enough. It does not come from rejection or from interviews.
- Time: 1–2 hours a day, every day, consistently. Before Sept 23 it was 1.5–3. His head clarity varies, so Claude holds the long-range plan and he holds the daily work and accurate reporting.

## 4. Where things stand (evidence, 2026-09-19)

**Fundamentals** (Python, roadmap.sh pattern order). About 11 problems in two weeks.
- Fully independent: Two Sum, Container With Most Water, Two Sum II. Container and Two Sum II were also stress-tested with 2000 random trials.
- Solved with minor bumps: Valid Anagram, Contains Duplicate, Top K Frequent (repeated-max extraction, which works but is not the standard approach), Valid Palindrome.
- Needed heavy help: Group Anagrams (the hashmap-of-lists mechanic).
- Needed a hint: 3Sum.
- Unsolved: Trapping Rain Water, his first Hard, after about 2.5 hours.
- Arrays & Hashing and Two Pointers are otherwise done. Stack is next.

**practice-tracker.** 8 commits from Sept 16 to 18.
- Features: dashboard with retest-due status, add, mark retest done, edit, delete, opt-in growing retest intervals, styling, and a pytest suite for the retest logic. The three test functions pass.
- Design strength: `logic.py` is a pure function that takes `today` as an argument, which is what makes it testable.
- Built with heavy guidance. Not deployed.
- Every known gap is an unhappy-path gap (see next actions 1).

**The bar this implies.** In two weeks he went from almost no implementation ability to independent mediums plus a working tested app. The remaining gaps are depth: the harder topic categories, blank-page design, unscaffolded features, and explaining it all cold.

## 5. Strategy — why the plan is shaped this way

**Two application windows matter.**
- Window 1: about Oct 2026–Mar 2027, for Summer 2027 internships (second wave Oct–Jan, backfill Jan–Mar per third-party timeline guides).
- Window 2: typically about Aug 2027–Feb 2028, for new-grad roles (June 2028 graduation).

Interview readiness must peak by Window 2 at the latest and be partly in place for Window 1. Most employers review on a rolling basis, so applying within a few days of a good-fit posting matters.

**Budget.** 1–2 hours a day for 21 months is about 950 hours, with more if summer 2027 is a sprint. Rough allocation:
- Interview skill: about 400 hours.
- Projects: about 300 (roughly 80 for the tracker including deploy, about 200 for the larger project).
- Applications and networking: about 100.
- Resume and interview stories: about 30.

**Why applications start now.** A previous roadmap held applications until winter. That contradicted both the recruiting calendar and Isaac's own agreed plan. Applications run as a standing 10–15 minute thread, never a full block and never zero.

**Why staggered.** A first application to a company usually cannot be redone within a cycle. Start with mid-size and smaller companies and adjacent roles. Hold the online-assessment-heavy companies until about November, when Sliding Window and Binary Search are done.

**Why deploy the tracker.** The Terraform/Azure deploy is the differentiator most student portfolios lack, and it re-verifies a skill he already used once.

**Why measure.** His panic comes from not knowing whether he is good enough. Measured evidence fixes that. Reassurance does not.

## 6. Calendar anchors

- Sept 23, 2026: fall classes begin. Dec 4 is the last day of instruction. Dec 7–11 is finals. Jan 4, 2027: winter begins.
- Oct 14, 2026: UC Davis Fall Career Fair, in person, 11am–3pm, register on Handshake.
- Jan 21, 2027 (tentative): UC Davis Engineering, Energy and Technology Career Fair.
- Sources: [UC Davis academic calendar](https://acadcalendar.com/uc-davis-academic-calendar/), [UC Davis career fairs](https://careercenter.ucdavis.edu/career-center-services/career-fairs), [Summer 2027 internship timeline](https://prachub.com/resources/when-do-summer-2027-swe-internships-open-oa-waves-rolling-recruiting-and-deadlines). The last is a third-party guide, so treat its dates as approximate.

## 7. Phases

### Phase A — now to Dec 11, 2026: receipts

**Weekly split:** about 5 hours fundamentals, 4 hours tracker, 1–1.5 hours applications and networking. Consistency beats heroic days.

**Fundamentals by Dec 11.**
- Floor: Stack, Sliding Window and Binary Search complete, Trapping Rain Water solved, both retests passed cold.
- Target: the floor plus Linked Lists and the start of Trees.
- Stretch: Trees complete and Heaps started.
- Problem counts are approximate, roughly 6–7 per topic.

**Tracker milestones.**
- About Oct 31: robustness fixes done, README explanation covers the four core flows, configuration moved to environment variables.
- About Nov 21: Terraform creates the Azure resources and the app connects to Postgres.
- By Dec 11 (winter break at the latest): live at a URL, reproducible from the README.
- If the Oct 31 milestone slips, the deploy moves to winter break. It does not take hours from fundamentals.

**Resume and applications.**
- Resume v2 by mid-October: internship bullets rewritten with specifics recovered from the blog posts, the tracker added, DVC 4.0 labeled as DVC, and the Davis GPA left off unless a form asks.
- Attend the Oct 14 fair.
- About 25 applications by Dec 11, and 3–5 real networking conversations.

**Also this quarter.** Map the remaining core CS courses (ECS 154A, 122A, 120/122B, 150 which requires 154A, 140A, a probability course, the upper-division writing requirement) against the 6 remaining quarters. Keep the heaviest courses from all landing in the final recruiting year.

**Checkpoint, Dec 11.** Review the scoreboard, the traction (online assessments and interviews), and this plan. Decide where winter hours go: interview prep if there is traction, backfill wave and building if not.

### Phase B — Jan–Mar 2027: interview fluency
- Linked Lists, Trees, and an intro to Graphs and DP.
- A monthly timed mock interview with Claude, scored 1–4 on understanding, approach, correctness, complexity, communication and testing.
- Finish the tracker deploy if it slipped. Jan 21 tech fair. Backfill-wave applications through March.
- Choose the larger project by Mar 31 (criteria in section 9).

**Checkpoint, Mar 31.**

### Phase C — Summer 2027 (branches on the outcome)
- **Internship secured:** do it. Keep 30 minutes a day of DSA so interview shape does not decay. Collect stories.
- **No internship:** a 6–8 hour a day sprint on the larger project with real users, graphs and DP, and an open-source PR to a smaller project. This is a real plan, not a consolation, and off-cycle internships stay in play.
- Either way, application-ready by mid-August.

**Checkpoint, Jun 15.**

### Phase D — Fall 2027 to winter 2028: new-grad recruiting
- Apply broadly in the main wave, work interview loops, and keep coursework from piling up.
- Roughly half of the time goes to interview prep, a third to applications, and the rest to the project.

**Checkpoint, Sept 1.**

### Phase E — Spring 2028: close out coursework, work live loops, decide among offers.

## 8. Confidence — scoreboard, thresholds, outside eyes

**Weekly scoreboard** (logged in `PROGRESS.md`): days practiced, problems solved independently, cold-retest pass rate, timed-set score, applications sent and responses.

**What "good enough" means.** This is Claude's calibration and not a guarantee.
- For the floor: most easies and about half of mediums in covered patterns solved in 30–35 minutes, plus the ability to explain the project and internships cold.
- For the ceiling: mediums consistently in about 25 minutes, including trees and graphs.

**Explain-back check.** At each tracker milestone, Isaac explains one feature across the files with no code open. Claude asks follow-ups such as "what breaks if this changes?"

**Outside eyes.** A resume review from the UC Davis career center or people he trusts. Reconnect with CTI/CodeDay mentors for feedback and referrals.

**Gap answer** (draft for Isaac to rewrite in his own words). "From 2025 until this summer I was the primary caregiver for a family member. Since that ended I have rebuilt my skills: I have worked through core data-structure patterns and built and tested a full web app, and I am looking for a role where I can keep growing."

**Rejection.** It is the base rate. For the first stretch, judge the process (applications sent, resume quality, prep done) and not the outcomes. No single application decides anything.

## 9. The larger project — criteria, not a topic

He wants something ambitious, with real impact, that he can manage, and Claude should not underestimate him. It should avoid two failures: a project any student could do with light AI help, and one so large that AI clearly did it.
- Real users other than Isaac (a student org, a nonprofit, a local business). That gives impact and proof at once.
- A real backend with data, authentication and deployment.
- A working slice in about 40–60 hours, growing in layers afterward.
- Provable authorship: incremental commit history, a design-decision log, tests, and the ability to modify and explain it live. AI can be used as a pair or reviewer, while design and core logic stay his.

## 10. Practice-tracker backlog

1. Robustness fixes (see next actions 1).
2. README "How it works", written by Isaac.
3. Deploy readiness: configuration from environment variables (`python-dotenv` is already in requirements), a production WSGI server, and Postgres compatibility. Optionally a small GitHub Actions workflow that runs `pytest`.
4. Terraform-provisioned Azure deploy: App Service plus PostgreSQL Flexible Server.
5. Consider consolidating retest-status logic that currently lives in two places.

## 11. Standing risks

- Whether 1–2 hours a day holds once classes start. Check it against three weeks of real logs, without guilt.
- Harder topic categories will slow the pace. That is expected and not falling behind.
- School as a floor: he is at the 2.0 line that matters for good standing and graduation. Protect it.
- Depending on one summer internship outcome. Off-cycle roles, adjacent roles, the larger project and open source exist so no single result carries the plan.
- The sprint pace of Sept 13–18 (long hours, 1–2am commits) is the ceiling and not the plan.

## 12. Change log

- **2026-09-19:** Plan rebuilt from scratch and approved by Isaac.
  - Reasons: the earlier roadmap was written from a stale README (the tracker's Phase 1 target was already met); it delayed applications until winter, against the recruiting calendar and Isaac's own agreed plan; it assumed 45–90 minutes on weekdays only instead of 1–2 hours daily; and Isaac's corrections (real paid internships, GPA 2.0, panic sources).
  - New: handoff section, scoreboard, confidence thresholds, the explain-back check, and the larger-project criteria.
