password = input("Enter your password: ")
if len(password) < 6:
    print("Password is too short")
elif len(password) > 10:
    print("Password is too long")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter")
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one number")
elif not any(not char.isalnum() for char in password):
    print("Password must contain at least one special character")
else:
    print("Valid Password")
