class Student:

    def __init__(self, name , age , grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


s1 = Student("Sangamita",30,99)
s2 = Student("Sabin", 36, 78)
s3 = Student("Prajwoal", 32,70)

course = Course("Science",2)
course.add_students(s1)
course.add_students(s2)
print(course.add_students(s3))
print(course.get_average_grade())




