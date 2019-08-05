import sys


hexdict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def count2bin(base10):
    exp = 8  # max exponent for 2 digit hexidecimal number
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


def hex2bin(hexstr):
    size = len(hexstr)
    count = size - 1
    base10 = 0
    for i in range(0, size):
        digit = hexdict[hexstr[i]]
        base10 += (digit * 16**(count))
        count -= 1
    
    return count2bin(base10)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 filename hexnumber")
        exit(0)
    
    number = sys.argv[1]  # hexidecimal number
    
    print("binary number is: %s" % hex2bin(number));


main()  # start execution