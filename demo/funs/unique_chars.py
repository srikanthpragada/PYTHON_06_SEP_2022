
def unique_chars(*names):
    uc = set()  # Empty set
    for n in names:
        uc = uc | set(n)

    return "".join(uc)  # Convert set to str

print( unique_chars("java", "c", "ruby"))



