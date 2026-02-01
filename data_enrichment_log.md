# Data Enrichment Log

This document tracks all additions and modifications made to the Ethiopia Financial Inclusion dataset.

## Summary

- **Date Started**: 2026-02-01
- **Total New Records Added**: TBD
- **New Observations**: TBD
- **New Events**: TBD
- **New Impact Links**: TBD

---

## New Observations Added

### Infrastructure Data

#### 1. Mobile Penetration Rate
- **Indicator Code**: `INF_MOBILE_PENETRATION`
- **Pillar**: Infrastructure/Enabler
- **Value**: TBD
- **Date**: TBD
- **Source**: ITU World Telecommunication/ICT Indicators Database
- **Source URL**: https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx
- **Confidence**: High
- **Notes**: Mobile penetration is a key enabler for mobile money adoption
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

#### 2. 4G Network Coverage
- **Indicator Code**: `INF_4G_COVERAGE`
- **Pillar**: Infrastructure/Enabler
- **Value**: TBD (% of population)
- **Date**: TBD
- **Source**: GSMA Mobile Connectivity Index / ITU
- **Source URL**: TBD
- **Confidence**: High
- **Notes**: 4G coverage enables advanced mobile money services
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

#### 3. ATM Density
- **Indicator Code**: `INF_ATM_DENSITY`
- **Pillar**: Infrastructure/Enabler
- **Value**: TBD (ATMs per 100,000 adults)
- **Date**: TBD
- **Source**: National Bank of Ethiopia / IMF Financial Access Survey
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: ATM density indicates physical banking infrastructure
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

#### 4. Agent Network Size
- **Indicator Code**: `INF_AGENT_NETWORK`
- **Pillar**: Infrastructure/Enabler
- **Value**: TBD (number of agents)
- **Date**: TBD
- **Source**: Mobile money operator reports (Telebirr, M-Pesa)
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: Agent network is critical for cash-in/cash-out services
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

### Active Account Metrics

#### 5. Active Mobile Money Accounts
- **Indicator Code**: `ACC_MM_ACTIVE`
- **Pillar**: Access
- **Value**: TBD (millions)
- **Date**: TBD
- **Source**: Mobile money operator reports
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: Active accounts (used in last 90 days) better reflect usage than registered accounts
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

### Transaction Data

#### 6. P2P Transaction Volume
- **Indicator Code**: `TXN_P2P_VOLUME`
- **Pillar**: Usage
- **Value**: TBD (millions of transactions)
- **Date**: TBD
- **Source**: EthSwitch / Mobile money operator reports
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: P2P transactions are the dominant use case in Ethiopia
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

### Disaggregated Data

#### 7. Account Ownership by Gender (Male)
- **Indicator Code**: `ACC_OWNERSHIP_MALE`
- **Pillar**: Access
- **Value**: TBD (%)
- **Date**: 2024
- **Source**: Global Findex 2024 Microdata
- **Source URL**: https://www.worldbank.org/en/publication/globalfindex
- **Confidence**: High
- **Notes**: Gender gap analysis is critical for understanding inclusion barriers
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

#### 8. Account Ownership by Gender (Female)
- **Indicator Code**: `ACC_OWNERSHIP_FEMALE`
- **Pillar**: Access
- **Value**: TBD (%)
- **Date**: 2024
- **Source**: Global Findex 2024 Microdata
- **Source URL**: https://www.worldbank.org/en/publication/globalfindex
- **Confidence**: High
- **Notes**: Gender gap analysis is critical for understanding inclusion barriers
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

---

## New Events Added

### Regulatory Events

#### 1. National Financial Inclusion Strategy II Launch
- **Category**: Policy
- **Event Date**: TBD
- **Event Name**: NFIS-II Launch
- **Description**: Launch of Ethiopia's second National Financial Inclusion Strategy
- **Source**: National Bank of Ethiopia
- **Source URL**: TBD
- **Confidence**: High
- **Notes**: Policy frameworks can significantly influence inclusion outcomes
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

### Infrastructure Investments

#### 2. EthSwitch Interoperability Expansion
- **Category**: Infrastructure
- **Event Date**: TBD
- **Event Name**: EthSwitch Interoperability Expansion
- **Description**: Expansion of interoperable payment infrastructure
- **Source**: EthSwitch / NBE
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: Interoperability reduces friction and increases network effects
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

### Market Events

#### 3. M-Pesa Full Market Entry
- **Category**: Product Launch
- **Event Date**: 2023-08-XX
- **Event Name**: M-Pesa Full Market Entry
- **Description**: Safaricom's M-Pesa service fully launched in Ethiopia
- **Source**: Safaricom Ethiopia / News reports
- **Source URL**: TBD
- **Confidence**: High
- **Notes**: Second major mobile money provider increases competition
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

---

## New Impact Links Added

### Telebirr Launch Impact

#### 1. Telebirr → Account Ownership
- **Parent Event**: Telebirr Launch (May 2021)
- **Pillar**: Access
- **Related Indicator**: ACC_OWNERSHIP
- **Impact Direction**: Positive
- **Impact Magnitude**: +5 to +8 percentage points over 3 years
- **Lag Months**: 0-36
- **Evidence Basis**: Comparable country evidence (Kenya M-Pesa, Tanzania mobile money)
- **Source**: GSMA Mobile Money Reports, Academic studies
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: Based on similar mobile money launches in East Africa
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

#### 2. Telebirr → Mobile Money Account Ownership
- **Parent Event**: Telebirr Launch (May 2021)
- **Pillar**: Access
- **Related Indicator**: ACC_MM_ACCOUNT
- **Impact Direction**: Positive
- **Impact Magnitude**: +4.75 percentage points (from 4.7% in 2021 to 9.45% in 2024)
- **Lag Months**: 0-36
- **Evidence Basis**: Historical observation
- **Source**: Global Findex 2021, 2024
- **Source URL**: TBD
- **Confidence**: High
- **Notes**: Directly observed impact
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

### M-Pesa Entry Impact

#### 3. M-Pesa Entry → Digital Payment Usage
- **Parent Event**: M-Pesa Full Market Entry (Aug 2023)
- **Pillar**: Usage
- **Related Indicator**: USG_DIGITAL_PAYMENT
- **Impact Direction**: Positive
- **Impact Magnitude**: +3 to +5 percentage points over 2 years
- **Lag Months**: 6-24
- **Evidence Basis**: Comparable country evidence, market competition effects
- **Source**: GSMA reports, market analysis
- **Source URL**: TBD
- **Confidence**: Medium
- **Notes**: Competition typically increases adoption and usage
- **Collected By**: Data Team
- **Collection Date**: 2026-02-01

---

## Data Quality Notes

### High Confidence Records
- Global Findex survey data
- Official NBE statistics
- Verified operator reports

### Medium Confidence Records
- Estimated from comparable countries
- Interpolated time series
- Third-party market research

### Low Confidence Records
- Expert estimates without direct evidence
- Projections based on limited data

---

## Schema Compliance

All new records follow the unified schema:
- All records share the same column structure
- `record_type` clearly identifies observation/event/impact_link/target
- Events have `category` but no `pillar` (pillar assigned via impact_links)
- Impact links connect events to indicators via `parent_id`
- All records include source documentation and confidence levels

---

## Next Steps

1. Complete data collection for all TBD fields
2. Validate new records against reference codes
3. Cross-check impact estimates with historical data
4. Document any schema modifications or extensions
