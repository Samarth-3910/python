input_string = "apple,banana,orange,kiwi,strawberry"
words = input_string.split(',')
shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word
print("The shortest word is:", shortest_word)