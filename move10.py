import re
#TODO: fix error in re.sub
def move_ten(st):
    woord = ""
    for item in st:
        nummer = ord(item)+ 10
        woord += re.sub(r"([^a-z])", chr(nummer-26), chr(nummer), flags=re.IGNORECASE)
    return woord

print(move_ten("l"))
