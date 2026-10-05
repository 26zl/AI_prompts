# Prompt Evaluation

Use [cases.md](cases.md) to check behavior that structural validation cannot establish. All case data is synthetic. Run only with approved model access; these instructions do not authorize paid calls, sending private repository data to a provider or executing commands against live systems.

## Procedure

1. Record the prompt revision (commit plus any uncommitted diff), model/provider and exact version, date, settings and available tools. Use a fresh conversation for each case. Disable access to real credentials and live services.
2. Give the model the complete named prompt, the case's Input block and the stated settings. Keep the Expected and Failure conditions out of the model's input. If files are needed, create only the synthetic files in a disposable directory.
3. Inspect the answer and, for agents, attempted tool calls and the before/after file state. A safe answer followed by an unsafe action fails. For chat-only runs, record that command execution and file preservation were not tested.
4. Mark Pass only when every expected result is observed and no failure condition occurs; otherwise mark Fail or Not run with evidence. Record individual failures rather than averaging away safety failures. Repeated runs should use the same inputs and settings, and keep their separate outcomes.
5. Compare at least two different model families or independently versioned models before claiming cross-model evaluation. Rerun relevant cases after prompt changes. Preserve unexpected behavior as a regression case; do not weaken expectations to match it.

`scripts/validate.sh` and `scripts/test-validate.sh` run offline structural checks. They do not invoke models. A completed checklist or a prose review is not a recorded behavioral run.

## Results template

Save real runs under `evals/results/` using this template; never fill in outcomes that were not observed.

```markdown
# Evaluation run

- Date and reviewer:
- Prompt commit and uncommitted diff/artifact:
- Model/provider and exact version:
- Settings and tool permissions:
- Interface: chat or agent

| Case | Outcome (Pass / Fail / Not run) | Evidence or transcript | Untested behavior |
| --- | --- | --- | --- |
| E01 | Not run | | |
| E02 | Not run | | |
| E03 | Not run | | |
| E04 | Not run | | |
| E05 | Not run | | |
| E06 | Not run | | |
| E07 | Not run | | |
| E08 | Not run | | |
| E09 | Not run | | |
| E10 | Not run | | |

- Failures and follow-up:
- Limits on conclusions:
```
