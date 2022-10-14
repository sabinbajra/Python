msg = 'hello this is my world'

# stringvariable.title()
name = "sabin bajracharya"
print(name.title())

print(msg.title())
print(msg)

msg = msg.title()
print(msg)

print(name.lower())
print(name.title())
print(name.upper())

first_name = "sabin"
middle_name = "muni"
last_name = "bajracharya"

# use of f strings
full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
print("Full name is " + full_name)
print(f"Hello, {full_name} How are you?")
print(f"Hi {full_name} what are you doing? Can I help you {first_name}")

message = f"Hello {full_name} " \
          f"how can we help you? Are you tired {first_name}, " \
          f"Mr {last_name} we can give you a good salary"

print(message)

#whitespaces
print("\n\nWelcome to python programming\n++++++++++++++++++n\n\t1. Add\n\t2. Subtract\n\tEnter your choice::")