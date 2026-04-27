# 1st Instructor's solution:

# Python code​​​​​​‌‌‌‌‌​​‌​​‌‌​‌‌‌​​‌‌​​​​​ below
import json 

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

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    # Your code goes here.
    with open(filename, 'r') as f:
        data = encodeString(f.read())

    with open(newFilename, 'w') as f:
        json.dump(data, f)

def decodeFile(filename):
    # Your code also goes here.
    with open(filename, 'r') as f:
        data = json.load(f)
    return decodeString(data)
    

# Original file size: 2749
# New file size: 2441