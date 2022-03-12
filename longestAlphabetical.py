def longestAlphabetical(string):
    subString =""
    result =string
    l=[]
    prevI=""
    for i in string:
        if prevI < i:
            subString += prevI


        else:
            subString += prevI
            l.append(subString)
            subString=""

        prevI = i

    if len(l):
        result =max(l, key=len)
    return result
print(longestAlphabetical('ndsabcrfe'))
print(longestAlphabetical('abdulrahman'))