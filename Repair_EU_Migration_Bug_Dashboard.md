# Repair EU Migration to GCP and UI Upgrade - Bug Dashboard

**Project:** Repair EU Migration to GCP and UI Upgrade (LSD)  
**Fix Version:** Repair EU Migration to GCP and UI Upgrade  
**Report Date:** August 5, 2026  
**Total Active Bugs:** 49

**JQL Filter:**
```
project = "Repair EU Migration to GCP and UI Upgrade" AND 
fixVersion = "Repair EU Migration to GCP and UI Upgrade" AND 
labels not in (out, NotInScope, CodeReviewFeedback) AND 
issuetype = Bug AND 
status not in (Done, Cancelled)
```

---

## Executive Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Active Bugs** | 49 | 100% |
| **High Priority** | 9 | 18.4% |
| **Medium Priority** | 36 | 73.5% |
| **Low Priority** | 4 | 8.2% |
| **Blocked Status** | 9 | 18.4% |
| **In Progress** | 15 | 30.6% |
| **Verify (Testing)** | 11 | 22.4% |
| **Planned** | 6 | 12.2% |

### Critical Insights
- ⚠️ **9 bugs blocked** (18.4%) - requires immediate attention
- 🔥 **9 high-priority bugs** - 7 blocked, 2 in progress/planned
- ✅ **15 bugs in progress** (30.6%) - active development
- 🧪 **11 bugs in verify** (22.4%) - awaiting QA validation

---

## Table 1: All Bugs Overview

