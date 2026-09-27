# this small exercise practices my lists/dicts knowledge since thats where i have the least knowledge on
# sept 27,2026

inputted_nums=[]
biggest_num=[0]
smallest_num=[0]


num1=int(input("Enter first number: "))
inputted_nums.append(num1)
num2=int(input("Enter second number: "))
inputted_nums.append(num2)
num3=int(input("Enter third number: "))
inputted_nums.append(num3)
num4=int(input("Enter fourth number: "))
inputted_nums.append(num4)
num5=int(input("Enter fifth number: "))
inputted_nums.append(num5)

for num in inputted_nums:
    if num > biggest_num:
        biggest_num = num
    if num < smallest_num:
        smallest_num=num

print(f'Largest Number: {biggest_num}')
print(f'Smallest Number: {smallest_num}')
