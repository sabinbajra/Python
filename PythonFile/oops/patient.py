class Invoice:
    # private data member
    __no = 0
    __amount = 0.0

    def setInvoice(self):
        self.__no = int(input("Enter the invoice number::"))

    def calc_amount(self, days):
        self.__amount = days * 10

    def displayinvoice(self):
        print(f"Invoice no :: {self.__no}\nAmount:: {self.__amount}")


class Patient:
    # private data member
    __name = ""
    __age = 0
    __gender = ""
    __discharge = False
    __days = 0

    # public function
    def __init__(self):
        print("Patient object created")

    def setData(self):
        self.__name = input("Enter patient name:: ")
        self.__age = int(input("Enter patient age::"))
        self.__gender = input("Enter patient sex (M/F)")

    def upDate(self):
        self.__days = int(input("Enter patient days stay::"))
        self.__discharge = True

    def display(self,invoice):
        print(f"\n\nName:: {self.__name}\nAge:: {self.__age}\nGender:: {self.__gender}")

        if self.__discharge:
            invoice.setInvoice()
            invoice.calc_amount(self.__days)
            invoice.displayinvoice()
        else:
            print("Not Discharged yet")

    def getDays(self):
        return self.__days


a = Patient()
a.setData()
a.upDate()
b = Invoice()
a.display(b)


