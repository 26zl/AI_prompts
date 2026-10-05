# Simplify and Refactor

Make this code simpler and easier to maintain without changing what it does. Every change must preserve behavior and be verifiable.

## Settings

- Target: auto
- Report language: English

`auto` target means: find the code that most needs it yourself. You can also name files, modules or functions. Write code and comments in the project's existing language, whatever the report language.

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): read the code, refactor it, and run the tests after each step.
- **Without access** (a plain chat): work on the code I paste, ask for callers and tests when behavior depends on them, and deliver the complete refactored code with an explanation of each change.

## How to work

1. **Set up a safety net**: find and run the existing tests for the target. If coverage is weak, first add characterization tests that capture the current behavior.
2. **Find what is worth changing**, for example:
   - duplicated logic, and long functions that do several things
   - deep nesting and unclear names
   - dead code and unused parameters, exports, files and dependencies
   - needless abstraction: interfaces with a single implementation, factories and wrappers that add nothing, configuration options nobody uses
   - several patterns for the same thing in one codebase
   - defensive checks for states that cannot happen, and redundant try/catch blocks
   - comments that restate the code, and other verbose leftovers from generated code
3. **Refactor in small steps**, each one preserving behavior, and run the tests after each step.
4. **Review the final diff**: the code should end up with fewer concepts, not just moved code.

## Rules

- Preserve behavior and public interfaces (APIs, CLI flags, configuration, database schema, output formats) unless I approve a change.
- Do not mix refactoring with bug fixes or new features. Report bugs you find; if one is small and safe to fix, fix it as a separate, clearly labeled change.
- Follow the codebase's existing conventions. Do not introduce new patterns, frameworks or dependencies.
- Do not reformat untouched code or rename things for taste.
- Prefer deleting code to adding it, and do not add abstractions for hypothetical future needs.
- If there are no tests and behavior cannot be verified, limit yourself to clearly safe mechanical changes and say so.
- Do not commit or push.

## Output

1. **Summary**: what got simpler, for example lines removed, functions merged or dependencies dropped.
2. **Changes by file**, one line each.
3. **Evidence that behavior is preserved**: the tests run and their results.
4. **Bugs and risks noticed**, and whether they were fixed separately.
5. **Larger opportunities** not done, with a rough effort estimate.
