# EMUU Project Research Report
**Global SaaS**

**Report Date:** August 4, 2026  
**Total Issues:** 61  
**Project Key:** EMUU  
**Project ID:** 17000

---

## Executive Summary

The **EMUU (Global SaaS)** project is ALLDATA's strategic initiative to build a unified Global Enterprise SaaS Platform. The project focuses on EU migration while establishing foundations for future NA convergence. The initiative spans 11 major epics covering data management, backend/frontend services, cloud infrastructure, authentication, AI strategy, security, and globalization.

**Key Metrics:**
- **Total Issues:** 61
- **Completed:** 15 (24.6%)
- **In Progress:** 1 (1.6%)
- **Backlog:** 24 (39.3%)
- **Agile Boards:** 4 (1 Kanban, 3 Scrum)

---

## 1. Project Overview

**Project Name:** Global SaaS  
**Project Key:** EMUU  
**Project Type:** Enterprise SaaS Platform Initiative

**Strategic Objectives:**
1. Migrate EU operations to global platform
2. Establish unified architecture for EU/NA convergence
3. Modernize frontend with React-based micro-frontends
4. Build global API strategy and backend services
5. Implement cloud-native infrastructure on GCP

---

## 2. Issue Status Breakdown

| Status | Count | Percentage |
|--------|-------|------------|
| **Backlog** | 24 | 39.3% |
| **Done** | 15 | 24.6% |
| **Review** | 4 | 6.6% |
| **Cancelled** | 3 | 4.9% |
| **Planned** | 2 | 3.3% |
| **Blocked** | 1 | 1.6% |
| **In Progress** | 1 | 1.6% |

**Analysis:**
- Large backlog (39.3%) indicates significant planned work
- Good completion rate (24.6%) shows steady progress
- Minimal blocking issues (1.6%) indicates healthy workflow

---

## 3. Issue Type Distribution

| Issue Type | Count | Percentage |
|------------|-------|------------|
| **Task** | 16 | 26.2% |
| **Dev Spike** | 13 | 21.3% |
| **Support** | 9 | 14.8% |
| **Enhancement** | 5 | 8.2% |
| **Epic** | 4 | 6.6% |
| **Technical Debt** | 2 | 3.3% |
| **QA Testing** | 1 | 1.6% |

**Analysis:**
- High number of Dev Spikes (21.3%) indicates research-heavy initiative
- Balanced mix of implementation (Tasks) and exploration (Spikes)
- Limited technical debt items suggest new platform approach

---

## 4. Priority Breakdown

| Priority | Count | Percentage |
|----------|-------|------------|
| **Medium** | 45 | 73.8% |
| **High** | 5 | 8.2% |

**Analysis:**
- Most work is medium priority (73.8%)
- Few high-priority items (8.2%) indicate controlled, strategic execution
- No critical/blocker items suggest stable planning

---

## 5. Technical Domain Analysis

Based on issue summaries, descriptions, and labels, issues are categorized across technical domains:

| Domain | Count | Key Focus Areas |
|--------|-------|-----------------|
| **Backend (BE)** | 30 | Microservices, API services, backend architecture |
| **Frontend (FE)** | 28 | React shell, MFEs, UI components, design system |
| **Database** | 27 | Storage, data patterns, caching, Redis, content stores |
| **API** | 24 | API contracts, stubs, endpoints, integration patterns |
| **Cloud/GCP** | 17 | GCP infrastructure, cloud platform, networking |
| **IAM/Auth** | 6 | Authentication, SSO, Keycloak, identity management |
| **Other** | 5 | Miscellaneous tasks |

### 5.1 Frontend (FE) - 28 Issues

**Key Initiatives:**
- React host shell with micro-frontend (MFE) architecture
- Global UI component library and design system
- Module Federation configuration
- EU/NA UI parity validation
- Localization and language behavior
- Frontend delivery via Akamai

**Strategic Epic:** EMUU-12 - "04. Global Frontend Services & UIs"

### 5.2 Backend (BE) - 30 Issues

**Key Initiatives:**
- Global backend services and APIs
- Microservices architecture
- API stub development for parallel team enablement
- EU/NA variance handling
- BMW API integration (passthrough)
- OEM data integration framework

**Strategic Epic:** EMUU-11 - "03. Global Backend Services & APIs"

### 5.3 API - 24 Issues

**Key Initiatives:**
- Global API contract definition
- API stub creation with sample payloads
- Vehicle API contracts
- Integration patterns
- OEM API adapters (BMW, future Mercedes/VW)

**Key Spike:** EMUU-4 - "Establish API Stubs"

### 5.4 Database - 27 Issues

**Key Initiatives:**
- Global data engineering foundations
- Storage patterns and content stores
- Caching strategies (Redis)
- Data performance primitives
- Canonical data models
- Data normalization and taxonomy

