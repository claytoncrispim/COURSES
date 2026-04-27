# The objective is to make the file even smaller by encoding the characters and their counts in a more compact way.

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


# Byte solution:
def encodeFile(filename, newFilename):
    with open(filename, 'r') as f:
        data = encodeString(f.read())
    output = bytearray()
    for item in data:
        # Character byte
        output.extend(bytes(item[0], 'utf-8'))
        #  Integer count byte
        output.extend(bytes(item[1].to_bytes(1, 'big')))
    with open(newFilename, 'wb') as binary_file:
        # Write the bytes to the file
        binary_file.write(output)

def decodeFile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        # Split data into pairs of character and count  
        bytePairs = [data[i:i+2] for i in range(0, len(data), 2)]
        encodedList = []
        for bytePair in bytePairs:
            encodedList.append((bytePair[0:1].decode('utf-8'), int.from_bytes(bytePair[1:2], 'big')))
    return decodeString(encodedList)

# Original file size: 2749
# New file size: 466