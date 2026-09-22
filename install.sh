#!/usr/bin/env bash
# Fruti Squad installer (git/clone path). Thin wrapper over bin/install.mjs so
# there is a single source of truth. Requires Node >= 16.
#
# Usage:
#   ./install.sh [install|list|help] [--target kiro|claude|codex] [--global]
#                [--dest <dir>] [--only <names>] [--force] [--dry-run]
#
# Examples:
#   ./install.sh install --target kiro
#   ./install.sh install --target claude --global
#   ./install.sh install --target codex --dest /path/to/project

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: Node.js (>=16) is required to run the installer." >&2
  echo "Install Node, then re-run:  ./install.sh install --target kiro" >&2
  exit 1
fi

# Default to 'install' if the first arg is a flag or missing.
if [[ $# -eq 0 || "${1:-}" == --* ]]; then
  exec node "$DIR/bin/install.mjs" install "$@"
else
  exec node "$DIR/bin/install.mjs" "$@"
fi
