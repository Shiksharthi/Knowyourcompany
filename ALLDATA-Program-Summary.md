# ALLDATA Global Enterprise SaaS Platform - Program Summary

## 1. What is the Program Name?

**ALLDATA Global Enterprise SaaS Platform - Replatforming and Rearchitecting Initiative**

This is a comprehensive program to rebuild ALLDATA's entire technology platform end-to-end on a modern, AI-first, globally scalable architecture.

---

## 2. What Program Strategy is Being Used?

### Multi-Pronged Strategy:

**A. Phased Execution Strategy (5 Phases)**
- **Phase 1 (Aug-Nov 2026)**: Foundations & Golden Path - 36 engineers
- **Phase 2 (Nov 2026-Jun 2027)**: Full-rate parallel build - scaling to ~120 engineers
- **Phase 3 (Jun-Oct 2027)**: Parity, enterprise features, GA
- **Phase 4 (Nov 2027-2028)**: Migration at scale
- **Phase 5 (2028+)**: Dominance & expansion

**B. Technology Strategy:**
- **Buy protocols, build product** - Use licensed estate (Ping, Zuora, Dynamics, Apigee, GCP)
- **AI-first development** - Every choice scored on "can an AI agent build on it, operate it, and be governed by it?"
- **One global codebase, many cells** - Deploy identically to every region
- **Contracts-first** - All APIs from OpenAPI specs, generated clients

**C. Organizational Strategy:**
- Wave-based hiring (36 → 76 → 120 engineers)
- Blended teams (ALLDATA + 66 Degrees partner)
- Domain-aligned tribes (6 tribes, ~19 squads)

---

## 3. What is BMad Method or Framework?

### BMad (Business-Managed Application Development) Method

**BMad is an AI-native development methodology** that uses AI agents to accelerate software delivery while maintaining quality and governance.

### Four Core Phases:

1. **Analysis** 
   - Understand the business problem
   - Research domain, users, constraints
   - Output: Analysis artifacts, research findings

2. **Planning (PRD)**
   - Define what to build
   - Create Product Requirements Document
   - Output: Feature PRD, acceptance criteria

3. **Solutioning (Architecture)**
   - Design how to build it
   - Technical architecture, UX design
   - Output: Architecture docs, UX specs, contracts

4. **Implementation**
   - Build the feature
   - Code, test, deploy
   - Output: Working software, tests, documentation

### Key BMad Artifacts:

```
📁 _bmad-output/
├── planning-artifacts/
│   ├── prd.md (Product Requirements)
│   ├── architecture.md (Technical Design)
│   ├── ux/ (User Experience specs)
│   └── vp-decisions/ (Decision records)
├── stories/
│   ├── STORY-001-create-tenant.md
│   └── STORY-002-user-login.md
└── sprints/
    └── SPRINT-2026-W32/
        ├── plan.yaml
        └── status.yaml
```

### How BMad Works with AI:

**Human Role:**
- Define WHAT to build (requirements)
- Make decisions
- Review and approve

**AI Agent Role:**
- Research and analyze
- Generate code from requirements
- Create tests automatically
- Update documentation
---

## 4. What is the Program Objective?

### Primary Objective:

**Build out a migration-ready, globally scalable SaaS platform by October 2027 that enables:**
- Migration of 115,000+ shops from legacy systems
- Support for US, EU, and preparation for ANZ/South Africa markets
- 99.99% availability
- AI-first development and agent-native operations

### Specific Deliverables by Oct 2027:

1. **Shop Manager** at migration-grade parity
2. **Repair** platform at migration-grade parity  
3. **Portal** (tenant control plane) - Phases A & B complete
4. **Enterprise identity** (SSO, SCIM) operational
5. **Agentic/API platform** (P1/P2) live
6. **First production migration cohorts** successfully moved
7. **GA (General Availability)** achieved

### Constraints:

- Maximum **~120 FTE** across all domains
- **Legacy platform continues running** in parallel (no big-bang)
- Must support **arbitrary-depth org tree** (partner → franchise → region → shop)
- **Three revenue channels**: direct sales, franchise, partner/distributor

---

## 5. What is the Program Goal?

### Overarching Goal:

**Transform ALLDATA into a modern, AI-first, multi-tenant SaaS platform that dominates the automotive repair data industry through:**

1. **Technical Excellence**
   - World-class developer experience
   - Agent-native operations
   - Enterprise-grade security and compliance

2. **Business Model Innovation**
   - Support direct, franchise, and partner sales
   - Enable data products (API/MCP) as new revenue stream
   - Platform for AI-powered workflows

3. **Market Leadership**
   - First-mover advantage in agentic automotive repair
   - Network effects through "Shops Like Mine" benchmarking
   - Unmatched data moat (100k+ shops operational reality)

### Success Metrics:

- **Migration Success**: 100k+ shops migrated by end of 2028
- **Availability**: 99.99% uptime measured annually
- **AI Velocity**: ≥2× conventional development speed
- **Quality**: Zero cross-tenant security incidents
- **Compliance**: SOC 2 Type II, ISO 27001, GDPR ready

---

## 6. What are the Program OKRs?

### Three-Tier Cascaded OKRs:

The program uses a **three-tier goal cascade** across five themes:

#### **Tier 1 - Executive (VP IT & Product)**

