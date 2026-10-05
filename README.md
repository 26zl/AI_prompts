# AI Prompts

[![Validate](https://github.com/26zl/AI_prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/26zl/AI_prompts/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Model-agnostic prompts for building, reviewing and shipping software with AI. They work in any chat (ChatGPT, Claude, Gemini, Copilot, Mistral, DeepSeek, local models) and in coding agents (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode and others), for any language, stack or project type.

## Start here

| Situation | Prompt |
| --- | --- |
| Starting something new | [Start a new project](development/start-project.md) sets up the whole baseline from the first commit |
| An existing project you want checked from end to end | [Full project audit](audits/full-project-audit.md) scores every area, applies project-type checks, and tells you which deep dives to run |
| About to release | [Production readiness review](audits/production-readiness-review.md), then [Prepare a release](development/prepare-release.md) |
| Something is broken in production | [Incident response and postmortem](operations/incident-response.md) |
| Day-to-day work | The [development](#development) prompts |

## Prompts

### Audits

| Prompt | Use it to |
| --- | --- |
| [Full project audit](audits/full-project-audit.md) | Score a project across 17 areas and 20 project types, and get the plan to 100% |
| [Production readiness review](audits/production-readiness-review.md) | Decide whether a project is ready for production, with safe fixes along the way |
| [Security audit](audits/security-audit.md) | Run 76 checks, from leaked secrets and broken access control to webhooks, CI/CD and AI features. `Depth: quick` covers the 25 launch essentials |
| [Threat model](audits/threat-model.md) | Map assets, attackers, trust boundaries and threats at the design level |
| [Legal and compliance review](audits/legal-compliance-review.md) | Catch privacy, cookie, consumer-protection, marketing-claim, accessibility and licensing risks before launch |
| [Accessibility audit](audits/accessibility-audit.md) | Audit against WCAG 2.2 AA and fix the barriers |
| [UX review](audits/ux-review.md) | Check usability, states, copy, emails, localization and command-line ergonomics |
| [Performance audit](audits/performance-audit.md) | Find and fix the bottlenecks that matter, backed by measurements |
| [Operations and reliability audit](audits/operations-audit.md) | Check observability, alerting, deployments, backups, recovery, resilience and cost |
| [Infrastructure and configuration audit](audits/infrastructure-audit.md) | Review Terraform, Ansible, Kubernetes, Docker, Nix, CI pipelines and cloud configuration |
| [Data and database audit](audits/data-audit.md) | Review schemas, migrations, queries, integrity, access, backups and pipelines |
| [API design review](audits/api-design-review.md) | Review REST, GraphQL, gRPC, webhooks and SDK surfaces for consistency and evolvability |
| [Architecture and codebase health review](audits/architecture-review.md) | Assess structure, risks and technical debt, with a prioritized plan |
| [AI feature review](audits/ai-feature-review.md) | Review LLM and ML features for reliability, evaluation, safety, privacy and cost |
| [CLI and scripts audit](audits/cli-and-scripts-audit.md) | Make command-line tools, shell and PowerShell scripts, installers and dotfiles safe and portable |
| [Repository audit](audits/repository-audit.md) | Check documentation, licensing, community files, metadata, history, automation and releases |

### Development

| Prompt | Use it to |
| --- | --- |
| [Start a new project](development/start-project.md) | Scaffold a project with structure, tests, CI, docs, security basics and licensing in place |
| [Implement a feature](development/implement-feature.md) | Plan, build, test and verify a feature |
| [Debug a problem](development/debug.md) | Find the root cause of a bug and fix it properly |
| [Write tests](development/write-tests.md) | Add tests that catch real bugs |
| [Simplify and refactor](development/refactor.md) | Make code simpler without changing behavior |
| [Code review](development/code-review.md) | Review a diff, branch or pull request |
| [Explain this codebase](development/explain-codebase.md) | Get an onboarding guide to an unfamiliar project |
| [Write documentation](development/write-docs.md) | Make the README and docs accurate and useful |
| [Upgrade dependencies](development/upgrade-dependencies.md) | Upgrade packages and runtimes safely, security fixes first |
| [Describe changes](development/describe-changes.md) | Write commit messages and pull request descriptions |
| [Prepare a release](development/prepare-release.md) | Decide the version, update the changelog, write release notes and verify artifacts |

### Operations

| Prompt | Use it to |
| --- | --- |
| [Incident response and postmortem](operations/incident-response.md) | Stabilize a live incident, find the cause, and write a blameless postmortem |

### Prompting

| Prompt | Use it to |
| --- | --- |
| [Improve a prompt](prompting/improve-prompt.md) | Turn any prompt into a clear, model-agnostic one |
| [Write agent instructions](prompting/write-agent-instructions.md) | Create an accurate `AGENTS.md` or `CLAUDE.md` for a repository |

## Which prompts for which project

Every project benefits from the full project audit, the repository audit and the development prompts. On top of those:

| Project type | Run these audits |
| --- | --- |
| Web app, SaaS, e-commerce | Security, legal, accessibility, UX, performance, operations, data, API design, threat model |
| API or backend service | Security, API design, data, operations, performance, threat model, infrastructure |
| CLI tool | CLI and scripts, security, UX (command-line section) |
| Shell or PowerShell scripts, installers, setup tools, dotfiles | CLI and scripts, security |
| Library, SDK or package | API design (SDK section), security, performance |
| Mobile app | Security, legal, accessibility, UX, performance, operations |
| Desktop app or browser extension | Security, legal, accessibility, UX |
| Infrastructure, configuration, homelab, NixOS | Infrastructure, security, operations, CLI and scripts |
| Data pipeline or analytics | Data, operations, security, performance |
| Machine learning or AI product | AI feature, data, security, legal, performance |
| Bot, integration, webhook, MCP server or agent skill | Security, AI feature, operations, API design (webhooks) |
| Documentation site, template or content | Accessibility, UX, legal (licenses) |
| Game | Performance, accessibility, UX, legal, security for multiplayer |
| Embedded, firmware or driver | Security, CLI and scripts (build and install scripts), operations |

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

- `Mode: report` makes a review read-only, and `Mode: fix` lets the AI apply safe, contained fixes. Each prompt states its default: reviews that touch infrastructure, data, contracts, design or legal questions start in `report`, the rest in `fix`. Changes are never committed or pushed unless you ask.
- `Report language: Norwegian` (or any other language) gets the report in that language. The prompts themselves are in English because that is the language models follow most consistently.
- `Scope: the payment flow only` narrows a review.

You can also add instructions after the prompt, for example "Focus on the admin panel" or "The app is only sold in Norway".

## What 100% means

A project is complete when every check that applies to it passes with evidence, and nothing is left "Not verified" that you have not consciously accepted. The full project audit defines the checks per area and per project type; each deep-dive prompt defines the same for its area. Checks that do not apply to a project type are marked "Not applicable", so the target is 100% of what applies, not every check in every prompt.

## Design principles

- **Self-contained and portable**: plain Markdown with no vendor-specific syntax, tools or features.
- **With or without project access**: with access, the AI verifies by itself; without it, the AI asks for what it needs.
- **Evidence over opinion**: findings cite files, lines, configuration or command output, and anything unverifiable is marked instead of guessed.
- **Safe by default**: no printed secrets, destructive commands, dependency changes, deployments, commits or pushes without approval.
- **Stack-agnostic**: the AI identifies the project type and adapts, marking irrelevant checks "Not applicable".
- **Consistent reports**: a verdict first, then findings by severity, then what remains.

## Adding a prompt

Start from this skeleton, run the result through [Improve a prompt](prompting/improve-prompt.md), test it with at least two different models, and run `scripts/validate.sh` before committing. CI runs the same script on every push; it checks structure, numbering, links, whitespace and secret-like strings.

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
