hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hexToDec(hexNum):
    # list = []    

    # for char in hexNum:
    #     list.append(char)   

    for char in hexNum:
        if (char not in hexNumbers):
            # return f'{char} is not a hex character!'
            return None
        
    if len(hexNum) == 3:
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
    if len(hexNum) == 2:
        return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
    
    if len(hexNum) == 1:
        return hexNumbers[hexNum[0]]
        
    if len(hexNum) > 3:
        return 'Max. 3 characters'        
        

# Testing case A2
print(hexToDec('A2')) # 162
# Testing case spam spam spam
print(hexToDec('spam spam spam')) # None
# Testing case A
print(hexToDec('A')) # 10
# Testing case 0
print(hexToDec('0')) # 0
# Testing case 1B
print(hexToDec('1B')) # 27
# Testing case 3C0
print(hexToDec('3C0')) # 960
# Testing case A6G
print(hexToDec('A6G')) # None
# Testing case ZZT0P
print(hexToDec('ZZT0P')) # None