| Theme | Objective | Key Results |
|-------|-----------|-------------|
| **E1: Velocity** | Prove and sustain the AI-velocity bet | • AI-velocity multiple ≥2× baseline by M1<br>• Cost/accepted story trending down<br>• Median story cycle time trending down |
| **E2: Value Delivery** | Hit migration-grade parity and GA on mandate | • M1–M6 milestones on schedule<br>• Shop Manager/Repair corpora promoted by M1<br>• Design-partner personas covered<br>• Cohorts migrated pre-GA |
| **E3: Quality & Trust** | Zero trust-destroying events | • 0 cross-tenant incidents<br>• 99.99% availability per-tenant annual<br>• Audit delivery SLO ≥99.9% ≤5 min<br>• Quarterly drills passed |
| **E4: Efficiency** | Cost-to-serve and cost-to-build inside envelope | • Cost-to-serve per tenant ≤ budget<br>• Infra $/engineer flat as headcount 3×<br>• AI spend per merged story trending down |
| **E5: Governance** | Decisions never become bottleneck | • VP Decision Request turnaround ≤5 days (aim 2)<br>• Sprint time blocked-on-decision <5%<br>• Wave onboarding ramp ≤2 weeks |

#### **Tier 2 - Manager (Squad Leads)**

| Theme | Objective | Key Results |
|-------|-----------|-------------|
| **M1: Velocity** | Keep flow moving | • Squad median MR cycle time ≤48h<br>• Merge-train success ≥95% |
| **M2: Value Delivery** | Predictable sprint delivery | • Sprint plan completion 80–90%<br>• Carryover <15% |
| **M3: Quality** | Ship it right first time | • Escaped defects/sprint decreasing<br>• Probe+UAT green rate ≥98%<br>• First-pass DoD ≥85%<br>• 0 flags past expiry |
| **M4: Efficiency** | Golden-path adherence | • ≥95% stories via generators/BMad<br>• Seed+UAT extension 100%<br>• Rework rate <10% |
| **M5: Governance** | Unblock fast | • Decision Requests filed pre-sprint ≥80%<br>• Blocked-time/story decreasing<br>• Retro closure ≥90% |

#### **Tier 3 - Individual Contributor (Engineer + Agent Pair)**

| Theme | Objective | Key Results |
|-------|-----------|-------------|
| **I1: Velocity** | Small, fast, dark | • Story cycle time median ≤3 days<br>• MR size within squad norm |
| **I2: Value Delivery** | Finish what story says | • AC met first demo ≥90%<br>• Zero silent scope drift |
| **I3: Quality** | First-pass clean | • Review-chain first-pass ≥80%<br>• DoD complete at MR open 100% |
| **I4: Efficiency** | Ride golden path | • 100% generator scaffolds<br>• Zero hand-rolled platform logic |
| **I5: Governance** | Never assume; never block | • Review turnaround ≤4 hours<br>• 0 assumption-based rework<br>• Findings resolved ≤24h |


---

## 7. What are the Program KPIs?

### Auto-Collected KPIs (No Manual Reporting):

#### **Executive KPIs (E-tier)**

**Velocity:**
- AI-velocity multiple vs frozen baseline
- Median story cycle time trend
- Cost per accepted story
- Token/compute cost per feature

**Value Delivery:**
- Milestone schedule adherence (M1-M6 on time)
- Domain corpus promotion status (Shop Manager, Repair)
- Design-partner persona coverage
- Migration cohort completion

**Quality & Trust:**
- Cross-tenant incidents (target: 0)
- Availability % per-tenant, measured annually
- Audit delivery SLO (≥99.9%, ≤5 min)
- Quarterly drill pass/fail

**Efficiency:**
- Cost-to-serve per tenant per cell
- Infrastructure $ per engineer
- AI spend per merged story

**Governance:**
- VP Decision Request median turnaround (target ≤5 days)
- % sprint time blocked on decisions (target <5%)
- Wave onboarding ramp time

#### **Manager KPIs (M-tier)**

**Flow:**
- Squad median MR cycle time (open→merged)
- Merge train success rate
- WIP limits adherence

**Delivery:**
- Sprint plan completion %
- Carryover %
- Epic burn-down vs phase plan

**Quality:**
- Escaped defects per sprint
- Probe + UAT green rate
- First-pass DoD %
- Expired flags count

**Efficiency:**
- Stories via generators/BMad %
- Seed+UAT extension compliance
- Rework rate

**Enablement:**
- Decision Requests filed pre-sprint %
- Blocked time per story
- Flight simulator graduation rate
- Retro action closure rate

#### **Individual KPIs (I-tier)**

**Cycle Time:**
- Story cycle time (in-progress→merged-dark)
- MR size

**Quality:**
- Review-chain first-pass %
- DoD complete at MR open %

**Adherence:**
- Generator scaffold usage
- Hand-rolled platform logic count

**Collaboration:**
- Review turnaround time
- Assumption-based rework count
- Finding resolution time

### KPI Collection Methods:

