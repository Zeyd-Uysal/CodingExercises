if __name__ == '__main__':
    n = int(input())
    if n >=2 and n<=10:
        arr = set(list(map(int, input().split()))[:n+1])
        list2 = []
        for i in arr:
            if i >= -100 and i <= 100:
                list2.append(i)
        print(sorted(list(list2))[len(arr)-2])
