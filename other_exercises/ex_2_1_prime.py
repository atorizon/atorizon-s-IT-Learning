# Part A: Primes with no flag variable

num=int(input("Number: "))

for n in range(2, num+1): #2
    for d in range(2,n): #2
        if n % d == 0:
            break
    else:
        print(n,end=" ")

print()