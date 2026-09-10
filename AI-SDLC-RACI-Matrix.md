# AI SDLC Program - RACI Matrix

**RACI Legend:**  
**R** = Responsible (Does the work)  
**A** = Accountable (Final decision authority)  
**C** = Consulted (Provides input)  
**I** = Informed (Kept in the loop)

---

## Governance & Decision-Making

| Activity | VP IT & Product | Dir Software Eng | Dir AI Infra | Dir Data Eng | Dir Product Program | Program Mgr | Product Owner | Architect |
|---|---|---|---|---|---|---|---|---|
| **Strategic Decisions** | **A** | C | C | C | C | I | I | C |
| **Technology Selection** | **A** | **R** | C | C | I | I | I | **R** |
| **Milestone Gate Approval** | **A** | C | C | C | C | **R** | I | C |
| **Executive Review Administration** | **A** | I | I | I | I | **R** | C | I |
| **Decision Request Triage** | **A** | I | I | I | I | **R** | C | I |
| **Architecture Decisions** | I | C | C | C | I | I | C | **A/R** |

---

## Program Operations

| Activity | VP IT & Product | Dir Software Eng | Dir AI Infra | Dir Data Eng | Dir Product Program | Program Mgr | Product Owner | Architect |
|---|---|---|---|---|---|---|---|---|
| **Dependency Brokering** | I | C | C | C | C | **R** | C | I |
| **Risk Register Maintenance** | **A** | C | C | C | C | **R** | I | I |
| **Evidence Assembly (Gate)** | **A** | I | I | I | C | **R** | C | I |
| **Sprint Planning** | I | I | I | I | C | I | **A/R** | C |
| **Backlog Refinement** | I | I | I | I | C | I | **A/R** | C |
| **DoR Gate Certification** | I | I | I | I | C | I | **A/R** | **A** |

---

## Product & Planning

| Activity | VP IT & Product | Dir Software Eng | Dir AI Infra | Dir Data Eng | Dir Product Program | Program Mgr | Product Owner | Architect |
|---|---|---|---|---|---|---|---|---|
| **PRD Approval** | **A** | I | I | I | C | I | **R** | C |
| **Epic Breakdown & Stories** | I | I | I | I | I | I | **A/R** | C |
| **Knowledge-Migration Gate** | **A** | I | I | I | C | **R** | C | **A** |
| **Design Partner Engagement** | **A** | I | I | I | C | **R** | C | I |
| **Product Brief Review** | **A** | C | C | C | C | I | **R** | C |

---

## Execution & Quality

| Activity | VP IT & Product | Dir Software Eng | Dir AI Infra | Dir Data Eng | Dir Product Program | Program Mgr | Product Owner | Architect |
|---|---|---|---|---|---|---|---|---|
| **Contract Review (API/MCP)** | I | C | C | C | I | I | C | **A/R** |
| **UAT & Demo Evidence** | I | I | I | I | C | **R** | **A** | I |
| **Sprint Review** | I | I | I | I | C | I | **A/R** | C |
| **Retrospective** | I | I | I | I | C | I | **A/R** | C |
| **Code Review** | I | **A** | C | C | I | I | C | C |
| **Security Controls** | **A** | C | **A/R** | I | I | I | I | **R** |

---

## Ceremonies Ownership

| Ceremony | VP IT & Product | Dir Software Eng | Dir AI Infra | Dir Data Eng | Dir Product Program | Program Mgr | Product Owner | Architect |
|---|---|---|---|---|---|---|---|---|
| **Executive Review (Tue/Thu)** | **A** (Chairs) | C | C | C | C | **R** (Admin) | C | I |
| **Scrum-of-Scrums (Wed)** | I | C | C | C | C | **R** (Facilitate) | C | I |
| **Architecture Board (Wed)** | I | C | C | C | I | I | C | **A/R** |
| **Portfolio Sync (Monthly)** | **A** | C | C | C | **A/R** | **R** (Assemble) | C | I |
| **Phase Gate (Quarterly)** | **A** | C | C | C | C | **R** (Admin) | C | C |

---

## Adoption & Team Health

| Activity | VP IT & Product | Dir Software Eng | Dir AI Infra | Dir Data Eng | Dir Product Program | Program Mgr | Product Owner | Architect |
|---|---|---|---|---|---|---|---|---|
| **Charter Ratification Tracking** | **A** | C | C | C | C | **R** | I | I |
| **Playbook Certifications** | **A** | **A/R** | **A/R** | **A/R** | **A/R** | **R** (Track) | I | I |
| **BMad Workflow Adoption** | I | C | C | C | **A** | **R** | C | C |
| **Team Onboarding** | I | **A/R** | **A/R** | **A/R** | **A/R** | **R** (Track) | I | I |

---

## Notes

### Program Manager Role (Zero Decision Authority)
- **The PgM prepares, administers, and follows through — NEVER decides**
- Files Decision Requests for anything decision-shaped
- Brokers dependencies to owner + date
- Chases aging items for escalation
- Assembles evidence and maintains registers
- Administers ceremonies on VP's behalf

### VP IT & Product (Final Decision Authority)
- All strategic, technology, and product decisions reserved to VP
- Chairs Executive Review (PgM administers)
- Approves gates and major milestones
- Decides on escalations

### Directors (Domain Accountability)
- Accountable for their domain's delivery and team health
- Represent their teams at Executive Review
- File Decision Requests for cross-domain issues
- Own playbook certifications for their teams

### Architects (Technical Authority)
- Accountable for architecture decisions and contract reviews
- Validate solutions against invariants (files 01-08)
- Lead Architecture Board
- Approve DoR for technical readiness

### Product Owners (Delivery Accountability)
- Accountable for sprint delivery and backlog health
- Own PRD, epic breakdown, and story creation
- Certify DoR (with Architect validation)
- Run sprint planning and reviews

---

## Escalation Paths (from RACI)

**Dependency aging >1 week:**  
PgM → Board/VP Queue (same week, automatic)

**Decision Request aging >SLA:**  
PgM flags in Tue metrics opening → VP decides or delegates with bounds

**Milestone slip signal:**  
PgM → VP + affected Directors (immediately, with data)

**Architecture question (undecided):**  
Squad/PO → Architect → Architecture Board → VP (if Board cannot resolve)

**Cross-Director conflict:**  
Directors → VP Decision Request (never PgM-mediated decision)

**Product question (undecided mid-sprint):**  
PO → PM → VP Decision Request (tracked as PM process failure in retro)
