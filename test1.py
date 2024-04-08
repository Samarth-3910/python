principal = int(input("Enter the principal amount: "))
rate  = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))

si = (principal * rate * time) / 100

final_amount = principal + si
print("The simple interest is: ", si)
print("The final amount is: ", final_amount)
