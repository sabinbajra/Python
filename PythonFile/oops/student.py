class Student:
    def __init__(self,admNo, sname, eng, math, science, nepali, total):
        self.admNo = admNo
        self.sname = sname
        self.eng = eng
        self.math = math
        self.science = science
        self.nepali = nepali
        self.total = total

    def calculate_total(self):
        self.total = self.eng + self.science + self.math + self.nepali
        print("Calculated total")

    def get_studentinfo(self):
        self.admNo = int(input("Enter the student administration ID::"))
        self.sname = input("Enter student name::")

    def get_mark_data(self):
        self.eng = int(input(f"Enter mark obtained in English subject::"))
        self.math = int(input(f"Enter mark obtained in Mathematics subject::"))
        self.science = int(input(f"Enter mark obtained in Science subject::"))
        self.nepali = int(input(f"Enter mark obtained in Nepali subject::"))

    def display(self):
        print(f"Name :: {self.sname}")
        print(f"Adm ID :: {self.admNo}")
        print(f"Marks obtained::::")
        print(f"English :: {self.eng}")
        print(f"Math :: {self.math}")
        print(f"Science :: {self.science}")
        print(f"Nepali :: {self.nepali}")
        print(f"Total is:: {self.total}")


s1 = Student(1,"sabin",45,66,45,78,0)

s1.get_studentinfo()
s1.get_mark_data()
s1.calculate_total()
s1.display()