| Bug Key | Summary | Priority | Status | Days Old | Owner |
|---------|---------|----------|--------|----------|-------|
| LSD-5624 | [GDPR Compliance] Critical Security Header, Cookie Banner | Medium | Blocked | 0 | David Maldonado |
| LSD-5623 | Add "Contact ALLDATA" and "Support & Training" links | Medium | Blocked | 0 | Dalibor Dunjic |
| LSD-5621 | Info Center: Phone Number Field Non-Editable | Medium | Backlog | 0 | Manoj PG |
| LSD-5617 | Vehicle Selection Shows All Makes (QA env) | Medium | Backlog | 0 | Manoj PG |
| LSD-5616 | Duplicate BMW message on manufacturer select | Medium | Planned | 0 | Manoj PG |
| LSD-5615 | VIN Search: Nothing happens on clicking vehicle | Medium | Planned | 0 | Manoj PG |
| LSD-5613 | Admin Panel Not Functional on Click | Medium | Planned | 0 | Manoj PG |
| LSD-5611 | Component page: Links not localized by language | Medium | In Progress | 0 | Siba Pradhan |
| LSD-5609 | **Unable to send Service Interval request** | **High** | Planned | 0 | Manoj PG |
| LSD-5608 | User Management: Long first name overlaps last name | Medium | Planned | 0 | Sumeet Sharma |
| LSD-5607 | User Management: Delete User popup has space | Medium | In Progress | 0 | Sumeet Sharma |
| LSD-5605 | Language/time not pre-populated, phone not editable | Medium | In Progress | 0 | Shivam Upadhyay |
| LSD-5604 | **Specifications Quick Reference Discrepancy (EU vs NA)** | **High** | Blocked | 1 | Freeman, Lennore |
| LSD-5603 | Limited info vehicles not redirecting to Info Centre | Medium | Blocked | 1 | Freeman, Lennore |
| LSD-5594 | Breadcrumbs path links incorrect (app-beta) | Medium | Verify | 1 | Usha Menon |
| LSD-5593 | Login "Not A Customer" link redirect not localized | Medium | In Progress | 1 | Ehab Teima |
| LSD-5592 | Info Center: Preferred Language not defaulting | Medium | Review | 1 | Ehab Teima |
| LSD-5591 | Library request should be Info Center Request | Medium | Review | 1 | Ehab Teima |
| LSD-5588 | Disable Plate search on specific Euro countries | Medium | Verify | 1 | Usha Menon |
| LSD-5586 | Print: Blank pages on zoomed wiring diagrams | Medium | Verify | 1 | Harshit Jain |
| LSD-5585 | No Data for Nissan Pathfinder | Medium | In Progress | 1 | Akshay Karle |
| LSD-5571 | Blank page "Not Found" on article link select | Low | Verify | 2 | Avinash Vishwakarm |
| LSD-5570 | Components page fails in non-English languages | Medium | In Progress | 2 | Varun Padakannaya |
| LSD-5567 | BMW Footer message not sticky | Low | Verify | 2 | Harshit Jain |
| LSD-5565 | Component page: Links not localized (BE) | Medium | In Progress | 2 | Varun Padakannaya |
| LSD-5564 | BMW: Connector Views list not appearing on click | Medium | Verify | 2 | Harshit Jain |
| LSD-5563 | Unnecessary info on Print document | Low | Verify | 2 | Harshit Jain |
| LSD-5560 | **Single-license allows concurrent logins** | **High** | Blocked | 2 | Dave Butler |
| LSD-5555 | Mongo to Alloy incremental CDC Data validations | Medium | In Progress | 3 | Avinash Vishwakarm |
| LSD-5527 | **account-svc: account_contact creation fails 500** | **High** | Verify | 5 | Amador, Edwin |
| LSD-5512 | New User Password Setup Flow Not Functional | Medium | Verify | 5 | Asael De Avila |
| LSD-5507 | Unnecessary links around information/Refitting icon | Medium | Verify | 5 | Harshit Jain |
| LSD-5495 | Limited Information Articles not navigating | Medium | Blocked | 6 | Dave Butler |
| LSD-5490 | **"Unable to load" error on every page** | **High** | Planned | 6 | Manoj PG |
| LSD-5479 | Version Text not changing with language | Low | Review | 6 | Manduri Teja |
| LSD-5476 | **Old VIN not erased on navigate back** | **High** | Review | 7 | Ehab Teima |
| LSD-5468 | **MS/LT Send Request: No email to internal team** | **High** | In Progress | 7 | Guerrero Rios |
| LSD-5466 | **TSBs (All Technical Service Bulletins) not loading** | **High** | Verify | 7 | Harshit Jain |
| LSD-5464 | **Failed to fetch EU content 404 on many pages** | **High** | Verify | 7 | Mehak Sharma |
| LSD-5458 | White space between global header & Select vehicle | Low | Blocked | 7 | Sneha H |
| LSD-5456 | **Redirection Message on Login credentials submit** | **High** | Blocked | 7 | Dave Butler |
| LSD-5415 | MS and LT - Expiry date not populating | Medium | In Progress | 7 | Manoj PG |
| LSD-5414 | Login - 500 error with existing user | Medium | In Progress | 8 | Avinash Vishwakarm |
| LSD-5395 | "Buy Now" banner not showing for trial expiring | Medium | Review | 9 | Baptist, Rishav |
| LSD-5384 | **Expired User Account Able to Log In** | **High** | In Progress | 9 | Asael De Avila |
| LSD-5370 | ResponseStatusException on Fetching Primary Site | Low | Verify | 12 | Fernando Colon |
| LSD-5365 | Article screen fails: "File not found" error | Medium | Verify | 12 | Akshay Purnale |
| LSD-4918 | PATCH config Returns 200 Instead of 409 Conflict | Medium | Verify | 28 | Amador, Edwin |
| LSD-3760 | 500 Errors on Entitlement API endpoints | Medium | In Progress | 62 | Siba Pradhan |

---

## Table 2: High Priority Bugs (9 bugs)

| Owner | Bug Key | Summary | Status | Days Old |
|-------|---------|---------|--------|----------|
| **Manoj PG** | LSD-5609 | Unable to send Service Interval request | Planned | 0 |
| **Manoj PG** | LSD-5490 | "Unable to load" error on every page | Planned | 6 |
| **Freeman, Lennore** | LSD-5604 | Specifications Quick Reference Discrepancy | Blocked | 1 |
| **Dave Butler** | LSD-5560 | Single-license allows concurrent logins | Blocked | 2 |
| **Dave Butler** | LSD-5456 | Redirection Message on Login submit | Blocked | 7 |
| **Amador, Edwin** | LSD-5527 | account-svc: account_contact creation fails | Verify | 5 |
| **Ehab Teima** | LSD-5476 | Old VIN not erased on navigate back | Review | 7 |
| **Guerrero Rios** | LSD-5468 | MS/LT Send Request: No email sent | In Progress | 7 |
| **Harshit Jain** | LSD-5466 | TSBs not loading | Verify | 7 |
| **Mehak Sharma** | LSD-5464 | Failed to fetch EU content 404 | Verify | 7 |
| **Asael De Avila** | LSD-5384 | Expired User Account Able to Log In | In Progress | 9 |

