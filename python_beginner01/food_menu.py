burger_pr=5
fries_pr=2
chicken_pr=10
steak_pr=15
soft_pr=3



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
customer_order=input("What will you be ordering? (1 for Burger, 2 for Fries, ...): ")

match customer_order:
    case "1":
        print("Burger it is!")
        order_total+=burger_pr
        score+=1
    case "2":
        print("Fries it is!")
        order_total+=fries_pr
    case "3":
        print("Chicken it is!")
        order_total+=chicken_pr
        score+=1
    case "4":
        print("Steak it is!")
        order_total+=steak_pr
        score+=1
    case "5":
        print("Softdrink it is!")
        order_total+=soft_pr
        score+=1
    case _:
        print("I'm sorry that isn't on the menu.")

print(f'Your current total is ${order_total}.')
customer_again=input("Would you like to order again? (y/n): ")


if customer_again=="y":
    customer_order=input("What will you be ordering? (1 for Burger, 2 for Fries, ...): ")
    score=0
elif customer_again=="n":
    print(f'Great! Thank you for ordering at Foodies!')
    print(f'Your total is {order_total}!')


        
