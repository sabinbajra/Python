class Batsman:
    # declaring private data members
    __bcode = 0
    __bname = ""
    __innings = 0
    __notout = 0
    __runs = 0
    __batavg = 0.0

    #declaring private functions
    def __calcavg(self):
        print("Calculating the average ::")
        self.__batavg = self.__runs/ (self.__innings-self.__notout)

    #declaring public functions
    def __init__(self):
        print("Object created::")

    def readdata(self):
        self.__bname = input("Enter the name of the bats man::")
        self.__bcode = int(input("Enter the batsman code::"))
        self.__innings = int(input("Enter the batsman innings::"))
        self.__notout = int(input("Enter the batsman not out::"))
        self.__runs = int(input("Enter the batsman total runs::"))
        self.__calcavg()

    def display_data(self):
        print(f"Code:: {self.__bcode}")
        print(f"Name:: {self.__bname}")
        print(f"Innings:: {self.__innings}")
        print(f"Notout:: {self.__notout}")
        print(f"Runs:: {self.__runs}")
        print(f"Average:: {self.__batavg}")


a = Batsman()
a.readdata()
a.display_data()