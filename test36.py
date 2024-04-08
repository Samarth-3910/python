l = map(int,input().split())
l1 = []
for i in l:
    if i % 3 == 0:
        l1.append(i)
l1.sort()
print(l1[-1])