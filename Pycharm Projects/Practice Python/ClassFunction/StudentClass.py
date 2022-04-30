class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    # class function .........
    def is_student_have_horor(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False



