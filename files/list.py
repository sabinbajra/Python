fruits = ["apple","banana"]
print(fruits)

for i in fruits:
    print(i)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Accessing the list items")
swap = fruits[1]
fruits[1] = fruits[0]
fruits[0] = swap

print(fruits)

#length of the list len(listname)
print(len(fruits))

names = list(("sabin","sangamita","mohan","ziad"))
for i in names:
    print(i)

print(len(names))
#print the types of the list
print(type(names))
print(type(fruits))

#variable list
varlist = [23,"Ram",True,4.59,'Hari']

for i in varlist:
    print(i)
    print(type(i))


i=0
x=0
while i < len(varlist):

    if i == 0:
        x = -1
    else:
        x = (i+1)*-1

    print(" From For Loop:: " , varlist[x])
    i = i + 1
else:
    print("End of while loop")

#range of list display
print(varlist[:4])
print(varlist[2:4])
print(varlist[1:])

