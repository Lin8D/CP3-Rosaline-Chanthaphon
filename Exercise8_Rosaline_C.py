usernameInput = input("Username :")
passwordInput = input("Password :")

total_price = 0

if usernameInput == "adminhf" and passwordInput == "hf1234":
    print(" Logged in successfully.......")
    print("--- Welcome to Heifu Asia ----")
    print("==============================")
    print("........Today's menu..........")
    print("1. Wantan             50 THB  ")
    print("2. Tempura            50 THB  ")
    print("3. Dumplings          60 THB  ")
    print("4. Shrimp fried rice  80 THB  ")
    print("5. Spring rolls       40 THB  ")
    print("==============================")
    wantTobuy = input("Would you like to order anything? (yes/no) ")
    if wantTobuy == "yes":
        while True:
            order = input("What would you like to order? ")
            if order.lower() == "wantan" or order.lower() == "tempura":
                howmany = int(input("How many would you like? "))
                price = int(howmany * 50)
                total_price = price + total_price
            elif order.lower() == "dumplings":
                howmany = int(input("How many would you like? "))
                price = int(howmany * 60)
                total_price = price + total_price
            elif order.lower() == "shrimp fried rice":
                howmany = int(input("How many would you like? "))
                price = int(howmany * 80)
                total_price = price + total_price
            elif order.lower() == "spring rolls":
                howmany = int(input("How many would you like? "))
                price = int(howmany * 40)
                total_price = price + total_price

            anythingElse = input("Would you like anything else? (yes/no)")
            if anythingElse == "no":
                break
            elif anythingElse == "yes":
                continue
            else:
                break
    if total_price != 0:
        vat = total_price * 0.07  # For 7% value added tax
        print("Vat 7% : ",int(vat) ,"THB")
        print("Total price :", int(vat+total_price), "THB")
    print("Have a nice day!")
    print("Enjoy your food!")
else:
    print("Wrong password or username!")





