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
	with open(DATA_FILE, 'w', encoding='utf-8') as f:
		json.dump(students, f, ensure_ascii=False, indent=2)


def delete_student_by_mssv(mssv: str) -> bool:
	"""Delete student with the given `mssv`.

	Returns True if a student was removed, False if no matching student found.
	"""
	students = _load_students()
	mssv_str = str(mssv)
	new_students = [s for s in students if str(s.get('mssv')) != mssv_str]
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