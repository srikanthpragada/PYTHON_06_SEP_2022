import re

with open(r"d:\classroom\sep6\old_man.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)
print('Total count = ', len(words))
uwords = set(words)
print('Unique Words = ', len(uwords))

for w in sorted(uwords):
    print(f"{w} -  {words.count(w)}")
