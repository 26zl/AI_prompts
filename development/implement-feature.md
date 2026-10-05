# Implement a Feature

Implement the feature described below the way a careful senior engineer would: understand the existing code first, make the smallest complete change that fits the project's conventions, then test and verify it.

## Feature

{{Describe the feature here or after this prompt: what it should do, for whom, the acceptance criteria, and any constraints, designs or examples.}}

If there is no feature description, ask for one before doing anything else.

## Settings

- Confirm plan first: for large or risky changes
- Report language: English

Set "Confirm plan first" to `always` to approve every plan before coding starts, or to `never` to proceed without stopping. Write code, comments and documentation in the project's existing language, whatever the report language.

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): explore the codebase, implement the change and run the project's checks.
- **Without access** (a plain chat): ask for the files and context you need (relevant code, similar existing features, data models, conventions), then deliver complete, ready-to-apply changes with file paths, and say how to verify them.

## How to work

1. **Understand**: restate the feature and its acceptance criteria. Read the relevant code, similar existing features, project instructions (README, CONTRIBUTING, AGENTS.md, CLAUDE.md or similar) and tests, and identify the patterns to follow.
2. **Clarify**: if something is ambiguous and a wrong guess would be costly, ask a few focused questions before coding. Otherwise state your assumptions and continue.
3. **Plan**: list the files to change, the approach, any data or schema changes, and how you will test it. Wait for my approval before coding when the setting requires it. A change is large or risky when it adds dependencies, changes the database schema, touches authentication, authorization or payments, changes a public API, or deletes code.
4. **Implement in small steps**, following the existing conventions for structure, naming, error handling, logging and styling, and reusing existing utilities and components.
5. **Handle the details**: input validation, authorization, empty, loading and error states, edge cases, accessibility for user interfaces, and user-facing text.
6. **Test**: add or update tests for the new behavior and its edge cases, following the project's testing patterns.
7. **Verify**: run the tests, linting, type checks and build. Review your own diff for unrelated changes, debug code, leftover TODOs and secrets.
8. **Document**: update documentation, configuration examples such as `.env.example`, or the changelog where the project keeps them.

## Rules

- Keep the diff focused: no drive-by refactoring, reformatting or renaming. Report unrelated problems you notice instead of ignoring them or fixing them silently.
- No placeholder implementations, mock data in production code, or TODOs presented as finished work. If you cannot complete something, say so clearly.
- Do not add dependencies without explaining why and getting my approval.
- Never hardcode secrets; use the project's configuration mechanism and document only the variable name.
- Add comments only for non-obvious intent or constraints.
- Do not commit or push unless I ask.

## Output

1. **Summary** of what was implemented.
2. **Files changed**, one line each.
3. **How to try it** manually.
4. **Tests and checks** run, with results.
5. **Assumptions, limitations and follow-ups**.
