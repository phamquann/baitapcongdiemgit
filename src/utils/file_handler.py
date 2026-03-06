("""Simple JSON file read/write helpers.

Functions:
- `read_json(path, default)` -> load JSON from `path`, return `default` on missing/invalid file
- `write_json(path, data)` -> write `data` as JSON to `path` (creates parent dirs)
""")

from __future__ import annotations

import json
import os
from typing import Any


def read_json(path: str, default: Any = None) -> Any:
	"""Read JSON from `path` and return parsed object.

	If file does not exist or contains invalid JSON, `default` is returned.
	"""
	if default is None:
		default = []

	if not os.path.exists(path):
		return default

	try:
		with open(path, "r", encoding="utf-8") as f:
			return json.load(f)
	except (json.JSONDecodeError, OSError):
		return default


def write_json(path: str, data: Any) -> None:
	"""Write `data` as JSON to `path`. Creates parent directories if needed."""
	dirpath = os.path.dirname(path)
	if dirpath and not os.path.exists(dirpath):
		os.makedirs(dirpath, exist_ok=True)

	# Use a temporary file pattern would be nicer, but keep it simple.
	with open(path, "w", encoding="utf-8") as f:
		json.dump(data, f, ensure_ascii=False, indent=2)

