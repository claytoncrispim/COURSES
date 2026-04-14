encString = 'AAAAABBBBBCCCCC'

# def returnChar(char):    
#     primaryList = []       
#     prevChar = None      
#     counter = 0    
#     for i in range(len(char)):
#         if char[i] != prevChar:
            
#             primaryList.append(char[i])

#         prevChar = char[i]                 
#         counter = counter + 1 
#         primaryList.append(counter)        

#     filteredTuple = prevChar, counter 
#     # print(type(filteredTuple))
#     return filteredTuple

# print(returnChar('BB'))


# Solutions by the instructor:
def encodeString(stringVal):    
    encodedList = []    
    prevChar = stringVal[0] # initialize the previous character to the first character of the string
    count = 0
    for char in stringVal: # loop through each character in the string
        if prevChar != char: # if the current character is different from the previous character, then we need to append the previous character and its count to the list
            encodedList.append((prevChar, count)) # append a tuple to the list
            count = 0 # reset the count for the new character
        prevChar = char # update the previous character to the current character
        count = count + 1 # increment the count for the current character
    
    encodedList.append((prevChar, count)) # append the last character and count as a tuple to the list    
    return encodedList

def decodeString(encodedList):
    decodedStr = ''    
    for item in encodedList: # loop through each tuple in the list
        print('decodedStr(Before): ', decodedStr)        
        decodedStr = decodedStr + item[0] * item[1] # append the character multiplied by its count to the decoded string
        print('decodedStr(After): ', decodedStr)
    return decodedStr




print(encodeString(encString))
print(decodeString(encodeString(encString)))


