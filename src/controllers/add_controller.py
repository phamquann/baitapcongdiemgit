from src.models.student import Student
from src.utils.file_handler import load_students, save_students


def add_student() -> None:
    """Nhập thông tin từ bàn phím và thêm sinh viên mới vào danh sách."""
    print("\n===== THÊM SINH VIÊN =====")

    # --- Nhập MSSV ---
    mssv = input("Nhập MSSV: ").strip()
    if not mssv:
        print("Lỗi: MSSV không được để trống.")
        return

    # --- Kiểm tra MSSV trùng ---
    danh_sach = load_students()
    if any(sv.mssv == mssv for sv in danh_sach):
        print(f"Lỗi: MSSV '{mssv}' đã tồn tại trong danh sách.")
        return

    # --- Nhập Tên ---
    ten = input("Nhập họ và tên: ").strip()
    if not ten:
        print("Lỗi: Tên sinh viên không được để trống.")
        return

    # --- Nhập Điểm ---
    diem_str = input("Nhập điểm trung bình (0 – 10): ").strip()
    try:
        diem = float(diem_str)
    except ValueError:
        print("Lỗi: Điểm phải là số thực (ví dụ: 8.5).")
        return

    if not (0.0 <= diem <= 10.0):
        print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10.")
        return

    # --- Tạo đối tượng và lưu ---
    sinh_vien_moi = Student(mssv=mssv, ten=ten, diem=diem)
    danh_sach.append(sinh_vien_moi)
    save_students(danh_sach)

    print(f"\nThêm sinh viên thành công!")
    print(sinh_vien_moi)
