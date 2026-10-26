# Private Markets Decision Benchmark (PMDB)

> An open benchmark for evaluating AI decision-making in private markets workflows.

## Overview

The **Private Markets Decision Benchmark (PMDB)** is a community-driven benchmark designed to evaluate a category of AI capability that is largely absent from today's benchmarks:

> **Operational decision-making in private markets.**

As of Q4 2026, most AI benchmarks measure coding ability, mathematical reasoning, knowledge retrieval, or content generation.

However Private Markets professionals face somewhat different challenges. Every day, investment operations, private credit, fund administration, real estate, securities finance, and middle office teams must determine:

- What should happen next?
- Which team should own the issue?
- How should a workflow progress?
- When should risk be escalated?
- When is no action required?

PMDB evaluates whether an AI system can correctly select the next operational action given a realistic business scenario.

---

## The Core Question

Each benchmark scenario asks:

> Given a set of facts, contractual obligations, policies, workflow state, and available actions, can the model select the correct next action?

Examples:

- Run a covenant test
- Request borrower information
- Escalate to credit
- Route to counsel
- Initiate collateral review
- Trigger portfolio manager review
- Record a reporting exception
- Take no action

Unlike traditional benchmarks, the objective is not to generate an explanation or conduct open-ended reasoning.

---
The core objective is:

> **Select the correct operational decision.**

---

## Why This Benchmark Exists

AI models become good at the things we measure.

Today the AI ecosystem benefits from mature benchmarks for:

- Software engineering
- Mathematics
- General reasoning
- Reading comprehension
- Agent tool use
- Legal reasoning
- Scientific research

Private Markets has trillions of dollars under management, yet there is no broadly adopted benchmark for evaluating AI decision-making within private markets workflows.

As AI increasingly enters investment operations, middle office, servicing, compliance, and portfolio monitoring functions, the industry needs a common way to evaluate:

- Decision quality
- Reliability
- Consistency
- Latency
- Cost-performance tradeoffs

PMDB aims to provide that framework.

---

## Benchmark Philosophy

A good benchmark case should:

✅ Reflect a realistic workflow

✅ Contain realistic business context

✅ Include policy guidance

✅ Include contractual terms when relevant

✅ Have a clearly defined action space

✅ Have a single intended next action

✅ Include irrelevant but realistic information (red herrings)

✅ Require interpretation of workflow state

✅ Avoid label leakage (where the title gives away the answer to the model)

✅ Be useful for comparing multiple AI systems

---

## Example Decision Types

Examples of actions included within PMDB may include:

| Workflow | Description |
|----------|-------------|
| covenant_test | Evaluates borrower compliance with loan covenants and identifies any breaches or exceptions. |
| borrower_follow_up | Requests additional information, clarification, or remediation actions from the borrower. |
| credit_review | Assesses the borrower's credit profile, financial condition, and overall creditworthiness. |
| counsel_review | Obtains legal review of loan documentation, contractual obligations, or legal risks. |
| collateral_review | Reviews the adequacy, valuation, and eligibility of pledged collateral. |
| cash_flow_analysis | Analyzes historical and projected cash flows to assess repayment capacity. |
| portfolio_manager_review | Seeks portfolio manager input on exposure, strategy alignment, and investment implications. |
| reporting_exception | Investigates missing, delayed, incomplete, or inconsistent reporting submissions. |
| operations_exception | Resolves operational issues, processing errors, or workflow execution failures. |
| risk_committee_review | Escalates material risks or exceptions to the risk committee for evaluation and decision. |
| watchlist_consideration | Determines whether the borrower should be placed on a watchlist due to emerging concerns. |
| waiver_evaluation | Assesses requests to waive covenant breaches, policy exceptions, or documentation requirements. |
| default_assessment | Evaluates whether conditions constitute an event of default and identifies potential actions. |
| second_level_review | Performs an independent secondary review for quality assurance or escalation purposes. |
| data_quality_investigation | Investigates data anomalies, inconsistencies, completeness issues, or accuracy concerns. |

New actions may be introduced as benchmark coverage expands.

---

## Covered Domains

Current and planned benchmark scenarios include:

### Private Equity

- Capital calls
- Distribution notices
- LP onboarding
- Subscription document review
- Side letter obligations
- Deal closing workflows
- Valuation governance
- Portfolio company reporting
- Investment committee exceptions
- Co-investment administration
- Fund liquidity events
- Investor communications

### Private Credit

- Covenant compliance
- Financial reporting review
- Borrowing base monitoring
- Direct lending surveillance
- Waivers and amendments
- Equity cures
- Credit escalation

### Asset-Based Lending

- Borrowing base certificates
- Collateral reporting
- Reserve analysis
- Availability monitoring

### Commercial Real Estate

- DSCR monitoring
- Debt yield review
- Property surveillance
- Major tenant events
- Cash management triggers

### Fund Operations

- Capital calls
- Distribution processing
- Subscription workflows
- Redemption workflows
- NAV exceptions

### Portfolio Monitoring

- Portfolio company reporting
- Material event detection
- Valuation exceptions
- Performance exceptions

