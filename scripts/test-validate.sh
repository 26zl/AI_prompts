#!/usr/bin/env bash
set -euo pipefail

repo_dir=$(cd "$(dirname "$0")/.." && pwd)
test_dir=$(mktemp -d "${TMPDIR:-/tmp}/ai-prompts-validation.XXXXXX")
trap 'rm -rf -- "$test_dir"' EXIT
fixture_dir="$test_dir/repo with spaces"
mkdir -p "$fixture_dir/scripts"
cp -R "$repo_dir/audits" "$repo_dir/development" "$repo_dir/operations" "$repo_dir/prompting" "$repo_dir/evals" "$fixture_dir/"
cp "$repo_dir/README.md" "$repo_dir/LICENSE" "$fixture_dir/"
cp "$repo_dir/scripts/validate.sh" "$fixture_dir/scripts/"

expect_failure() {
  if bash "$fixture_dir/scripts/validate.sh" >"$test_dir/output" 2>&1; then
    printf 'error: validator accepted %s\n' "$1" >&2
    exit 1
  fi
  if ! grep -Fq -- "$2" "$test_dir/output"; then
    printf 'error: validator rejected %s for the wrong reason\n' "$1" >&2
    exit 1
  fi
}

bash "$fixture_dir/scripts/validate.sh"

sed '/^## Safety boundaries$/d' "$repo_dir/development/debug.md" >"$fixture_dir/development/debug.md"
expect_failure 'missing safety boundaries' "missing '## Safety boundaries'"
cp "$repo_dir/development/debug.md" "$fixture_dir/development/debug.md"

printf '\n[Broken](missing-prompt.md)\n' >>"$fixture_dir/README.md"
expect_failure 'broken README link' 'links to a missing file: missing-prompt.md'
cp "$repo_dir/README.md" "$fixture_dir/README.md"

sed 's/^2\. /999. /' "$repo_dir/development/debug.md" >"$fixture_dir/development/debug.md"
expect_failure 'invalid checklist numbering' 'list item 999'
cp "$repo_dir/development/debug.md" "$fixture_dir/development/debug.md"

sed '/^| 1\.3\.4 | AA |/d' "$repo_dir/audits/accessibility-audit.md" >"$fixture_dir/audits/accessibility-audit.md"
expect_failure 'missing WCAG criterion' 'requires all 55 unique WCAG'
sed 's/^| 1\.3\.4 | AA |/| 2.5.2 | A |/' "$repo_dir/audits/accessibility-audit.md" >"$fixture_dir/audits/accessibility-audit.md"
expect_failure 'duplicate WCAG criterion' 'requires all 55 unique WCAG'
cp "$repo_dir/audits/accessibility-audit.md" "$fixture_dir/audits/accessibility-audit.md"

synthetic_token='sk_test_'
synthetic_token+='SYNTHETICEXAMPLEONLY123'
printf '\n%s\n' "$synthetic_token" >>"$fixture_dir/README.md"
printf '\n%s\t \n' "$synthetic_token" >>"$fixture_dir/development/debug.md"
expect_failure 'synthetic secret marker' 'a secret-like string was found'
if grep -Fq -- "$synthetic_token" "$test_dir/output"; then
  printf 'error: validator disclosed the synthetic secret marker\n' >&2
  exit 1
fi
cp "$repo_dir/README.md" "$fixture_dir/README.md"
cp "$repo_dir/development/debug.md" "$fixture_dir/development/debug.md"

bash "$fixture_dir/scripts/validate.sh"
printf 'ok: validator regression checks passed\n'
