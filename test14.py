#to show vowel and consonant
string = input()
vowels = 0
consonants = 0
for i in string:
    if i in 'aeiouAEIOU':
        vowels += 1
    else:
        consonants += 1