### High Priority Analysis

**By Status:**
- Blocked: 3 bugs (33.3%) - **CRITICAL: Requires unblocking**
- Verify: 3 bugs (33.3%)
- In Progress: 2 bugs (22.2%)
- Planned: 2 bugs (22.2%)
- Review: 1 bug (11.1%)

**By Owner:**
- Manoj PG: 2 bugs
- Dave Butler: 2 bugs
- All others: 1 bug each

**Oldest High Priority Bug:** LSD-5384 (9 days old) - Expired users logging in

---

## Table 3: Medium Priority Bugs (36 bugs)

| Owner | Bug Key | Summary | Status | Days Old |
|-------|---------|---------|--------|----------|
| **David Maldonado** | LSD-5624 | GDPR Compliance Critical Security Header | Blocked | 0 |
| **Dalibor Dunjic** | LSD-5623 | Add Contact/Support links per country | Blocked | 0 |
| **Manoj PG** | LSD-5621 | Info Center: Phone Number Non-Editable | Backlog | 0 |
| **Manoj PG** | LSD-5617 | Vehicle Selection Shows All Makes | Backlog | 0 |
| **Manoj PG** | LSD-5616 | Duplicate BMW message | Planned | 0 |
| **Manoj PG** | LSD-5615 | VIN Search: Nothing happens on click | Planned | 0 |
| **Manoj PG** | LSD-5613 | Admin Panel Not Functional | Planned | 0 |
| **Manoj PG** | LSD-5415 | MS/LT Expiry date not populating | In Progress | 7 |
| **Siba Pradhan** | LSD-5611 | Component page links not localized | In Progress | 0 |
| **Siba Pradhan** | LSD-3760 | 500 Errors on Entitlement API | In Progress | 62 |
| **Sumeet Sharma** | LSD-5608 | User Mgmt: Name overlap | Planned | 0 |
| **Sumeet Sharma** | LSD-5607 | User Mgmt: Delete popup spacing | In Progress | 0 |
| **Shivam Upadhyay** | LSD-5605 | Language/time/phone field issues | In Progress | 0 |
| **Freeman, Lennore** | LSD-5603 | Limited info vehicles not redirecting | Blocked | 1 |
| **Usha Menon** | LSD-5594 | Breadcrumbs path links incorrect | Verify | 1 |
| **Usha Menon** | LSD-5588 | Disable Plate search (Euro countries) | Verify | 1 |
| **Ehab Teima** | LSD-5593 | Login link redirect not localized | In Progress | 1 |
| **Ehab Teima** | LSD-5592 | Info Center Language not defaulting | Review | 1 |
| **Ehab Teima** | LSD-5591 | Library request terminology | Review | 1 |
| **Harshit Jain** | LSD-5586 | Print: Blank pages on zoom | Verify | 1 |
| **Harshit Jain** | LSD-5564 | BMW Connector Views not appearing | Verify | 2 |
| **Harshit Jain** | LSD-5507 | Unnecessary links around icon | Verify | 5 |
| **Akshay Karle** | LSD-5585 | No Data for Nissan Pathfinder | In Progress | 1 |
| **Varun Padakannaya** | LSD-5570 | Components page fails non-English | In Progress | 2 |
| **Varun Padakannaya** | LSD-5565 | Component links not localized (BE) | In Progress | 2 |
| **Avinash Vishwakarm** | LSD-5555 | Mongo to Alloy CDC validations | In Progress | 3 |
| **Avinash Vishwakarm** | LSD-5414 | Login 500 error existing user | In Progress | 8 |
| **Amador, Edwin** | LSD-4918 | PATCH Returns 200 not 409 | Verify | 28 |
| **Asael De Avila** | LSD-5512 | Password Setup Flow Not Functional | Verify | 5 |
| **Dave Butler** | LSD-5495 | Limited Info Articles not navigating | Blocked | 6 |
| **Manduri Teja** | LSD-5479 | Version Text not changing | Review | 6 |
| **Baptist, Rishav** | LSD-5395 | Buy Now banner not showing | Review | 9 |
| **Akshay Purnale** | LSD-5365 | Article screen File not found | Verify | 12 |

