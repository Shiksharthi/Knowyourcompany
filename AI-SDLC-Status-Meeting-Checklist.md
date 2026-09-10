# AI SDLC Program Status Check — Pre-Meeting Checklist

**Program Manager:** [Your Name]  
**Meeting Date:** [Insert Date]  
**Preparation Time Required:** 60-90 minutes

---

## 24-48 Hours Before Meeting

### 📊 **Decision Request Queue Audit**
- [ ] Pull all active DRs from `vp-decisions/` folder
- [ ] Calculate median age (Target: ≤2 days, SLA: ≤5 days)
- [ ] Flag DRs aging >5 days for escalation
- [ ] Verify completeness: options + recommendation + blast radius
- [ ] Return incomplete DRs to submitters (kindly)
- [ ] Prepare DR summary slide: count, age distribution, aging items

---

### 🎯 **Milestone & Gate Evidence Collection**
- [ ] Review milestone table (from executive tracking sheet)
- [ ] Identify slip signals ≥2 weeks before gate
- [ ] Collect sprint review evidence:
  - [ ] Demo recordings/screenshots from golden demo tenant
  - [ ] E2 parity burn-down status (current %)
  - [ ] UAT results per squad (Playwright-MCP green status)
  - [ ] KPI snapshots (from delivery & quality review dashboards)
- [ ] Review gate table: current status vs. target dates
- [ ] Update milestone tracker with latest status

---

### 🔗 **Dependency Brokering Review**
- [ ] Pull asks-and-owners log from Scrum-of-Scrums (Wed sessions)
- [ ] Verify 100% of dependencies have owner + date
- [ ] Flag dependencies aging >1 week for auto-escalation
- [ ] Calculate dependency closure rate (this sprint)
- [ ] Identify cross-tribe blockers requiring Board/VP escalation
- [ ] Prepare dependency summary: total active, resolved, aging, escalations

---

### ⚠️ **Risk Register Refresh**
- [ ] Review risk register (monthly cycle)
- [ ] Check for new trigger events since last review
- [ ] Update mitigation status for active risks
- [ ] Classify risks: High / Medium / Low
- [ ] Document surprise escalations (Target: 0)
- [ ] Prepare risk summary: count by severity, top 2-3 high risks

---

### 📚 **Knowledge-Migration Gate Status**
- [ ] Review domain/promotion/design-partner registers
- [ ] Check promotion gate status for legacy domains
- [ ] Flag domains with unpromoted legacy context
- [ ] Identify evidence gaps ≥2 weeks before gate
- [ ] Verify source/SME coverage for active domains
- [ ] Document contradiction aging (anything >1 week without owner)

---

### 👥 **Adoption Tracking**
- [ ] Verify charter ratifications (Target: 100%)
- [ ] Review first-sprint checklist completion by squad
- [ ] Check playbook certifications by role:
  - [ ] Systems Engineers
  - [ ] Data Engineers  
  - [ ] Software Engineers
  - [ ] Product Owners
  - [ ] Architects
- [ ] Assess BMad workflow adoption (DoR compliance, Jira sync %)
- [ ] Pull blocked-time analytics (Target: <5%)

---

## 2-4 Hours Before Meeting

### 📝 **Pre-Read Preparation**
- [ ] Assemble pre-read deck/document:
  - [ ] Queue metrics summary
  - [ ] Milestone status with slip signals
  - [ ] Dependency aging report
  - [ ] Risk register snapshot
  - [ ] Adoption tracking dashboard
- [ ] Distribute pre-read to all attendees (via email/Teams)
- [ ] Set expectation: 100% pre-read compliance

---

### 🎤 **Talking Points & Slides**
- [ ] Finalize PPT with data from above sections
- [ ] Add context for escalations (why escalating, recommended action)
- [ ] Highlight wins (gates cleared, dependencies closed)
- [ ] Prepare 1-slide executive summary (program health at-a-glance)
- [ ] Include technical breakdown if needed (FE, BE, API, AI services, Apigee, Akamai, Ping, IAM, GCP, GKE, GCS, Database, Figma)
- [ ] Test demo tenant links (if showing live evidence)

---

### 🚨 **Escalation Preparation**
- [ ] Document escalations with:
  - [ ] Context (what's blocked, why it matters)
  - [ ] Options (with trade-offs)
  - [ ] Recommendation (your call)
  - [ ] Blast radius (scope of impact)
  - [ ] Owner + date for resolution
- [ ] Pre-brief Directors on sensitive escalations (no surprises)
- [ ] Prepare fallback plan if decision is deferred

---

## 1 Hour Before Meeting

### ✅ **Final Checks**
- [ ] Confirm all attendees received pre-read
- [ ] Test meeting room tech (screen share, projector)
- [ ] Load PPT and backup materials
- [ ] Print agenda for backup (if needed)
- [ ] Set timer for 30-minute hard stop
- [ ] Prepare action-item tracking sheet (live capture)

---

### 🎯 **Mental Prep**
- [ ] Review your role: **zero decision authority** — you present, VP decides
- [ ] Frame escalations as **data + options + recommendation** (not open questions)
- [ ] Prepare to timebox discussions (30 min = ~5 min per section)
- [ ] Be ready to capture action items with owner + date

---

## During Meeting

### 📋 **Live Capture**
- [ ] Open action-item log (shared doc or whiteboard)
- [ ] Capture decisions with owner + revisit date
- [ ] Note deferred items with follow-up deadline
- [ ] Track new dependencies/risks flagged during meeting

---

## Within 2 Hours After Meeting

### 📤 **Same-Day Publication (100% Compliance)**
- [ ] Publish meeting outcomes:
  - [ ] Decisions made (with owner + date)
  - [ ] Deferred items (with revisit date)
  - [ ] Action items (with owner + deadline)
  - [ ] Updated milestone table (if slips surfaced)
  - [ ] Updated risk register (if new risks added)
- [ ] Distribute to all attendees + affected squads
- [ ] Update tracking registers (dependencies, risks, gates)
- [ ] File VP decisions in `vp-decisions/` folder
- [ ] Schedule follow-ups for aging items

---

## Success Criteria
✅ Pre-read distributed 24 hours before meeting  
✅ 100% data accuracy (no surprises, no "I'll check and get back to you")  
✅ All aging items escalated with owner + date  
✅ Meeting outcomes published same day  
✅ Zero decision-shaped items left in PM hands (escalate or assign)

---

## Tools & References
- **Decision Requests:** `vp-decisions/` folder
- **Asks-and-owners log:** Scrum-of-Scrums notes
- **Milestone table:** Executive tracking sheet
- **Risk register:** Program risk log
- **Adoption tracking:** Squad onboarding dashboard
- **Evidence assembly:** Sprint review recordings + UAT results
- **BMad references:** https://docs.bmad-method.org/

---

## Notes
- **If a dependency ages >1 week:** Auto-escalate to Board or VP queue that same week
- **If a milestone slip is detected:** Notify VP + affected Directors immediately (don't wait for gate)
- **If pre-read compliance <100%:** Open meeting with compliance metric (gentle accountability)
