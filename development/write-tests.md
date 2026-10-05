# Write Tests

Add meaningful tests for the most important untested behavior in this project. The goal is confidence, not a coverage number: tests that would catch real bugs and are easy to maintain.

## Settings

- Target: auto
- Report language: English

`auto` target means: find the most critical, least tested behavior yourself. You can also name files, modules, features or a bug to cover. Write test code in the project's existing language, whatever the report language.

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): inspect the code and test setup, write the tests and run them.
- **Without access** (a plain chat): ask for the code under test, an existing test file as a style example, and the test framework and versions. Deliver complete test files and explain how to run them.

## How to work

1. **Learn the existing test setup**: frameworks, folder structure, naming, fixtures, factories, mocking conventions and how tests are run. Run the existing suite to get a baseline.
2. **Find what matters most** (when the target is `auto`): business rules, money and payments, authentication and permissions, data transformations, parsing and validation, error handling, recently changed or bug-prone code, and anything without tests. Use coverage tools if they are already set up.
3. **Plan the cases** for each unit or flow: the main path, edge cases (empty, null, boundaries, large inputs, Unicode, time zones), error paths and permission checks. A few high-value cases beat many redundant ones.
4. **Write the tests**, following the project's conventions.
5. **Prove that they can fail**: for important tests, temporarily break the code under test, confirm that the test fails, then restore the code. Without project access, explain which change to the code would make each test fail.
6. **Run the relevant suite** and make sure everything passes reliably.

## What makes a good test

- It tests behavior through public interfaces, not implementation details or private functions.
- It is deterministic: no real network calls and no dependence on the current time, randomness, execution order or shared state. Use the project's fakes, fixtures, clock control or seeds.
- It is independent and fast, and cleans up after itself.
- It mocks only at boundaries (network, external services, time), never the code under test.
- Its name describes the scenario and the expected outcome, and it follows an arrange, act, assert structure.
- Its assertions are specific: no tests that pass no matter what, and no snapshot tests for logic.
- It uses synthetic data, never real personal data or real secrets.
- It sits at the right level: unit tests for logic, integration tests for database and API boundaries, and a few end-to-end tests for critical flows if the project has that setup.

## If a test reveals a bug

Do not change the test to match the buggy behavior, and do not silently change production code. Keep the test, mark it as an expected failure if the framework supports that so the bug stays visible, and report the bug with evidence.

Do not add new test frameworks or dependencies without my approval. Do not commit or push.

## Output

1. **Tests added or changed**: each file and what it covers.
2. **Bugs found**, with evidence.
3. **Results** of the test run, and coverage before and after if available.
4. **Remaining gaps**, in priority order.
