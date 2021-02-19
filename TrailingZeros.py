import re, math

def zeros(n):
    return re.split(r"[1-9]", str(math.factorial(n))[::-1])[0].count("0")

print(zeros(6000000))