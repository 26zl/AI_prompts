# Write Agent Instructions

Write the instruction file that tells AI coding agents how to work in this repository, so every agent and every session starts with the same accurate knowledge of how to build, test and change the project, and the same boundaries. The file is for agents, but it is read and maintained by people, so it has to stay short and true.

## Settings

- Agents: all
- Report language: English

Agents can be `all` or a list, for example "Claude Code and Codex". Write the instruction file in English unless the repository's documentation is consistently in another language.

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): explore the repository and verify every command you write down by running it.
- **Without access** (a plain chat): ask for the README, the file tree, package manifests and scripts, CI configuration, contributing guidelines and any existing agent files; mark the commands you could not verify.

## How to work

1. **Check what exists**: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/`, `.windsurf/rules/`, `.clinerules` and similar; README, CONTRIBUTING and CI configuration. Extend and correct existing files rather than duplicating them.
2. **Learn the project**: how to install, run, test (all and a single test), lint, format, type check and build; the structure and where things live; conventions for code, tests, commits and branches; the domain vocabulary; environments and configuration; what is generated, vendored or must not be edited; what is dangerous (production data, deployments, payments, migrations); and the pitfalls that have cost time (flaky tests, slow commands, platform quirks).
3. **Write the canonical file** (`AGENTS.md` unless the repository already uses another name) using the structure below.
4. **Add thin files for other agents** only where needed: a `CLAUDE.md` that imports or points to the canonical file, and a `.github/copilot-instructions.md`, `GEMINI.md` or Cursor rules that reference it, so there is one source of truth. Check each agent's current documentation for the file name and format it expects, since these change.
5. **Verify**: every command runs as written; every path exists; nothing contradicts README or CONTRIBUTING; the file is short enough to read in two minutes.

## Structure of the instruction file

1. **Project in two lines**: what it is, the stack, and the main entry points.
2. **Commands**: install, run, test (all, one file, one test), lint, format, type check, build, and database or migration commands, exactly as they should be run, with the working directory if it matters.
3. **Structure**: the top-level directories and what belongs where, plus where to add a new feature, endpoint, component, migration or test.
4. **Conventions**: language, style and formatting (point to the configuration rather than restating it), naming, error handling, logging, tests (framework, location, naming, what must be covered), commits and branches, documentation language.
5. **Boundaries**: what never to do without asking (deploy, touch production data, run migrations, change public APIs, add dependencies, modify generated or vendored files, commit secrets, force push), and what must always be done before finishing (run the tests, run the linter, update docs or the changelog).
6. **Domain notes**: terms, invariants and business rules an agent must not get wrong.
7. **Pitfalls**: the known traps, flaky areas and platform quirks, each in one line with the workaround.
8. **Where to look**: documentation, architecture notes, decision records, the issue tracker, and existing examples of good code to imitate.

## Rules

- Keep it short: aim for under 150 lines; link to documents instead of copying them; no generic advice an agent already follows.
- Everything must be true and verified; a wrong command in this file costs more than no file.
- Be specific and imperative: "Run `make test` before finishing" rather than "Testing is important".
- Do not duplicate the README; summarize and link.
- Do not add secrets, personal data, internal URLs that should not be shared, or anything that would be wrong to commit.
- Write for both humans and agents; avoid shouting, threats and stacked warnings.
- Do not commit or push unless I ask.

## Output

1. The instruction file or files, each with its path, as complete file contents.
2. **Verification**: the commands run and their results, and anything that could not be verified.
3. **Notes**: existing files updated or superseded, contradictions found between README, CONTRIBUTING and reality, and suggested follow-ups (for example a stale README).
