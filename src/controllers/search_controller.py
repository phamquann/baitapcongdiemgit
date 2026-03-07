"""
Search Controller
Tìm kiếm sinh viên theo tên hoặc MSSV
"""

from src.utils.file_handler import read_students_from_file


def search_by_name(name):
    """
    Tìm kiếm sinh viên theo tên
    
    Args:
        name (str): Tên sinh viên cần tìm kiếm
    
    Returns:
        list: Danh sách sinh viên có tên khớp (không phân biệt hoa/thường)
    """
    students = read_students_from_file()
    search_name = name.lower().strip()
    
    results = [
        student for student in students 
        if search_name in student['name'].lower()
    ]
    
    return results


def search_by_mssv(mssv):
    """
    Tìm kiếm sinh viên theo MSSV (Mã Số Sinh Viên)
    
    Args:
        mssv (str): MSSV của sinh viên cần tìm
    
    Returns:
        list: Danh sách sinh viên có MSSV khớp
    """
    students = read_students_from_file()
    search_mssv = str(mssv).strip()
    
    results = [
        student for student in students 
        if str(student['mssv']) == search_mssv
    ]
    
    return results


def search_students(query, search_type='name'):
    """
    Tìm kiếm sinh viên theo tên hoặc MSSV
    
    Args:
        query (str): Từ khóa tìm kiếm
        search_type (str): Loại tìm kiếm ('name' hoặc 'mssv'). Mặc định là 'name'
    
    Returns:
        list: Danh sách sinh viên khớp với điều kiện tìm kiếm
    """
    if search_type.lower() == 'mssv':
        return search_by_mssv(query)
    else:
        return search_by_name(query)


def display_search_results(results):
    """
    Hiển thị kết quả tìm kiếm
    
    Args:
        results (list): Danh sách sinh viên tìm được
    """
    if not results:
        print("Không tìm thấy sinh viên nào!")
        return
    
    print(f"\n{'='*60}")
    print(f"Tìm thấy {len(results)} sinh viên:")
    print(f"{'='*60}")
    print(f"{'MSSV':<15} {'Tên':<30} {'Điểm':<10}")
    print(f"{'-'*60}")
    
    for student in results:
        print(f"{student['mssv']:<15} {student['name']:<30} {student['score']:<10}")
    
    print(f"{'='*60}\n")

# Cập nhật lần 2: Hoàn thiện chức năng tìm kiếm