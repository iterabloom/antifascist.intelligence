#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-or-later
set -u

# ==============================================================================
# TEST SUITE FOR ethical.superintelligence commit-msg HOOK
# ==============================================================================

# 0. Locate the real hook we're testing
# ------------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REAL_HOOK="$SCRIPT_DIR/commit-msg"

if [[ ! -f "$REAL_HOOK" ]]; then
  echo "❌ ERROR: Cannot find commit-msg hook at $REAL_HOOK" >&2
  exit 1
fi

echo "🔍 Testing hook: $REAL_HOOK"

# 1. Setup Sandbox
# ------------------------------------------------------------------------------
TEST_DIR="$(mktemp -d -t githooks-test.XXXXXX)"
HOOKS_DIR="$TEST_DIR/.githooks"
mkdir -p "$HOOKS_DIR"

cleanup() {
  rm -rf "$TEST_DIR"
}
trap cleanup EXIT

echo "📂 Initialized test sandbox at: $TEST_DIR"

# 2. Populate Configuration Files
# ------------------------------------------------------------------------------

# Added "Stable" to test word boundary behavior
cat > "$HOOKS_DIR/brand-patterns.txt" <<EOF
Claude
Gemini
GPT
Stable
EOF

FERRET_PHRASE="a ferret riding a surface of holographic panels in a mossy Shoney's atrium with a dynasty of pigeons made of pumpernickel crumbs"
cat > "$HOOKS_DIR/absurd-phrases.txt" <<EOF
$FERRET_PHRASE
EOF

