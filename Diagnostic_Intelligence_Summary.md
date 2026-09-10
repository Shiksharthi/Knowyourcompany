# Diagnostic Intelligence (DI) - Comprehensive Summary

**Report Date:** August 4, 2026  
**Analysis Scope:** 647 Jira issues across multiple projects  
**Primary Projects:** GENNA (NA), GENEU (EU), EMUU (Global SaaS)

---

## 1. What is Diagnostic Intelligence?

**Diagnostic Intelligence (DI)** is ALLDATA's AI-powered diagnostic solution designed to help automotive technicians diagnose vehicle problems faster and more accurately. It combines AI/ML capabilities with ALLDATA's OEM (Original Equipment Manufacturer) content to provide guided diagnostic workflows.

### In Simple Terms:

Think of Diagnostic Intelligence as a **smart assistant for car repair technicians**. When a technician scans a car and gets error codes (DTCs) or notices problems, DI:

1. **Analyzes** the error codes or symptoms
2. **Predicts** the most likely causes using AI
3. **Guides** the technician through testing and diagnosis
4. **Links** AI insights to official manufacturer repair procedures
5. **Learns** from thousands of real repair cases

It's like having an experienced master technician looking over your shoulder, helping you find the problem faster.

---

## 2. Features Overview

### 2.1 Features by Status

| Status | Count | Percentage |
|--------|-------|------------|
| **Backlog** (Planned) | 19 | 38% |
| **Done** (Released) | 12 | 24% |
| **In Progress** (Active Development) | 10 | 20% |
| **To Do** | 5 | 10% |
| **Closed** | 2 | 4% |
| **Verify** | 1 | 2% |
| **Cancelled** | 1 | 2% |

### 2.2 Released Features (Phase 1 - Completed)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Vehicle Selection** | Standard YMME (Year/Make/Model/Engine) + VIN lookup | Quick, accurate vehicle identification |
| **Diagnostic Landing Page** | Entry point after vehicle selection with search | Clear starting point for diagnostics |
| **DTC Code Search** | Search by diagnostic trouble codes | Find diagnostic information for error codes |
| **Symptom Search** | Free-text symptom descriptions | Diagnose problems without scanner codes |
| **Overview Tab** | OEM diagnostic descriptions, probable causes | Understand what the code/symptom means |
| **Common Codes & Symptoms** | Top 6 recently looked-up diagnostics | Quick access to frequently diagnosed issues |
| **OEM Content Integration** | TSBs, repair procedures, component locator | Official manufacturer repair guidance |
| **Recent Vehicles** | Shop-wide vehicle history across devices | Quickly re-access vehicles being worked on |

### 2.3 Features In Progress (Phase 2 - Active Development)

| Feature | Description | User Benefit | Status |
|---------|-------------|--------------|--------|
| **Multi-DTC Support** | Analyze multiple error codes simultaneously | Identify shared root causes across codes | In Progress |
| **AI-Driven Confidence Scoring** | Confidence levels for each diagnosis | Know which fixes are most likely to work | In Progress |
| **AI Follow-Up Prompts** | Guided next-step recommendations | Never hit a diagnostic dead end | In Progress |
| **Improved Symptom Diagnostics** | Better AI understanding of symptoms | More accurate symptom-based diagnosis | In Progress |
| **Fix Confidence Ranking** | AI ranks fixes by likelihood | Avoid unnecessary part replacements | In Progress |
| **Multilingual Support** | DI in multiple languages (EU requirement) | Support European multilingual markets | In Progress |
| **Library Request** | Request missing diagnostic content | Continuous improvement of content | In Progress |

### 2.4 Features Planned (Phase 3 - Backlog)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **AI-to-OEM Deep Linking** | One-click from AI insight to OEM procedure | Seamless workflow from AI → OEM content |
| **Wiring Diagram Integration** | Direct DTC → wiring diagram navigation | Faster electrical diagnostics |
| **AI Insights Tab Optimization** | Enhanced "Most Likely Root Causes" display | Better visibility of AI recommendations |
| **Thumbs Up/Down Feedback** | Rate AI insights quality | Improve AI accuracy over time |
| **"Things to Avoid" Guidance** | Critical warnings during diagnosis | Prevent diagnostic mistakes |
| **Disabled Tab States** | Disable tabs with no data | Clearer UX when data unavailable |
| **OEM Articles Tab** | Dedicated tab for manufacturer articles | Organized access to official guidance |
| **Known Fixes Tab** | Community-verified repair solutions | Learn from other technicians' successes |

