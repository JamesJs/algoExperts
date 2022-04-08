
#tempo: O(nlogn) espaço:O(n)
def sortedSquaredArray(array):
    result = []
    for value in array:
        result.append(pow(value,2))
    return (sorted(result))

#tempo: O(n) espaço:O(n)
def sortedSquaredArrayOp(array):
    i = 0
    j = len(array) - 1
    result = [0] * len(array)
    while(j>=i):
        result[abs(j)-abs(i)] = max(pow(array[i],2),pow(array[j],2))
        if(abs(array[j]) >= abs(array[i])):
            j = j - 1
        else:
            i = i + 1
    return result

print(sortedSquaredArrayOp([-3, -2, -1]))