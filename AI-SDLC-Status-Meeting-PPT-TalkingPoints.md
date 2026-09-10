# AI SDLC Program Status Check — PowerPoint Talking Points

**Meeting Date:** [Insert Date]  
**Program Manager:** [Your Name]  
**Program:** AI SDLC (Global SaaS Platform)  
**Duration:** 30 minutes

---

## 📊 SLIDE 1: Title Slide

### Visual Elements
- **Title:** AI SDLC Program Status Check
- **Subtitle:** [Sprint Number] | [Date]
- **Logo:** AutoZone
- **Footer:** Program Manager: [Your Name]

### Talking Points
- "Good morning/afternoon everyone. Welcome to our AI SDLC program status check."
- "Today we'll cover program health, milestones, dependencies, risks, and team adoption."
- "This is a 30-minute session focused on surfacing blockers and ensuring we're on track."

---

## 🎯 SLIDE 2: Executive Summary — Program Health at a Glance

### Visual Elements
**Dashboard-style layout with 4 quadrants:**

| **Milestone Status** | **Decision Queue** |
|---|---|
| 🟢 On Track / 🟡 At Risk / 🔴 Behind | DRs in queue: [X] |
| Current: [M1/M2/M3] | Median age: [Y] days |
| Target: [Date] | Aging >5 days: [Z] |

| **Dependencies** | **Risks** |
|---|---|
| Total active: [X] | High: [X] |
| With owner+date: [Y%] | Medium: [X] |
| Aging >1 week: [Z] ⚠️ | Surprise escalations: [X] |

**Program Blocked Time:** [X%] (Target: <5%)  
**Sprint Velocity Trend:** ↗️ / → / ↘️

### Talking Points
- "Here's our program health snapshot at a glance."
- **If green:** "We're on track for [milestone]. Key indicators are healthy."
- **If yellow/red:** "We have [X] areas requiring attention today, which I'll detail in subsequent slides."
- "Our blocked time is at [X%], [below/at/above] our 5% target."
- "Decision queue is [healthy/needs attention] with [X] DRs in flight."

---

## ⏱️ SLIDE 3: Queue Metrics — Decision Request Status

### Visual Elements
**Bar chart showing DR age distribution:**
- 0-2 days (Target zone): [X] DRs
- 3-5 days (SLA zone): [Y] DRs  
- >5 days (Escalation zone): [Z] DRs 🚨

**Table of aging DRs:**
| DR ID | Topic | Age (days) | Owner | Status |
|---|---|---|---|---|
| DR-XXX | [Topic] | [X] | [Name] | Pending |

**Metric callout box:**
- Median DR age: [X] days (Target: ≤2, SLA: ≤5)
- Pre-read compliance: [X%] (Target: 100%)

### Talking Points
- "Our decision request queue currently has [X] items."
- "Median age is [X] days — [within/outside] our 2-day target and [within/outside] our 5-day SLA."
- **If aging DRs exist:** "We have [X] DRs aging beyond 5 days that require escalation today: [list DR topics]."
- **If no aging DRs:** "No DRs are aging beyond our SLA — the queue is healthy."
- "All DRs submitted this cycle have been vetted for completeness: options, recommendation, and blast radius."
- "Any incomplete DRs were returned to submitters for revision."

---

## 📍 SLIDE 4: Milestone & Gate Tracking

### Visual Elements
**Timeline diagram:**
```
M0 ─────── M1 ─────── M2 ─────── M3
  ✅       ➤ (Current)   (Target)
         [Date]       [Date]
         [Status: On Track / At Risk / Behind]
```

**Gate Evidence Checklist:**
- ✅ Demo evidence collected: [X of Y squads]
- ⚠️ E2 parity burn-down: [X%] (Target: [Y%])
- ✅ UAT on golden demo tenant: [X of Y squads green]
- ⚠️ KPI snapshots: [list incomplete items]

**Slip Signals (if any):**
- [Squad/Workstream]: [Slip description] | Impact: [X weeks] | Root cause: [reason]

### Talking Points
- "We're currently tracking to [milestone] with a target date of [date]."
- **If on track:** "We're on track. Evidence collection is [X%] complete, and all squads are [green/yellow] on UAT."
- **If at risk:** "We have a potential slip signal from [squad/workstream]. Root cause is [reason], estimated impact is [X weeks]. We're working with [owner] to mitigate."
- **If behind:** "We are behind on [milestone] due to [reason]. Recommending [action]: [rescope / extend timeline / add resources]."
- "Gate evidence status: [X of Y] items complete. Outstanding items: [list with owners and dates]."
- **Knowledge-migration gates:** "For legacy domains, [X of Y] promotion gates are cleared. [List any unpromoted domains blocking PRD/DoR]."

---

