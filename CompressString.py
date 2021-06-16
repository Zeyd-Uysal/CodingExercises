# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    uncompressed_string = input()
    re.sub(r"([a-z])\1+", "(\1, len(\1))", uncompressed_string)
    print(uncompressed_string)
