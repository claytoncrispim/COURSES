# Instructions
#
# Compress a file and expand it to its original text
#
# This challenge builds off of the challenge from Chapter 4, "Encoding ASCII art." # If it's been a little while, then you may want to review your solution from that
# exercise. Here, I've included my solutions for the encodeString and decodeString
# functions, but you can feel free to use your own as well.
#
# Your task
# Create two new functions: encodeFile and decodeFile.
#
# encodeFile opens a file containing an ASCII art smiley face, performs some
# modification to the data in the file, and writes that data to a new file. The new
# file size should be smaller than the original file size.
#
# decodeFile opens the file and performs some reverse of the original modification
# to expand the data in the file to its original form. It then returns the original
# string.
#
# In the ASCII art provided, the original file size is 2,749 bytes. Ideally, your new
# file should be at most 2,748 bytes. If you can get your new file just a little bit
# smaller, you win; however, can you get your new file even smaller? What's the
# smallest you can possibly get this new file?
#
# Parameters
# filename: The filename you must open in order to perform the required file operation
#
# newFilename: The filename you must save the modified file to in the encodeFile
# function
#
# Result
# decodeFile must return the "decoded" (uncompressed) data string.
#
# Want a hint?
# Check out the Jupyter Notebook hints file for this challenge. (Hint: Python-Essential-Training/Ex_Files_Python_EssT/Exercise Files/exercise_files/10_04_Challenge_Hints.ipynb)
# 
# 
# Summary (by Copilot):
# In this challenge, you will create two functions, encodeFile and decodeFile, to compress and expand an ASCII art file. The encodeFile function will read the original file, modify its data to reduce its size, and save it to a new file. The decodeFile function will read the modified file, reverse the modifications to restore the original data, and return it as a string. The goal is to achieve a smaller file size than the original while ensuring that the decoded data matches the original content.

# ---------------------------------------------------------------------------

import json 
from json import JSONDecodeError, JSONEncoder

# From ASCII art compression exercise in Chapter 4, "Encoding ASCII art."
encString = 'AAAAABBBBBCCCCC'


# Given code:
# Python code​​​​​​‌‌‌‌‌​​‌​​‌‌​‌‌‌​​‌‌​​​​​ below


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


# Remembering:
# encodeFile opens a file containing an ASCII art smiley face, performs some
# modification to the data in the file, and writes that data to a new file. The new
# file size should be smaller than the original file size.
# 
# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    # Your code goes here.
    txt = [encodeString(filename)]
    f = open(str(txt), 'r')
    n = open(newFilename, 'w')
    for line in f.readlines():
        with open(newFilename, 'a') as n:
            n.write(line.strip())
    return n

# Remembering:
# decodeFile opens the file and performs some reverse of the original modification
# to expand the data in the file to its original form. It then returns the original
# string.
def decodeFile(filename):
    # Your code also goes here.
    txt = [decodeString(filename)]
    f = open(str(txt), 'r')
    decodedStr = ''
    for line in f.readlines():
        decodedStr = decodedStr + line.strip()
    return decodedStr

encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

# Note: I wasn't able to make the whole thing work. Everything crashed. Jumped straight to the solution file to see how it was done. I think I understand the general idea, but I just couldn't get it to work. I think I need to review the code and try to understand it better before I can attempt to write it myself.