## 🔗 SLIDE 5: Dependency Brokering — Cross-Squad & Cross-Tribe

### Visual Elements
**Dependency funnel:**
```
Total Dependencies: [X]
  ├─ With owner + date: [Y] (Target: 100%) ✅
  ├─ Aging >1 week: [Z] ⚠️ 🚨
  └─ Resolved this sprint: [W] ✅
```

**Aging Dependencies Table (>1 week):**
| Dependency | From Squad | To Squad | Age (days) | Owner | Date | Status |
|---|---|---|---|---|---|---|
| [Description] | [Squad A] | [Squad B] | [X] | [Name] | [Date] | Blocked |

**Cross-Tribe Blockers:**
- [Tribe A] → [Tribe B]: [Blocker description] | Owner: [Name] | Resolution date: [Date]

### Talking Points
- "We're tracking [X] active dependencies across squads and tribes."
- **If 100% coverage:** "[Y] dependencies have assigned owners and dates — 100% coverage, meeting our target."
- **If <100% coverage:** "We have [Z] dependencies without owners or dates. These will be assigned provisional owners today and escalated to the Board."
- **If aging dependencies:** "🚨 ESCALATION: [X] dependencies are aging beyond 1 week: [list]. These require immediate attention from [owner/Director]."
- **If no aging dependencies:** "No dependencies are aging beyond our 1-week threshold. Closure rate is healthy."
- "This sprint we resolved [W] dependencies, maintaining our closure velocity."
- "Cross-tribe blockers flagged at Scrum-of-Scrums: [list with mitigation plan]."

---

## ⚠️ SLIDE 6: Risk Register Review

### Visual Elements
**Risk heat map:**
```
         Likelihood
         Low  Med  High
Impact
High    [ ]  [1]  [2]  ← Active high risks
Med     [ ]  [3]  [ ]
Low     [ ]  [ ]  [ ]
```

**Active High Risks:**
| Risk ID | Description | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| R-001 | [Description] | High | High | [Mitigation plan] | [Name] | In progress |
| R-002 | [Description] | Med | High | [Mitigation plan] | [Name] | Monitoring |

**New Triggers Since Last Review:**
- [Trigger description] → Added to register on [date]

**Surprise Escalations:** [X] (Target: 0)

### Talking Points
- "Our risk register currently tracks [X] active risks: [Y] high, [Z] medium, [W] low."
- "Top 2 high risks requiring attention:"
  - **Risk 1:** "[Description]. Mitigation: [plan]. Owner: [name]. Status: [in progress/monitoring]."
  - **Risk 2:** "[Description]. Mitigation: [plan]. Owner: [name]. Status: [in progress/monitoring]."
- **If new triggers:** "Since our last review, [X] new trigger events occurred: [list]. These have been added to the register with mitigation plans."
- **If surprise escalations:** "⚠️ We had [X] surprise escalation(s) this sprint: [description]. Root cause analysis: [reason]. Preventive action: [plan]."
- **If no surprise escalations:** "✅ Zero surprise escalations this sprint — meeting our target."
- "Next monthly risk review scheduled for [date]."

---

## 👥 SLIDE 7: Adoption & Team Health

### Visual Elements
**Adoption Dashboard:**

**Charter Ratifications:**
- Progress bar: [X of Y squads] ([Z%]) ✅ Target: 100%

**First-Sprint Checklists:**
- Progress bar: [X of Y squads] ([Z%])

**Playbook Certifications by Role:**
| Role | Certified | Total | % |
|---|---|---|---|
| Systems Engineers | X | Y | Z% |
| Data Engineers | X | Y | Z% |
| Software Engineers | X | Y | Z% |
| Product Owners | X | Y | Z% |
| Architects | X | Y | Z% |

**BMad Workflow Adoption:**
- Squads running full BMad cycle: [X of Y] ([Z%])
- Stories mastered in-repo with Jira sync: [X%]
- DoR gate compliance: [X%]

**Program Blocked Time:** [X%] (Target: <5%)

### Talking Points
- "Team adoption is tracking at [high/medium/low] maturity across the program."
- **Charter ratifications:** "[X of Y] squads have ratified charters — [on track / needs follow-up with {squad names}]."
- **First-sprint checklists:** "[X of Y] squads completed onboarding checklists. Outstanding: [list squads]."
- **Playbook certifications:** "By role, we're at [average %] certification. [Highlight any roles lagging]."
- **BMad workflow adoption:** "[X of Y] squads are running the full BMad cycle. DoR compliance is at [X%], [above/below] our target."
- **Blocked time:** "Program coordination is consuming [X%] of squad capacity, [within/outside] our <5% target."
- **If above 5%:** "Blocked time is elevated due to [reason: dependencies, onboarding, tooling]. Mitigation: [plan]."

