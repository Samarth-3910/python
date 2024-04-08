#PERFECT SQUARES
import math

n = int(input())

sqrt = math.sqrt(n)
if sqrt == int(sqrt):
    print("Perfect Square")
else:
    print("Not a Perfect Square")