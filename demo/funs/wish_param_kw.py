# wish("df","dfd")

def wish(user: str, message: str):
    print(message, user)


wish("Andy", "Hi")  # Positional
wish(message="Hello", user="Scott")  # keyword
wish("Steve", message="Good Morning")  # Mixed
