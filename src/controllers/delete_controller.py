import json
import os
from typing import Any, Dict, List


def _students_file_path() -> str:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return os.path.join(root, "data", "students.json")


def delete_student_by_mssv(mssv: str) -> bool:
    """Delete a student from data/students.json by MSSV.

    Args:
        mssv: Student ID to delete (string comparison).

    Returns:
        True if a student was found and deleted, False otherwise.
    """
    path = _students_file_path()
    if not os.path.exists(path):
        return False

    try:
        with open(path, "r", encoding="utf-8") as f:
            # Check if file is empty
            content = f.read()
            if not content:
                return False
            data = json.loads(content)
    except (json.JSONDecodeError, OSError):
        return False

    if not isinstance(data, list):
        return False

    # Find the student index
    original_len = len(data)
    # Perform case-insensitive comparison if mssv is alphanumeric string
    filtered = [s for s in data if str(s.get("mssv", "")).strip().lower() != str(mssv).strip().lower()]

    if len(filtered) == original_len:
        # No student found with that MSSV
        return False

    try:
        # Ensure directory exists before writing (though it should since we read from it)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(filtered, f, ensure_ascii=False, indent=4)
    except OSError:
        return False

    return True


if __name__ == "__main__":
    # quick manual test: pass MSSV as input
    import sys

    if len(sys.argv) < 2:
        print("Usage: python delete_controller.py <mssv>")
    else:
        m = sys.argv[1]
        ok = delete_student_by_mssv(m)
        print("Deleted" if ok else "Not found or error")
