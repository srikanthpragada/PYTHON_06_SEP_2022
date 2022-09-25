# Keyword-only arguments
def wish(*, message: str, user: str):
    print(message, user)


# wish("Andy", "Hi")  # Positional
wish(message="Hello", user="Scott")  # keyword
