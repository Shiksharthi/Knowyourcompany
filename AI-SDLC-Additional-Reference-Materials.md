# AI SDLC Program - Additional Reference Materials

---

## 1. Program KPI Definitions (PGM-1 through PGM-6)

### PGM-1: Executive Review Operations
**Metrics:**
- Decision Request SLA: Median ≤2 days (Target), ≤5 days (SLA)
- Pre-read compliance: 100%
- Same-day publication: 100%

**How Measured:**
- Track all DRs from submission to decision date
- Calculate median age weekly
- Pre-read sent 24 hours before meeting = compliant
- Outcomes published within 2 hours of meeting = compliant

**Escalation Trigger:**
- Any DR aging >5 days flagged in Tue metrics opening

---

### PGM-2: Dependency Brokering
**Metrics:**
- Cross-squad asks with owner + date: 100%
- Dependencies aging >1 week: 0

**How Measured:**
- Asks-and-owners log from Scrum-of-Scrums (Wed)
- Every dependency must have assigned owner + resolution date
- Age calculated from log entry date

**Escalation Trigger:**
- Any dependency aging >1 week → Board or VP queue (same week, automatic)

---

### PGM-3: Milestone Tracking
**Metrics:**
- Gate table always current: 100%
- Slip signals surfaced ≥2 weeks before gate: 100%

**How Measured:**
- Milestone table updated after every sprint review
- Slip signal = any evidence showing target date at risk
- Must notify VP + Directors immediately when detected

**Escalation Trigger:**
- Any slip signal detected → VP + Directors notification (immediate, with data)

---

### PGM-4: Risk Register
**Metrics:**
- Monthly review: 100% compliance
- Surprise escalations: 0

**How Measured:**
- Risk register reviewed at monthly Portfolio Sync
- Triggers monitored between reviews
- Surprise escalation = unregistered risk requiring VP attention

**Escalation Trigger:**
- Any surprise escalation → Root cause analysis + preventive action

---

### PGM-5: Program Blocked Time
**Metrics:**
- Target: <5% of squad capacity

**How Measured:**
- Tracked from Delivery & Quality Review (Thu)
- Blocked time = meetings, dependency waits, escalations
- Excludes planned ceremonies

**Escalation Trigger:**
- Blocked time >5% → Analyze root cause, propose mitigation

---

### PGM-6: Adoption Tracking
**Metrics:**
- Charter ratifications: 100%
- First-sprint checklists: 100%
- Playbook certifications: 100%

**How Measured:**
- Charter: Squad has signed charter on file
- First-sprint: Onboarding checklist completed
- Playbook: Role-specific certification test passed

**Escalation Trigger:**
- Report incomplete adoptions at monthly Portfolio Sync

---

## 2. Sprint Ceremonies Quick Reference

### Daily
- **Standup:** 15 min, per squad
- **PO availability:** Same-day AC questions

### Weekly (Every Wed)
- **Backlog Refinement:** 60 min (W1: grooming, W2: DoR gate)
- **Scrum-of-Scrums:** 30 min (PgM-facilitated, dependency brokering)
- **Architecture & Contract Review Board:** 60 min

### Weekly (Tue/Thu)
- **Executive Review (Tue):** 60 min (VP-chaired, PgM-administered)
- **Executive Review (Thu):** 30 min (Follow-ups, PgM-administered)
- **Delivery & Quality Review (Thu):** 30 min (M-tier KPIs)

### Bi-Weekly (Sprint Cycle)
- **W1 Monday: Sprint Planning:** 60-90 min
- **W2 Monday: Mid-sprint Checkpoint:** 30 min
- **W2 Friday AM: Sprint Review:** 60 min (Golden demo tenant)
- **W2 Friday PM: Retrospective:** 45 min

### Monthly
- **Portfolio / Roadmap Sync:** 60 min (PM leadership + VP)
- **Risk Register Review:** Folded into Portfolio Sync
- **Design-Partner Evidence Review:** Folded into Portfolio Sync

### Quarterly
- **Phase Gate Review + Drills:** Half day (Milestone evidence presentation)

---

## 3. Decision Request (DR) Template

**File Location:** `vp-decisions/DR-[NUMBER]-[SHORT-SLUG].md`