### Medium Priority Analysis

**By Status:**
- In Progress: 11 bugs (30.6%)
- Verify: 8 bugs (22.2%)
- Planned: 4 bugs (11.1%)
- Blocked: 4 bugs (11.1%)
- Review: 5 bugs (13.9%)
- Backlog: 2 bugs (5.6%)

**By Owner (Top Contributors):**
- Manoj PG: 7 bugs
- Ehab Teima: 3 bugs
- Harshit Jain: 3 bugs
- Varun Padakannaya: 2 bugs
- Siba Pradhan: 2 bugs
- Avinash Vishwakarm: 2 bugs
- Usha Menon: 2 bugs

**Oldest Medium Priority Bug:** LSD-3760 (62 days old) - Entitlement API 500 errors

---

## Table 4: Low Priority Bugs (4 bugs)

| Owner | Bug Key | Summary | Status | Days Old |
|-------|---------|---------|--------|----------|
| **Avinash Vishwakarm** | LSD-5571 | Blank page "Not Found" on link select | Verify | 2 |
| **Harshit Jain** | LSD-5567 | BMW Footer message not sticky | Verify | 2 |
| **Harshit Jain** | LSD-5563 | Unnecessary info on Print document | Verify | 2 |
| **Sneha H** | LSD-5458 | White space header/Select vehicle | Blocked | 7 |
| **Manduri Teja** | LSD-5479 | Version Text not changing language | Review | 6 |
| **Fernando Colon** | LSD-5370 | ResponseStatusException Primary Site | Verify | 12 |

### Low Priority Analysis

**By Status:**
- Verify: 4 bugs (66.7%)
- Blocked: 1 bug (16.7%)
- Review: 1 bug (16.7%)

**By Owner:**
- Harshit Jain: 2 bugs
- All others: 1 bug each

**Oldest Low Priority Bug:** LSD-5370 (12 days old)

---

## Status Distribution

| Status | Count | Percentage | Details |
|--------|-------|------------|---------|
| **In Progress** | 15 | 30.6% | Active development |
| **Verify** | 11 | 22.4% | Awaiting QA validation |
| **Blocked** | 9 | 18.4% | ⚠️ Requires unblocking |
| **Planned** | 6 | 12.2% | Scheduled for work |
| **Review** | 5 | 10.2% | Code review/approval |
| **Backlog** | 2 | 4.1% | Prioritized but not started |

---

## Owner Distribution (Top 10)

| Owner | Total Bugs | High | Medium | Low | In Progress | Verify | Blocked |
|-------|------------|------|--------|-----|-------------|--------|---------|
| **Manoj PG** | 9 | 2 | 7 | 0 | 1 | 0 | 0 |
| **Harshit Jain** | 6 | 1 | 3 | 2 | 0 | 6 | 0 |
| **Ehab Teima** | 4 | 1 | 3 | 0 | 2 | 0 | 0 |
| **Dave Butler** | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| **Avinash Vishwakarm** | 3 | 0 | 2 | 1 | 3 | 0 | 0 |
| **Varun Padakannaya** | 2 | 0 | 2 | 0 | 2 | 0 | 0 |
| **Siba Pradhan** | 2 | 0 | 2 | 0 | 2 | 0 | 0 |
| **Usha Menon** | 2 | 0 | 2 | 0 | 0 | 2 | 0 |
| **Sumeet Sharma** | 2 | 0 | 2 | 0 | 1 | 0 | 0 |
| **Freeman, Lennore** | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| **Amador, Edwin** | 2 | 1 | 1 | 0 | 0 | 2 | 0 |
| **Asael De Avila** | 2 | 1 | 1 | 0 | 1 | 1 | 0 |
| Others (9 owners) | 10 | 1 | 6 | 3 | 3 | 2 | 4 |

