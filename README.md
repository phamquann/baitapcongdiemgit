# Hệ Thống Quản Lý Sinh Viên

## Mô tả dự án
Đây là dự án nhóm để thực hành làm việc với Git. Hệ thống giúp quản lý thông tin sinh viên bao gồm thêm, xoá, tìm kiếm, cập nhật và hiển thị danh sách sinh viên.

## Thành viên nhóm và phân công

| STT | Họ và Tên | Chức năng code | Nhiệm vụ quản lý | Nhánh |
|-----|-----------|----------------|------------------|-------|
| 1 | Phạm Xuân Minh Quân | `main.py` – Menu điều hướng chính + `src/controllers/sort_controller.py` – Hàm sắp xếp sinh viên theo tên hoặc điểm | Tạo dự án, phân công, duyệt PR, merge develop→main, tag v1.0 | `main` / `develop` / `feature/sort-controller` |
| 2 | Vũ Đức Mạnh | `src/models/student.py` – Định nghĩa class Student (tên, MSSV, điểm) | — | `feature/model-student` |
| 3 | Trần Đức Minh | `src/controllers/add_controller.py` – Hàm thêm sinh viên | — | `feature/add-controller` |
| 4 | Trần Thị Thanh Mai | `src/controllers/delete_controller.py` – Hàm xoá sinh viên theo MSSV | — | `feature/delete-controller` |
| 5 | Trần Như Liễu | `src/controllers/search_controller.py` – Hàm tìm kiếm theo tên hoặc MSSV | — | `feature/search-controller` |
| 6 | Lượng Thị Thủy Hằng | `src/controllers/update_controller.py` – Hàm cập nhật thông tin sinh viên | — | `feature/update-controller` |
| 7 | Bùi Thị Bích Liêu | `src/controllers/display_controller.py` + `src/utils/file_handler.py` – Hiển thị danh sách & lưu/đọc file JSON | — | `feature/display-controller` |

## Cấu trúc dự án
```
baitapcongdiemgit/
├── main.py                          # Entry point chương trình
├── requirements.txt                 # Thư viện sử dụng
├── README.md                        # Tài liệu dự án
├── data/
│   └── students.json                # Dữ liệu sinh viên
└── src/
    ├── models/
    │   └── student.py               # Class Student
    ├── controllers/
    │   ├── __init__.py
    │   ├── add_controller.py        # Thêm sinh viên
    │   ├── delete_controller.py     # Xoá sinh viên
    │   ├── search_controller.py     # Tìm kiếm sinh viên
    │   ├── update_controller.py     # Cập nhật sinh viên
    │   ├── display_controller.py    # Hiển thị danh sách
    │   └── sort_controller.py       # Sắp xếp sinh viên
    └── utils/
        └── file_handler.py          # Lưu/đọc file JSON
```

## Hướng dẫn làm việc với GitHub Desktop

### Clone dự án
1. Mở **GitHub Desktop**
2. Chọn **File** → **Clone Repository**
3. Dán link: `https://github.com/phamquann/baitapcongdiemgit.git`
4. Chọn thư mục lưu → **Clone**

### Chuyển sang nhánh của mình
1. Click vào **"Current Branch"** (góc trên giữa)
2. Tìm và chọn nhánh `feature/<tên-của-mình>`

### Quy trình làm việc
1. Chuyển sang nhánh `feature` của mình
2. Mở file, code và lưu
3. Trong GitHub Desktop: điền **Summary** → click **Commit**
4. Lặp lại ít nhất **3 lần commit**
5. Click **"Push origin"** để đẩy lên GitHub
6. Click **"Create Pull Request"** → thêm Reviewer + Label → Submit

### Commit message theo chuẩn
```
feat: thêm class Student
feat: hoàn thiện hàm thêm sinh viên
fix: sửa lỗi kiểm tra MSSV trùng
```

## Cách chạy dự án
```
python main.py
```

## License
MIT License
