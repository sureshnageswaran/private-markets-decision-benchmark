# Private Markets Decision Benchmark (PMDB)

> An open benchmark for evaluating AI decision-making in private markets workflows.

## Overview

The **Private Markets Decision Benchmark (PMDB)** is a community-driven benchmark designed to evaluate a category of AI capability that is largely absent from today's benchmarks:

> **Operational decision-making in private markets.**

Most AI benchmarks measure coding ability, mathematical reasoning, knowledge retrieval, or content generation.

Private markets professionals face a different challenge.

Every day, investment operations, private credit, fund administration, real estate, securities finance, and middle office teams must determine:

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

The objective is simple:

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

✅ Include irrelevant but realistic information

✅ Require interpretation of workflow state

✅ Avoid label leakage

✅ Be useful for comparing multiple AI systems

---

## Example Decision Types

Examples of actions included within PMDB may include:

- `covenant_test`
- `borrower_follow_up`
- `credit_review`
- `counsel_review`
- `collateral_review`
- `cash_flow_analysis`
- `portfolio_manager_review`
- `reporting_exception`
- `operations_exception`
- `risk_committee_review`
- `watchlist_consideration`
- `waiver_evaluation`
- `default_assessment`
- `second_level_review`
- `data_quality_investigation`
- `no_action`

New actions may be introduced as benchmark coverage expands.

---

## Covered Domains

Current and planned benchmark scenarios include:

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

Each benchmark case contains:

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

- Private Credit professionals
- Private Equity professionals
- Real Estate investors
- Fund Administrators
- Asset Servicers
- Securities Finance practitioners
- Operations teams
- Compliance teams
- Technology providers
- AI researchers
- Academic institutions

The goal is not to promote a particular vendor or model.

The goal is to establish a transparent and repeatable way to measure AI decision quality in private markets workflows.

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

PMDB aims to become an open standard for evaluating AI systems operating in private markets environments.

If private markets wants AI optimized for private markets workflows, now is the time to start defining the tests.

---

## License

This project is licensed under the Apache License 2.0.

See [LICENSE](LICENSE) for details.