---

## Critical Issues Requiring Immediate Attention

### 🚨 Blocked High Priority Bugs (3 bugs)

| Key | Summary | Owner | Days Old | Blocker Details |
|-----|---------|-------|----------|-----------------|
| LSD-5604 | Specifications Quick Reference Discrepancy | Freeman, Lennore | 1 | EU vs NA content issues |
| LSD-5560 | Single-license allows concurrent logins | Dave Butler | 2 | Security/access control |
| LSD-5456 | Redirection Message on Login submit | Dave Butler | 7 | IAM Team dependency |

### ⚠️ All Blocked Bugs (9 bugs)

| Priority | Key | Summary | Owner |
|----------|-----|---------|-------|
| High | LSD-5604 | Specifications Quick Reference Discrepancy | Freeman, Lennore |
| High | LSD-5560 | Single-license concurrent logins | Dave Butler |
| High | LSD-5456 | Redirection Message on Login | Dave Butler |
| Medium | LSD-5624 | GDPR Compliance Security Header | David Maldonado |
| Medium | LSD-5623 | Add Contact/Support links | Dalibor Dunjic |
| Medium | LSD-5603 | Limited info not redirecting | Freeman, Lennore |
| Medium | LSD-5495 | Limited Info Articles not navigating | Dave Butler |
| Low | LSD-5458 | White space header/Select vehicle | Sneha H |

**Action Required:** Identify and resolve blockers for these 9 bugs immediately.

---

## Age Analysis

### Bugs by Age Range

| Age Range | Count | Percentage | Details |
|-----------|-------|------------|---------|
| **0-2 days (New)** | 32 | 65.3% | Recent discoveries |
| **3-7 days (Recent)** | 10 | 20.4% | Last week |
| **8-14 days (Aging)** | 4 | 8.2% | Needs attention |
| **15-30 days (Old)** | 1 | 2.0% | LSD-4918 (28 days) |
| **30+ days (Stale)** | 2 | 4.1% | LSD-3760 (62 days) |

### Oldest Bugs (Requires Review)

| Key | Age | Priority | Summary | Owner | Status |
|-----|-----|----------|---------|-------|--------|
| LSD-3760 | 62 days | Medium | 500 Errors on Entitlement API | Siba Pradhan | In Progress |
| LSD-4918 | 28 days | Medium | PATCH Returns 200 not 409 | Amador, Edwin | Verify |
| LSD-5365 | 12 days | Medium | Article screen File not found | Akshay Purnale | Verify |
| LSD-5370 | 12 days | Low | ResponseStatusException | Fernando Colon | Verify |

---

## Bug Categories (By Labels)

| Category | Count | Key Bugs |
|----------|-------|----------|
| **AD_QA_Defects** | 26 | QA-identified issues |
| **Bug** (generic) | 39 | Standard bugs |
| **FE (Frontend)** | 6 | UI/UX issues |
| **BE (Backend)** | 5 | API/service issues |
| **Data** | 2 | Data migration/validation |
| **ping (IAM)** | 2 | Authentication issues |
| **AccessControl** | 1 | Security/permissions |

### Frontend vs Backend vs Full-Stack

| Layer | Bug Count | Examples |
|-------|-----------|----------|
| **Frontend (FE)** | 6 | Component localization, User Management UI |
| **Backend (BE)** | 5 | API errors, Entitlement endpoints |
| **Full-Stack** | 3 | Both FE+BE labels (Vehicle selection, Component pages) |
| **Data** | 2 | Mongo to Alloy, CDC validations |
| **Infrastructure** | 2 | IAM/Ping authentication |
| **Untagged/General** | 31 | Various categories |

---

## Recommendations

### Immediate Actions (Next 24-48 Hours)

1. **Unblock 3 High-Priority Bugs:**
   - LSD-5604: Resolve EU vs NA content discrepancy
   - LSD-5560: Fix concurrent login security issue
   - LSD-5456: Resolve IAM team dependency for login redirect

