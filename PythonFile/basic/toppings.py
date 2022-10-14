requested_toppings = ['mushrooms','salami','peppers','beef','chicken','cheese']
yes_no = ''
extra_topping = ''


print("Welcome to Sabin Pizzeria\n1.Do you want to order (y/n)::")
yes_no = input()

if yes_no.lower() == 'y':
    yes_no = input("Do you want Pizza with extra toppings:: (y/n)::")
    if yes_no.lower() == 'y':
        extra_topping = input("Which extra toppings do you want::")
        for requested_topping in requested_toppings:
            if extra_topping.lower() == requested_topping and extra_topping.lower() == 'salami':
                print("Sorry we don't have salami, so making normal pizza for you.")
            elif extra_topping.lower() == requested_topping:
                print(f"Making your delicious pizza with extra {extra_topping}, Wait for your order to finish::")
        print("Your Pizza is ready.")
    else:
        print("Thanks for ordering normal pizza")
        print("Your Pizza is ready.")
else:
    print("Thanks for the visit, hope you order with us next time. Thank you!!!")