def isValidSubsequence(array, sequence):
    i = 0
    j = 0
    for i in range(0,len(array)):
        if(j<len(sequence) and array[i] == sequence[j]):
            j = j+1
    if(j == len(sequence)):
        return True
    return False

print(isValidSubsequence([1, 1, 1, 1, 1],[1, 1, 1]))
