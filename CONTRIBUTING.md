# Contributing

This page explains how the repository is organised, which checks a change must pass and how a change gets merged. The README's [Adding a prompt](README.md#adding-a-prompt) section has the skeleton a new prompt starts from.

## Layout

- `audits/`, `development/`, `operations/`, `prompting/`: one prompt per file. Each file is a complete, self-contained Markdown document: a level-1 title, then `## Settings`, `## Working environment`, `## Safety boundaries` and the working sections, ending with `## Report` (or `## Output` or `## Cover`).
- `evals/`: synthetic behavioural cases and the procedure for running them against models.
- `scripts/validate.sh`: structural checks. `scripts/test-validate.sh`: checks that the validator still rejects what it should. `scripts/export-skills.py`: exports the prompts as Agent Skills.
- `README.md`: links every prompt. The validator fails when a prompt is missing from it.

## Checks

Run both from the repository root before opening a pull request:

```sh
scripts/validate.sh
bash scripts/test-validate.sh
```

CI (`.github/workflows/validate.yml`) runs the same two commands on every pull request and on pushes to `main`. `validate.sh` checks, for every prompt file:

- the first line is a level-1 title and the required sections exist;
- numbered items either restart at 1 or continue from the previous item;
- no trailing whitespace and no non-ASCII characters, except the star that marks quick-depth items and the Norwegian letters that appear in law names;
- the README links to the file, and every relative link in the README resolves;
- no secret-like strings in any Markdown file;
- the accessibility audit maps all 55 WCAG 2.2 A/AA criteria, and the check counts quoted in the README match the security audit.

`test-validate.sh` copies the repository into a temporary directory and confirms that the validator rejects a prompt without safety boundaries, a broken README link, bad numbering, a missing or duplicate WCAG criterion and a synthetic secret marker, without echoing the marker.

Neither script runs a model. Passing checks mean the structure is right, not that the prompt works; behaviour is checked with the [evaluation procedure](evals/README.md) and the cases in `evals/cases.md`.

## Writing a prompt

- Plain Markdown with no vendor-specific syntax, so the prompt works in any chat and any coding agent.
- Keep the `## Safety boundaries` block identical to the one in the other prompts; copy it from any audit.
- Make the prompt work with and without project access: say what the AI should ask for when it cannot see the project.
- Findings cite evidence; anything unverifiable is marked, not guessed.
- Write the prompt in English; `Report language` in the settings is what changes the output language.
- When you add, rename or remove a prompt, update the README tables and the `SKILLS` table in `scripts/export-skills.py`. The export refuses to run when the prompt files and that table disagree.

## Changing a prompt

1. Edit the file, or create a new one from the README skeleton.
2. Run the result through `prompting/improve-prompt.md`.
3. Evaluate the relevant cases from `evals/cases.md` with at least two different models, following `evals/README.md`. Record the prompt revision, models, settings and outcomes; cases you did not run stay "Not run".
4. Run `scripts/validate.sh` and `bash scripts/test-validate.sh`.
5. Open a pull request against `main`. Say what changed and why, and include the evaluation record when behaviour changed.

A change to `scripts/validate.sh` that alters what is accepted or rejected needs a matching case in `scripts/test-validate.sh`. `scripts/export-skills.py` uses only the Python standard library; keep it that way.

## Exporting the skills

The collection is distributed as Agent Skills through [universal-agent-skills](https://github.com/26zl/universal-agent-skills). After a prompt changes, regenerate the skills from a checkout of that repository and open a pull request there with the result:

```sh
scripts/export-skills.py <path-to-universal-agent-skills>
```

For every prompt the script writes `skills/<name>/SKILL.md` (frontmatter from the `SKILLS` table, then the converted prompt body) and `skills/<name>/agents/openai.yaml`. The conversion replaces references to prompt paths with skill names, adds the note that text given with the invocation overrides the settings, and rewrites the placeholders that only make sense when pasting a prompt. The skill name is the file name; `development/review-code.md` is called that, rather than `code-review`, because `code-review` is a built-in Claude Code command.

## Commits and pull requests

- Commit subjects are imperative and explain what changed; use the body for why. There is no prefix convention.
- One topic per pull request, with CI green. The maintainer reviews and merges.
- There are no releases: `main` is what people use and what the skills are exported from.

## Questions and problems

Open an [issue](https://github.com/26zl/AI_prompts/issues) for a mistake in a prompt, a false positive in the validator or a suggestion. For anything security-related, see [SECURITY.md](SECURITY.md).
