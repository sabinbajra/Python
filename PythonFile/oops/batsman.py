class Batsman:
    # private members
    __bcode = 0
    __bname = ""
    __innings = 0
    __notout =0
    __runs = 0
    __batavg = 0.0

    # private functions
    def __init__(self):
        print("Inside the constructor")

    def __calcavg(self):
        self.__batavg = self.__runs/(self.__innings-self.__notout)

    # public function
    def readdata(self):
        self.__bcode = int(input("Enter the batsman code::"))
        self.__bname = input("Enter the batsman name::")
        self.__innings = int(input("Enter the batsman innings::"))
        self.__notout = int(input("Enter the batsman notout::"))
        self.__runs = int(input("Enter the batsman runs::"))
        self.__calcavg()

    def display_data(self):
        print(f"Code:: {self.__bcode}")
        print(f"Name:: {self.__bname}")
        print(f"Innings:: {self.__innings}")
        print(f"Notout:: {self.__notout}")
        print(f"Runs:: {self.__runs}")
        print(f"Average:: {self.__batavg}")


dhoni = Batsman()
dhoni.readdata()
dhoni.display_data()

