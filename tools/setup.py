"""Repository setup entrypoint: explicit, deterministic and configuration-neutral."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from specialize import main

if __name__ == '__main__':
    raise SystemExit(main())