**Strategic Epics:**
- EMUU-9 - "01. Global Data Engineering & Storage"
- EMUU-3 - "02. Global Data Management"

### 5.5 Cloud/GCP Infrastructure - 17 Issues

**Key Initiatives:**
- GCP project provisioning
- GKE cluster setup and sizing
- EU subnet configuration
- Multi-region deployment (US Central-1)
- Environment setup (Dev, QA, Stage, Prod)

**Strategic Epic:** EMUU-14 - "09. Global Cloud Platform and Infrastructure"

**Infrastructure Tasks:**
- EMUU-8: EU subnet & GKE cluster sizing
- EMUU-7: GCP project naming (addv1-global, adqa1-global, adst1-global, adpr1-global)

### 5.6 IAM/Authentication - 6 Issues

**Key Initiatives:**
- Keycloak-based authentication
- SSO modernization
- Federated identity
- Third-party integrator support
- Session management
- Multi-modal authentication

**Strategic Epic:** EMUU-15 - "05. Global Authentication & SSO Modernization"

---

## 6. Agile Boards

| Board ID | Board Name | Type |
|----------|------------|------|
| 461 | Copy of Repair Europe Scrum Board | Scrum |
| 456 | Global SaaS | Kanban |
| 277 | Repair Europe Scrum Board | Scrum |
| 457 | Test | Scrum |

---

## 7. Team & Resource Allocation

### 7.1 Assignee Distribution

| Assignee | Issues Assigned | Percentage |
|----------|-----------------|------------|
| **Unassigned** | 14 | 23.0% |
| **Naval Kishor** | 11 | 18.0% |
| **Ashish Kumar** | 10 | 16.4% |
| **Himanshu Sharma** | 4 | 6.6% |
| **Priya Sharma** | 3 | 4.9% |
| **Tanmay Verma** | 3 | 4.9% |
| **Hari Pillai** | 2 | 3.3% |
| **Others** | 3 | 4.9% |

**Analysis:**
- 23% of issues unassigned - requires attention for resource planning
- Top 3 contributors handle 52.4% of assigned work
- Relatively concentrated team structure

---

## 8. Strategic Epics Overview

The EMUU project is organized around 11 strategic epics:

### Epic 01: Global Data Engineering & Storage (EMUU-9)
**Status:** Review  
**Focus:** Storage foundations, content stores, data patterns, caching, migration inputs

### Epic 02: Global Data Management (EMUU-3)
**Status:** Review  
**Focus:** Canonical data models, governance, taxonomy alignment, vehicle management

### Epic 03: Global Backend Services & APIs (EMUU-11)
**Status:** Review (Updated: July 30, 2026)  
**Focus:** API strategy, contract direction, stubs, EU/NA variance

### Epic 04: Global Frontend Services & UIs (EMUU-12)
**Status:** Review (Updated: July 29, 2026)  
**Focus:** React shell, MFEs, design system, localization, delivery enablement

### Epic 05: Global Authentication & SSO Modernization (EMUU-15)
**Status:** Review  
**Focus:** Keycloak, federated identity, SSO, third-party integrators

### Epic 06: AI Strategy (EMUU-16)
**Status:** Review  
**Focus:** TBD (Under definition)

### Epic 07: Product Globalization (EMUU-17)
**Status:** Review (Updated: July 29, 2026)  
**Focus:** TBD (Under definition)

### Epic 08: Product Security (EMUU-18)
**Status:** Review (Updated: July 24, 2026)  
**Focus:** TBD (Under definition)

### Epic 09: Global Cloud Platform and Infrastructure (EMUU-14)
**Status:** Review  
**Focus:** GCP, networking, GKE clusters

### Epic 10: Global Product Training (EMUU-46)
**Status:** Review  
**Focus:** React training, GCP certifications

### Epic 11: Global Diagnostic Intelligence (EMUU-74)
**Status:** Review  
**Focus:** TBD

---

## 9. Key Technical Initiatives

### 9.1 BMW API Integration (EMUU-44)
**Type:** Dev Spike (High Priority)  
**Status:** Backlog

**Scope:**
- API passthrough integration for BMW data
- Microservices approach for OEM-specific data
- Internal data format transformation
- Caching strategy for transformed data
- Emulation of platform taxonomy
- Future extensibility for Mercedes, VW integrations

**Architecture Pattern:**
```
OEM API Response → Transformation Layer → Internal Data Format → UI Rendering
BMW API → BMW Adapter → Internal Data Format
Mercedes API → Mercedes Adapter → Internal Data Format
VW API → VW Adapter → Internal Data Format
```

### 9.2 Google Analytics Disablement (EMUU-76)
**Type:** Support  
**Status:** Done

**Scope:**
- Disable Google Analytics in Global Repair product
- Validation across all environments
- Ensure no impact on existing functionality