---

## 🏗️ SLIDE 8: Technical Architecture Status Breakdown

### Visual Elements
**Component health matrix:**

| Component | Status | Sprint Progress | Blockers |
|---|---|---|---|
| **Frontend (FE)** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| React 19 MFE | 🟢/🟡/🔴 | [X stories done] | — |
| React Native (Mobile) | 🟢/🟡/🔴 | [X stories done] | — |
| Figma Design System | 🟢/🟡/🔴 | [X components] | — |
| **Backend (BE)** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| Spring Boot 4 Services | 🟢/🟡/🔴 | [X services] | — |
| **API Layer** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| Apigee Gateway | 🟢/🟡/🔴 | [X endpoints] | — |
| MCP Integration | 🟢/🟡/🔴 | [X tools] | — |
| **AI Services** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| AI SDLC Workflows | 🟢/🟡/🔴 | [X agents] | — |
| **Identity & Access** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| Ping AIC | 🟢/🟡/🔴 | [Integration status] | — |
| IAM (4-Gate Model) | 🟢/🟡/🔴 | [Gates implemented] | — |
| **Cloud (GCP)** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| GKE Autopilot | 🟢/🟡/🔴 | [Cluster status] | — |
| GCS (Storage) | 🟢/🟡/🔴 | [Bucket setup] | — |
| **Database** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| AlloyDB | 🟢/🟡/🔴 | [Schema status] | — |
| Spanner | 🟢/🟡/🔴 | [Schema status] | — |
| **CDN & Edge** | 🟢/🟡/🔴 | [X% complete] | [List blockers] |
| Akamai | 🟢/🟡/🔴 | [Config status] | — |

### Talking Points
- "Here's our technical stack status breakdown by component."
- **Frontend:** "[Status]. React 19 MFE: [X stories complete]. Mobile (React Native): [X stories complete]. Figma design system: [X components ready]. [Blockers: list if any]."
- **Backend:** "[Status]. Spring Boot 4 services: [X services deployed]. [Blockers: list if any]."
- **API:** "[Status]. Apigee: [X endpoints live]. MCP integration: [X tools registered]. [Blockers: list if any]."
- **AI Services:** "[Status]. AI SDLC workflows: [X agents operational]. BMad adoption: [X% of squads]. [Blockers: list if any]."
- **Identity:** "[Status]. Ping AIC integration: [complete/in-progress]. 4-Gate Model: [X of 4 gates implemented]. [Blockers: list if any]."
- **Cloud (GCP):** "[Status]. GKE: [cluster status]. GCS: [buckets configured]. [Blockers: list if any]."
- **Database:** "[Status]. AlloyDB: [schema migration status]. Spanner: [schema status]. RLS enforcement: [enabled/pending]. [Blockers: list if any]."
- **CDN/Edge:** "[Status]. Akamai config: [live/staging]. [Blockers: list if any]."
- "Critical path items requiring escalation: [list with recommended actions]."

---

## 🎯 SLIDE 9: Action Items & Escalations

### Visual Elements
**Decisions Required Today:**
| DR ID | Topic | Recommendation | Owner | Deadline |
|---|---|---|---|---|
| DR-XXX | [Topic] | [Recommendation] | VP | [Date] |

**Escalations for VP Queue:**
| Item | Description | Owner | Deadline | Impact |
|---|---|---|---|---|
| [Item 1] | [Description] | [Name] | [Date] | High/Med/Low |

**Follow-Up Actions:**
| Action | Owner | Due Date | Status |
|---|---|---|---|
| [Action 1] | [Name] | [Date] | Open/In Progress |
| [Action 2] | [Name] | [Date] | Open/In Progress |

### Talking Points
- "Three action categories from today's session: decisions, escalations, and follow-ups."
- **Decisions required:**
  - "[DR-XXX]: [Topic]. My recommendation: [one-liner]. Requesting VP decision by [date]."
- **Escalations:**
  - "[Item]: [Description]. This is blocking [squad/milestone]. Recommended owner: [name]. Deadline: [date]."
- **Follow-ups:**
  - "[Action 1]: [Owner] to [action] by [date]."
  - "[Action 2]: [Owner] to [action] by [date]."
- "All actions will be published within 2 hours of this meeting with owners and dates."

---

## 📅 SLIDE 10: Next Steps & Closing

### Visual Elements
**Next Meeting:**
- Date: [Insert date]
- Pre-read deadline: [24 hours before]

**Key Dates:**
- Next Sprint Planning: [Date]
- Next Scrum-of-Scrums: [Date]
- Next Architecture Board: [Date]
- Next Phase Gate: [Date]

**Contact:**
- Program Manager: [Your Name]
- Email: [Your Email]
- Teams: [Your Teams handle]

