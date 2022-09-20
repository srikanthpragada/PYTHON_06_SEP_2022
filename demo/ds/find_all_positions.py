
st = "how do you do"
ss = "do"

pos = -1
while True:
    pos = st.find(ss, pos + 1)
    if pos == -1:
        break

    print(pos)

