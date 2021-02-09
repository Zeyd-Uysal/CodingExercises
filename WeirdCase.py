def to_weird_case(string):
    txt = ""
    for item in string.split(" "):
        txt += "".join([(item[i].upper() if i%2 == 0 else item[i].lower()) for i in range(len(item))]) + " "
    return txt.strip()
print(to_weird_case("appel peer"))