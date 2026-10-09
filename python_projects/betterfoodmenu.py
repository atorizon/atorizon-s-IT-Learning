# A better menu than my previous python exercise because it offers a wider variety of food choices
# this wasnt that hard to do but there were so many things/choices it made me confused a bunch of times
order_total=0
food_receipt=[]
current_order=[]

garlic_chk=6
sign_chk=9
honey_chk=7

cheese_burg=4
chick_burg=5
reg_burg=3

lemon_juice=2
sweet_soda=3
water=1

def food_category(category_choice,current_order):
    match category_choice:
        case "1":
            current_order.append("1")
            print(
                "===== MENU ====="
                "\n A - Garlic Chicken" \
                "\n B - Signature Chicken"
                "\n C - Honey Butter Chicken"
            )

        case "2":
            current_order.append("2")
            print(
                "===== MENU ====="
                "\n A - Cheeseburger" \
                "\n B - Chicken Burger"
                "\n C - Regular Burger"
            )
        case "3":
            current_order.append("3")
            print(
                "===== MENU ====="
                "\n A - Lemon Juice" \
                "\n B - Sweet Soda"
                "\n C - Water"
            )
    
        case _:
            print("Invalid Choice.")
    return current_order


def specific_food(food_choice,current_order,food_receipt,order_total):
    match food_choice.upper():
        case "A":
            if current_order[0]=="1":
                print("Great! Garlic Chicken it is!")
                food_receipt.append("Garlic Chicken")
                order_total+=garlic_chk
            elif current_order[0]=="2":
                print("Great! Cheeseburger it is!")
                food_receipt.append("Cheeseburger")
                order_total+=cheese_burg
            elif current_order[0]=="3":
                print("Great! Lemon Juice it is!")
                food_receipt.append("Lemon Juice")
                order_total+=lemon_juice
            current_order.append(food_choice)
        case "B":
            if current_order[0]=="1":
                print("Great! Signature Chicken it is!")
                food_receipt.append("Signature Chicken")
                order_total+=sign_chk
            elif current_order[0]=="2":
                print("Great! Chicken Burger it is!")
                food_receipt.append("Chicken Burger")
                order_total+=chick_burg
            elif current_order[0]=="3":
                print("Great! Sweet Soda it is!")
                food_receipt.append("Sweet Soda")
                order_total+=sweet_soda
            current_order.append(food_choice)
        case "C":
            if current_order[0]=="1":
                print("Great! Honey Butter Chicken it is!")
                food_receipt.append("Honey Butter Chicken")
                order_total+=honey_chk
            elif current_order[0]=="2":
                print("Great! Regular Burger it is!")
                food_receipt.append("Regular Burger")
                order_total+=reg_burg
            elif current_order[0]=="3":
                print("Great! Water it is!")
                food_receipt.append("Water")
                order_total+=water
            current_order.append(food_choice)
    current_order="".join(current_order)
    return current_order,food_receipt,order_total


def menu():
    print(
        "Welcome to Foodies! Please choose a category."
        "\n===== MENU ====="
        "\n1 - Chicken"
        "\n2 - Burger" \
        "\n3 - Drinks" \
    )

while True:
    menu()
    category_choice=input("What category would you like to order?: ")
    food_category(category_choice,current_order)
    food_choice=input("What would you like to order under this category?: ")
    current_order,food_receipt,order_total=specific_food(food_choice,current_order,food_receipt,order_total)
    category_choice_again=input("Would you like to order again?: ")
    match category_choice_again:
        case "y":
            current_order=[]
            continue
        case "n":
            print(f'Okay! \nHere is your receipt: \n{food_receipt}')
            print(f'Your total is ${order_total}')
            break
        case _:
            category_choice_again=input("Invalid Choice. Would you like to order again?: ")
            current_order=[]
            continue
