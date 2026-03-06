"""
main.py
-------
Tac gia : Pham Xuan Minh Quan
Nhanh   : main / develop
Mo ta   : Entry point - Menu dieu huong chinh cua he thong quan ly sinh vien.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

# Import cac controller - dung try/except de khong bao loi neu file chua co code
try:
    from src.controllers.add_controller import them_sinh_vien
except ImportError:
    them_sinh_vien = None

try:
    from src.controllers.delete_controller import xoa_sinh_vien
except ImportError:
    xoa_sinh_vien = None

try:
    from src.controllers.search_controller import tim_kiem_sinh_vien
except ImportError:
    tim_kiem_sinh_vien = None

try:
    from src.controllers.update_controller import cap_nhat_sinh_vien
except ImportError:
    cap_nhat_sinh_vien = None

try:
    from src.controllers.display_controller import hien_thi_danh_sach
except ImportError:
    hien_thi_danh_sach = None

try:
    from src.utils.file_handler import load_students, save_students
except ImportError:
    def load_students():
        return []
    def save_students(_):
        pass

from src.controllers.sort_controller import menu_sort


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    print("=" * 50)
    print("  HE THONG QUAN LY SINH VIEN".center(50))
    print("=" * 50)


def print_menu():
    print("\n+------------------------------------------+")
    print("|              MENU CHINH                  |")
    print("+------------------------------------------+")
    print("|  1. Them sinh vien                       |")
    print("|  2. Xoa sinh vien                        |")
    print("|  3. Tim kiem sinh vien                   |")
    print("|  4. Cap nhat thong tin sinh vien         |")
    print("|  5. Hien thi danh sach sinh vien         |")
    print("|  6. Sap xep sinh vien (ten / diem)       |")
    print("|  0. Thoat chuong trinh                   |")
    print("+------------------------------------------+")


def _chua_lam(ten_chuc_nang):
    print("\nChuc nang '{}' chua duoc trien khai.".format(ten_chuc_nang))
    input("   Nhan Enter de quay lai...")


def main():
    students = load_students()

    while True:
        clear_screen()
        print_header()
        print_menu()

        choice = input("\nNhap lua chon cua ban: ").strip()

        if choice == "1":
            if them_sinh_vien:
                students = them_sinh_vien(students)
                save_students(students)
            else:
                _chua_lam("Them sinh vien")

        elif choice == "2":
            if xoa_sinh_vien:
                students = xoa_sinh_vien(students)
                save_students(students)
            else:
                _chua_lam("Xoa sinh vien")

        elif choice == "3":
            if tim_kiem_sinh_vien:
                tim_kiem_sinh_vien(students)
            else:
                _chua_lam("Tim kiem sinh vien")
            input("\n   Nhan Enter de quay lai...")

        elif choice == "4":
            if cap_nhat_sinh_vien:
                students = cap_nhat_sinh_vien(students)
                save_students(students)
            else:
                _chua_lam("Cap nhat thong tin sinh vien")

        elif choice == "5":
            if hien_thi_danh_sach:
                hien_thi_danh_sach(students)
            else:
                _chua_lam("Hien thi danh sach sinh vien")
            input("\n   Nhan Enter de quay lai...")

        elif choice == "6":
            students = menu_sort(students)
            save_students(students)
            input("\n   Nhan Enter de quay lai...")

        elif choice == "0":
            print("\nCam on da su dung chuong trinh. Tam biet!\n")
            break

        else:
            print("\nLua chon khong hop le. Vui long nhap lai.")
            input("   Nhan Enter de tiep tuc...")


if __name__ == "__main__":
    main()