| KPI Source | Collection Method | Frequency |
|------------|------------------|-----------|
| **GitLab CI/CD** | Pipeline events → BigQuery | Real-time |
| **Jira** | Atlassian MCP Server | Daily sync |
| **Code Metrics** | nx affected, SonarQube | Per MR |
| **Deployment** | Argo CD events | Per deploy |
| **Costs** | GCP billing API | Daily |
| **Availability** | Cloud Monitoring | Continuous |
| **Audit** | Probo/CISO Assistant | Real-time |

### Dashboard Hierarchy:

```
Friday Auto-Publish (No Meeting):
├─ Executive Dashboard (E-tier KPIs)
│  └─ VP IT & Product view
│
├─ Tribe Dashboards (M-tier KPIs)  
│  └─ Director + Squad Lead view
│
└─ Squad Dashboards (I-tier KPIs)
   └─ Individual engineer view
```

---

## 8. What are the Benefits?

### **A. Business Benefits**

1. **Revenue Growth**
   - New revenue stream: API/MCP data products
   - Enable partner/franchise channel expansion
   - Self-serve purchasing increases conversion

2. **Market Expansion**
   - Global reach: US, EU, ANZ, South Africa
   - New verticals: Fleet management, insurance validation, legal services
   - Agent-as-distribution channel

3. **Cost Efficiency**
   - Exploit licensed estate (Ping, Zuora, Dynamics, Apigee)
   - Reduce support costs through self-service
   - Lower customer acquisition cost

4. **Competitive Advantage**
   - First-mover in agentic automotive repair
   - Data moat: 100k+ shops operational reality
   - "Shops Like Mine" benchmarking (network effect)

### **B. Technical Benefits**

1. **Developer Velocity**
   - ≥2× faster development vs conventional methods
   - Golden path eliminates rework
   - AI agents handle repetitive tasks

2. **Quality Improvement**
   - Zero cross-tenant incidents (database-enforced isolation)
   - 99.99% availability target
   - Immutable audit trail

3. **Scalability**
   - One codebase, many cells (US, EU, ANZ, ZA)
   - Supports arbitrary-depth org tree
   - Horizontal scaling on GKE Autopilot

4. **Maintainability**
   - Contracts-first (always in sync)
   - Generated code follows patterns
   - Documentation auto-generated

### **C. Operational Benefits**

1. **Compliance Ready**
   - SOC 2 Type II, ISO 27001, GDPR by design
   - Audit trail built-in
   - Evidence automation

2. **Multi-Tenant Efficiency**
   - Shared infrastructure
   - Per-tenant isolation
   - Efficient resource usage

3. **Disaster Recovery**
   - Multi-region active-active
   - Quarterly failover drills
   - <5 minute RTO target

4. **Observability**
   - Real-time monitoring
   - Automated alerting
   - Cost tracking per tenant

### **D. Customer Benefits**

1. **Better Experience**
   - Faster, more reliable platform
   - AI-powered assistance
   - Mobile-first for technicians

2. **More Control**
   - Self-service tenant management
   - SSO/SCIM for enterprises
   - Customizable workflows

3. **Better Insights**
   - KPI dashboards
   - Benchmarking vs peers
   - Predictive maintenance

4. **Global Access**
   - Multi-region deployment
   - Local data residency
   - 24/7 availability

### **E. Strategic Benefits**

1. **Future-Proof Architecture**
   - Agent-native from day one
   - Extensible platform
   - Replaceable vendors (seams)

2. **Innovation Platform**
   - Rapid feature deployment
   - A/B testing via flags
   - Progressive rollouts

3. **Data Monetization**
   - API products
   - Agentic tools
   - Benchmarking insights

4. **Partnership Enablement**
   - Partner/distributor support
   - Franchise management
   - Integration ecosystem

### **Example Benefit Realization:**

**Scenario: Franchise Customer (500 shops)**

**Before (Legacy Platform):**
- No visibility across locations
- Manual consolidation of reports
- Cannot set labor rates centrally
- Support via phone only

**After (New Platform):**
- Real-time rollups (per-store and all-at-once)
- Automated KPI dashboards
- Config-down-tree (set rates once)
- Audited take-over for support
- Result: 20 hours/week saved in reporting

---

## 9. What Program Metrics are Addressed?

### **Velocity Metrics**

**Development Speed:**
- Story cycle time (in-progress → merged)
- MR cycle time (open → merged)
- Time to first deployment
- Release frequency

**AI Effectiveness:**
- AI-velocity multiple vs baseline
- Agent-authored code %
- First-pass acceptance rate
- Token cost per feature

**Flow Efficiency:**
- Work in progress (WIP)
- Blocked time %
- Merge train success rate
- PR environment spin-up time

### **Quality Metrics**

**Code Quality:**
- First-pass DoD %
- Review chain pass rate
- Code coverage %
- Security scan findings

**Product Quality:**
- Escaped defects per sprint
- Production incidents
- Bug fix time
- Customer-reported issues

**Test Coverage:**
- Unit test coverage
- Integration test coverage
- UAT automation coverage
- Probe suite pass rate

### **Delivery Metrics**

**Sprint Performance:**
- Sprint completion %
- Carryover %
- Velocity (story count)
- Epic burn-down rate

**Release Performance:**
- Deployment frequency
- Lead time for changes
- Time to restore service
- Change failure rate

**Migration Progress:**
- Cohorts migrated
- Parity gaps closed
- Beta shop satisfaction
- Migration success rate

### **Operational Metrics**

