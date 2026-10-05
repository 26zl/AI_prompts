# Write and Update Documentation

Make this project's documentation accurate, useful and easy to follow, starting with the README. Documentation must match what the code actually does.

## Settings

- Target: README
- Language: match the existing documentation (English if there is none)

Target can also be `all` (all project documentation) or a specific document or topic.

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): inspect the code and existing documents, run commands to check them where that is safe, and edit the files.
- **Without access** (a plain chat): ask for the current documentation, the file tree, dependency manifests, scripts and configuration examples, then deliver complete documents ready to paste.

## How to work

1. **Take inventory** of existing documentation: README, docs folder, CONTRIBUTING, CHANGELOG, comments in configuration files, `.env.example`, command-line help and links to external wikis.
2. **Check it against reality**: install steps, commands, scripts, environment variables, configuration options, API endpoints and examples must exist and work. Run the commands where that is safe. Note everything that is outdated, missing or wrong.
3. **Write and update**, keeping documentation in a small number of canonical places: extend existing documents rather than creating new ones, merge duplicates, and remove obsolete content.

## A good README covers, where relevant

1. **Name and one-sentence description**: what it is and who it is for.
2. **What it does**: the key features or the problem it solves, briefly and without marketing language.
3. **Quick start**: prerequisites with versions, installation, configuration and running, as copy-pasteable commands.
4. **Configuration**: environment variables and options with descriptions and defaults, pointing to `.env.example` for the names, never real values.
5. **Usage**: common tasks with examples.
6. **Development**: running tests, linting and builds, and a brief overview of the project structure.
7. **Deployment and operations**, if relevant.
8. **Troubleshooting**: common errors and how to fix them.
9. **Contributing, security reporting and license**.

## Rules

- Never document features, commands or options that do not exist. If something is unclear, list it as an open question in your reply instead of guessing.
- Use plain, concise language, short sections, and examples rather than long prose.
- No badges, screenshots or links to things that do not exist or do not work.
- Never include secrets, real personal data, or internal URLs that should not be public.
- Do not create summary, notes or plan files; put that information in your reply.
- Keep docstrings for public APIs accurate, and do not add tutorial-style comments to code.
- Do not commit or push.

## Output

1. **Files changed or created**, and why.
2. **Problems found** (outdated, wrong or missing information) and how they were fixed.
3. **Commands verified**, and any that could not be verified.
4. **Open questions** for me.
