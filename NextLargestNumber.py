# def next_bigger(n):
#     l =[]
#     notfound = True
#     specialcase = False
#     savednumber= n % 10
#     savedindex = 0 
#     l = list(reversed(str(n)))
#     lowestnumber = min(l)
#     for i in range(1,len(str(n))):
#         if int(savednumber) == int(lowestnumber):
#             savednumber = l[i]
#             savedindex = i
#         elif int(savednumber) < int(l[i]) and i+1 < len(str(n)) and int(l[i]) > int(l[i+1]) and int(l[i-1]) == int(savednumber):
#             savednumber = l[i]
#             savedindex = i
#             specialcase = True
#         if int(savednumber) > int(l[i]):
#             l.insert(i+1, savednumber)
#             l.pop(savedindex)
#             if savedindex+1 != i and i >=2 or specialcase is True:
#                 l[0:i] = sorted(l[:i], reverse=True)
#             notfound = False
#             break
#     if notfound:
#         return -1
#     return (int("".join([str(k) for k in (list(reversed(l)))])))

def next_bigger(n):
    l =[]
    previousnumbers = {}
    notfound = True
    specialcase = False
    savednumber= int(n % 10)
    savedindex = 0 
    end = False
    l = list(map(int,reversed(str(n))))
    lowestnumber = min(l)
    previousnumbers[int(savedindex)] = savednumber
    for i in range(1,len(str(n))):
        if int(savednumber) == int(lowestnumber):
            savednumber = int(l[i])
            savedindex = i
        if i+1 < len(str(n)):
            if l[i-1] < l[i]:
                if l[i+1] >= savednumber:
                    if l[i+1] < l[i] and not specialcase:
                        savednumber = int(l[i])
                        savedindex = i
                    elif i+2 < len(str(n)) :
                        if l[i+2] < l[i] and not specialcase:
                            savednumber = int(l[i])
                            savedindex = i
                            specialcase = True
        if int(savednumber) > int(l[i]) :
            if not any(y > int(l[i]) for _,y in previousnumbers.items()):
                l.insert(i+1, savednumber)
                l.pop(savedindex)
                if i >=1 or specialcase is True:
                    l[0:i] = sorted(l[:i], reverse=True)
                notfound = False
                break
            else:
                for x in sorted(list(previousnumbers.values())):
                    if int(x) > int(l[i]):
                        l.insert(i+1, x)
                        for key, value in previousnumbers.items():
                            if int(x) == int(value):
                                l.pop(key)
                                break
                        if i >=1 or specialcase is True:
                            l[0:i] = sorted(l[:i], reverse=True)
                        notfound = False
                        end = True
                        break
                if end is True:
                    break
        previousnumbers[i] = int(l[i])
    if notfound:
        return -1
    return (int("".join([str(k) for k in (list(reversed(l)))])))

if __name__ == '__main__':
    print(next_bigger(144))
    4843738
    