**Availability:**
- Uptime % per tenant
- Uptime % per cell
- Mean time to detect (MTTD)
- Mean time to recover (MTTR)

**Performance:**
- API response time (p50, p95, p99)
- Database query time
- Page load time
- Mobile app performance

**Scalability:**
- Concurrent users
- Requests per second
- Data growth rate
- Cost per tenant

### **Compliance Metrics**

**Security:**
- Cross-tenant incidents
- Security vulnerabilities
- Pen test findings
- Access violations

**Audit:**
- Audit trail completeness
- Audit delivery SLO
- Evidence collection %
- Control effectiveness

**Privacy:**
- GDPR compliance %
- Data residency compliance
- Retention policy adherence
- Right-to-erasure response time

### **Cost Metrics**

**Infrastructure:**
- Cost per tenant
- Cost per transaction
- Cloud spend vs budget
- Resource utilization

**Development:**
- Cost per story
- Cost per deploy
- Tool licensing costs
- AI/token costs

**Efficiency:**
- Infrastructure $/engineer
- Support cost per tenant
- Automation savings
- Waste reduction

### **Governance Metrics**

**Decision Velocity:**
- VP Decision Request turnaround
- Aging queue count
- Blocked sprint time %
- Escalation rate

**Process Compliance:**
- DoR compliance %
- DoD compliance %
- Golden path adherence
- Generator usage %

**Knowledge Management:**
- Domain corpus promotion %
- Context promotion compliance
- Documentation coverage
- Training completion rate

### **Customer Metrics**

**Adoption:**
- Active users
- Feature utilization
- Mobile adoption
- API usage

**Satisfaction:**
- NPS score
- Support ticket volume
- Beta feedback score
- Churn rate

**Value Realization:**
- Time to value
- ROI per customer
- Renewal rate
- Expansion revenue

## 10. What Business Value, Strategic Value and Technical Value Will This Program Address?

### **A. BUSINESS VALUE**

#### **1. Revenue Impact**

**New Revenue Streams:**
- **API/MCP Data Products**: $XX million ARR potential
  - Flat-rate subscriptions
  - Metered usage (API calls, agent interactions)
  - Data products for insurers, fleets, OEMs
  
- **Self-Service Purchasing**: Instant activation, reduced sales friction
  - In-product upsells
  - Feature unlock at point of need
  - Channel-aware (direct, franchise, partner)

- **Premium Features**:
  - Franchise roll-ups and control
  - Advanced analytics
  - Benchmarking ("Shops Like Mine")

#### **2. Market Expansion**

**Geographic Growth:**
- **Current**: US, Canada, Mexico, Germany, UK, EU
- **Phase 5+**: Australia/New Zealand (2028), South Africa (2029)
- **Advantage**: Built-in multi-region from day one

**Vertical Expansion:**
- **Fleet Management**: Large vehicle fleet customers
- **Insurance**: Claims validation, warranty verification
- **Legal**: Authoritative repair data for litigation

**Channel Expansion:**
- **Direct Sales**: Self-serve for SMB shops
- **Franchise**: MSO/dealer group management
- **Partner/Distributor**: Wholesale and agency models

#### **3. Cost Reduction**

**Support Cost Savings:**
- Self-service tenant management: -30% support tickets
- In-product AI assistant: -40% tier-1 support
- Automated provisioning: -80% provisioning time

**Infrastructure Efficiency:**
- Multi-tenant architecture: 10:1 efficiency vs single-tenant
- Auto-scaling: Pay only for usage
- Exploit licensed estate: $XX million saved vs rebuilding

**Development Efficiency:**
- AI-assisted development: 2× velocity
- Reduced rework: Golden path compliance
- Faster time-to-market: Weeks → Days

#### **4. Customer Lifetime Value**

**Improved Retention:**
- 99.99% availability → Less churn
- Better features → Higher satisfaction
- Enterprise features → Longer contracts

**Increased ARPU:**
- Upsell premium features
- Add-on data products
- API/agent access tiers

**Expansion Revenue:**
- Franchise grows → More locations on platform
- Shop success → More features purchased
- Network effects → Benchmarking value increases

### **B. STRATEGIC VALUE**

#### **1. Competitive Moat**

**Data Network Effects:**
- 115,000+ shops → Unmatched operational data
- "Shops Like Mine" benchmarking
- AI training on real repair data
- Competitors cannot replicate at any price

**First-Mover Advantage:**
- **Agentic platform**: No incumbent has MCP/agent-native platform
- Industry survey (July 2026): Zero competitors with governed agent platform
- 12-18 month lead time

**Technology Leadership:**
- AI-first development
- Agent-native operations
- Governed write-actions (unique differentiator)

#### **2. Market Position**

**Industry Consolidation:**
- Migrate 100k+ shops from legacy
- Become the standard platform
- Lock-in through network effects

**OEM Relationships:**
- Authoritative repair data provider
- Compliance ready (SERMI, TISAX)
- Trusted partner for right-to-repair

**Ecosystem Platform:**
- Parts suppliers integrate (AutoZone+)
- Tool manufacturers connect
- Insurance/fleet/legal adjacencies

#### **3. M&A Readiness**

**Acquisition Target Attractiveness:**
- Modern tech stack
- Scalable architecture
- Recurring revenue model
- Data assets