**Required Sections:**

```markdown
# Decision Request: [Title]

**DR ID:** DR-[NUMBER]  
**Submitted By:** [Name, Role]  
**Date Submitted:** [Date]  
**Deadline:** [Date]  
**Blast Radius:** Low / Medium / High

## Context
[What decision is needed and why? What problem are we solving?]

## Options
### Option A: [Name]
- **Description:** [What is this option?]
- **Pros:** [Benefits]
- **Cons:** [Drawbacks]
- **Cost/Effort:** [Estimate]

### Option B: [Name]
- **Description:** [What is this option?]
- **Pros:** [Benefits]
- **Cons:** [Drawbacks]
- **Cost/Effort:** [Estimate]

[Add Option C, D, etc. as needed]

## Recommendation
[Your recommended option with 1-2 sentence rationale]

## Blast Radius
[Who/what is impacted if we decide today? What's blocked if we defer?]

## Supporting Materials
- [Link to PRD, spike, design doc, etc.]

---

## Decision (VP Only)
**Decision:** [Decide / Defer / Delegate]  
**Chosen Option:** [Option X]  
**Rationale:** [VP's reasoning]  
**Owner:** [Who executes this decision]  
**Revisit Date:** [If deferred, when to revisit]  
**Date Decided:** [Date]
```

**Completeness Check (PgM triage):**
- [ ] Context clear and decision-framed
- [ ] ≥2 options presented with pros/cons
- [ ] Recommendation included
- [ ] Blast radius stated
- [ ] Supporting materials linked (if applicable)

**If incomplete:** Return to submitter (kindly) with specific gaps

---

## 4. Dependency Asks-and-Owners Log Format

**Maintained By:** Program Manager  
**Source:** Scrum-of-Scrums (Wed)  
**Updated:** Weekly

**Log Entry Format:**

| Dep ID | From Squad | To Squad | Ask Description | Owner | Target Date | Status | Age (days) | Notes |
|---|---|---|---|---|---|---|---|---|
| D-001 | Squad A | Squad B | API contract for user service | [Name] | [Date] | Open | 3 | [Notes] |
| D-002 | Squad C | Squad D | Shared UI component | [Name] | [Date] | In Progress | 8 🚨 | ESCALATE |
| D-003 | Squad E | Squad F | Database schema review | [Name] | [Date] | Resolved | 0 | Closed [Date] |

**Statuses:**
- Open (new, awaiting owner)
- In Progress (owner working)
- Blocked (external blocker)
- Resolved (closed)

**Escalation Rule:**
- Any dependency aging >7 days → Auto-escalate to Board or VP queue that same week

**Closure:**
- Mark "Resolved" only when receiving squad confirms completion
- Archive closed dependencies monthly

---

## 5. Knowledge-Migration Gate Checklist

**For Legacy Domains Only** (before PRD/DoR)

**Gate Criteria (from file 29):**

### Phase 0: Discovery (Isolated Workspace)
- [ ] Evidence corpus collected (interviews, transcripts, docs)
- [ ] SME coverage: ≥2 SMEs per capability area
- [ ] Architect reviewed for target boundary validation

### Phase 1: Synthesis
- [ ] Domain narrative drafted
- [ ] Glossary with legacy/target term mapping
- [ ] Capability map (legacy capabilities identified)
- [ ] Parity/variance register (what stays, what changes)
- [ ] Decision history captured
- [ ] Traceability manifest (legacy → target mapping)

### Phase 2: Review
- [ ] Contradictions identified and dispositioned
- [ ] Architect validates target boundaries
- [ ] Product Manager curates and presents
- [ ] SMEs review and sign off

### Phase 3: Promotion
- [ ] All artifacts marked `PROMOTED`
- [ ] Design-partner evidence plan created
- [ ] Design-partner persona coverage verified
- [ ] Evidence gaps documented with owner + date
- [ ] Raw material excluded from planning context

**Gate Owner:** Program Manager (tracks and administers)  
**Gate Decider:** Architect (validates) + VP IT & Product (approves)

**Outcome:**
- `PROMOTED` artifacts enter BMad planning context
- PRD/DoR may now proceed for this domain
- Unpromoted legacy context remains isolated

