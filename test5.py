ascii_values_string = input("Enter ASCII values of each character separated by '&': ")
ascii_values = ascii_values_string.split('&')

funny_name = ''.join(chr(int(ascii_val)) for ascii_val in ascii_values)
print("Funny name:", funny_name)