**Platform for Acquisitions:**
- Easy integration via APIs
- Multi-tenant by design
- Proven migration machinery

#### **4. Future-Proofing**

**Technology Independence:**
- Vendor seams enable swapping
- Not locked into any single cloud/tool
- 3-year vendor commitment horizon

**Regulatory Compliance:**
- GDPR, SOC 2, ISO 27001 by design
- Multi-jurisdiction ready
- AI Act compliant

**Emerging Technologies:**
- Agent-first architecture
- MCP standard adoption
- Future model swappable

### **C. TECHNICAL VALUE**

#### **1. Architecture Excellence**

**Scalability:**
- Horizontal scaling (add cells)
- Supports arbitrary org depth
- 100k+ tenants on shared infrastructure

**Reliability:**
- 99.99% availability target
- Multi-region active-active
- Quarterly failover drills

**Security:**
- Database-enforced isolation (RLS)
- Zero cross-tenant incidents target
- Immutable audit trail

**Performance:**
- <100ms API response (p95)
- Offline-capable mobile
- Edge caching for content

#### **2. Developer Experience**

**Velocity:**
- ≥2× faster than baseline
- Golden path generators
- AI-assisted development

**Quality:**
- Contracts-first (always in sync)
- Auto-generated tests
- Consistent patterns

**Onboarding:**
- New developer productive in <1 hour
- Flight simulator training
- Comprehensive docs (auto-generated)

**Maintenance:**
- One codebase, many deployments
- Feature flags for progressive rollout
- Automated dependency updates

#### **3. Operational Excellence**

**Observability:**
- Real-time monitoring
- Distributed tracing
- Cost attribution per tenant

**Compliance Automation:**
- Evidence pipeline
- Continuous controls
- Audit-ready reports

**Disaster Recovery:**
- RTO <5 minutes
- RPO <60 seconds
- Automated failover

**Cost Management:**
- Per-tenant cost tracking
- Right-sizing recommendations
- Spot instance usage

#### **4. Integration Capabilities**

**API-First:**
- OpenAPI specs
- Generated clients
- Versioned contracts

**Event-Driven:**
- Pub/Sub architecture
- Webhooks
- Real-time updates

**Agent-Native:**
- MCP servers
- OAuth-based access
- Governed actions

**Partner Ecosystem:**
- Standard integrations
- Apigee management
- Rate limiting/quotas
---

## 11. What Artifacts Does the Program Manager Need to Create for Each Phase and Gating Criteria?

### **Phase-by-Phase Artifact Requirements**

---

### **PHASE 1: FOUNDATIONS & GOLDEN PATH (Aug–Nov 2026)**

#### **Gate Criteria (Milestone M1 - Nov 2026):**
✓ Golden-path demo (generate → deployed service, untouched by hand)
✓ Tenant provisioned end-to-end in <1 hour
✓ Demo tenant seeded in all environments
✓ UAT harness green in CI
✓ Cell failover drill #1 executed
✓ Shop Manager + Repair domain corpora promoted
✓ AI-SDLC v1 released with rollback
✓ Flight simulator graduation demonstrated
✓ Vanguard velocity report (≥2× baseline with quality held)

#### **Program Manager Artifacts:**

**1. Program Charter & Roadmap**
```
Artifact: program-charter.md
BMad Method: bmad-product-brief

Content:
- Vision and objectives
- Scope (in/out of scope)
- Success criteria
- Stakeholder matrix
- Phase 1 roadmap with milestones
- Resource plan (36 vanguard → 120 scale)
- Budget and timeline
- Risk register

How to Create:
1. Run: bmad-product-brief
2. Prompt: "Create program charter for ALLDATA replatforming"
3. Input: Technology strategy, business requirements
4. Review: With VP IT & Product
5. Approve: Executive Review
6. Store: _bmad-output/planning-artifacts/charter/
```

**2. Squad Charters (6 tribes, ~6 vanguard squads)**
```
Artifact: squad-charters.md
BMad Method: bmad-product-brief per squad

Content per squad:
- Mission and scope
- Domain ownership (Nx boundaries)
- Responsibilities
- Interfaces with other squads
- Success metrics
- Squad composition

How to Create:
1. Run: bmad-product-brief for each squad
2. Prompt: "Define charter for [Platform Core / Shop Manager / etc] squad"
3. Input: Chapter 12 squad charters
4. Review: Architecture & Contract Review Board
5. Approve: VP IT & Product
6. Store: _bmad-output/planning-artifacts/squads/
```

**3. VP Decision Request Register**
```
Artifact: vp-decisions/register.md
Manual tracking + BMad support

Content:
- All open VP Decision Requests
- Status: Open, Decided, Deferred, Delegated
- Owner, date filed, decision deadline
- Decision outcome and rationale

How to Create:
1. Template in: _bmad-output/planning-artifacts/vp-decisions/
2. Each DR: NNN-<slug>.md with:
   - Context
   - Options
   - Recommendation
   - Blast radius
   - Urgency
3. Track: Spreadsheet or Jira board
4. Update: After Tue/Thu Executive Review
5. Publish: Same day to all stakeholders
```

