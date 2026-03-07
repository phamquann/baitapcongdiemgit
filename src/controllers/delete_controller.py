"""Controller for deleting a student by MSSV.

This module intentionally reads/writes the JSON data file directly so it
doesn't require changes to other modules.
"""
from __future__ import annotations

import json
import os
from typing import List, Dict, Any


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_FILE = os.path.join(ROOT, 'data', 'students.json')


def _load_students() -> List[Dict[str, Any]]:
	try:
		with open(DATA_FILE, 'r', encoding='utf-8') as f:
			return json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		return []


def _save_students(students: List[Dict[str, Any]]) -> None:
	os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
	# Write to a temporary file and atomically replace the data file.
	tmp_path = DATA_FILE + '.tmp'
	with open(tmp_path, 'w', encoding='utf-8') as f:
		json.dump(students, f, ensure_ascii=False, indent=2)
	# Use os.replace for an atomic rename (works across platforms)
	os.replace(tmp_path, DATA_FILE)


def delete_student_by_mssv(mssv: str) -> bool:
	"""Delete student with the given `mssv`.

	Returns True if a student was removed, False if no matching student found.
	"""
	def _normalize_mssv(value: Any) -> str:
		"""Normalize MSSV for comparison: strip whitespace, collapse numeric forms.

		If the value is purely numeric, convert to canonical integer string
		(to avoid mismatches like '001' vs '1'). Otherwise compare lower-cased
		stripped strings.
		"""
		s = str(value).strip()
		if s.isdigit():
			try:
				return str(int(s))
			except ValueError:
				return s
		return s.lower()

	students = _load_students()
	norm = _normalize_mssv(mssv)
	new_students = [s for s in students if _normalize_mssv(s.get('mssv', '')) != norm]
	if len(new_students) == len(students):
		return False
	_save_students(new_students)
	return True


if __name__ == '__main__':
	import sys

	if len(sys.argv) < 2:
		print('Usage: python delete_controller.py <mssv>')
		raise SystemExit(1)

	mssv_arg = sys.argv[1]
	ok = delete_student_by_mssv(mssv_arg)
	if ok:
		print(f'Deleted student with mssv={mssv_arg}')
	else:
		print(f'No student found with mssv={mssv_arg}')