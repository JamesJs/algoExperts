def createMatrix(n):
    m = [0] * n
    for i in range(0,n):
        m[i] = []
    return m

def longestIncreasingSubsequence(array):
    n = len(array)
    m = createMatrix(n)
    for index,number in enumerate(array):
        for i in range(index+1,n):
            if(array[i] > number):
                m[index].append(i)
    for i in range(n-1,-1,-1):
        if m[i] == []:
            m[i] = [i]
            continue
        aux = len(m[m[i][0]])
        index = m[i][0]
        for j in range(0,len(m[i])):
            if(len(m[m[i][j]]) > aux):
                aux = len(m[m[i][j]])
                index = m[i][j]
        m[i] = []
        m[i] = m[index][:]
        m[i].append(i)
    
    maxIndex = 0
    for index,i in enumerate(m):
        if(len(m[maxIndex]) < len(i)):
            maxIndex = index
    return len(m[maxIndex])
    result = []
    for i in m[maxIndex]:
        result.append(array[i])
    return sorted(result)
print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))

