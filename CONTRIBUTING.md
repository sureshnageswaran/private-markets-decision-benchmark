# Contributing to PMDB

Thanks for helping build the Private Markets Decision Benchmark. The most valuable contribution is a new, realistic scenario with one clearly correct next action.

## Ways to Contribute

- New benchmark scenarios
- New workflow domains
- Evaluation tooling and benchmark runners
- Data schemas and validation
- Leaderboards, research, and analysis of model performance

For anything larger than a single scenario, please open an issue first so we can agree on direction.

## Adding a Scenario

1. **Pick a domain folder** under `benchmarks/` (`direct-lending`, `abl`, `cre`, `governance`). To propose a new domain, open an issue or mention it in your PR.
2. **Create `benchmarks/<domain>/<id>.json`.** The `id` is a kebab-case summary of the situation and the expected action, and it must match the filename, e.g. `final-certificate-requires-covenant-test`.
3. **Fill in the case** using the structure below.
4. **Add an entry to `benchmarks/manifest.json`** (`id`, `domain`, `path`, `expected_action`) and increase `test_count`.
5. **Run `python3 scripts/bundle.py`.** It fails if the manifest and files disagree. It writes `tests.json`, which is gitignored, so don't commit it.
6. **Open a pull request.**

### Case structure

```json
{
  "id": "case-id",
  "expected_action": "credit_review",
  "rationale": "Why this is the correct action",
  "state": {
    "as_of": "2026-10-01T10:00:00-04:00",
    "borrower": "Synthetic Borrower, Inc.",
    "facility": "Synthetic Term Loan B",
    "observed_fact": {},
    "agreement_terms": {},
    "workflow_context": {},
    "policy": {}
  }
}
```

- **`observed_fact`**: what happened, its source, and its status.
- **`agreement_terms`**: what the governing documents say (definitions, thresholds, deadlines, cure rights, waivers, amendment status).
- **`workflow_context`**: where the process stands (what has been done, what is pending or missing).
- **`policy`**: the available actions, as a map of action name to a description of when it applies. `expected_action` must be one of these keys. Include `no_action` where doing nothing is a plausible answer.

Look at an existing case in the same domain and follow its shape.

### Actions

Valid actions are those listed under "Example Decision Types" in the [README](README.md), plus `no_action`. To introduce a new action, update that table in the same PR and explain why no existing action fits.

## Quality Checklist

Before submitting, confirm that your scenario:

- [ ] Has **one** intended next action, and the other actions in `policy` are clearly worse given the facts
- [ ] Is realistic for how the workflow actually runs
- [ ] Is internally consistent (dates, figures, thresholds, party names, document status)
- [ ] Includes realistic distractors: true but irrelevant facts that a careless reader might act on
- [ ] Avoids **label leakage**: the `id`, facility name, field names, and wording of the facts don't reveal the answer. (Case `id`s name the answer for maintainers; make sure nothing the model sees does.)
- [ ] Gives the rationale in terms of the facts and terms, not just the label
- [ ] For interpretation cases (e.g. `counsel_review`), contains a clause or fact pattern that genuinely doesn't resolve the question, rather than one that is merely long
- [ ] For `no_action` cases, includes something that looks like it needs action but is already handled (e.g. an executed waiver, a cure already submitted)

## Confidentiality

By submitting a scenario you represent that:

- It is synthetic, anonymized, or appropriately modified.
- It contains no confidential client information and no material non-public information.
- It reproduces no proprietary documents.
- Borrower, sponsor, and investor names are fictional.

## Review Process

Maintainers check each PR against the quality checklist and for confidentiality problems. Where possible, a reviewer with domain experience also checks that the expected action is the one a practitioner would choose. If reviewers disagree about the correct action, the scenario is revised to remove the ambiguity or is not merged. A case with a contested answer weakens the benchmark.

## Pull Requests

- Keep PRs focused: one scenario, or a small related batch.
- Describe the situation and why the expected action is correct.
- Be ready to revise based on reviewer feedback.

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE).