### 9.3 GCP Infrastructure Setup

**Active Tasks:**
- **EMUU-8:** EU subnet & GKE cluster sizing (In Progress - Chaitanya Malpe)
  - Sizing: /21 for nodes (Stage/Prod), /24 for nodes (Dev/QA), /18 for pods
  - Target: Stage/Prod subnets ready by Feb 25, 2026

- **EMUU-7:** GCP project naming (Cancelled)
  - Projects: addv1-global, adqa1-global, adst1-global, adpr1-global

### 9.4 Data Services Deep Dive (EMUU-2)
**Type:** Dev Spike  
**Status:** Planned  
**Assignee:** Hari Pillai

**Focus:**
- Current state EU data services analysis
- API gap analysis (EU vs NA)
- Target state definition
- GDPR/GRC compliance constraints

### 9.5 Vincario Cache Management (EMUU-45)
**Type:** Enhancement  
**Status:** Backlog  
**Assignee:** Tanmay Verma

**Scope:**
- Admin endpoint to clear Redis cache
- Clear DB logs endpoint for vincario_api_log

---

## 10. Risk & Dependency Analysis

### 10.1 High-Priority Items (5 Total)

1. **EMUU-44:** BMW API Integration Spike
2. Additional high-priority items in backlog

### 10.2 Blocked Items

- **1 issue blocked** - requires investigation

### 10.3 Key Dependencies

**Frontend → Backend:**
- UI modernization depends on API stubs and contracts
- React MFE development requires backend service endpoints

**Data → All Layers:**
- Storage foundations must support both EU migration and NA convergence
- Canonical data models required for API contract consistency

**Infrastructure → Deployment:**
- GCP setup and GKE clusters prerequisite for all deployments
- Network subnets must be ready for environment provisioning

---

## 11. Recommendations

### 11.1 Immediate Actions

1. **Reduce Unassigned Backlog**
   - Assign 14 unassigned issues to team members
   - Prioritize epic alignment

2. **Clear Blocked Issue**
   - Investigate and resolve the 1 blocked item
   - Document resolution process

3. **Define TBD Epics**
   - Complete descriptions for Epics 6, 7, 8, 11
   - Establish acceptance criteria and scope

### 11.2 Strategic Focus Areas

1. **API-First Development**
   - Prioritize API stub creation (EMUU-4)
   - Enable parallel UI/backend development

2. **Infrastructure Readiness**
   - Complete GKE cluster setup (EMUU-8)
   - Validate all environments (Dev, QA, Stage, Prod)

3. **OEM Integration Framework**
   - Finalize BMW integration approach (EMUU-44)
   - Establish patterns for future OEM integrations

4. **Training & Enablement**
   - Execute React training for team (Epic 10)
   - GCP certifications for infrastructure team

### 11.3 Process Improvements

1. **Sprint Planning**
   - Convert more Dev Spikes to executable Tasks
   - Define clear acceptance criteria for all backlog items

2. **Documentation**
   - Maintain architectural decision records
   - Document API contracts and data models

3. **Cross-Functional Coordination**
   - Establish regular sync between FE, BE, and Infra teams
   - Create dependency tracking across epics

---

## 12. Project Health Indicators

### Positive Indicators ✅
- Balanced technical approach across all domains
- Strong epic structure providing clear organization
- Multiple agile boards supporting different workstreams
- Low blocking/critical issues
- Recent activity on key epics (July 2026 updates)

### Areas of Concern ⚠️
- 39.3% of work in backlog requires refinement
- 23% unassigned issues may impact velocity
- Several epics still in "TBD" state
- Limited high-priority items may indicate unclear criticality

### Overall Assessment
**Status:** HEALTHY with MODERATE RISKS

The EMUU project demonstrates strong architectural planning with comprehensive epic coverage. The initiative is methodically addressing the complex challenge of building a global SaaS platform while migrating EU operations. Key success factors include completing infrastructure setup, finalizing API contracts, and maintaining parallel progress across frontend, backend, and data domains.

---

## 13. Timeline Indicators

**Project Creation:** January 28-29, 2026  
**Recent Epic Updates:** July 24-30, 2026  
**Active Development:** Ongoing

**Key Milestones Referenced:**
- Feb 25, 2026: Target for Stage/Prod subnets (EMUU-8)

---

## Appendix: Reference Links

- **Jira Project:** [EMUU - Global SaaS](https://jira.alldata.com/browse/EMUU)
- **Related AutoZone Jira Tickets:**
  - [PDK-11305] Create GKE Clusters For ALLDATA EU Global SaaS Platform
  - [PDK-11426] Create GKE Cluster for ALLDATA EU Global SaaS Platform (Done ✅)

---

**Report Generated By:** Claude Code  
**Data Source:** Jira EMUU Project  
**Analysis Date:** August 4, 2026
