from os.path import ismount

name = " "
c_units = 0
p_units = 0
units = 0
amount = 500
surcharge = 0

print("Nepal Electricity Authority\n1: Enter your name::")
name = input()
c_units = int(input("Enter the current reading::"))
p_units = int(input("Enter the previous current reading::"))
units = c_units - p_units

if units < 0:
    print("Error in reading units, Please try again.")
else:
    if units <= 100:
        amount = amount + units*0.4
    elif units <= 200:
        amount = amount + (units-100)*0.5
    else:
        if units > 250:
            surcharge = units*0.15
        amount = amount + 100*0.5 + (units-200)*0.6 + surcharge

print(f"\nCalculated bill for {name}\nCurrent Meter Reading:: {c_units}\nElectrictiy used::{units}\nTotal amount::{amount}")

