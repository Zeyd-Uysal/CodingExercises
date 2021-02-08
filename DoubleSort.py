
#def db_sort(arr): 
#    nummers = []
#    woorden = []
#    strnummers = []
#    nummersasint = []
#    for item in arr:
#        if isinstance(item , int) or item.isdigit() == True:
#            if isinstance(item , str):
#                strnummers.append(item)
#                nummersasint.append(int(item))
#            else:
#                nummers.append(int(item))
#        else:
#            woorden.append(item) 
#    nummers.sort()
#    nummersasint.sort()
#    woorden.sort()
#    for item in strnummers:
#        nummersasint.insert(nummersasint.index(int(item)), item)
#    for item in nummersasint:
#        nummers.append(item)
#    for item in woorden:
#        nummers.append(item)
#    return nummers

nummers =[]
def db_sort(arr):
    woorden =[]
    strnummers =[]
    strnummersint =[]
    for item in arr:
        if isinstance(item,int) or item.isdigit():
            if isinstance(item , str):
                strnummers.append(item)
                strnummersint.append(int(item))    
            else:
                nummers.append(int(item))
        else:
            woorden.append(item) 
    nummers.sort()
    strnummersint.sort()
    woorden.sort()
    for item in woorden:
        if item == "!":
            nummers.append(item)
    for item in strnummers:
        strnummersint[strnummersint.index(int(item))] = item
    for item in strnummersint:
        nummers.append(item)    
    for item in woorden:
        if item != "!":
            nummers.append(item)
    return nummers
print(db_sort(["3",2,  "1", "Banana"]))