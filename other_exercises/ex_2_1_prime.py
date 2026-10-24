# Part A: Primes with no flag variable

# num=int(input("Number: "))

# for n in range(2, num+1): #2
#     for d in range(2,n): #2
#         if n % d == 0:
#             break
#     else:
#         print(n,end=" ")

# print()


# Part B: Free port finder

busy=[8000,8001,8002,8003,8004,8005]

for i in range(8000,8005+1):
    if i not in busy:
        print(f'First free port: {i}')
        break
else:
    print('No free ports.')