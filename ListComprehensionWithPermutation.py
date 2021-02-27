if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = []
    lst1 = []
    lst2 = []
    lst3 = []
    for i in range(x + 1):
        lst1.append(i)
    for j in range(y + 1):
        lst2.append(j)
    for k in range(z + 1):
        lst3.append(k)
    for i in lst1:
        for j in lst2:
            for k in lst3:
                if i+j+k != n:
                    lst.append([i,j,k])
    lst.sort()
    print(lst)
