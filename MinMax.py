def calculateMinMax(lst):
        lst = sorted(lst)
        return [min(lst),max(lst)]

if __name__ == '__main__':
    for i in range(int(input())):
        lst = []
        for j in range(int(input())):
            lst.append(int(input()))
        output = calculateMinMax(lst)
        print("{:0.0f} {:0.0f} {:0.0f}".format((i+1) , output[0], output[1]))