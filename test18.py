#prime number
n = int(input())
count = 0
for i in range(1, n+1):
    if n % i == 0: #mtlb aagar ki remainder na bache toh vo prime number hoga
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")