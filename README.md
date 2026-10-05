# AI Prompts

Model-agnostic prompts for building, reviewing and shipping software with AI. They work in any chat (ChatGPT, Claude, Gemini, Copilot, Mistral, DeepSeek, local models) and in coding agents (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode and others), for any language or stack.

## Prompts

### Audits

| Prompt | Use it to |
| --- | --- |
| [Production readiness review](audits/production-readiness-review.md) | Decide whether a project is ready for production across 12 areas, with safe fixes along the way |
| [Security audit](audits/security-audit.md) | Run 76 checks, from leaked secrets and broken access control to webhooks, CI/CD and AI features. `Depth: quick` covers the 25 launch essentials |
| [Legal and compliance review](audits/legal-compliance-review.md) | Catch privacy, cookie, consumer-protection, marketing-claim, accessibility and licensing risks before launch |
| [Accessibility audit](audits/accessibility-audit.md) | Audit against WCAG 2.2 AA and fix the barriers |
| [Performance audit](audits/performance-audit.md) | Find and fix the bottlenecks that matter, backed by measurements |

### Development

| Prompt | Use it to |
| --- | --- |
| [Code review](development/code-review.md) | Review a diff, branch or pull request |
| [Debug a problem](development/debug.md) | Find the root cause of a bug and fix it properly |
| [Implement a feature](development/implement-feature.md) | Plan, build, test and verify a feature |
| [Write tests](development/write-tests.md) | Add tests that catch real bugs |
| [Simplify and refactor](development/refactor.md) | Make code simpler without changing behavior |
| [Explain this codebase](development/explain-codebase.md) | Get an onboarding guide to an unfamiliar project |
| [Write documentation](development/write-docs.md) | Make the README and docs accurate and useful |

### Prompting

| Prompt | Use it to |
| --- | --- |
| [Improve a prompt](prompting/improve-prompt.md) | Turn any prompt into a clear, model-agnostic one |

## Usage

Each file is one complete prompt: copy the whole file, nothing else is needed.

**In a chat.** Paste the prompt and add your material: code, files, a URL or a description. Without access to your project, the AI asks for what it needs and marks what it could not verify, so the result depends on what you give it.

**In a coding agent.** Start the agent in your project folder and paste the prompt, or point it to the file if the agent can read outside the project:

```text
Read ~/path/to/AI_prompts/audits/security-audit.md and follow it for this project.
```

**As a reusable command.** Most coding agents can also store a prompt as a custom command or skill (for example Claude Code and Codex skills, Cursor commands or GitHub Copilot prompt files). See your agent's documentation for the location and format.

## Settings

Most prompts start with a short **Settings** block. The defaults work as they are; edit a value to change the behavior:

- `Mode: report` makes a review read-only, and `Mode: fix` lets the AI apply safe, contained fixes. The legal review and code review start in `report`; the other prompts with a Mode setting start in `fix`. Changes are never committed or pushed unless you ask.
- `Report language: Norwegian` (or any other language) gets the report in that language. The prompts themselves are in English because that is the language models follow most consistently.
- `Scope: the payment flow only` narrows a review.

You can also add instructions after the prompt, for example "Focus on the admin panel" or "The app is only sold in Norway".

## Design principles

- **Self-contained and portable**: plain Markdown with no vendor-specific syntax, tools or features.
- **With or without project access**: with access, the AI verifies by itself; without it, the AI asks for what it needs.
- **Evidence over opinion**: findings cite files, lines, configuration or command output, and anything unverifiable is marked instead of guessed.
- **Safe by default**: no printed secrets, destructive commands, dependency changes, deployments, commits or pushes without approval.
- **Stack-agnostic**: the AI identifies the project type and adapts, marking irrelevant checks "Not applicable".
- **Consistent reports**: verdict first, then findings by severity, then what remains.

## Adding a prompt

Start from this skeleton, run the result through [Improve a prompt](prompting/improve-prompt.md), and test it with at least two different models:

```markdown
# Title

The goal in one or two sentences, and what a good result looks like.

## Settings

- Mode: report
- Report language: English

## Working environment

- With access to the project: ...
- Without access (a plain chat): ...

## How to work

1. ...

## Rules

- ...

## Report

1. ...
```

## Limitations

AI reviews miss things and sometimes get them wrong. Use these prompts to find problems faster, not as a replacement for professional penetration testing, accessibility testing with real users, or legal advice.

The security and legal checklists started from popular "checks for your AI-built app" lists and were expanded with OWASP guidance, WCAG 2.2 and current regulation.

## License

[MIT](LICENSE)
