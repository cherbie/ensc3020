import sys
from hexdict import hexdict


def count2bin(base10):
    exp = 10  # max exponent for 2 digit hexidecimal number
    remainder = 0;
    binstr = ""
    while exp >= 0:
        # print(f"R = {remainder} & DECIMAL = {base10} & exp = {exp}")
        remainder = (base10 // (2**exp))
        binstr += str(remainder)
        # print(" - " + binstr)
        if remainder == 1:
            base10 = base10 % (2**exp)  # fetch the decimal remainder
        exp -= 1
    
    return binstr

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 filename base10number")
        exit(0)
    
    number = int(sys.argv[1])  # decimal number
    
    print("binary number is: %s" % count2bin(number));


main()  # start execution