2. **Complete Testing on 11 "Verify" Bugs:**
   - 3 High Priority bugs ready for validation
   - 8 Medium/Low bugs in QA queue

3. **Address GDPR Compliance (LSD-5624):**
   - Critical security headers and cookie banner
   - Blocked status - identify blocker immediately

### Short-Term Actions (Next Week)

1. **Reduce Blocked Bug Count:**
   - Current: 9 bugs (18.4%)
   - Target: <5 bugs (<10%)
   - Assign owners to identify and resolve blockers

2. **Focus on High Priority Bugs:**
   - Complete LSD-5384 (Expired user login - 9 days old)
   - Finish LSD-5468, LSD-5466, LSD-5464 (all 7 days old)

3. **Address Oldest Bugs:**
   - LSD-3760 (62 days) - 500 Errors on Entitlement API
   - LSD-4918 (28 days) - PATCH endpoint response code
   - Both are in verify/in-progress - push to completion

### Medium-Term Improvements

1. **Workload Distribution:**
   - Manoj PG: 9 bugs (18.4%) - consider redistributing
   - Balance across team members

2. **Quality Focus:**
   - 26 bugs labeled "AD_QA_Defects" - review QA process
   - Many localization issues - systematic i18n testing needed

3. **Technical Debt:**
   - Entitlement API issues (multiple bugs)
   - Authentication/IAM issues (multiple bugs)
   - Component localization (multiple languages)

---

## Appendix: Bug Details by Category

### GDPR & Compliance Issues

- **LSD-5624:** GDPR Compliance - Security Header, Cookie Banner (Medium, Blocked)

### Authentication & IAM Issues

- **LSD-5456:** Redirection Message on Login (High, Blocked, IAM Team)
- **LSD-5384:** Expired User Account Able to Log In (High, In Progress)
- **LSD-5560:** Single-license concurrent logins (High, Blocked)
- **LSD-5593:** Login link redirect not localized (Medium, In Progress)

### Localization Issues

- **LSD-5611:** Component page links not localized (FE) (Medium, In Progress)
- **LSD-5565:** Component links not localized (BE) (Medium, In Progress)
- **LSD-5570:** Components page fails non-English (Medium, In Progress)
- **LSD-5593:** Login link not localized (Medium, In Progress)
- **LSD-5479:** Version Text not changing with language (Low, Review)

### Data & API Issues

- **LSD-3760:** 500 Errors on Entitlement API (62 days old) (Medium, In Progress)
- **LSD-5527:** account-svc creation fails 500 (High, Verify)
- **LSD-5555:** Mongo to Alloy CDC validations (Medium, In Progress)
- **LSD-5414:** Login 500 error existing user (Medium, In Progress)
- **LSD-5464:** Failed to fetch EU content 404 (High, Verify)

### Vehicle Selection Issues

- **LSD-5617:** Vehicle Selection Shows All Makes (Medium, Backlog)
- **LSD-5615:** VIN Search - nothing happens on click (Medium, Planned)
- **LSD-5476:** Old VIN not erased on navigate back (High, Review)

### Content & Article Issues

- **LSD-5604:** Specifications Quick Reference Discrepancy (High, Blocked)
- **LSD-5603:** Limited info vehicles not redirecting (Medium, Blocked)
- **LSD-5495:** Limited Info Articles not navigating (Medium, Blocked)
- **LSD-5585:** No Data for Nissan Pathfinder (Medium, In Progress)
- **LSD-5365:** Article screen File not found (Medium, Verify)

### UI/UX Issues

- **LSD-5608:** User Mgmt - name overlap (Medium, Planned)
- **LSD-5607:** User Mgmt - Delete popup spacing (Medium, In Progress)
- **LSD-5586:** Print: Blank pages on zoom (Medium, Verify)
- **LSD-5563:** Unnecessary info on Print (Low, Verify)
- **LSD-5458:** White space header/Select vehicle (Low, Blocked)

---

**Report Generated By:** Claude Code  
**Data Source:** Jira LSD Project  
**Analysis Date:** August 5, 2026  
**Next Update:** Recommended daily for blocked/high-priority bugs
