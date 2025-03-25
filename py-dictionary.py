user = {
    "name": "Aqila Riza Dzahabi",
    "age": 17,
    "is_admin": True
}

username = user.get("username", "aqlaar")
print(username)

user["name"] = "Abie Coyy"
print(user)

user["school"] = "SMA Citra Nusa"
print(user)