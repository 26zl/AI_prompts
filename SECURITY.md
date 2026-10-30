# Security policy

## What counts as a security issue here

This repository holds Markdown prompts, two offline validation scripts and an export script. There is no service, no runtime and no dependency beyond bash, coreutils and Python 3. Reports that matter:

- a prompt that leads a model to unsafe behaviour: a weakened `## Safety boundaries` block, instructions that authorize destructive, paid or external actions the user did not ask for, or wording that makes a model print secrets or personal data;
- a way to make `scripts/validate.sh`, `scripts/test-validate.sh` or `scripts/export-skills.py` do something harmful through a crafted file or argument;
- a secret or personal data committed to the repository.

## How to report

Use GitHub's private vulnerability reporting: [open a draft security advisory](https://github.com/26zl/AI_prompts/security/advisories/new). Only the maintainer sees it. Do not open a public issue for something that could be misused before it is fixed; ordinary mistakes in a prompt belong in a normal [issue](https://github.com/26zl/AI_prompts/issues).

Include the file and section, what the model did or could do because of it, and how to reproduce it (model, interface, settings). Use synthetic examples only; never include real credentials, private code or personal data.

## What to expect

This is a personal project maintained by one person, so there is no guaranteed response time; reports are read and answered as soon as possible. Fixes land on `main`, which is the only supported version, since there are no tagged releases. When a fix changes a prompt, the exported skills in [universal-agent-skills](https://github.com/26zl/universal-agent-skills) are regenerated as well. If you want, you are credited in the advisory once it is published.