**4. Risk & Issue Register**
```
Artifact: risks-issues.md
Manual tracking

Content:
- Risk ID, description, probability, impact
- Mitigation plan
- Owner
- Status
- Issues with severity and resolution

How to Create:
1. Initial: Extract from strategy docs
2. Weekly: Update from tribe standups
3. Review: Monthly portfolio sync
4. Escalate: High risks to Executive Review
5. Store: _bmad-output/program-mgmt/
```

**5. Domain Knowledge Migration Plan**
```
Artifact: knowledge-migration-plan.md
BMad Method: bmad-technical-research

Content:
- Shop Manager domain plan
- Repair domain plan
- Evidence capture schedule
- SME interview plan
- Promotion criteria
- Traceability requirements

How to Create:
1. Run: bmad-technical-research
2. Prompt: "Create knowledge migration plan for [domain]"
3. Input: Chapter 29 requirements
4. Review: With domain curators
5. Approve: Director of Product Program
6. Track: Promotion register
```

**6. Dependency Matrix**
```
Artifact: dependency-matrix.xlsx
Manual tracking

Content:
- Cross-squad dependencies
- Status: Identified, In Progress, Blocked, Resolved
- Owner (providing squad)
- Requester (consuming squad)
- Target date
- Impact if delayed

How to Create:
1. Source: Wednesday Scrum-of-Scrums
2. Update: After each SoS
3. Escalate: Aging >1 week to Contract Board
4. Publish: Weekly to all squads
5. Tool: Spreadsheet or Jira dependencies
```

**7. Phase 1 Progress Dashboard**
```
Artifact: Looker Studio dashboard
Auto-generated from BigQuery

Content:
- 21 Phase 1 items completion %
- Vanguard velocity metrics
- AI-velocity multiple vs baseline
- Quality metrics (first-pass DoD, escaped defects)
- Cost metrics ($/story, token costs)
- Blocked time trending

How to Create:
1. Data sources: GitLab CI/CD → BigQuery
2. Dashboard: Looker Studio template
3. Refresh: Real-time
4. Publish: Friday auto-publish (no meeting)
5. Review: Weekly Executive Review
```

