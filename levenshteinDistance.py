def levenshteinDistance(str1, str2):
    move = 0
    strArray = list(str1[:])
    i = 0 
    while i < len(strArray):
        if(strArray[i] != str2[i]):
            move = move + 1
            if(len(strArray) < len(str2)):
                strArray.insert(i,str2[i])
            else:
                strArray[i] = str2[i]
        i = i + 1
    return move + abs(len(strArray) - len(str2))

print(levenshteinDistance("","abcx"))