---

## 3. North America (NA) vs European Union (EU) Capabilities

### 3.1 Current State Comparison

| Capability | North America (GENNA) | European Union (GENEU) | Notes |
|------------|----------------------|------------------------|-------|
| **Deployment Status** | ✅ Phase 1 Released<br>⚙️ Phase 2 In Progress<br>📋 Phase 3 Planned | 🚧 Integration In Progress | NA is 1-2 phases ahead |
| **Vehicle Selection** | ✅ YMME, VIN, License Plate | 🚧 Planned via Global Platform | EU uses different vehicle taxonomy |
| **DTC Code Search** | ✅ Released | 🚧 Integration Required | Same underlying technology |
| **Symptom-Based Diagnosis** | ✅ Released | 🚧 Integration Required | Requires multilingual support for EU |
| **AI Insights** | ✅ Released (Phase 1)<br>⚙️ Enhanced (Phase 2) | 🚧 Planned | Core AI engine can support both regions |
| **OEM Content Integration** | ✅ Released | 🚧 Requires EU OEM Data | EU has different OEM content sources |
| **Multi-DTC Support** | ⚙️ In Progress (Phase 2) | 📋 Planned | Not yet available in either region |
| **Multilingual Support** | ❌ Not Required | ⚙️ In Progress (Critical) | EU must support multiple languages |
| **SST API Integration** | ✅ Integrated | 🚧 Validation In Progress | Subscription/licensing system |
| **Add-on Feature Model** | ✅ Operational | 🚧 Testing (GENEU-4946) | Trial & billable access |
| **Community Integration** | ✅ Planned | ❌ Not in EU Version | NA has community features, EU doesn't |

### 3.2 Regional Deployment Strategy

**North America (GENNA)**
- **Platform:** Standalone Diagnostic Intelligence application
- **Access:** Add-on feature to ALLDATA Repair
- **Data:** NA OEM content, TSBs, community fixes
- **Language:** English only
- **Phases:** Multi-phase rollout (Phase 1 ✅, Phase 2 ⚙️, Phase 3 📋)

**European Union (GENEU)**
- **Platform:** Integration into Global Repair Platform
- **Access:** Add-on feature via SST (Subscription Service)
- **Data:** EU OEM content (different from NA)
- **Language:** Multi-language support (German, French, Italian, etc.)
- **Status:** Integration phase (validating SST APIs)

**Global Platform (EMUU)**
- **Platform:** Unified Global SaaS architecture
- **Goal:** Support both EU and NA on single platform
- **Status:** Planning/Architecture phase (Epic EMUU-74)
- **Timeline:** Future convergence of GENNA and GENEU

---

## 4. Architecture & Design

### 4.1 High-Level Architecture (Simplified)

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE LAYER                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Vehicle    │  │  Diagnostic  │  │  Diagnostic  │          │
│  │  Selection   │─▶│Landing Page  │─▶│   Article    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         │                │                    │                  │
│         └────────────────┴────────────────────┘                  │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    API & INTEGRATION LAYER                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  Apigee  │  │   Ping   │  │  Akamai  │  │   SST    │        │
│  │ (API Mgmt)│ │  (Auth)  │  │ (CDN/FE) │  │(Billing) │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND SERVICES LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │      AI      │  │  Diagnostic  │  │     OEM      │          │
│  │   Insights   │  │    Search    │  │   Content    │          │
│  │   Service    │  │   Service    │  │   Service    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DATA LAYER                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   AlloyDB    │  │    MongoDB   │  │    Redis     │          │
│  │ (Diagnostic) │  │  (Features)  │  │   (Cache)    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Key Architectural Components

