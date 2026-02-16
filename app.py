import os

users = []

def register(username, password):
    if not username or not password:
        return "Invalid input"

    user = {
        "username": username,
        "password": password  # In real project, hash this
    }

    users.append(user)
    return "User registered successfully"

def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return "Login successful"
    return "Invalid credentials"

print(register("admin", "1234"))
print(login("admin", "1234"))
