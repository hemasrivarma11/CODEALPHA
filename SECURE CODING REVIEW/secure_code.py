import hashlib

stored_username = "admin"
stored_password = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and hashed_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials")