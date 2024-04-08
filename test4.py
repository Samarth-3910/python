c = int(input("Initially total no of ants is : ", ))
k = int(input("group of ants on the start of day makes itself k times : ", ))
n = int(input("no of days : ", ))

total_ants = c * (k ** n)
print("Total no of ants at the end of N days : ", total_ants)
