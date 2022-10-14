class User:
    def __init__(self, fname="", lname="", id=0):
        self.fname = fname
        self.lname = lname
        self.id = id

    def display(self):
        print(f"Name:: {self.fname} {self.lname} \nID:: {self.id}")

    def greet(self):
        print(f"Hello {self.fname} {self.lname}")


class Admin(User):

    def __init__(self, fname="", lname="", id=0, privileges=[]):
        super().__init__(fname, lname, id)
        self.priveleges = privileges

    def showAdmin(self):
        self.display()
        self.greet()
        for i in self.priveleges:
            print(f"Admin can :: {i}")


a = Admin("sabin","bajracharya",121,["ADD","Delete","Update"])
a.showAdmin()









