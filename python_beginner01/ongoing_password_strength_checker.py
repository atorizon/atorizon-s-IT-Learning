# This password checker made my head ache (i think i had too many reqs)
# sept 26, added a list of invalid passwords inputted

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
score=0
special_char="!@#$%^&*"
used_passwords=[]
def requirements(password):
    pass_upper=False
    pass_lower=False
    pass_digit=False
    length_enough=False

    for char in password:
        if char.isupper():
            pass_upper=True
        elif char.islower():
            pass_lower=True
        elif char.isdigit():
            pass_digit=True

    length_enough = len(password) >=8

    return pass_upper, pass_lower, pass_digit, length_enough

def reqs_add():
    score=0
    if pass_upper:
        score+=1
    if pass_lower:
        score+=1
    if pass_digit:
        score+=1
    if length_enough:
        score+=1

    if len(password) > 8:
        score+=1
    for char in password:
        if char in special_char:
            score+=1
            break
    if len(password) > 12:
        score+=1
    return score

password=input("Enter a password: ")
pass_upper, pass_lower, pass_digit, length_enough=requirements(password)
score=reqs_add()

while score < 4 or pass_upper==False or pass_lower==False or pass_digit==False or not length_enough:
    print("Invalid Password.\nYour password must have the following requirements:")
    if pass_upper==False:
        print("Your password must have an UPPERCASE letter.")
    if pass_lower==False:
        print("Your password must have a LOWERCASE letter.")
    if pass_digit==False:
        print("Your password must have a DIGIT.")
    if not length_enough:
        print("Your password must be at least 8 characters.")
    used_passwords.append(password)

    password = input("Enter a password: ")
    pass_upper, pass_lower, pass_digit, length_enough=requirements(password)
    score=0
    score=reqs_add()

if score >=4:
    print("Minimum Password Requirements Met.")
    if score==5:
        print("Weak Password.")
    elif score==6:
        print("Moderate Password.")
    elif score==7:
        print("Strong Password.")


print("Successful!")
print(used_passwords)

