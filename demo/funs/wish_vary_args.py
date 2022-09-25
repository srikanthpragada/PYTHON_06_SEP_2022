def wish(*users, message: str = "Hi"):
    print(type(users))
    for u in users:
        print(message, u)


wish("Andy", "Scott")
wish("Li", "Hu", "Ci", message = "Hello")


