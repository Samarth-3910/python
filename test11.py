string = input()
str = string.split(' ')
for _ in str:
    print(_[::-1], end=' ')