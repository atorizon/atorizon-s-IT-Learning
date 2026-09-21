"""
Minimum Requirements for a Password:
    8 characters
    1 Uppercase
    1 Lowercase
    1 Digit

Requirements for a Strong Password:
    12 Characters
    2 Uppercase
    2 Lowercase
    2 Digits
    1 Special Character
"""
def requirements(password):
    pass_upper=False
    pass_lower=False
    pass_digit=False
    pass_special=False
    length_enough=False
    special_char="!@#$%^&*"

    for char in password:
        if char.isupper():
            pass_upper=True
        elif char.islower():
            pass_lower=True
        elif char.isdigit():
            pass_digit=True
        elif char in special_char:
            pass_special=True
        elif len(password) >=8:
            length_enough=True

    return pass_upper, pass_lower, pass_digit, pass_special, length_enough


password=input("Enter a password: ")
pass_upper, pass_lower, pass_digit, pass_special, length_enough=requirements(password)



score=0
if pass_upper:
    score+=1
if pass_lower:
    score+=1
if pass_digit:
    score+=1
if pass_special:
    score+=1

while score < 4:
    print("Invalid Password.\nYour password must have the following requirements:")
    if pass_upper==False:
        print("Your password must have an UPPERCASE letter.")
    if pass_lower==False:
        print("Your password must have a LOWERCASE letter.")
    if pass_digit==False:
        print("Your password must have a DIGIT.")
    if length_enough==False:
        print("Your password must be at least 8 characters.")
    score=0

    password = input("Enter a password: ")
    pass_upper, pass_lower, pass_digit, pass_special,length_enough=requirements(password)


print("Successful!")

