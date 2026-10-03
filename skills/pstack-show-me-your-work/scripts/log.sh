#!/usr/bin/env bash
# Keep the original six-argument entrypoint; append logic is stdlib Python.
set -euo pipefail
script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "${script_dir}/log.py" "$@"
