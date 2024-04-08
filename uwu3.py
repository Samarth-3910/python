def is_palindrome(string):
    return string == string[::-1]


str1 = input("Enter a string: ")
print(is_palindrome(str1))