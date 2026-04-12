hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hexToDec(hexNum):
    for char in hexNum:
        if (char not in hexNumbers):            
            return None
    converted = 0 # Initialize converted variable to store the converted decimal number value.
    exponent = len(hexNum) -1 # Initialize exponent variable to store the exponent value for each character in hexNum. The exponent value is determined by the position of the character in hexNum, starting from 0 for the rightmost character and increasing by 1 for each character to the left.
    print("Before loop", "converted:", converted, "exponent:", exponent)
    for char in hexNum:
        converted = converted + (hexNumbers[char] * (16 ** exponent)) # Update the converted variable by adding the value of the current character in hexNum multiplied by 16 raised to the power of the current exponent value. This is done for each character in hexNum, starting from the leftmost character and moving to the rightmost character.
        exponent = exponent -1 # Decrease the exponent value by 1 for the next character in hexNum. This is done after processing each character in hexNum, so that the exponent value is correctly updated for the next character.
        print("During loop", "converted:", converted, "exponent:", exponent)
    return converted


# Testing case A2
print(hexToDec('A2')) # 162
# # Testing case spam spam spam
# print(hexToDec('spam spam spam')) # None
# # Testing case A
# print(hexToDec('A')) # 10
# # Testing case 0
# print(hexToDec('0')) # 0
# # Testing case 1B
# print(hexToDec('1B')) # 27
# # Testing case 3C0
# print(hexToDec('3C0')) # 960
# # Testing case A6G
# print(hexToDec('A6G')) # None
# # Testing case ZZT0P
# print(hexToDec('ZZT0P')) # None