programmers = {}
flag = True
msg1 = "What is your name?"
msg2 = "Which Programming language do you like?"
msg3 = "Do you want to continue (y/n)"
while flag:
    name = input(msg1)
    language = input(msg2)

    programmers[name] = language
    cont = input(msg3)
    if cont.lower() == 'n':
        break

print(programmers)