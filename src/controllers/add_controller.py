"""Simple add controller to append a student record to the JSON file."""

from __future__ import annotations

from typing import Any, Dict

from pathlib import Path

from ..utils.file_handler import read_json, write_json


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATH = str(ROOT / "data" / "students.json")


def add_student(student: Dict[str, Any], path: str = DEFAULT_PATH) -> None:
	"""Append `student` (dict) to the JSON list stored at `path`."""
	data = read_json(path, default=[])
	if not isinstance(data, list):
		# try to handle dict container
		if isinstance(data, dict) and "students" in data and isinstance(data["students"], list):
			data = data["students"]
		else:
			data = []

	data.append(student)
	write_json(path, data)


if __name__ == "__main__":
	# small demo add
	demo = {"id": "SV003", "name": "Lê Văn C", "age": 22, "grade": 6.9}
	add_student(demo)
	print("Added demo student.")
