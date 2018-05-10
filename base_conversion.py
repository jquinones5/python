base_eight = {"000":"0","001":"1","010":"2","011":"3",
              "100":"4","101":"5","110":"6","111":"7",
              "0":"000","1":"001","2":"010","3":"011",
              "4":"100","5":"101","6":"110","7":"111"}
base_hex = {"0000":"0","0001":"1","0010":"2","0011":"3",
            "0100":"4","0101":"5","0110":"6","0111":"7",
            "1000":"8","1001":"9","1010":"A","1011":"B",
            "1100":"C","1101":"D","1110":"E","1111":"F",
            "0":"0000","1":"0001","2":"0010","3":"0011",
            "4":"0100","5":"0101","6":"0110","7":"0111",
            "8":"1000","9":"1001","A":"1010","B":"1011",
            "C":"1100","D":"1101","E":"1110","F":"1111"}
def bin_to_oct(number):
    parts = ""
    conversion = ""
    for n in range(len(number) - 1, -1, -1):
        parts = number[n] + parts
        if len(parts) == 3:
            conversion = base_eight[parts] + conversion
            parts = ""
    if len(parts) > 0:
        for n in range(0, 3 - len(parts)):
            parts = "0" + parts
        conversion = base_eight[parts] + conversion
    return conversion

def oct_to_bin(number):
    conversion = ""
    for n in number:
        conversion += base_eight[n]
    if conversion[0] == "0":
        conversion = conversion[1:]
        if conversion[0] == "0":
            conversion = conversion[1:]
    return conversion

def bin_to_ten(number):
    conversion = 0
    for n in range(0,len(number)):
        conversion += int(number[len(number) - 1 - n]) * (2 ** n)
    return conversion

def ten_to_bin(number):
    conversion = ""
    result = int(number)
    while True:
        if result % 2 == 1:
            conversion = "1" + conversion
        else:
            conversion = "0" + conversion
        result = result // 2
        if result == 0:
            return conversion

def bin_to_hex(number):
    parts = ""
    conversion = ""
    for n in range(len(number) - 1, -1, -1):
        parts = number[n] + parts
        if len(parts) == 4:
            conversion = base_hex[parts] + conversion
            parts = ""
    if len(parts) > 0:
        for n in range(0, 4 - len(parts)):
            parts = "0" + parts
        conversion = base_hex[parts] + conversion
    return conversion

def hex_to_bin(number):
    conversion = ""
    for n in number:
        if n.isalpha():
            conversion += base_hex[n.upper()]
        else:
            conversion += base_hex[n]
    if conversion[0] == "0":
        conversion = conversion[1:]
        if conversion[0] == "0":
            conversion = conversion[1:]
            if conversion[0] == "0":
                conversion = conversion[1:]
    return conversion

def convert(base, to, number):
    if base == "0":
        if to == "0":
            return number
        elif to == "8":
            return bin_to_oct(number)
        elif to == "9":
            return bin_to_ten(number)
        else:
            return bin_to_hex(number)
    elif base == "8":
        if to == "0":
            return oct_to_bin(number)
        elif to == "8":
            return number
        elif to == "9":
            temp = oct_to_bin(number)
            return bin_to_ten(temp)
        else:
            temp = oct_to_bin(number)
            return bin_to_hex(temp)
    elif base == "9":
        if to == "0":
            return ten_to_bin(number)
        elif to == "8":
            temp = ten_to_bin(number)
            return bin_to_oct(temp)
        elif to == "9":
            return number
        else:
            temp = ten_to_bin(number)
            return bin_to_hex(temp)
    else:
        if to == "0":
            return hex_to_bin(number)
        elif to == "8":
            temp = hex_to_bin(number)
            return bin_to_oct(temp)
        elif to == "9":
            temp = hex_to_bin(number)
            return bin_to_ten(temp)
        else:
            return number

def main():
    allowed = '089fF'
    base = input("From: Base 2 [0], Base 8 [8], Base 10 [9], Base 16 [F]: ")
    to = input("To: Base 2 [0], Base 8 [8], Base 10 [9], Base 16 [F]: ")
    while base not in allowed or to not in allowed:
        print("Please use the number in brackets.")
        base = input("From: Base 2 [0], Base 8 [8], Base 10 [9], Base 16 [F]: ")
        to = input("To: Base 2 [0], Base 8 [8], Base 10 [9], Base 16 [F]: ")
    number = input("Input number to convert: ")
    convertion = convert(base,to,number)
    return convertion

stop = False
while not stop:
    print(main())
    if input("Enter space to continue") != " ":
        stop = True
