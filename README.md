# AI Prompts

[![Validate](https://github.com/26zl/AI_prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/26zl/AI_prompts/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Model-agnostic prompts for building, reviewing and shipping software with AI. Designed for chats (ChatGPT, Claude, Gemini, Copilot, Mistral, DeepSeek, local models) and coding agents (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode and others), across languages and stacks. They provide a broad baseline; the depth of the review depends on the project, supplied evidence, model and available tools.

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
| [Full project audit](audits/full-project-audit.md) | Score a project across 17 areas and 22 project types, add its domain-specific requirements, and get the plan to 100% |
| [Production readiness review](audits/production-readiness-review.md) | Decide whether a project is ready for production, with safe fixes along the way |
| [Security audit](audits/security-audit.md) | Run 76 checks, from leaked secrets and broken access control to webhooks, CI/CD and AI features. `Depth: quick` covers the 25 launch essentials |
| [Threat model](audits/threat-model.md) | Map assets, attackers, trust boundaries and threats at the design level |
| [Legal and compliance review](audits/legal-compliance-review.md) | Catch privacy, cookie, consumer-protection, marketing-claim, accessibility and licensing risks before launch |
| [Accessibility audit](audits/accessibility-audit.md) | Review every WCAG 2.2 A and AA criterion, record evidence and fix practical barriers |
| [UX review](audits/ux-review.md) | Check usability, states, copy, emails, localization and command-line ergonomics |
| [Performance audit](audits/performance-audit.md) | Find and fix the bottlenecks that matter, backed by measurements |
| [Operations and reliability audit](audits/operations-audit.md) | Check observability, deployments, recovery, resilience, cost and safe retirement |
| [Infrastructure and configuration audit](audits/infrastructure-audit.md) | Review Terraform, Ansible, Kubernetes, Docker, Nix, CI pipelines and cloud configuration |
| [Data and database audit](audits/data-audit.md) | Review schemas, migrations, queries, integrity, access, backups and pipelines |
| [API design review](audits/api-design-review.md) | Review REST, GraphQL, gRPC, WebSocket, SSE, webhooks and SDK surfaces for consistency and compatibility |
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
| Shell or PowerShell scripts, installers, setup and hardening tools, dotfiles | CLI and scripts, security |
| Security and offensive tooling (scanners, auditors, sandboxes) | Security, threat model, CLI and scripts, legal (authorized use) |
| Automation acting on external accounts, devices or money (bots, trading, banking CLIs, device tweaks) | Security, CLI and scripts, operations, legal |
| Agent skills, MCP servers, plugins | Security, AI feature, repository |
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

Mobile, desktop, extensions, embedded systems, smart contracts and research code have baseline checks in the full audit, not a complete specialist audit. Identify the target platforms, hazards and applicable domain standards before judging readiness. Regulated health, finance or safety-critical systems also need domain expertise and any required independent assessment.

## Usage

Each file is one complete prompt: copy the whole file, nothing else is needed.

**In a chat.** Paste the prompt and add your material: code, files, a URL or a description. Without access to your project, the AI asks for what it needs and marks what it could not verify, so the result depends on what you give it.

**In a coding agent.** Start the agent in your project folder and paste the prompt, or point it to the file if the agent can read outside the project:

```text
Read ~/path/to/AI_prompts/audits/security-audit.md and follow it for this project.
```

**Deep dives.** The full project audit names the deep-dive prompt for each gap by its path in this repository, for example `audits/security-audit.md`. An agent that can read this folder follows it on its own, with the same mode and permissions; otherwise paste the named prompt into a new conversation. Nothing needs to be copied into the project.

**As a reusable command.** Most coding agents can also store a prompt as a custom command or skill (for example Claude Code and Codex skills, Cursor commands or GitHub Copilot prompt files). See your agent's documentation for the location and format.

## Settings

Most prompts start with a short **Settings** block. The defaults work as they are; edit a value to change the behavior:

- `Mode: report` makes a review read-only, and `Mode: fix` lets the AI apply the contained fixes listed in that prompt. Each prompt states its default. Referenced prompts and delegated tasks inherit the current mode, scope and permissions, retaining any stricter limits; their defaults cannot broaden them. Changes are never committed or pushed unless you ask.
- `Report language: Norwegian` (or any other language) gets the report in that language. The prompts themselves are in English because that is the language models follow most consistently.
- `Scope: the payment flow only` narrows a review.

You can also add instructions after the prompt, for example "Focus on the admin panel" or "The app is only sold in Norway".

## What 100% means

A project is at 100% when every check that applies to it passes with evidence: the universal areas, the project-type checks, and any domain requirements identified for it. The full project audit defines those checks; each deep-dive prompt defines the same for its area. "Not applicable" needs a reason, and "Not verified" never counts as a pass, even when you accept the risk; accepted risks are listed separately with an owner, a rationale and a review date. The score measures completion of the declared checks, not proof that no defect exists, and an unknown critical requirement blocks an unconditional readiness verdict.

## Design principles

- **Self-contained and portable**: plain Markdown with no vendor-specific syntax, tools or features.
- **With or without project access**: with access, the AI verifies by itself; without it, the AI asks for what it needs.
- **Evidence over opinion**: findings cite files, lines, configuration or command output, and anything unverifiable is marked instead of guessed.
- **Safe by default**: every prompt includes safety boundaries. Inspect commands and their target environments before running them; isolate checks that write artifacts. Never print secrets or personal data. Dependency changes, destructive actions and external side effects require explicit authorization, which can already be supplied by the task.
- **Stack-agnostic**: the AI identifies the project type and adapts, marking irrelevant checks "Not applicable".
- **Consistent reports**: a verdict first, then findings by severity, then what remains.

## Adding a prompt

Start from this skeleton, run the result through [Improve a prompt](prompting/improve-prompt.md), and evaluate relevant [synthetic cases](evals/cases.md) with at least two different models using the [evaluation procedure](evals/README.md). Record the prompt revision, model versions, results and evidence; unexecuted cases stay Not run. Before committing, run `scripts/validate.sh` and `bash scripts/test-validate.sh`. CI runs both checks; they check structure, safety sections, numbering, links, whitespace and secret-like strings, plus rejection of invalid inputs. They do not execute models or establish prompt quality.

```markdown
# Title

The goal in one or two sentences, and what a good result looks like.

## Settings

- Mode: report
- Report language: English

## Working environment

- With access to the project: ...
- Without access (a plain chat): ...

## Safety boundaries

(Copy the four bullets from any audit; every prompt carries the same block.)

## How to work

1. ...

## Rules

- ...

## Report

1. ...
```

## Limitations

AI reviews miss things and sometimes get them wrong. Use these prompts to find problems faster, not as a replacement for professional penetration testing, accessibility testing with real users, or legal advice.

The security and legal checklists started from popular "checks for your AI-built app" lists and were expanded with OWASP guidance, WCAG 2.2 and examples of relevant regulation. Legal, store and platform requirements change: each review must state its date, markets and the official sources checked, including effective dates and uncertainty. The collection does not certify security, accessibility or legal compliance.

## License

[MIT](LICENSE)