### Investment Operations

- Workflow exceptions
- Data quality incidents
- Operations escalations
- Process controls

### Regulatory & Compliance

- KYC
- AML
- Investor onboarding
- Documentation exceptions

### Securities Finance

- Loan exceptions
- Collateral shortfalls
- Recall processing
- Counterparty monitoring

---

## Benchmark Structure

Each benchmark case is expressed in JSON format:

```json
{
  "id": "case-id",
  "expected_action": "credit_review",
  "rationale": "Why this is the correct action",
  "state": {
    "observed_fact": {},
    "agreement_terms": {},
    "workflow_context": {},
    "policy": {}
  }
}
```
P.S: I'll be providing a user-friendly UI, to accomodate folks unfamiliar with JSON file formats.

### Repository Layout

Each case lives in its own file, grouped by domain under `benchmarks/`:

```text
benchmarks/
├── direct-lending/   # covenant tests, borrower follow-up, credit review, counsel review, equity cures
├── abl/              # borrowing base certificates
├── cre/              # DSCR monitoring, major tenant events
├── governance/       # waivers and superseded metrics
└── manifest.json     # index of all cases
scripts/
└── bundle.py         # builds tests.json from benchmarks/
```

Files are named after the case `id` (e.g. `final-certificate-requires-covenant-test.json`).

`benchmarks/manifest.json` lists every case with its `id`, `domain`, `path`, and `expected_action`, plus a `version` and `test_count`. Add each new case to the manifest.

### Bundling into a Single File

Some runners prefer one file. From the repository root:

```bash
python3 scripts/bundle.py
```

This writes `tests.json`, a flat list of all cases in manifest order. Each case gets a `domain` field (taken from the manifest) right after `id`. The script fails if a case's `id` differs from its manifest entry, if `test_count` is wrong, or if the manifest and the files on disk disagree.

`tests.json` is generated and listed in `.gitignore`; regenerate it rather than editing it.

### Components

#### Observed Fact

What happened?

Example:

- Borrower submitted a compliance certificate
- Major tenant filed bankruptcy
- Reporting package is late
- Covenant ratio exceeded threshold

#### Agreement Terms

What do the governing documents say?

Examples:

- Covenant definitions
- Reporting obligations
- Cure rights
- Waiver provisions
- Escalation triggers

#### Workflow Context

Where are we in the process?

Examples:

- Calculation completed
- Information missing
- Review pending
- Escalation already performed

#### Policy

What actions are available?

The benchmark intentionally constrains the decision space to realistic actions available to the workflow.

---

## Evaluation Metrics

The benchmark is designed to support evaluation of:

### Accuracy

Percentage of decisions matching the expected action.

### Confidence

Probability assigned to the selected action.

### Consistency

Repeatability across multiple runs.

### Latency

Time required to reach a decision.

### Cost Efficiency

Decision quality relative to inference cost.

### Error Analysis

Common failure modes such as:

- False escalations
- Missed escalations
- Incorrect legal routing
- Premature closure
- Workflow confusion

---

## Benchmark Goals

PMDB seeks to answer questions such as:

- Which models make the highest quality operational decisions?
- Which models are fast enough for real workflow execution?
- Which domains remain difficult?
- Which workflow patterns cause the most mistakes?
- How much context is required for reliable decisions?

---

## Open Collaboration

This project is intended to be community-driven.

Contributions are encouraged from:

- Private Equity professionals
- Private Credit professionals
- Real Estate investors
- Fund Administrators
- Asset Servicers
- Securities Finance practitioners
- Operations teams
- Compliance teams
- Technology providers
- AI researchers
- Academic institutions

The goal is be totally AGNOSTIC to both vendor and model.

Success means we are able to establish a transparent and repeatable way to measure AI decision quality in private markets workflows.

---

## Contributing

Contributions may include:

- New benchmark scenarios
- Additional workflow domains
- Evaluation tooling
- Benchmark runners
- Data schemas
- Leaderboards
- Research papers
- Analysis of model performance

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

## Scenario Requirements

Contributed scenarios should:

- Be realistic
- Be internally consistent
- Have one intended next action
- Include supporting rationale
- Include policy guidance
- Include realistic distractors
- Avoid confidential information
- Avoid non-public borrower, investor, or transaction data

### Confidentiality Requirements

By submitting scenarios, contributors represent that:

- The scenario is synthetic, anonymized, or appropriately modified.
- No confidential client information is included.
- No material non-public information is disclosed.
- No proprietary documents are reproduced.

---

## Vision

The long-term goal is not simply to benchmark models.

The long-term goal is to help the private markets industry define:

> **What does good AI decision-making look like?**

As AI becomes increasingly embedded in investment and operational workflows, the industry will need objective ways to measure decision quality.

PMDB aims to become an *OPEN STANDARD* for evaluating AI systems operating in private markets environments.

If private markets wants AI optimized for private markets workflows, now is the time to start defining the tests.

---

## License

This project is licensed under the Apache License 2.0.

See [LICENSE](LICENSE) for details.
