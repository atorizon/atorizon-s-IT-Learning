# this was an activity for my major sub in programming in 1st year
# this was like the very first code that made my head hurt during lab
# now that i coded it myself, its actually easy i just forgot about .isalpha


def amount_input():
    total=input("Enter total purchase amount: ")
    while total.isalpha():
        print("Enter numeric value only.")
        total=input("Enter total purchase amount: ")
    return float(total)

def calculate_discount(total):
    if total >=5000:
        discount=total*.2
    elif total >=3000:
        discount=total*.15
    elif total >=1000:
        discount=total*.1
    elif total < 1000:
        discount=total*0
    return discount

total=amount_input()
discount=calculate_discount(total)

print(f'Discount amounted: {discount}')