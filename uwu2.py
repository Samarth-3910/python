def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

str1 = input("Enter a string: ")
print(count_vowels(str1))