import sys
from hexdict import hexdict

'''
Returns 1 if the sign is positive.
Returns -1 if the sign is negative.
'''
def calcsign(c):
    val = hexdict[c]
    if val > 7:
        return -1  # signed digit is negative
    return 1


'''
Takes signed hexidecimal number (string) as a parameter and returns the decimal number
'''
def hex2dec(hexnum):
    size = len(hexnum)
    sign = calcsign(hexnum[0])
    base10 = 0
    count = size - 1  # the placeholder of the digit
    for i in range(1, size):
        base10 += hexdict[hexnum[i]] * 16**count
        count -= 1
    
    return base10 * sign


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 sighex2dec.py hexnum")
    
    print("solution currently incorrect & remains a work in progress.")
    print(hex2dec(sys.argv[1]))


main()