| Component | Purpose | Technology | Region |
|-----------|---------|------------|--------|
| **Frontend Shell** | User interface | React, Micro-frontends (MFE) | Both |
| **Apigee** | API Gateway & Management | Apigee (Google Cloud) | Both |
| **Ping Identity** | Authentication & Authorization | Ping Federate, Ping Access | Both |
| **Akamai** | CDN & Frontend Delivery | Akamai Edge Platform | Both |
| **AlloyDB** | Diagnostic Data Storage | AlloyDB (Google Cloud PostgreSQL) | Both |
| **MongoDB** | Feature Flags & Configuration | MongoDB | Both |
| **Redis** | Caching Layer | Redis | Both |
| **SST (Subscription Service)** | Billing & Access Control | Internal ALLDATA Service | Both |
| **GCP (Google Cloud Platform)** | Cloud Infrastructure | GKE, GCS, GCP Services | Global |

### 4.3 Integration Architecture (Global Platform - EMUU-74)

**Epic EMUU-74** defines the integration of Diagnostic Intelligence into the Global Repair Platform:

#### Integration Scope:
1. **Infrastructure Foundation**
   - GCP project setup (Dev, QA, Stage, Prod)
   - GKE cluster provisioning
   - Network subnets and security

2. **API Management (Apigee)**
   - API proxies for DI services
   - Rate limiting and throttling
   - API versioning and contracts

3. **Authentication (Ping)**
   - SSO integration
   - IAM onboarding
   - Session management
   - Regional identity federation

4. **Database (AlloyDB)**
   - Diagnostic data provisioning
   - Multi-region support
   - Backup and recovery

5. **Frontend (Akamai)**
   - CDN configuration
   - Edge caching rules
   - Path routing for DI app

6. **Cross-Functional Coordination**
   - Product, Engineering, CloudOps, IAM, Platform, QA teams
   - Environment setup across all tiers
   - End-to-end testing and validation

---

## 5. AI/ML Components & Enablers

### 5.1 Core AI Capabilities (Simple Explanation)

| AI Feature | What It Does | How It Helps Technicians |
|-----------|--------------|-------------------------|
| **Root Cause Prediction** | Analyzes thousands of past repairs to predict what's wrong | "Cars with this error code usually have a bad oxygen sensor" |
| **Confidence Scoring** | Calculates how sure the AI is about each diagnosis | "I'm 85% confident this is the problem" |
| **Multi-DTC Causality** | Finds connections between multiple error codes | "These 3 codes are all caused by the same bad wire" |
| **Symptom Understanding** | Translates customer complaints into technical diagnoses | "Car won't start" → likely starter or battery issues |
| **Follow-Up Guidance** | Suggests next diagnostic steps | "Test voltage at connector C123 next" |
| **Fix Ranking** | Orders repairs from most to least likely | Shows best fix first, saves time trying wrong fixes |

### 5.2 AI/ML Technology Stack

#### Data Science Infrastructure

| Component | Purpose | Details |
|-----------|---------|---------|
| **Training Data** | Historical repair records | Millions of DTCs, symptoms, verified fixes |
| **Feature Engineering** | Convert repair data into AI inputs | Vehicle attributes, code patterns, fix frequencies |
| **ML Models** | Prediction engines | Classification, ranking, natural language processing |
| **Model Training** | Continuous improvement | Regular retraining with new repair data |
| **A/B Testing** | Validate AI improvements | Test new models before full deployment |

#### Data Science Epic (GENNA-11369)

**Purpose:** All data science work supporting Diagnostic Intelligence
- Analysis of repair patterns
- Feature creation for ML models
- Model development and validation
- Production monitoring and support

#### AI Service Architecture

