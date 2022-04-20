# Tempo: O(n^2) Espaço: O(n^2)
def makeMatrix(array):
    m = [0] * len(array)
    for i in range(0,len(m)):
        m[i] = [array[i],[]]
    return m

def maxSumIncreasingSubsequence(array):
    m = makeMatrix(array)
    for index,number in enumerate(array):
        for i in range(index+1,len(array)):
            if(array[i] > number):
                m[index][1].append(i)
    for i in range(len(m)-1,-1,-1):
        if(m[i][1] == []):
            m[i][1] = [i]
            continue
        aux = -999999
        index = -1
        for j in m[i][1]:
            if(m[j][0] > aux):
                aux = max(aux,m[j][0])  
                index = j         
        m[i][0] = m[i][0] + aux
        m[i][1] = m[index][1][0:]
        m[i][1].append(i)
    maxNumber = -3
    indexMax = -1
    for index,i in enumerate(m):
        if(i[0] > maxNumber):
            maxNumber = i[0]
            indexMax = index
    for index,number in enumerate(m[indexMax][1]):
        m[indexMax][1][index] = array[m[indexMax][1][index]]
    m[indexMax][1] = sorted(m[indexMax][1])
    return m[indexMax]
print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))