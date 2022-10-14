name = ["sabin","ram","mohan","rajesh","sunil"]
print(name)
#accessing list element wise using index start with 0 to size-1
for i in name:
    print(i)
print("\n++++++++++++\n")
#printing list one by one
print(name[0].upper())
print(name[1].upper())
print(name[2].upper())
print(name[3].upper())
print(name[4].upper())
print(f"last item in the list is {name[-1]}")
print(name[-1].upper())
print(name[-2].upper())
print(name[-3].upper())
print(name[-4].upper())
print(name[-5].upper())
#append list
name.append("Sangamita".lower())
print(f"The added name is {name[-1]}")
print("\n")
for i in name:
    print(i)
#changing sabin to rabin
name[0] = "RABIN".lower()
print("\nChange Successful\n")
for i in name:
    print(i)

#creating empty list and adding data using append

auto = [] #creating an empty auto list
auto.append("HOndA".lower())
auto.append("biCYCLE".lower())
auto.append("caR".lower())
auto.append("HelcoptR".lower())
auto.append("Sheep".lower())

print("\nAccessing Auto\n")
for i in auto:
    print(i)

auto[3] = "heliCopter".lower()
auto[4] = "ship".lower()
print("\nAccessing Auto\n")
for i in auto:
    print(i)

print(auto)

#adding new list element at the beginning
auto.insert(0,"AeroPlane".lower())
print(auto)
auto.insert(2,"mounTAINBIKe".lower())
print(auto)

#to remove elements from the list
#we use del functions

del auto[2]
print("\n+++++++++++++\n")
print(auto)

'''for i in auto:
    print(auto)
    del_element = auto.pop()
    print(f"\nThe element {del_element} is deleted from the list")
'''
