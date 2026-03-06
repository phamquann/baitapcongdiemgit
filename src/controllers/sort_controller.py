"""
sort_controller.py
------------------
Tac gia : Pham Xuan Minh Quan
Nhanh   : feature/sort-controller
Mo ta   : Cac ham sap xep danh sach sinh vien theo ten hoac theo diem.
"""


def sort_by_name(students: list, ascending: bool = True) -> list:
    """
    Sap xep danh sach sinh vien theo ten (ho va ten).

    Tham so:
        students  (list) : Danh sach dict sinh vien.
        ascending (bool) : True = A->Z, False = Z->A.

    Tra ve:
        list: Danh sach da duoc sap xep (ban sao moi).
    """
    if not students:
        print("Danh sach sinh vien dang trong.")
        return []

    sorted_list = sorted(
        students,
        key=lambda sv: sv.get("ten", "").strip().lower(),
        reverse=not ascending,
    )

    order_label = "A -> Z" if ascending else "Z -> A"
    print("\nDa sap xep theo TEN ({}):".format(order_label))
    _print_table(sorted_list)
    return sorted_list


def sort_by_score(students: list, ascending: bool = False) -> list:
    """
    Sap xep danh sach sinh vien theo diem trung binh.

    Tham so:
        students  (list) : Danh sach dict sinh vien.
        ascending (bool) : True = thap->cao, False = cao->thap.

    Tra ve:
        list: Danh sach da duoc sap xep (ban sao moi).
    """
    if not students:
        print("Danh sach sinh vien dang trong.")
        return []

    sorted_list = sorted(
        students,
        key=lambda sv: float(sv.get("diem", 0)),
        reverse=not ascending,
    )

    order_label = "Thap -> Cao" if ascending else "Cao -> Thap"
    print("\nDa sap xep theo DIEM ({}):".format(order_label))
    _print_table(sorted_list)
    return sorted_list


def _print_table(students: list) -> None:
    """In danh sach sinh vien dang bang."""
    print("-" * 55)
    print("{:<5} {:<12} {:<25} {:>6}".format("STT", "MSSV", "Ho va Ten", "Diem"))
    print("-" * 55)
    for idx, sv in enumerate(students, start=1):
        print("{:<5} {:<12} {:<25} {:>6.2f}".format(
            idx,
            sv.get("mssv", ""),
            sv.get("ten", ""),
            float(sv.get("diem", 0))
        ))
    print("-" * 55)


def menu_sort(students: list) -> list:
    """
    Hien thi sub-menu chon kieu sap xep.

    Tham so:
        students (list): Danh sach sinh vien hien tai.

    Tra ve:
        list: Danh sach sau khi sap xep (hoac nguyen ban neu huy).
    """
    print("\n============================")
    print("     SAP XEP SINH VIEN     ")
    print("============================")
    print("  1. Sap xep theo Ten (A-Z)")
    print("  2. Sap xep theo Ten (Z-A)")
    print("  3. Sap xep theo Diem (Cao nhat)")
    print("  4. Sap xep theo Diem (Thap nhat)")
    print("  0. Quay lai")
    print("============================")

    choice = input("Chon: ").strip()

    if choice == "1":
        return sort_by_name(students, ascending=True)
    elif choice == "2":
        return sort_by_name(students, ascending=False)
    elif choice == "3":
        return sort_by_score(students, ascending=False)
    elif choice == "4":
        return sort_by_score(students, ascending=True)
    elif choice == "0":
        return students
    else:
        print("Lua chon khong hop le.")
        return students
