def solution(number):
    #     sum =0
#     for i in range(number):
#         if i %3 ==0: sum +=i
#         elif i %5 ==0: sum +=i
#     if sum < 0: return 0
#     return sum

    print (sum([x if x %3 ==0 else (x if x%5==0 else 0) for x in range(number)]))
    
if __name__ == '__main__':
    solution(6)
    