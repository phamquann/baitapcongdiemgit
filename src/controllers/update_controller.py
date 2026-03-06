from src.models.student import Student
from src.utils.file_handler import FileHandler
import json

class UpdateController:
    def __init__(self):
        self.file_handler = FileHandler()
    
    def update_student(self, student_id, new_data):
        """
        Cập nhật thông tin sinh viên theo mã sinh viên
        """
        # Đọc dữ liệu hiện tại
        students = self.file_handler.read_data()
        
        # Tìm sinh viên cần cập nhật
        for student in students:
            if student['student_id'] == student_id:
                # Cập nhật thông tin
                student.update(new_data)
                break
        
        # Lưu dữ liệu
        self.file_handler.write_data(students)
        
        return True
