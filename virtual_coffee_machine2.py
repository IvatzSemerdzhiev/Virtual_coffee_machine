espresso = {"water": 100,
            "milk": 20,
            "coffee": 20,


}

latte = {"water": 200,
            "milk": 50,
            "coffee": 25


}

capuccino = {"water": 250,
            "milk": 70,
            "coffee": 25


}

money = []

water = 1000
milk = 500
coffee = 200
price_espresso = 2
price_latte = 2.5
price_capuccino = 3


while water > 0 and milk > 0 and coffee > 0:
    drink = input("Select your drink- Espresso/ Latte / Capuccino ->").lower()

    if drink == 'espresso':
        print(f"Insert ${price_espresso}")
        payment_q = int(input("Quarters -> "))
        payment_d = int(input("Dimes -> "))
        payment_n = int(input("Nickels -> "))
        payment_p = int(input("Pennies -> "))
        sum_payment= (payment_q * 0.25 + payment_d * 0.10 + payment_n * 0.05 + payment_p * 0.01)
        if sum_payment >= price_espresso:
            # if price_espresso - sum_payment > 0:
            print(f"Your change ${sum_payment - price_espresso:.2f}")
            for x in espresso:
                if x == 'water':
                    water -= espresso[x]
                    if water < 0:
                        break
                if x == 'milk':
                    milk -= espresso[x]
                    if milk < 0:
                        break
                if x == 'coffee':
                    coffee -= espresso[x]
                    if coffee < 0:
                        break
            money.append(price_espresso)
            print(f"Enjoy your {drink}!")
        else:
            print("Insufficient credit")
            continue
    elif drink == 'latte':
        print(f"Insert ${price_latte}")
        payment_q = int(input("Quarters -> "))
        payment_d = int(input("Dimes -> "))
        payment_n = int(input("Nickels -> "))
        payment_p = int(input("Pennies -> "))
        sum_payment = (payment_q * 0.25 + payment_d * 0.10 + payment_n * 0.05 + payment_p * 0.01)
        if sum_payment >= price_latte:
            print(f"Your change ${sum_payment - price_latte:.2f}")
            for x in latte:
                if x == 'water':
                    water -= latte[x]
                    if water < 0:
                        break
                if x == 'milk':
                    milk -= latte[x]
                    if milk < 0:
                        break
                if x == 'coffee':
                    coffee -= latte[x]
                    if coffee < 0:
                        break
            money.append(price_latte)
            print(f"Enjoy your {drink}!")
        else:
            print("Insufficient credit")
            continue
    elif drink == 'capuccino':
        print(f"Insert ${price_capuccino}")
        payment_q = int(input("Quarters -> "))
        payment_d = int(input("Dimes -> "))
        payment_n = int(input("Nickels -> "))
        payment_p = int(input("Pennies -> "))
        sum_payment = (payment_q * 0.25 + payment_d * 0.10 + payment_n * 0.05 + payment_p * 0.01)
        if sum_payment >= price_capuccino:
            print(f"Your change ${sum_payment - price_capuccino:.2f}")
            for x in capuccino:
                if x == 'water':
                    water -= capuccino[x]
                    if water < 0:
                        break
                if x == 'milk':
                    milk -= capuccino[x]
                    if milk < 0:
                        break
                if x == 'coffee':
                    coffee -= capuccino[x]
                    if coffee < 0:
                        break
            money.append(price_capuccino)
            print(f"Enjoy your {drink}!")
        else:
            print("Insufficient credit")
            continue
    elif drink == 'off':
        print("Goodbye")
        break
    elif drink == 'report':
        print(f"Water left {water}")
        print(f"Milk left {milk}")
        print(f"Coffee left {coffee}")

        print(f"${sum(money)}")
    else:
        print("repeat selection")
        continue