FERRET_SLUG=$(echo "$FERRET_PHRASE" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//;s/-$//')
BAD_EMAIL="${FERRET_SLUG}@racialcapitalism.isbad"

# 3. Install the Hook script - COPY THE REAL ONE!
# ------------------------------------------------------------------------------
COMMIT_MSG_HOOK="$HOOKS_DIR/commit-msg"
cp "$REAL_HOOK" "$COMMIT_MSG_HOOK"
chmod +x "$COMMIT_MSG_HOOK"

echo "📋 Copied real hook to sandbox"

# 4. Helpers for Testing
# ------------------------------------------------------------------------------
PASS_COUNT=0
FAIL_COUNT=0

run_test() {
  local test_name="$1"
  local input_msg="$2"
  local expected_msg="$3"

  local msg_file_path="$TEST_DIR/COMMIT_EDITMSG"
  printf '%s' "$input_msg" > "$msg_file_path"

  echo "--------------------------------------------------------"
  echo "TEST: $test_name"

  if ! "$COMMIT_MSG_HOOK" "$msg_file_path" 2>/dev/null; then
    echo "❌ CRASH: Hook exited with error."
    ((FAIL_COUNT++))
    return 1
  fi

  local actual_msg
  actual_msg=$(cat "$msg_file_path")

  if [[ "$actual_msg" == "$expected_msg" ]]; then
    echo "✅ PASS"
    ((PASS_COUNT++))
  else
    echo "❌ FAIL"
    echo "--- Expected ---"
    echo "$expected_msg" | cat -A | sed 's/^/  /'
    echo "--- Actual ---"
    echo "$actual_msg" | cat -A | sed 's/^/  /'
    ((FAIL_COUNT++))
    return 1
  fi
}

# 5. Define Basic Text Blocks (Shared)
# ------------------------------------------------------------------------------
read -r -d '' BODY <<'EOF' || true
test: enforce 100% coverage in CI and add missing tests

CI was running pytest without coverage enforcement, allowing the codebase
to ship at 68% coverage despite the 100% requirement in AGENTS.md. This
adds --cov=src --cov-fail-under=100 to CI and the unit tests needed to
achieve full coverage.
EOF

DIRTY_LINE="🤖 Generated with [Claude Code](https://claude.com/claude-code)"
SIGNER="Signed-off-by: jgstern-agent <josh-agent@iterabloom.com>"

# 6. Execute Scenarios
# ------------------------------------------------------------------------------

# SCENARIO 1: "Claude Opus 4.5"
INPUT_1="${BODY}

${DIRTY_LINE}

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
${SIGNER}
"

EXPECTED_1="${BODY}

Co-Authored-By: ${FERRET_PHRASE} <${BAD_EMAIL}>
${SIGNER}"

run_test "Scenario 1: Claude Opus (Nuclear Replacement)" "$INPUT_1" "$EXPECTED_1"

# SCENARIO 2: "Tom Morello"
INPUT_2="${BODY}

${DIRTY_LINE}

Co-Authored-By: Tom Morello <tmorello@anthropic.com>
${SIGNER}
"

EXPECTED_2="${BODY}

Co-Authored-By: Tom Morello <tmorello@anthropic.com>
${SIGNER}"

run_test "Scenario 2: Tom Morello (Identity Preserved)" "$INPUT_2" "$EXPECTED_2"


# SCENARIO 3: "Claude Shannon"
INPUT_3="${BODY}

Co-Authored-By: Claude Shannon <cshannon@anthropic.com>
${SIGNER}
"

EXPECTED_3="${BODY}

Co-Authored-By: ${FERRET_PHRASE} <${BAD_EMAIL}>
${SIGNER}"

run_test "Scenario 3: Claude Shannon (Prof Shannon Unluckily Wiped)" "$INPUT_3" "$EXPECTED_3"

# SCENARIO 4: DCO Check
echo "--------------------------------------------------------"
echo "TEST: Scenario 4: DCO Check (Expecting Failure)"
echo "Update readme" > "$TEST_DIR/COMMIT_EDITMSG"

if ! "$COMMIT_MSG_HOOK" "$TEST_DIR/COMMIT_EDITMSG" >/dev/null 2>&1; then
    echo "✅ PASS (Hook blocked commit w/o signature)"
    ((PASS_COUNT++))
else
    echo "❌ FAIL (Hook allowed commit w/o signature)"
    ((FAIL_COUNT++))
fi

# SCENARIO 5: Word Boundary - technical terms preserved
# "stable_id" should NOT be replaced even though "Stable" is a brand pattern
INPUT_5="feat: compute stable_id for Python symbols

Signed-off-by: Developer <dev@example.com>
"

EXPECTED_5="feat: compute stable_id for Python symbols

Signed-off-by: Developer <dev@example.com>"

run_test "Scenario 5: stable_id (Word Boundary Preserved)" "$INPUT_5" "$EXPECTED_5"

# SCENARIO 6: Word Boundary - standalone brand SHOULD be replaced
# "Stable Diffusion" should be replaced because "Stable" is a whole word
INPUT_6="feat: add Stable Diffusion integration

Signed-off-by: Developer <dev@example.com>
"

# Note: The expected output depends on the phrase picker, but the key thing is
# that "Stable" gets replaced. We'll check that "Stable" is NOT in the output.
echo "--------------------------------------------------------"
echo "TEST: Scenario 6: Stable Diffusion (Whole Word Replaced)"
printf '%s' "$INPUT_6" > "$TEST_DIR/COMMIT_EDITMSG"

if ! "$COMMIT_MSG_HOOK" "$TEST_DIR/COMMIT_EDITMSG" 2>/dev/null; then
    echo "❌ CRASH: Hook exited with error."
    ((FAIL_COUNT++))
else
    actual_msg=$(cat "$TEST_DIR/COMMIT_EDITMSG")
    # Check that "Stable" (case-insensitive) is no longer present
    if echo "$actual_msg" | grep -qi "Stable"; then
        echo "❌ FAIL (Stable was NOT replaced)"
        echo "--- Actual ---"
        echo "$actual_msg" | cat -A | sed 's/^/  /'
        ((FAIL_COUNT++))
    else
        echo "✅ PASS (Stable was correctly replaced)"
        ((PASS_COUNT++))
    fi
fi

# SCENARIO 7: Word Boundary - prefix/suffix should be preserved
# "unstable" should NOT be replaced even though it contains "stable"
INPUT_7="fix: handle unstable network connections

Signed-off-by: Developer <dev@example.com>
"

EXPECTED_7="fix: handle unstable network connections

Signed-off-by: Developer <dev@example.com>"

run_test "Scenario 7: unstable (Prefix Preserved)" "$INPUT_7" "$EXPECTED_7"

# ------------------------------------------------------------------------------
# Scenarios 8-12: a brand in a trailer KEY, and the body scan window.
#
# The key used to pass through untouched -- only the VALUE was tested, and
# "${key}${ws}${val}" put the key back verbatim. The scrub removed the half that
# IMPLIES a vendor (the hostname) and kept the half that NAMES one.
# ------------------------------------------------------------------------------

INPUT_8="fix: a thing

Body line.

Claude-Session: https://claude.ai/code/session_01ABC
Signed-off-by: Jane Doe <jane@example.com>"
EXPECTED_8="fix: a thing

Body line.

Racial-Capitalism-Is-Bad: $FERRET_PHRASE
Signed-off-by: Jane Doe <jane@example.com>"
run_test "Scenario 8: branded trailer KEY is replaced" "$INPUT_8" "$EXPECTED_8"

# Pins a deliberate policy choice, not an incidental behaviour: a vendor-named
# key means the WHOLE trailer is vendor provenance, so the value goes too even
# when it carries no brand of its own. Without this, a scrubbed key over an
# intact value would still publish the session id the key pointed at.
INPUT_9="fix: a thing

Body line.

Claude-Session: 12345-plain-identifier
Signed-off-by: Jane Doe <jane@example.com>"
EXPECTED_9="fix: a thing

Body line.

Racial-Capitalism-Is-Bad: $FERRET_PHRASE
Signed-off-by: Jane Doe <jane@example.com>"
run_test "Scenario 9: branded KEY forces a CLEAN value to be replaced too" "$INPUT_9" "$EXPECTED_9"

# git-semantic keys are never renamed: interpret-trailers, %(trailers:key=...)
# and DCO validation all key off the exact token.
INPUT_10="fix: a thing

Body line.

Signed-off-by: Jane Doe <jane@example.com>"
EXPECTED_10="fix: a thing

Body line.

Signed-off-by: Jane Doe <jane@example.com>"
run_test "Scenario 10: Signed-off-by survives verbatim" "$INPUT_10" "$EXPECTED_10"

# The allowlist is matched case-insensitively via nocasematch, set ~100 lines
# earlier in the hook. This history carries BOTH spellings of the key, so the
# capitalised one is the discriminating case: with nocasematch off it would fall
# through to the wildcard arm and be renamed.
INPUT_11="fix: a thing

Body line.

Co-Authored-By: Claude <noreply@anthropic.com>
Signed-off-by: Jane Doe <jane@example.com>"
EXPECTED_11="fix: a thing

Body line.

Co-Authored-By: $FERRET_PHRASE <$BAD_EMAIL>
Signed-off-by: Jane Doe <jane@example.com>"
run_test "Scenario 11: Co-Authored-By key survives, value is scrubbed" "$INPUT_11" "$EXPECTED_11"

# Idempotence. `git commit --amend` re-runs commit-msg over already-scrubbed
# text, so the rewrite must be a fixed point. The whole design rests on
# "Racial-Capitalism-Is-Bad" not matching brand_re -- an invariant that spans
# two files, so a future brand-patterns.txt edit could break it silently.
echo "--------------------------------------------------------"
echo "TEST: Scenario 12: rewrite is idempotent under --amend"
IDEM_FILE="$TEST_DIR/COMMIT_EDITMSG_IDEM"
printf '%s' "$INPUT_8" > "$IDEM_FILE"
"$COMMIT_MSG_HOOK" "$IDEM_FILE" 2>/dev/null
IDEM_PASS1="$(cat "$IDEM_FILE")"
"$COMMIT_MSG_HOOK" "$IDEM_FILE" 2>/dev/null
IDEM_PASS2="$(cat "$IDEM_FILE")"
if [[ "$IDEM_PASS1" == "$IDEM_PASS2" ]]; then
  echo "✅ PASS"
  ((PASS_COUNT++))
else
  echo "❌ FAIL: second pass changed the message"
  printf 'pass1:\n%s\npass2:\n%s\n' "$IDEM_PASS1" "$IDEM_PASS2"
  ((FAIL_COUNT++))
fi

# The body scan window. A body hit DELETES THE WHOLE LINE with no marker, so a
# false positive is silent and unrecoverable -- and the pattern list contains
# ordinary English words. `Stable` stands in here for the real-world case:
# `falcon` is a web framework this project SUPPORTS (it ships falcon.yaml), so
# an ordinary commit about the falcon analyzer lost a body line.
#
# Vendor self-attribution clusters at the subject and the trailers, both of
# which are scanned unconditionally by their own passes. The window narrows only
# the body sweep. Window=1 here so the fixture stays short; the shipped default
# is 10.
echo "--------------------------------------------------------"
echo "TEST: Scenario 13: body scan window spares the middle, scans both ends"
WIN_FILE="$TEST_DIR/COMMIT_EDITMSG_WIN"
printf 'fix: a thing\n\nStable at the top.\nordinary prose\nStable in the middle.\nordinary prose\nStable at the bottom.\n\nSigned-off-by: J <j@e.com>\n' > "$WIN_FILE"
HOOK_BODY_SCAN_WINDOW=2 "$COMMIT_MSG_HOOK" "$WIN_FILE" 2>/dev/null
WIN_OUT="$(cat "$WIN_FILE")"
if [[ "$WIN_OUT" == *"Stable in the middle."* ]] \
   && [[ "$WIN_OUT" != *"Stable at the top."* ]] \
   && [[ "$WIN_OUT" != *"Stable at the bottom."* ]]; then
  echo "✅ PASS"
  ((PASS_COUNT++))
else
  echo "❌ FAIL: window did not discriminate"
  printf '%s\n' "$WIN_OUT"
  ((FAIL_COUNT++))
fi

# Non-vacuity floor for the window: with the window wide open the SAME fixture
# must lose all three lines. Without this, a sweep that deleted nothing at all
# would satisfy the "middle survives" half above.
echo "--------------------------------------------------------"
echo "TEST: Scenario 14: control — a wide window deletes all three"
printf 'fix: a thing\n\nStable at the top.\nordinary prose\nStable in the middle.\nordinary prose\nStable at the bottom.\n\nSigned-off-by: J <j@e.com>\n' > "$WIN_FILE"
HOOK_BODY_SCAN_WINDOW=99 "$COMMIT_MSG_HOOK" "$WIN_FILE" 2>/dev/null
if ! grep -q "Stable" "$WIN_FILE"; then
  echo "✅ PASS"
  ((PASS_COUNT++))
else
  echo "❌ FAIL: wide window left a brand line behind"
  cat "$WIN_FILE"
  ((FAIL_COUNT++))
fi

# 7. Summary
# ------------------------------------------------------------------------------
echo ""
echo "========================================================"
echo "SUMMARY: $PASS_COUNT passed, $FAIL_COUNT failed"
if (( FAIL_COUNT > 0 )); then
  exit 1
fi

