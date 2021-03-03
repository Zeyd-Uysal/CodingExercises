# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == '__main__':
    c = int(input())
    a = int(input())
    b = math.sqrt((math.pow(c,2) + math.pow(a,2)))
    MC = b/2
    percentage = c/a
    angleC = math.acos((math.pow(b, 2) + math.pow(a,2) - math.pow(c,2) )/ (2* (b * a)))
    print("{:0.2f}".format(math.degrees(angleC))+ '\N{DEGREE SIGN}')