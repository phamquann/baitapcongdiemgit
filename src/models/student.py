"""
Module định nghĩa class Student cho hệ thống quản lý sinh viên.
"""


class Student:
    """
    Class đại diện cho một sinh viên với thông tin cơ bản.
    
    Attributes:
        name (str): Họ và tên sinh viên
        student_id (str): Mã số sinh viên (MSSV)
        score (float): Điểm số của sinh viên
    """
    
    def __init__(self, name: str, student_id: str, score: float):
        """
        Khởi tạo đối tượng Student.
        
        Args:
            name (str): Họ và tên sinh viên
            student_id (str): Mã số sinh viên
            score (float): Điểm số (0.0 - 10.0)
        
        Raises:
            ValueError: Nếu điểm số không hợp lệ
        """
        self.name = name.strip()
        self.student_id = student_id.strip()
        
        # Validate score
        if not 0.0 <= score <= 10.0:
            raise ValueError("Điểm số phải trong khoảng 0.0 - 10.0")
        self.score = float(score)
    
    def __str__(self) -> str:
        """
        Trả về chuỗi đại diện cho sinh viên.
        
        Returns:
            str: Thông tin sinh viên đã format
        """
        return f"MSSV: {self.student_id} | Tên: {self.name} | Điểm: {self.score:.1f}"
    
    def __repr__(self) -> str:
        """
        Trả về chuỗi đại diện chính thức cho sinh viên.
        
        Returns:
            str: Representation string
        """
        return f"Student('{self.name}', '{self.student_id}', {self.score})"
    
    def __eq__(self, other) -> bool:
        """
        So sánh hai sinh viên dựa trên MSSV.
        
        Args:
            other: Đối tượng khác để so sánh
            
        Returns:
            bool: True nếu MSSV giống nhau
        """
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id
    
    def to_dict(self) -> dict:
        """
        Chuyển đổi sinh viên thành dictionary.
        
        Returns:
            dict: Dictionary chứa thông tin sinh viên
        """
        return {
            'name': self.name,
            'student_id': self.student_id,
            'score': self.score
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Tạo sinh viên từ dictionary.
        
        Args:
            data (dict): Dictionary chứa thông tin sinh viên
            
        Returns:
            Student: Đối tượng sinh viên mới
        """
        return cls(
            name=data['name'],
            student_id=data['student_id'],
            score=data['score']
        )
    
    def update_score(self, new_score: float) -> None:
        """
        Cập nhật điểm số cho sinh viên.
        
        Args:
            new_score (float): Điểm số mới (0.0 - 10.0)
            
        Raises:
            ValueError: Nếu điểm số không hợp lệ
        """
        if not 0.0 <= new_score <= 10.0:
            raise ValueError("Điểm số phải trong khoảng 0.0 - 10.0")
        self.score = float(new_score)
    
    def get_grade_letter(self) -> str:
        """
        Trả về xếp loại học lực dựa trên điểm số.
        
        Returns:
            str: Xếp loại (A, B, C, D, F)
        """
        if self.score >= 8.5:
            return 'A'
        elif self.score >= 7.0:
            return 'B'
        elif self.score >= 5.5:
            return 'C'
        elif self.score >= 4.0:
            return 'D'
        else:
            return 'F'