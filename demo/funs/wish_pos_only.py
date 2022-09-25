# Positional-only arguments
def wish(msg: str, user: str, /):
    print(msg, user)


wish("Andy", "Hi")  # Positional
#wish(message="Hello", user="Scott")  # keyword
