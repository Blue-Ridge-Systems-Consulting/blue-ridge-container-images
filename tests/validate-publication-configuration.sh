#!/usr/bin/env bash
set -euo pipefail

workflow=.github/workflows/publish-reo-laptop-containers.yml
readme=README.md

grep -Fqx '        default: localhost/reo-ai:fedora44-20260915,localhost/reo-tools:fedora44-20260903,localhost/olmoai:fedora44,localhost/apertusai:fedora44' "$workflow"
grep -Fqx '            [[ "$source" =~ ^localhost/(reo-ai|reo-tools|olmoai|apertusai):[A-Za-z0-9._-]+$ ]] || {' "$workflow"
grep -Fqx '      - name: Verify anonymous public pulls' "$workflow"
grep -Fqx '| `apertusai` | `podman pull ghcr.io/blue-ridge-systems-consulting/apertusai:blue-ridge-public` |' "$readme"

if [[ -n "${GITHUB_BASE_REF:-}" ]]; then
    git diff --check "origin/${GITHUB_BASE_REF}...HEAD"
else
    git diff --check HEAD^...HEAD
fi