---

## 6. Golden Demo Tenant Requirements

**Purpose:** Evidence-based sprint reviews and UAT

**Requirements:**
- Live tenant in UAT environment
- Seeded with realistic data (from `08-application-stub.md` DoD)
- All released features enabled (flags ON)
- All squads demo against the SAME tenant (consistency)
- Data reset between sprint cycles (clean slate)

**Data Seed Extensions (per story DoD):**
- Every story that touches data MUST extend the golden seed
- Extensions versioned in repo alongside story
- Seed script runs automatically in UAT pipeline

**UAT Harness:**
- Playwright-MCP tests run against golden demo tenant
- Tests must pass before sprint review demo
- Test evidence captured for gate assembly

**Demo Protocol:**
- Product Owner presents on golden demo tenant
- Demo against stated Acceptance Criteria
- Working software only (no slideware demos)
- Demo recording/screenshots = evidence for E2 parity burn-down

---

## 7. Escalation Paths Summary

| Situation | Escalate To | Timing | Action |
|---|---|---|---|
| Dependency aging >1 week | Architecture Board or VP Queue | Same week (automatic) | PgM escalates with context + options |
| DR aging >5 days (SLA) | VP (flagged in Tue metrics) | Next Tue Executive Review | PgM presents queue health first |
| Milestone slip signal detected | VP + affected Directors | Immediate | PgM notifies with data (≥2 weeks before gate) |
| Surprise escalation (unregistered risk) | VP | Immediate | PgM files, root cause analysis in retro |
| Cross-Director conflict | VP Decision Request | Within 1 sprint | Directors file DR, VP decides |
| Architecture question (undecided) | Architecture Board → VP (if unresolved) | Next Wed Board meeting | Squad/PO flags, Architect reviews |
| Product question (undecided mid-sprint) | VP Decision Request | Immediate (flags PM process failure) | PO → PM → VP DR; tracked in retro |
| Decision-shaped item (PgM tempted to decide) | File DR (never decide) | Before taking action | PgM files with options + recommendation |

**Key Principle:** Program Manager has **zero decision authority**. All decision-shaped items escalate via DR process.

---

## 8. BMad Workflow Quick Commands

**Product Planning:**
- `bmad-product-brief` — Create product brief
- `bmad-prd` — Create/validate PRD

**Epic & Story Creation:**
- `bmad-create-epics-and-stories` — Break down PRD into epics/stories
- `bmad-check-implementation-readiness` — DoR gate check

**Sprint Operations:**
- `bmad-sprint-planning` — Generate sprint plan
- `bmad-sprint-status` — Mid-sprint status readout
- `bmad-correct-course` — Record scope changes

**Development:**
- `bmad-create-story` — Initialize story workspace
- `bmad-dev-story` — Full development cycle
- `bmad-quick-dev` — Small items (quick path)

**Quality & Completion:**
- `bmad-code-review` — Review code changes
- `bmad-qa-generate-e2e-tests` — Generate UAT tests
- `bmad-retrospective` — Sprint retro facilitation

**Architecture:**
- `bmad-architecture` — Solution design
- `bmad-spec` — Machine contract specs
- `bmad-ux` — UI/UX design (with Figma MCP)

**Reference:** https://docs.bmad-method.org/reference/commands/

---

## 9. Pre-Read Template (for Executive Review)

**Sent:** 24 hours before Tue/Thu Executive Review  
**Distribution:** VP, Directors, Squad Leads

**Subject:** Executive Review Pre-Read — [Date]

**Body:**

```
Executive Review Pre-Read
Date: [Tue/Thu, Date]
Time: [Time]
Location: [Teams link]

QUEUE METRICS
• DRs in queue: [X]
• Median age: [Y] days (Target: ≤2, SLA: ≤5)
• Aging >5 days: [List DR IDs and topics]
• Pre-read compliance last session: [X%]

DECISIONS THIS SESSION
1. [DR-XXX]: [Topic] — Recommendation: [One-liner]
2. [DR-YYY]: [Topic] — Recommendation: [One-liner]
[Link to full DR documents]

DEPENDENCY ESCALATIONS
• [Dep ID]: [Description] | Age: [X days] | From [Squad] to [Squad]
[Link to asks-and-owners log]

MILESTONE/RISK UPDATES
• [Brief summary if any slip signals or new high risks]

ACTION ITEMS FROM LAST SESSION
• [Action 1]: [Owner] — Status: [Complete / In Progress / Blocked]
• [Action 2]: [Owner] — Status: [Complete / In Progress / Blocked]

PRE-READ MATERIALS
• [Attach/link DR documents, data charts, etc.]

See you at [Time].
[Your Name], Program Manager
```

