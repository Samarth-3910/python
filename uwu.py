# write a program to show factorial of a number using recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter a number: "))
print(fact(num))
