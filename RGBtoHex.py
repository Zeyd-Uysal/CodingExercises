def rgb(r, g, b):
    return_value = ""
    for i in [r,g,b]:
        return_value += ("0" + str(hex(i))[2:])[-2:] if ispossible(i) else outofrange(i)
    return ((return_value).upper())
def ispossible(x):
    return 255>= x >= 0
def outofrange(x):
    return "00" if x<0 else "FF"