#!/usr/bin/env bash
# Checks the structure and hygiene of every prompt file and the README; runs locally and in CI.
set -euo pipefail

cd "$(dirname "$0")/.."
status=0

fail() {
  printf 'error: %s\n' "$*" >&2
  status=1
}

prompt_files=$(find audits development operations prompting -name '*.md' | sort)

for file in $prompt_files; do
  [ "$(head -n 1 "$file" | cut -c1-2)" = "# " ] || fail "$file: the first line must be a level-1 title"
  grep -q '^## Settings' "$file" || fail "$file: missing '## Settings'"
  grep -q '^## Working environment' "$file" || fail "$file: missing '## Working environment'"
  grep -qE '^## ([0-9]+\. )?(Report|Output|Cover)' "$file" || fail "$file: missing a '## Report', '## Output' or '## Cover' section"

  # Numbered items must either restart at 1 or continue from the previous item.
  awk -v file="$file" '
    /^[0-9]+\. / {
      n = $1 + 0
      if (n != 1 && n != prev + 1) {
        printf "error: %s:%d: list item %d follows %d\n", file, NR, n, prev > "/dev/stderr"
        bad = 1
      }
      prev = n
    }
    END { exit bad }
  ' "$file" || status=1

  if grep -nE ' +$' "$file"; then fail "$file: trailing whitespace"; fi
  # The star marks quick-depth items; Norwegian letters appear in law names.
  if sed -e 's/★//g' -e 's/æ//g' -e 's/ø//g' -e 's/å//g' -e 's/Æ//g' -e 's/Ø//g' -e 's/Å//g' "$file" | LC_ALL=C grep -n '[^ -~]'; then
    fail "$file: unexpected non-ASCII characters"
  fi
  grep -q "($file)" README.md || fail "README.md does not link $file"
done

for target in $(grep -oE '\]\([^)]+\)' README.md | sed -E 's/^\]\((.*)\)$/\1/' | grep -vE '^(https?:|#)' | sort -u); do
  [ -e "$target" ] || fail "README.md links to a missing file: $target"
done

if grep -rnE '(sk_(live|test)_[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' --include='*.md' .; then
  fail "a secret-like string was found"
fi

# Keep the counts stated in the README in step with the security audit.
total=$(awk '/^## Checklist/ { on = 1 } /^## Fixing/ { on = 0 } on && /^[0-9]+\. / { count++ } END { print count }' audits/security-audit.md)
stars=$(grep -cE '^[0-9]+\. ★' audits/security-audit.md)
grep -q "Run $total checks" README.md || fail "README.md: the security audit has $total checks"
grep -q "the $stars launch essentials" README.md || fail "README.md: the security audit marks $stars launch essentials"

if [ "$status" -eq 0 ]; then
  echo "ok: all checks passed"
fi
exit "$status"
