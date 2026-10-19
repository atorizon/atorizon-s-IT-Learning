# A = P * (1+r/n)^(n*t)
# a simple compound interest calculator
principal=int(input("Enter principal: "))
annual_rate=float(input("Enter annual rate (%): "))
compound=int(input("Enter compound/s per year: "))
years=int(input("Enter number of years: "))

annual_rate=annual_rate/100
final_amount=principal*(1+annual_rate/compound)**(compound*years)
interest=final_amount-principal
print(f'Final amount: $ {final_amount:.2f}')
print(f'Interest earned: $ {interest:.2f}')