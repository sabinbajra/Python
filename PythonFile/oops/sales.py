class SalesPerson:
    sales = 0

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def makeSale(self,sales):
        self.sales += sales

    def salesReport(self):
        print(f"My total sales is {self.sales}")


s = SalesPerson("Sangamita","Shakya")
s.salesReport()
s.makeSale(100)
s.salesReport()
s.makeSale(250)
s.salesReport()