# Explanation:
# The JSON blob has a lot characters in it.
# E.g. [("A", 1), ("B", 80), ("C", 10)]
# It becomes: A|1~B|80~C|10
# The ~ is the separator between the different characters, and the | is the separator between the character and the count.
# So the string becomes much smaller, and we can easily decode it by splitting the string on the ~ and then splitting each item on the | to get the character and the count.

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

# 2nd Instructor's solution:
def encodeFile(filename, newFilename):
    with open(filename, 'r') as f:
        data = encodeString(f.read())
    
    data = [f"{char}|{count}" for char, count in data] # Convert the list of tuples into a list of strings in the format "char|count"

    with open(newFilename, 'w') as f:
        f.write('~'.join(data))


def decodeFile(filename):
    with open(filename) as f:
        data = f.read()

    pairs = data.split('~') # Split the string into pairs of character and count
    pairs = [p.split('|') for p in pairs] # Split each pair into character and count
    pairs = [(p[0], int(p[1])) for p in pairs] # Convert the count from string to integer

    return decodeString(pairs)


# Original file size: 2749
# New file size: 1007