**Compliance Tracking:**
- Recipients must acknowledge receipt
- 100% compliance = all recipients ack within 24 hours
- Report compliance at session opening

---

## 10. Phase Gate Evidence Pack Template

**Prepared By:** Program Manager  
**Gate:** [M1/M2/M3]  
**Target Date:** [Date]

**Evidence Pack Contents:**

### 1. Executive Summary
- Gate name and target date
- Overall status (On track / At risk / Behind)
- Confidence level
- Key achievements since last gate
- Outstanding items with owners + dates

### 2. Milestone Table
- All milestones with target dates and status
- Slip history (if any)
- Next gate preview

### 3. Sprint Review Evidence
- Demo recordings/screenshots from golden demo tenant
- E2 parity burn-down chart (current %)
- UAT results per squad (Playwright-MCP green/red)
- KPI snapshots (velocity, DoR/DoD compliance, etc.)

### 4. Knowledge-Migration Gates (if applicable)
- Domains promoted since last gate
- Domains in promotion (current status)
- Evidence gaps with mitigation plans

### 5. Risk Register Snapshot
- Active risks by severity
- New risks since last gate
- Resolved risks
- Surprise escalations (count + root causes)

### 6. Dependency Status
- Total dependencies: resolved vs. active
- Aging dependencies (if any, with escalation plan)
- Cross-tribe blockers

### 7. Team Health Metrics
- Charter ratifications: [X%]
- Playbook certifications by role
- BMad adoption: [X%]
- Blocked time: [X%]

### 8. Decision Log
- DRs decided since last gate
- DRs deferred (with revisit dates)
- DRs pending (with aging)

### 9. Technical Stack Status
- Component health matrix (FE, BE, API, AI, Identity, Cloud, DB, CDN)
- Architecture Board decisions
- Contract changes approved

### 10. Next Phase Preview
- Next gate date and criteria
- Work planned for next phase
- Readiness estimate

**Delivery:**
- Dry run with Directors 1 week before gate
- Pre-read to VP 48 hours before gate
- Presentation on gate day (half day session)

---

## 11. Contact Directory

**VP & Directors:**

| Role | Name | Email | Teams | Office Hours |
|---|---|---|---|---|
| VP IT & Product | [Name] | [Email] | [Handle] | [Days/Times] |
| Dir Software Engineering | [Name] | [Email] | [Handle] | [Days/Times] |
| Dir AI Infrastructure & Ops | [Name] | [Email] | [Handle] | [Days/Times] |
| Dir Data Engineering | [Name] | [Email] | [Handle] | [Days/Times] |
| Dir Product Program & Scrum Mgmt | [Name] | [Email] | [Handle] | [Days/Times] |
| Dir Business Systems | [Name] | [Email] | [Handle] | [Days/Times] |

**Program Manager:**

| Role | Name | Email | Teams | Office Hours |
|---|---|---|---|---|
| Program Manager (AI SDLC) | [Your Name] | [Your Email] | [Your Handle] | [Days/Times] |

**Key Resources:**

| Resource | Location | Owner |
|---|---|---|
| Decision Requests | `vp-decisions/` folder | Program Manager |
| Milestone Tracker | [SharePoint link] | Program Manager |
| Risk Register | [SharePoint link] | Program Manager |
| Asks-and-Owners Log | [Location] | Program Manager |
| BMad Method Docs | https://docs.bmad-method.org/ | — |
| Technology Strategy | `TECHNOLOGY-STRATEGY.md` v1.5 | VP IT & Product |
| Requirements Catalog | `09-requirements-catalog.md` | Architects |
| Playbook Files | `14-28-*.md` files | Directors (by org) |

---

**End of Reference Materials**
