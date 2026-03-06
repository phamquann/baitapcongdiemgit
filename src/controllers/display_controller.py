"""Display controller: load and show student list from JSON file."""

from __future__ import annotations

from pathlib import Path
from typing import Any, List

from ..utils.file_handler import read_json


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATH = str(ROOT / "data" / "students.json")


def get_students(path: str = DEFAULT_PATH) -> List[Any]:
	"""Return the list of students loaded from `path`.

	Returns an empty list if file is missing or invalid.
	"""
	data = read_json(path, default=[])
	if isinstance(data, list):
		return data
	# If file contains a dict (e.g., {"students": [...]}) try to extract list
	if isinstance(data, dict):
		for key in ("students", "data", "items"):
			if key in data and isinstance(data[key], list):
				return data[key]
	return []


def display_students(path: str = DEFAULT_PATH) -> List[Any]:
	"""Load and print the students in a formatted table. Returns the list."""
	students = get_students(path)
	if not students:
		print("Không có sinh viên nào.")
		return students

	# Determine columns (keys) and column widths
	keys = []
	for s in students:
		if isinstance(s, dict):
			for k in s.keys():
				if k not in keys:
					keys.append(k)

	if not keys:
		for i, s in enumerate(students, start=1):
			print(f"{i}. {s}")
		return students

	# compute max width per column
	widths = {k: len(k) for k in keys}
	rows = []
	for s in students:
		row = []
		for k in keys:
			v = s.get(k, "") if isinstance(s, dict) else ""
			text = str(v)
			row.append(text)
			widths[k] = max(widths[k], len(text))
		rows.append(row)

	# print header
	header_cells = [k.ljust(widths[k]) for k in keys]
	header = " | ".join(header_cells)
	sep = "-+-".join("-" * widths[k] for k in keys)
	print(header)
	print(sep)

	# print rows
	for i, row in enumerate(rows, start=1):
		cells = [row[idx].ljust(widths[keys[idx]]) for idx in range(len(keys))]
		print(f"{i:>2}. " + " | ".join(cells))

	return students


if __name__ == "__main__":
	display_students()

