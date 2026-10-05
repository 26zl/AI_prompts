#!/usr/bin/env bash
# Checks prompt structure and hygiene; model behavior needs separate evaluation.
set -euo pipefail

cd "$(dirname "$0")/.."
status=0

fail() {
  printf 'error: %s\n' "$*" >&2
  status=1
}

while IFS= read -r file; do
  [ "$(head -n 1 "$file" | cut -c1-2)" = "# " ] || fail "$file: the first line must be a level-1 title"
  grep -q '^## Settings' "$file" || fail "$file: missing '## Settings'"
  grep -q '^## Working environment' "$file" || fail "$file: missing '## Working environment'"
  grep -q '^## Safety boundaries$' "$file" || fail "$file: missing '## Safety boundaries'"
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

  if grep -qE ' +$' "$file"; then fail "$file: trailing whitespace"; fi
  # The star marks quick-depth items; Norwegian letters appear in law names.
  if sed -e 's/★//g' -e 's/æ//g' -e 's/ø//g' -e 's/å//g' -e 's/Æ//g' -e 's/Ø//g' -e 's/Å//g' "$file" | LC_ALL=C grep '[^ -~]' >/dev/null; then
    fail "$file: unexpected non-ASCII characters"
  fi
  grep -Fq -- "($file)" README.md || fail "README.md does not link $file"
done < <(find audits development operations prompting -name '*.md' | sort)

while IFS= read -r target; do
  [ -e "$target" ] || fail "README.md links to a missing file: $target"
done < <(grep -oE '\]\([^)]+\)' README.md | sed -E 's/^\]\((.*)\)$/\1/' | grep -vE '^(https?:|#)' | sort -u)

if grep -rlE '(sk_(live|test)_[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' --include='*.md' .; then
  fail "a secret-like string was found"
fi

# Keep the criterion map complete for the published WCAG 2.2 A/AA set.
awk -F '|' '
  BEGIN {
    n = split("1.1.1:A 1.2.1:A 1.2.2:A 1.2.3:A 1.2.4:AA 1.2.5:AA 1.3.1:A 1.3.2:A 1.3.3:A 1.3.4:AA 1.3.5:AA 1.4.1:A 1.4.2:A 1.4.3:AA 1.4.4:AA 1.4.5:AA 1.4.10:AA 1.4.11:AA 1.4.12:AA 1.4.13:AA 2.1.1:A 2.1.2:A 2.1.4:A 2.2.1:A 2.2.2:A 2.3.1:A 2.4.1:A 2.4.2:A 2.4.3:A 2.4.4:A 2.4.5:AA 2.4.6:AA 2.4.7:AA 2.4.11:AA 2.5.1:A 2.5.2:A 2.5.3:A 2.5.4:A 2.5.7:AA 2.5.8:AA 3.1.1:A 3.1.2:AA 3.2.1:A 3.2.2:A 3.2.3:AA 3.2.4:AA 3.2.6:A 3.3.1:A 3.3.2:A 3.3.3:AA 3.3.4:AA 3.3.7:A 3.3.8:AA 4.1.2:A 4.1.3:AA", items, " ")
    for (i = 1; i <= n; i++) expected[items[i]] = 1
  }
  /^\| [1-4]\.[0-9]+\.[0-9]+ \| (A|AA) \|/ {
    gsub(/ /, "", $2); gsub(/ /, "", $3)
    key = $2 ":" $3
    if (!(key in expected) || seen[key]++) bad = 1
    rows++
  }
  END {
    if (rows != n || bad) {
      print "error: audits/accessibility-audit.md: requires all 55 unique WCAG 2.2 A/AA criteria at their correct levels" > "/dev/stderr"
      exit 1
    }
  }
' audits/accessibility-audit.md || status=1

# Keep the counts stated in the README in step with the security audit.
total=$(awk '/^## Checklist/ { on = 1 } /^## Fixing/ { on = 0 } on && /^[0-9]+\. / { count++ } END { print count }' audits/security-audit.md)
stars=$(grep -cE '^[0-9]+\. ★' audits/security-audit.md)
grep -q "Run $total checks" README.md || fail "README.md: the security audit has $total checks"
grep -q "the $stars launch essentials" README.md || fail "README.md: the security audit marks $stars launch essentials"

if [ "$status" -eq 0 ]; then
  echo "ok: structural checks passed; model behavior was not evaluated"
fi
exit "$status"
