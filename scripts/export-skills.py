#!/usr/bin/env python3
"""Export every prompt as an Agent Skill into a universal-agent-skills checkout."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ("audits", "development", "operations", "prompting")

# name -> (display name, short description, description with trigger conditions)
SKILLS: dict[str, tuple[str, str, str]] = {
    "full-project-audit": (
        "Full Project Audit",
        "Score every area of a project and plan the remaining checks",
        "Assess a project across 17 areas and 22 project types, score each area with evidence, and plan the remaining checks. Use when the user asks what a project is missing, wants a complete review, or asks for a full project audit.",
    ),
    "production-readiness-review": (
        "Production Readiness Review",
        "Decide whether a project is ready for production",
        "Review a whole project for production readiness across functionality, security, configuration, tests, operations and documentation, apply safe fixes, and give a Ready, Almost ready, Not ready or Insufficient evidence verdict. Use when the user asks whether a project is ready to ship or wants a pre-launch review.",
    ),
    "security-audit": (
        "Security Audit",
        "Find exploitable vulnerabilities with a 76-item checklist",
        "Audit an application for exploitable vulnerabilities with a 76-item checklist covering secrets, authentication, authorization, injection, uploads, APIs, payments, transport, infrastructure, supply chain and AI features; Depth: quick covers the 25 launch essentials. Use when the user asks for a security review, a vulnerability audit or a pentest-style check of code.",
    ),
    "threat-model": (
        "Threat Model",
        "Design-level threats, controls and mitigations",
        "Build a design-level threat model: data flows, trust boundaries, assets, attackers, STRIDE threats, existing controls, prioritized mitigations and a verification plan. Use when the user asks for a threat model, a risk analysis or a security design review before building or launching.",
    ),
    "legal-compliance-review": (
        "Legal and Compliance Review",
        "Privacy, consumer-protection, marketing and licensing risks",
        "Review a product for privacy, cookie, consumer-protection, marketing-claim, accessibility-obligation and licensing risks, compare policies with what the code actually does, and prepare points for a lawyer. Use when the user asks about GDPR, cookies, terms, refunds, legal risk or compliance before launch.",
    ),
    "accessibility-audit": (
        "Accessibility Audit",
        "Audit against every WCAG 2.2 A and AA criterion",
        "Audit a user interface against every WCAG 2.2 A and AA criterion with evidence, fix safe barriers, and produce a manual test plan. Use when the user asks about accessibility, WCAG, screen readers, keyboard use or contrast.",
    ),
    "ux-review": (
        "UX Review",
        "Usability, states, copy, emails, localization and CLI ergonomics",
        "Review usability: onboarding, navigation, forms, states, copy, emails, localization and command-line ergonomics, with concrete fixes. Use when the user asks for a UX or usability review, better copy or error messages, or a localization check.",
    ),
    "performance-audit": (
        "Performance Audit",
        "Find and fix the bottlenecks that matter, with measurements",
        "Find and fix the performance problems that matter, backed by measurements: queries, caching, bundles, Core Web Vitals, scaling limits and cost. Use when the user reports slowness, asks for optimization or a performance review, or wants to know what breaks under load.",
    ),
    "operations-audit": (
        "Operations and Reliability Audit",
        "Observability, deployments, backups, recovery and resilience",
        "Audit observability, alerting, deployments, backups, disaster recovery, resilience, security operations, cost and incident readiness. Use when the user asks whether a system can be operated and recovered, or wants an SRE, reliability or operations review.",
    ),
    "infrastructure-audit": (
        "Infrastructure and Configuration Audit",
        "Review IaC, containers, Kubernetes, Nix and CI without applying",
        "Audit infrastructure and configuration code: Terraform, Pulumi, Ansible, Kubernetes, Helm, Docker, Compose, Nix, CI pipelines and cloud settings, without applying anything. Use when the user asks for an infrastructure, IaC, container, Kubernetes, Ansible or NixOS review.",
    ),
    "data-audit": (
        "Data and Database Audit",
        "Schemas, migrations, queries, integrity, backups and pipelines",
        "Audit schemas, migrations, queries, integrity, access control, backups, data quality and pipelines, without running anything against a live database. Use when the user asks for a database, schema, migration or data pipeline review.",
    ),
    "api-design-review": (
        "API Design Review",
        "REST, GraphQL, gRPC, realtime, webhook and SDK surfaces",
        "Review REST, GraphQL, gRPC, WebSocket, SSE, webhook and SDK interfaces for consistency, errors, pagination, versioning, compatibility and documentation. Use when the user asks for an API design review, an API consistency check or a breaking-change assessment.",
    ),
    "architecture-review": (
        "Architecture and Codebase Health Review",
        "Structure, risks and technical debt with a prioritized plan",
        "Assess architecture and codebase health: boundaries, consistency, runtime qualities, evolvability, hotspots and technical debt, with ranked risks and a prioritized plan. Use when the user asks whether the architecture fits, how healthy the codebase is, or which technical debt to pay first.",
    ),
    "ai-feature-review": (
        "AI Feature Review",
        "Reliability, evaluation, safety, privacy and cost of AI features",
        "Review LLM, agent, retrieval and ML features for reliability, evaluation, safety, privacy, cost and user experience. Use when the user asks to review an AI feature, prompts, RAG, agents with tools or a trained model.",
    ),
    "cli-and-scripts-audit": (
        "CLI and Scripts Audit",
        "Make CLIs, shell and PowerShell scripts safe and portable",
        "Audit command-line tools, shell and PowerShell scripts, installers, setup scripts and dotfiles for safety, robustness, portability, testing and distribution, and fix the safe parts. Use when the user asks to review a CLI, a shell or PowerShell script, an installer or a setup tool.",
    ),
    "repository-audit": (
        "Repository Audit",
        "Docs, licensing, metadata, history, automation and releases",
        "Audit a repository as a product: README, license, community and security files, metadata, history hygiene, branch protection, CI, dependency automation and releases. Use when the user asks to prepare a repository for publishing, open source or contributors, or wants a repository hygiene check.",
    ),
    "start-project": (
        "Start a New Project",
        "Scaffold a project with its whole baseline in place",
        "Set up a new project with structure, build, tests, quality gates, CI, documentation, security basics, licensing and agent instructions from the first commit. Use when the user starts a new project or asks to scaffold or bootstrap one.",
    ),
    "implement-feature": (
        "Implement a Feature",
        "Plan, build, test and verify a feature",
        "Implement a feature with a plan, small verified changes that follow the project's conventions, tests and documentation. Use when the user asks to build, add or implement functionality.",
    ),
    "debug": (
        "Debug a Problem",
        "Find the root cause and fix it properly",
        "Find the root cause of a bug by reproducing it, testing hypotheses one at a time, fixing the cause and adding a regression test. Use when the user reports a bug, an error, a crash or unexpected behavior.",
    ),
    "write-tests": (
        "Write Tests",
        "Add tests that catch real bugs",
        "Add tests that catch real bugs for the most important untested behavior, following the project's test setup, and prove that they can fail. Use when the user asks for tests, coverage or a regression test.",
    ),
    "refactor": (
        "Simplify and Refactor",
        "Make code simpler without changing behavior",
        "Simplify code without changing behavior: remove duplication, dead code and needless abstraction in small steps verified by tests. Use when the user asks to refactor, simplify, clean up or reduce complexity.",
    ),
    "review-code": (
        "Review Code",
        "Review a diff, branch or pull request",
        "Review a diff, branch or pull request for correctness, security, data compatibility, tests and maintainability, with a verdict and concrete findings. Use when the user asks for a code review or a review of a pull request.",
    ),
    "explain-codebase": (
        "Explain This Codebase",
        "An onboarding guide to an unfamiliar project",
        "Explain an unfamiliar codebase: purpose, stack, how to run it, architecture, key flows, data model, conventions, where to make changes and gotchas. Use when the user asks how a project works, wants onboarding or an overview.",
    ),
    "write-docs": (
        "Write Documentation",
        "Make the README and docs accurate and useful",
        "Write or update documentation so it matches what the code does, starting with the README. Use when the user asks for a README, documentation, or fixes to outdated documentation.",
    ),
    "upgrade-dependencies": (
        "Upgrade Dependencies",
        "Upgrade packages and runtimes safely, security fixes first",
        "Upgrade dependencies and runtimes safely in small verified batches, security fixes first, with a lockfile review. Use when the user asks to update, upgrade or bump dependencies or a runtime version.",
    ),
    "describe-changes": (
        "Describe Changes",
        "Commit messages and pull request descriptions",
        "Write commit messages and pull request descriptions that explain what changed and why, matching the repository's conventions. Use when the user asks for a commit message or a pull request description.",
    ),
    "prepare-release": (
        "Prepare a Release",
        "Version, changelog, release notes and verified artifacts",
        "Prepare a release: decide the version, check readiness, update the version and changelog, write release notes, verify artifacts and list the commands to tag and publish. Use when the user asks to release, cut a version or write release notes.",
    ),
    "incident-response": (
        "Incident Response and Postmortem",
        "Stabilize, diagnose, then write a blameless postmortem",
        "Handle a production incident: stabilize first, then diagnose, then write a blameless postmortem, never acting on live systems without confirmation. Use when something is broken in production or the user asks for a postmortem.",
    ),
    "improve-prompt": (
        "Improve a Prompt",
        "Turn any prompt into a clear, model-agnostic one",
        "Rewrite a prompt so it works reliably across AI models, with clear structure, scope, output format and handling of missing information. Use when the user asks to improve, fix or rewrite a prompt.",
    ),
    "write-agent-instructions": (
        "Write Agent Instructions",
        "An accurate AGENTS.md or CLAUDE.md for a repository",
        "Write an accurate AGENTS.md or CLAUDE.md with verified commands, structure, conventions, boundaries and pitfalls, plus thin pointer files for other agents. Use when the user asks for an AGENTS.md, CLAUDE.md, Copilot instructions or Cursor rules.",
    ),
}

# Sentences that only make sense for a prompt file, with their skill equivalents.
EXACT = [
    (
        "The deeper prompts live next to this file in the same collection (the paths below, such as `audits/security-audit.md`, are relative to the collection's root, not to the project). If you can read them, follow them for the areas with gaps, carrying over this audit's mode, scope and permissions regardless of their defaults; if you cannot, name them in the report so I can supply them.",
        "The deeper prompts are installed as skills next to this one; invoke them by name (for example the `security-audit` skill) for the areas with gaps, carrying over this audit's mode, scope and permissions regardless of their defaults.",
    ),
    (
        "Name the deep-dive prompt for each area with gaps; I will paste it into a new conversation.",
        "Name the deep-dive skill for each area with gaps.",
    ),
    (
        "Most areas have a deeper prompt in this collection, named in the area heading;",
        "Most areas have a deeper skill, named in the area heading;",
    ),
    ("pasted with this prompt", "given with the skill invocation"),
    ("the refactoring prompt does the changes", "the `refactor` skill does the changes"),
    ("Accessibility has its own prompt;", "Accessibility has its own skill;"),
    ("This prompt needs no project access", "This skill needs no project access"),
    ("the deep-dive prompt to run", "the deep-dive skill to run"),
]
REFERENCE_RE = re.compile(r"`(?:audits|development|operations|prompting)/([a-z-]+)\.md`")
SETTINGS_RE = re.compile(r"(## Settings\n\n(?:- .*\n)+)")
PLACEHOLDER_RE = re.compile(r"\{\{Describe the (\w+) here or after this prompt: (.*?)\}\}", re.S)
PASTE_RE = re.compile(r"\{\{Paste the prompt here or after this prompt\.\}\}")
OVERRIDE = "Text given with the skill invocation overrides these defaults."
RENAMED = {"code-review": "review-code"}


def skill_name(path: Path) -> str:
    return RENAMED.get(path.stem, path.stem)


def convert(text: str) -> str:
    for old, new in EXACT:
        text = text.replace(old, new)
    text = REFERENCE_RE.sub(lambda m: f"the `{RENAMED.get(m.group(1), m.group(1))}` skill", text)
    text = SETTINGS_RE.sub(lambda m: f"{m.group(1)}\n{OVERRIDE}\n", text, count=1)
    text = PLACEHOLDER_RE.sub(
        lambda m: f"The {m.group(1)} description comes with the skill invocation and should cover {m.group(2)}",
        text,
    )
    text = PASTE_RE.sub("The prompt to improve comes with the skill invocation.", text)
    return text


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def export(target: Path) -> int:
    skills_dir = target / "skills"
    if not skills_dir.is_dir():
        print(f"error: {skills_dir} is not a directory", file=sys.stderr)
        return 1
    prompts = sorted(p for folder in FOLDERS for p in (ROOT / folder).glob("*.md"))
    names = {skill_name(p) for p in prompts}
    if names != set(SKILLS):
        print(f"error: prompt files and SKILLS table differ: {sorted(names ^ set(SKILLS))}", file=sys.stderr)
        return 1
    for path in prompts:
        name = skill_name(path)
        display, short, description = SKILLS[name]
        body = convert(path.read_text(encoding="utf-8")).strip()
        if "TODO" in body or re.search(r"\{\{(Describe|Paste) ", body):
            print(f"error: {path}: unconverted marker in exported body", file=sys.stderr)
            return 1
        skill = skills_dir / name
        (skill / "agents").mkdir(parents=True, exist_ok=True)
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {yaml_quote(description)}\nlicense: MIT\n---\n\n{body}\n",
            encoding="utf-8",
        )
        (skill / "agents" / "openai.yaml").write_text(
            "interface:\n"
            f"  display_name: {yaml_quote(display)}\n"
            f"  short_description: {yaml_quote(short)}\n"
            f"  default_prompt: {yaml_quote(f'Use ${name} to {short[0].lower()}{short[1:]}.')}\n",
            encoding="utf-8",
        )
    print(f"exported {len(prompts)} skills to {skills_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="path to a universal-agent-skills checkout")
    args = parser.parse_args()
    return export(args.target.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