### Talking Points
- "To summarize: [1-sentence program health statement]."
- **If green:** "We're on track. Key focus areas for next sprint: [list 2-3 items]."
- **If yellow/red:** "We have [X] blockers requiring immediate action. Owners are assigned and resolution dates set."
- "Next status check: [date]. Pre-read will be distributed 24 hours in advance."
- "Thank you. Questions?"

---

## 💡 Additional Talking Points Reference

### If Asked About Budget/Resourcing
- "Current squad capacity: [X FTEs across Y squads]."
- "Budget burn rate: [on track / over / under] against plan."
- "Resource requests: [list any pending requests with justification]."

### If Asked About Quality/Defects
- "UAT pass rate: [X%] (from Delivery & Quality Review)."
- "Critical defects: [X open] | High: [X] | Medium: [X]."
- "DoD first-pass rate: [X%] (Target: [Y%])."

### If Asked About Vendor/External Dependencies
- "Vendor SLAs: [On track / At risk]."
- "External blockers: [list if any, e.g., Ping AIC API delay, Zuora integration issue]."
- "Design partner engagement: [X partners, Y personas covered]."

### If Asked About Compliance/Security
- "Security controls: [X of Y] implemented (from file 07)."
- "Audit/GRC: Probo system integration [status]."
- "Data preservation: 100% compliance — no destructive ops outside lifecycle."

### If Asked About Technical Debt
- "Tech debt stories in backlog: [X]."
- "Flag debt: [X flags pending deletion] (Target: ≤30 days post-release)."
- "Refactoring items scheduled: [list if prioritized]."

---

## 🎬 Presentation Tips

### Delivery Style
- **Be concise:** 30 minutes = ~3 min per slide. Practice pacing.
- **Lead with status, then context:** "We're on track" before "Here's why."
- **No surprises:** Pre-brief Directors on sensitive escalations before the meeting.
- **Data-driven:** Reference specific numbers, not "we're doing fine."
- **Action-oriented:** Every blocker must have owner + date by end of meeting.

### Body Language & Tone
- **Confident, not defensive:** You're presenting facts, not defending decisions.
- **Neutral on escalations:** Frame as "here's the data, here are options" — let VP decide.
- **Own the process:** You administer the queue, you broker dependencies, you chase owners.
- **Celebrate wins briefly:** "We closed [X] dependencies this sprint — great work by [squad]."

### Handling Questions
- **If you don't know:** "I'll verify and follow up within [timeframe]." Never guess.
- **If it's out of scope:** "That's a great question for [owner/forum]. I'll connect you."
- **If it's a decision:** "Let me capture that as a Decision Request for the VP queue."
- **If it's contentious:** "I'm hearing [position A] and [position B]. Let's take this offline and bring a recommendation to Thursday's review."

### Time Management
- **Start on time, end on time:** 30 minutes is a hard stop.
- **Timebox discussions:** "We have 3 minutes for this section. Let's capture follow-ups if we need more time."
- **Parking lot:** Keep a visible list of "offline topics" to avoid derailing the agenda.
- **Final 3 minutes:** Always reserve for action items and next steps.

---

## 📎 Appendix: Backup Slides (if needed)

### Backup Slide A: Sprint Velocity Trend
- Chart showing story count + cycle time over last 4-6 sprints
- Trend line: ↗️ improving / → stable / ↘️ declining

### Backup Slide B: DoR/DoD Compliance Detail
- DoR gate pass rate by squad
- DoD first-pass rate by squad
- Retro action closure rate

### Backup Slide C: Knowledge-Migration Gate Detail
- Full list of legacy domains in promotion
- Evidence corpus status (interviews, transcripts, synthesis)
- Contradiction aging report

### Backup Slide D: BMad Workflow Metrics
- Agent usage by skill (bmad-prd, bmad-dev-story, etc.)
- Context window efficiency
- Story sizing distribution (hours not days)

---

## ✅ Pre-Flight Checklist for Presenter

- [ ] All data points updated from latest sources
- [ ] Pre-read distributed 24 hours prior (100% compliance)
- [ ] Slides tested (no broken links, charts render correctly)
- [ ] Backup slides prepared for anticipated deep-dive questions
- [ ] Action-item capture sheet ready (digital or paper)
- [ ] Timer set for 30-minute hard stop
- [ ] Meeting room tech tested (screen share, mic, projector)
- [ ] Directors pre-briefed on sensitive escalations (no surprises)

---

**End of Talking Points Document**

**Notes:**
- Replace all [placeholders] with actual data before meeting
- Color-code status indicators: 🟢 Green = On track, 🟡 Yellow = At risk, 🔴 Red = Behind
- Practice 30-minute delivery at least once before live meeting
- Keep a parking lot slide for off-agenda topics
