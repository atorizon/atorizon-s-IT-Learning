# another scuffed practice on creating a food menu
# it will always loop as long as the customer wants to order again
# it calculates the total price of the order
# also lists all the ordered food

burger_pr=5
fries_pr=2
chicken_pr=10
steak_pr=15
soft_pr=3
receipt=[]


print(
    "Welcome to Foodies!" \
    "\n=== MENU ===" \
    "\n1 — Burger ($5)" \
    "\n2 — Fries ($2)" \
    "\n3 — Chicken ($10)" \
    "\n4 — Steak ($15)" \
    "\n5 — Softdrink ($3)"
)

score=0
order_total=0

def order(customer_order,order_total,burger_pr,fries_pr,chicken_pr,steak_pr,soft_pr):
    match customer_order:
        case "1":
            print("Burger it is!")
            order_total+=burger_pr
            receipt.append("Burger === $3")
            
        case "2":
            print("Fries it is!")
            order_total+=fries_pr
            receipt.append("Fries === $2")
        case "3":
            print("Chicken it is!")
            order_total+=chicken_pr
            receipt.append("Chicken === $10")
            
        case "4":
            print("Steak it is!")
            order_total+=steak_pr
            receipt.append("Steak === $15")
        case "5":
            print("Softdrink it is!")
            order_total+=soft_pr
            receipt.append("Softdrink === 3")
        case _:
            print("I'm sorry that isn't on the menu.")
    return order_total

while True:
    customer_order = input("What will you be ordering? (1 for Burger, 2 for Fries, ...): ")
    order_total = order(customer_order, order_total, burger_pr, fries_pr, chicken_pr, steak_pr, soft_pr)
    print(f'Your current total is ${order_total}.')

    customer_again = input("Would you like to order again? (y/n): ")
    if customer_again == "n":
        print("Great! Thank you for ordering at Foodies!")
        print(receipt)
        print(f'Your total is ${order_total}!')
        break


        
