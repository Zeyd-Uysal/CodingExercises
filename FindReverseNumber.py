import re


def find_reverse_number(nummer):
    strnummer = str(nummer)
    if nummer < 11:
        result = nummer - 1
    elif nummer == 11:
        result = nummer
    elif re.sub(r"[0]", "", strnummer) == "1":
        result = "9" + re.sub(r"[1]", "", strnummer)[1:] + "9"
    else:
        firstchar = strnummer[:1]
        if firstchar > "1":
            strnummer = str(int(firstchar) - 1) + strnummer[1:]
            result = getResult(strnummer)
        elif strnummer[1:2] == "0":
            strnummer = "9" + strnummer[2:]
            result = getResult(strnummer)
        else:
            strnummer = strnummer[1:]
            result = strnummer + strnummer[::-1]
    return int(result)


def getResult(strnummer):
    result = strnummer
    strnummer = strnummer[:len(strnummer) - 1]
    result += strnummer[::-1]
    return result


print(find_reverse_number(95434249))
print(find_reverse_number(10734434148))
