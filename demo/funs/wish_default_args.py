def wish(user: str = "Guest", message: str = "Hello"):
    print(message, user)


wish("Andy", "Hi")
wish("Tom")
wish()
wish(message = "Hi")