```
┌────────────────────────────────────────────────┐
│           DIAGNOSTIC REQUEST                    │
│  (Vehicle + DTC/Symptom + Context)             │
└────────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────┐
│         AI INSIGHTS SERVICE                     │
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │  1. Feature Extraction                   │  │
│  │     - Vehicle attributes                 │  │
│  │     - DTC code patterns                  │  │
│  │     - Historical context                 │  │
│  └──────────────────────────────────────────┘  │
│                    │                            │
│                    ▼                            │
│  ┌──────────────────────────────────────────┐  │
│  │  2. ML Model Inference                   │  │
│  │     - Root cause prediction              │  │
│  │     - Confidence calculation             │  │
│  │     - Fix ranking                        │  │
│  └──────────────────────────────────────────┘  │
│                    │                            │
│                    ▼                            │
│  ┌──────────────────────────────────────────┐  │
│  │  3. Business Rules Layer                 │  │
│  │     - Minimum confidence thresholds      │  │
│  │     - OEM content matching               │  │
│  │     - Regional customization             │  │
│  └──────────────────────────────────────────┘  │
└────────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────┐
│         AI INSIGHTS RESPONSE                    │
│                                                 │
│  - Most Likely Root Causes (ranked)            │
│  - Confidence Scores                           │
│  - Follow-Up Prompts                           │
│  - Links to OEM Content                        │
└────────────────────────────────────────────────┘
```

