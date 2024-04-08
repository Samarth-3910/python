C = int(input("Chocolates you already have : ", ))
D = int(input("Uncle who gave you chocolates : ", ))
N = int(input("uncle who gave you chocolates upto N number of days : ", ))
uncle_chocolates = C * N
total_chocolates = uncle_chocolates + D
total_chocolates_left = total_chocolates - N# agar 2 chocolates per day khate hai toh n*2 so.on....
print("Total chocolates left at the end of N days : ", total_chocolates_left)
