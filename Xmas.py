import math
def xmastree(n):
    ls = []
    for i in range(1,n+1):
        hs = "".join("-"for i in range(n-(i))) + "".join("#"for i in range(math.floor((i)*1.9999))) + "".join("-"for i in range(n-(i)))
        ls.append(hs)
    for i in range(2):
        hs = "".join("-"for i in range(n-1)) + "".join("#"for i in range(1)) + "".join("-"for i in range(n-1))
        ls.append(hs)
    return(ls)
if __name__ == '__main__':
    xmastree(4)