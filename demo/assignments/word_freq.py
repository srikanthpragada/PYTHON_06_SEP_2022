s = "how do you do today and how you were yesterday"
words = s.split()
for w in sorted(set(words)):
    print(f"{w} - {words.count(w)}")