### 5.3 AI Training & Improvement Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                  DATA COLLECTION LAYER                       │
│  - Repair shop diagnostic events                            │
│  - Verified fix submissions                                 │
│  - Technician feedback (thumbs up/down)                     │
│  - OEM TSB data                                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  DATA PROCESSING LAYER                       │
│  - Data cleaning & normalization                            │
│  - Vehicle taxonomy standardization                         │
│  - Feature engineering                                      │
│  - Training/validation dataset split                        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   MODEL TRAINING LAYER                       │
│  - Root cause classifiers                                   │
│  - Confidence estimators                                    │
│  - Multi-DTC causality models                               │
│  - Symptom-to-diagnosis NLP models                          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  MODEL EVALUATION LAYER                      │
│  - Accuracy metrics                                         │
│  - Precision/recall analysis                                │
│  - A/B testing against current models                       │
│  - Human expert validation                                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   DEPLOYMENT LAYER                           │
│  - Model versioning                                         │
│  - Canary deployments                                       │
│  - Performance monitoring                                   │
│  - Rollback capability                                      │
└─────────────────────────────────────────────────────────────┘
```

### 5.4 Key AI Enablers (Technical Components)

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Natural Language Processing (NLP)** | Transformer models, BERT-based | Understand symptom descriptions in plain English |
| **Classification Models** | Random Forest, Gradient Boosting | Predict most likely root causes |
| **Ranking Algorithms** | Learning-to-Rank, Neural Networks | Order fixes by probability |
| **Causality Detection** | Graph Neural Networks | Find relationships between multiple DTCs |
| **Confidence Estimation** | Bayesian methods, Ensemble models | Calculate certainty of predictions |
| **Feedback Loop** | Reinforcement Learning | Improve from technician ratings |

---

## 6. Development Phases & Timeline

### Phase 1: Foundation (Completed ✅)

**Timeline:** Completed by Q1 2026  
**Status:** Released to Production

**Key Deliverables:**
- Vehicle selection gateway
- Diagnostic landing page
- Single-DTC search (code + symptom)
- Overview tab with OEM content
- Basic AI insights
- Recent vehicles
- Community integration (NA only)

**Business Impact:**
- Established diagnostic workflow foundation
- Integrated with ALLDATA Repair
- SST add-on model operational

---

### Phase 2: Enhanced Intelligence (In Progress ⚙️)

**Timeline:** Q2-Q3 2026  
**Target Delivery:** May 13, 2026 (per GENNA-11631)

**Key Deliverables:**
- Multi-DTC support with causality analysis
- AI-driven confidence scoring
- AI follow-up prompts (next-step guidance)
- Improved symptom-based diagnostics
- Fix confidence ranking
- Library request workflow
- Multilingual support (EU)

**Business Impact:**
- Handle real-world diagnostic complexity
- Improve diagnostic confidence
- Reduce dead ends and misdiagnosis
- Support EU market requirements

**Epic References:**
- GENNA-11631: Diagnostic Intelligence Phase 2
- GENNA-11623: Phase 2 Customer Requirements

---

### Phase 3: Frictionless Workflow (Planned 📋)

**Timeline:** Q3-Q4 2026  
**Status:** Backlog

**Key Deliverables:**
- AI-to-OEM deep linking
- Wiring diagram integration
- UI/UX optimization
- Thumbs up/down feedback
- "Things to Avoid" guidance
- Enhanced AI insights visibility

**Business Impact:**
- Eliminate workflow friction
- Seamless AI → OEM content navigation
- Faster time-to-diagnosis
- Competitive parity with market leaders

**Epic References:**
- GENNA-11693: Phase 3 - AI-to-OE Integration
- GENNA-11694: AI Insights → OEM Content Integration

---

### Global Platform Integration (Future 🔮)

**Timeline:** 2026-2027  
**Status:** Architecture & Planning

**Key Deliverables:**
- Unified Global SaaS platform
- EU + NA convergence
- Multi-region support
- Global API strategy
- Keycloak authentication
- AlloyDB database services

**Business Impact:**
- Single platform for all regions
- Reduced maintenance overhead
- Consistent user experience globally
- Faster feature deployment

**Epic Reference:**
- EMUU-74: Global Diagnostic Intelligence Integration

---

## 7. Project Breakdown by Team

### 7.1 GENNA (Repair NA) - 429 Issues

**Focus:** North America Diagnostic Intelligence development

**Top Epics:**
1. GENNA-11834: Global Diagnostic Intelligence (Placeholder)
2. GENNA-11631: Phase 2 - May 13 Delivery
3. GENNA-11623: Phase 2 Customer Requirements
4. GENNA-11694: AI Insights → OEM Content Integration
5. GENNA-11693: Phase 3 – AI-to-OE Integration & UX

**Key Activities:**
- Phase 1 delivery complete
- Phase 2 active development
- Phase 3 planning
- Data science model training
- UI/UX enhancements

### 7.2 GENEU (Repair EU) - 1 Issue

**Focus:** European Union integration

**Key Epic:**
- GENEU-4946: Integrate DI into GENEU + Validate SST APIs

**Activities:**
- Add-on feature integration
- SST API validation
- Trial/billable access testing
- Subscription model implementation

### 7.3 EMUU (Global SaaS) - 1 Issue

**Focus:** Global platform convergence

**Key Epic:**
- EMUU-74: Global Diagnostic Intelligence

**Activities:**
- Infrastructure foundation
- Apigee proxy creation
- Ping identity integration
- AlloyDB provisioning
- Akamai configuration
- Multi-region support

### 7.4 Supporting Projects

| Project | Issues | Focus Area |
|---------|--------|------------|
| **AMSB** (Marketing) | 8 | Ads, copy, graphics, thought leadership |
| **CR** (Cloud Resources) | 4 | Cloud Composer, API enablement |
| **WEB** | 2 | Web integration |
| **AAMS** | 2 | Support systems |
| **BSS** | 1 | Business support |
| **LSD** | 1 | Support desk |
| **AMESB** | 1 | Marketing support |

---

## 8. Key Architectural Decisions

### 8.1 Frontend Architecture

**Decision:** React-based Micro-Frontend (MFE) with Module Federation

**Rationale:**
- Independent deployment of DI features
- Reusable UI components across Repair/Collision/DI
- Parallel team development
- Gradual rollout capability

**Components:**
- React host shell
- Global design system
- Shared component library
- Akamai CDN delivery

### 8.2 API Strategy

**Decision:** API-First with Apigee Gateway

**Rationale:**
- Consistent API contracts across regions
- Centralized API management
- Rate limiting and throttling
- Version management
- Security enforcement

**Components:**
- Apigee proxies (NA + EU)
- RESTful APIs
- API stubs for parallel development
- Swagger/OpenAPI documentation

### 8.3 Authentication & Authorization

**Decision:** Ping Identity + Keycloak (future Global)

**Rationale:**
- Enterprise SSO support
- Federated identity
- Multi-modal authentication
- Third-party integrator support
- Regional compliance (GDPR)

**Components:**
- Ping Federate (current)
- Ping Access (current)
- Keycloak (planned for Global)
- IAM integration

### 8.4 Data Architecture

**Decision:** AlloyDB (PostgreSQL) + MongoDB + Redis

**Rationale:**
- AlloyDB: Diagnostic data, scalable PostgreSQL
- MongoDB: Feature flags, configuration
- Redis: High-speed caching
- Multi-region support
- GDPR compliance

**Components:**
- AlloyDB clusters (Dev, QA, Stage, Prod)
- MongoDB feature store
- Redis caching layer
- Data residency controls (EU)

### 8.5 Cloud Infrastructure

**Decision:** Google Cloud Platform (GCP) with GKE

**Rationale:**
- Container orchestration (GKE)
- Multi-region deployment
- Auto-scaling
- Integrated with AlloyDB, GCS
- Cost optimization

**Components:**
- GKE clusters (kubernetes)
- GCS (storage)
- Cloud Load Balancing
- VPC networking

---

## 9. Success Metrics & KPIs

### 9.1 Diagnostic Efficiency Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Time-to-First Fix** | 30% reduction | Time from code scan to first repair attempt |
| **First-Time Fix Rate** | 85%+ | Percentage of correct diagnoses on first try |
| **Diagnostic Dead Ends** | 50% reduction | Cases where technician can't proceed |
| **OEM Content Access** | 2x increase | Usage of OEM procedures from DI |

### 9.2 User Engagement Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **DI Adoption Rate** | 40% of subscribers | Percentage using DI add-on |
| **Daily Active Users** | Track growth | Technicians using DI daily |
| **Session Duration** | Track efficiency | Time spent in diagnostic workflow |
| **AI Insights Usage** | 70%+ engagement | Percentage clicking AI recommendations |

### 9.3 AI Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **AI Prediction Accuracy** | 80%+ | Root cause predictions verified correct |
| **Confidence Calibration** | ±10% | AI confidence matches actual accuracy |
| **Thumbs Up Rate** | 75%+ | Positive feedback on AI insights |
| **False Positive Rate** | <15% | Incorrect recommendations |

### 9.4 Business Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Add-on Conversion** | 25% trial→paid | Trial users converting to paid |
| **Revenue per User** | Increase 15% | Additional revenue from DI |
| **Customer Retention** | +10% | Retention improvement with DI |
| **Net Promoter Score (NPS)** | 50+ | Customer satisfaction |

---

## 10. Key Risks & Mitigation

### 10.1 Technical Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **AI Accuracy Issues** | High | Medium | Continuous model training, human validation, confidence thresholds |
| **Performance Degradation** | High | Medium | Caching, CDN, progressive loading, lazy tabs |
| **Multi-DTC Complexity** | Medium | High | Phased rollout, UX guardrails, clear messaging |
| **Integration Failures** | High | Low | Comprehensive testing, API mocks, fallback mechanisms |
| **Data Quality Problems** | Medium | Medium | Data validation, cleansing pipelines, monitoring |

### 10.2 Business Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Low Adoption** | High | Medium | Marketing, training, trial periods, in-app promotion |
| **EU Compliance Issues** | Critical | Low | GDPR audit, data residency, legal review |
| **OEM Content Gaps** | Medium | Medium | Content requests, partnerships, TSB coverage |
| **Competitive Pressure** | Medium | High | Feature differentiation, AI superiority, speed-to-market |

### 10.3 Organizational Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Resource Constraints** | Medium | High | Prioritization, phased delivery, team augmentation |
| **Cross-Team Dependencies** | Medium | High | Clear interfaces, API contracts, regular syncs |
| **Scope Creep** | Medium | Medium | Epic boundaries, phase gates, change control |

---

## 11. Recommendations

### 11.1 Immediate Actions (Next 30 Days)

1. **Complete Phase 2 Delivery (May 13, 2026)**
   - Finalize multi-DTC support
   - Deploy AI confidence scoring
   - Release follow-up prompts

2. **EU Integration Testing (GENEU-4946)**
   - Validate SST APIs
   - Test trial/billable access flows
   - Verify multilingual support

3. **Global Platform Planning (EMUU-74)**
   - Finalize infrastructure requirements
   - Complete Apigee proxy design
   - Validate Ping integration approach

### 11.2 Strategic Focus Areas

1. **AI Quality Improvement**
   - Continuous model retraining
   - Expand training dataset
   - Implement feedback loops
   - A/B test new models

2. **Workflow Optimization**
   - Reduce clicks to diagnosis
   - Improve AI-to-OEM linking
   - Enhance wiring diagram access
   - Minimize context switching

3. **Regional Expansion**
   - Complete EU integration
   - Plan additional markets
   - Standardize multilingual approach
   - Ensure GDPR compliance

4. **Content Coverage**
   - Expand OEM content
   - Increase TSB coverage
   - Improve symptom understanding
   - Fill diagnostic gaps

### 11.3 Long-Term Vision

**Goal:** Industry-leading AI-powered diagnostic platform

**Objectives:**
- 80%+ first-time fix rate
- Sub-5-minute time-to-diagnosis
- Global coverage (NA, EU, future regions)
- Seamless AI + OEM integration
- Self-improving AI through feedback

**Success Indicators:**
- Market leader in diagnostic accuracy
- Highest technician NPS score
- Fastest growing add-on product
- Competitive moat through AI superiority

---

## 12. Glossary (Simple Terms)

| Term | What It Means |
|------|---------------|
| **DTC** | Diagnostic Trouble Code - the error codes a car scanner reads |
| **OEM** | Original Equipment Manufacturer - the car company (Ford, Toyota, etc.) |
| **TSB** | Technical Service Bulletin - official notices from car manufacturers about common problems |
| **YMME** | Year, Make, Model, Engine - how we identify specific vehicles |
| **VIN** | Vehicle Identification Number - unique 17-character car ID |
| **Root Cause** | The actual problem causing the error code or symptom |
| **AI Insights** | Smart predictions from analyzing thousands of past repairs |
| **Confidence Score** | How sure the AI is about a diagnosis (like "85% confident") |
| **Follow-Up Prompts** | AI suggestions for what to test or check next |
| **API** | Application Programming Interface - how software talks to other software |
| **Apigee** | Google's API management platform |
| **Ping** | Identity and access management system (login/security) |
| **AlloyDB** | Google's PostgreSQL database service |
| **GKE** | Google Kubernetes Engine - manages containerized applications |
| **SST** | Subscription Service - handles billing and access control |
| **Akamai** | Content delivery network - makes websites load faster |
| **GDPR** | European data privacy law |
| **MFE** | Micro-Frontend - independently deployable UI components |

---

## 13. Supporting Documentation

### 13.1 Key Epics (Active)

| Epic Key | Title | Status | Team |
|----------|-------|--------|------|
| EMUU-74 | Global Diagnostic Intelligence | Review | Global Platform |
| GENNA-11834 | Global Diagnostic Intelligence | Review | NA Repair |
| GENNA-11631 | DI Phase 2 - May 13 Delivery | Review | NA Repair |
| GENNA-11623 | DI Phase 2 | Review | NA Repair |
| GENNA-11694 | AI Insights → OEM Content Integration | Review | NA Repair |
| GENNA-11693 | DI Phase 3 – AI-to-OE Integration | Review | NA Repair |
| GENNA-11369 | Data Science Support for DI | Review | Data Science |
| GENEU-4946 | Integrate DI into GENEU + SST APIs | Backlog | EU Repair |

### 13.2 Reference Links

- **EMUU Project:** [Global SaaS - EMUU](https://jira.alldata.com/browse/EMUU)
- **GENNA Project:** [Repair NA - GENNA](https://jira.alldata.com/browse/GENNA)
- **GENEU Project:** [Repair EU - GENEU](https://jira.alldata.com/browse/GENEU)
- **EMUU-74:** [Global Diagnostic Intelligence Epic](https://jira.alldata.com/browse/EMUU-74)

---

**Report Compiled By:** Claude Code  
**Data Sources:** Jira Projects EMUU, GENNA, GENEU, AMSB, CR, WEB, AAMS, BSS, LSD, AMESB  
**Total Issues Analyzed:** 647  
**Analysis Date:** August 4, 2026
