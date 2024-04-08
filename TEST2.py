principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = 2

compound_interest = principal * (pow((1 + rate / 100), time))
ci = compound_interest - principal
print("Compound interest is: ", ci)