**8. M1 Gate Evidence Pack**
```
Artifact: M1-gate-evidence.md
Compiled from multiple sources

Content:
- Golden path demo recording
- Provisioning time evidence (screenshot <1 hour)
- UAT test results
- Failover drill report
- Domain corpus promotion certificates
- Velocity baseline comparison report
- Flight simulator graduation records
- AI-SDLC release notes

How to Create:
1. Collect: From all squads week 12
2. Compile: Into single evidence document
3. Review: Dry run at week 12
4. Present: M1 gate review week 13
5. Archive: For audit trail
---

## 13. How Can Program Manager Automate Reporting and Monitoring Using BMad Method?
---

### **STEP 1: Set Up Data Collection Infrastructure**

#### **1.1 Configure GitLab CI/CD Event Pipeline**

**What to Automate:**
- MR cycle time (open → merged)
- Review chain pass rate
- Pipeline success rate
- Merge train metrics
- Deployment frequency
---

## 14. How to Capture All Program Metrics Using BMad Method

### **Complete Metrics Collection Framework**

---

### **A. VELOCITY & THROUGHPUT METRICS**

#### **Development Velocity**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| AI Velocity Multiple | GitLab CI/CD → BigQuery calculation | bmad-sprint-status | Weekly | ≥2.0× |
| Story Cycle Time | Jira status transitions | bmad-sprint-status | Per story | ≤3 days |
| MR Cycle Time | GitLab merge request events | Automated | Per MR | ≤48 hours |
| Lines of Code per Story | GitLab diff stats | Automated | Per MR | Trend only |
| Stories Completed per Sprint | Jira sprint reports | bmad-sprint-status | Sprint | 80-90% plan |
| Epic Burn-down Rate | Jira epic progress | bmad-product-brief | Weekly | On track |
| Features Shipped per Month | Release tags | Automated | Monthly | Increasing |
| Time to First Deploy | GitLab pipeline timestamps | Automated | Per feature | <1 day |
| Deployment Frequency | Argo CD events | Automated | Daily | Multiple/day |
| Lead Time for Changes | Git commit → production | DORA metrics | Weekly | <7 days |
---

#### **Agent Effectiveness**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Agent-Authored Code % | Git commit metadata | Automated | Weekly | Trend |
| Token Cost per Feature | Inference gateway logs | Automated | Per feature | Decreasing |
| First-Pass AI Acceptance | Code review outcomes | bmad-code-review | Per MR | ≥80% |
| Agent Prompt Success Rate | BMad tool logs | Automated | Daily | ≥90% |
| Human Intervention Rate | Review chain data | Automated | Weekly | Decreasing |
| Code Generation Time | BMad skill duration | Automated | Per story | Minutes |
| Test Auto-Generation % | Test coverage analysis | Automated | Per MR | ≥90% |

---

### **B. QUALITY METRICS**

#### **Code Quality**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| First-Pass DoD % | GitLab MR reviews | Automated | Per MR | ≥85% |
| Review Chain Pass Rate | CodeRabbit + Gemini + Human | Automated | Weekly | ≥80% |
| Code Coverage % | Jacoco + Jest reports | Automated | Per MR | ≥80% |
| SonarQube Quality Gate | Sonar API | Automated | Per MR | Pass |
| Security Scan Findings | Fortify + Grype | Automated | Per MR | 0 critical |
| Code Smells | SonarQube metrics | Automated | Weekly | Decreasing |
| Technical Debt Ratio | SonarQube metrics | Automated | Monthly | <5% |
| Cyclomatic Complexity | SonarQube metrics | Automated | Per MR | <15 avg |
---

#### **Product Quality**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Escaped Defects per Sprint | Jira bug tracking | bmad-sprint-status | Sprint | <5 |
| Production Incidents | PagerDuty + Jira | Automated | Real-time | Decreasing |
| Bug Fix Time (MTTR) | Jira issue lifecycle | Automated | Per bug | <24 hours |
| Customer-Reported Issues | D365 CS + Jira | Automated | Weekly | Decreasing |
| Critical Bugs Open | Jira dashboard | Automated | Daily | 0 |
| Bug Reopen Rate | Jira transitions | Automated | Monthly | <5% |
| Defect Density | Bugs / KLOC | Calculated | Monthly | <1.0 |

---

### **C. DELIVERY & SPRINT METRICS**

#### **Sprint Performance**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Sprint Completion % | Jira sprint report | bmad-sprint-status | Sprint | 80-90% |
| Sprint Carryover % | Jira sprint report | bmad-sprint-status | Sprint | <15% |
| Velocity (Story Count) | Jira sprint metrics | bmad-sprint-status | Sprint | Stable |
| Sprint Goal Achievement | Manual assessment | bmad-retrospective | Sprint | ≥90% |
| Stories Added Mid-Sprint | Jira sprint changes | Automated | Sprint | <10% |
| Blocked Stories | Jira status | Automated | Daily | <3 |
| Sprint Predictability | Completed / Planned | bmad-sprint-planning | Sprint | 85-95% |

---

#### **Release Performance (DORA Metrics)**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Deployment Frequency | Argo CD events | Automated | Weekly | Multiple/day |
| Lead Time for Changes | Git → production time | Automated | Per deploy | <7 days |
| Change Failure Rate | Failed deploys / total | Automated | Weekly | <15% |
| Time to Restore Service | Incident MTTR | PagerDuty | Per incident | <1 hour |
| Rollback Rate | Deployment rollbacks | Argo CD | Weekly | <5% |
| Deploy Success Rate | Successful deploys | Argo CD | Weekly | ≥95% |

---

### **D. OPERATIONAL METRICS**

#### **Availability & Reliability**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Uptime % per Tenant | Cloud Monitoring | Automated | Continuous | 99.99% |
| Uptime % per Cell | Cloud Monitoring | Automated | Continuous | 99.99% |
| API Availability | Apigee analytics | Automated | Real-time | 99.99% |
| Mean Time to Detect (MTTD) | Alert timestamps | Automated | Per incident | <2 min |
| Mean Time to Recover (MTTR) | Incident lifecycle | PagerDuty | Per incident | <5 min |
| Error Rate | Cloud Error Reporting | Automated | Real-time | <0.1% |
| SLO Compliance | SLO dashboard | Automated | Weekly | 100% |
---

#### **Performance**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| API Response Time (p50) | Apigee analytics | Automated | Real-time | <50ms |
| API Response Time (p95) | Apigee analytics | Automated | Real-time | <100ms |
| API Response Time (p99) | Apigee analytics | Automated | Real-time | <200ms |
| Database Query Time | AlloyDB insights | Automated | Continuous | <10ms avg |
| Page Load Time (Web) | Quantum Metric | Automated | Real-time | <2s |
| Mobile App Performance | Sentry RN | Automated | Real-time | <3s |
| Cache Hit Rate | Redis metrics | Automated | Hourly | ≥90% |
| CDN Hit Rate | Cloud CDN | Automated | Hourly | ≥95% |

---

### **E. COST & EFFICIENCY METRICS**

#### **Development Efficiency**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Cost per Story | GCP billing / story count | Calculated | Weekly | Decreasing |
| Cost per Deploy | GCP billing / deploy count | Calculated | Weekly | Decreasing |
| Infrastructure $/Engineer | GCP billing / headcount | Calculated | Monthly | Flat |
| AI Spend per Story | Token costs / story count | Calculated | Weekly | Decreasing |
| Rework Rate % | Re-opened MRs / total MRs | Automated | Weekly | <10% |
| Golden Path Adherence % | Generator usage / total | Automated | Weekly | ≥95% |
| Generator Usage % | Stories via generators | bmad-create-story | Weekly | 100% |

---

#### **Infrastructure Costs**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Cost per Tenant | GCP billing / tenant count | Calculated | Monthly | Decreasing |
| Cost per Transaction | GCP billing / transaction count | Calculated | Weekly | <$0.001 |
| Cloud Spend vs Budget | GCP billing API | Automated | Daily | Within 5% |
| Resource Utilization % | GKE metrics | Automated | Hourly | 70-85% |
| Wasted Resources $ | Right-sizing recommender | Automated | Weekly | <10% |
| Spot Instance Usage % | GCP billing | Automated | Monthly | ≥30% |
---

### **F. GOVERNANCE & PROCESS METRICS**

#### **Decision Velocity**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| VP DR Median Turnaround | DR register | Manual tracking | Weekly | ≤5 days |
| VP DR Aging Queue Count | DR register | Manual tracking | Daily | <5 |
| Blocked Sprint Time % | Sprint status | bmad-sprint-status | Sprint | <5% |
| Escalation Rate | Support tickets | D365 CS | Weekly | <10% |
| Policy Exception Requests | Approval logs | Manual tracking | Monthly | <5 |
| Architecture Board Throughput | Meeting minutes | Manual tracking | Weekly | Same-day |

---

#### **Process Compliance**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| DoR Compliance % | Story readiness checks | bmad-check-implementation-readiness | Sprint | 100% |
| DoD Compliance % | MR merge criteria | Automated | Per MR | 100% |
| Golden Path Adherence % | Generator usage tracking | Automated | Weekly | ≥95% |
| Generator Usage % | Stories via generators | bmad-create-story | Weekly | 100% |
| Code Review Compliance % | All MRs reviewed | GitLab | Weekly | 100% |
| Security Review Compliance % | High-risk MRs reviewed | GitLab | Weekly | 100% |
| Audit Trail Completeness % | Every mutation captured | Automated | Daily | 100% |
---

### **G. SECURITY & COMPLIANCE METRICS**

#### **Security**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Cross-Tenant Incidents | Security events | Automated | Real-time | 0 |
| Security Vulnerabilities | Grype + Fortify | Automated | Per MR | 0 critical |
| Secrets Exposed | Gitleaks | Automated | Per commit | 0 |
| Pen Test Findings | Manual testing | Manual | Quarterly | 0 critical |
| Access Violations | Audit log analysis | Automated | Daily | 0 |
| Failed Auth Attempts | AIC logs | Automated | Real-time | <1% |
| Patch Compliance % | Renovate PRs | Automated | Weekly | ≥95% |

---

#### **Compliance Evidence**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Control Effectiveness % | CISO Assistant | Automated | Daily | 100% |
| Audit Trail Completeness % | Probo validation | Automated | Daily | 100% |
| Evidence Collection % | CISO Assistant | Automated | Weekly | 100% |
| Policy Violations | Audit log analysis | Automated | Daily | 0 |
| Data Residency Compliance % | Tenant region check | Automated | Daily | 100% |
| Retention Policy Adherence % | GCS lifecycle rules | Automated | Weekly | 100% |
| GDPR Right Fulfillment Time | Request tracking | Manual | Per request | <30 days |

---

### **H. CUSTOMER & ADOPTION METRICS**

#### **Adoption**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Active Users (DAU) | Usage events | Automated | Daily | Increasing |
| Active Users (WAU) | Usage events | Automated | Weekly | Increasing |
| Active Users (MAU) | Usage events | Automated | Monthly | Increasing |
| Feature Utilization % | Feature flags + events | Automated | Weekly | ≥60% |
| Mobile Adoption % | Mobile app users / total | Automated | Weekly | ≥40% |
| API Usage (Calls/Day) | Apigee analytics | Automated | Daily | Increasing |
| Agent Connections | MCP connections | Automated | Daily | Increasing |

---

#### **Satisfaction**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| NPS Score | In-app surveys | Manual | Quarterly | ≥40 |
| Beta Feedback Score | Survey monkey | Manual | Weekly | ≥4/5 |
| Support Ticket Volume | D365 CS | Automated | Weekly | Decreasing |
| Support CSAT | D365 CS surveys | Automated | Per ticket | ≥4.5/5 |
| Churn Rate % | Zuora subscriptions | Automated | Monthly | <5% |
| Renewal Rate % | Zuora subscriptions | Automated | Quarterly | ≥90% |

---

### **I. PROGRAM-SPECIFIC METRICS**

#### **Migration Progress**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Shops Migrated (Count) | Migration tooling | Automated | Daily | Per plan |
| Shops Migrated (%) | Migrated / total | Calculated | Daily | Per plan |
| Migration Success Rate % | Successful / attempted | Automated | Per cohort | ≥95% |
| Rollback Count | Migration tooling | Automated | Per cohort | <5% |
| Migration Time per Shop | Migration tooling | Automated | Per shop | <4 hours |
| Data Validation Pass Rate % | Reconciliation reports | Automated | Per migration | 100% |

---

#### **Parity Tracking**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Parity Features Complete % | Parity register | Manual tracking | Weekly | 100% at M6 |
| Variance Items Approved % | Parity register | Manual tracking | Weekly | 100% |
| Beta Validation % | Beta shop feedback | Manual | Weekly | ≥90% |
| Critical Gaps Open | Parity register | Manual tracking | Daily | 0 at M6 |

---

#### **Knowledge Migration**
| Metric | Collection Method | BMad Skill | Frequency | Target |
|--------|------------------|------------|-----------|---------|
| Domain Corpus Promotion % | Promotion register | Manual tracking | Weekly | 100% at M1 |
| Evidence Coverage % | Evidence register | Manual tracking | Weekly | 100% |
| Contradiction Resolution % | Synthesis docs | Manual tracking | Weekly | 100% |
| Traceability Completeness % | Traceability manifest | Manual tracking | Weekly | 100% |
| Design Partner Coverage % | Partner register | Manual tracking | Weekly | 5 personas |

---

*End of Complete Program Summary*

