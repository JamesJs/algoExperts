
def createMatrix(r):
    m = [0] * r
    for i in range(r):
        m[i] = []
    return m 


#Tempo: O(w*h), Espaço: O(w*h)
def maximumSumSubmatrix(matrix, size):
    sumsMatix = createMatrix(len(matrix))
    count = 0
    n = len(matrix)
    c = len(matrix[0])
    for i in range(0,n):
        sum = 0
        for j in range(c):
            sum = sum + matrix[i][j]
            if(j >= size-1):
                sumsMatix[i].append(sum)
                sum = (sum-matrix[i][j-(size-1)])
    result = []
    print(sumsMatix)
    for i in range(0,len(sumsMatix[0])):
        sum = 0
        for j in range(n):
            sum = sum + sumsMatix[j][i]
            if(j >= size-1):
                result.append(sum)
                sum = (sum-sumsMatix[j-(size-1)][i])
    return max(result)

print(maximumSumSubmatrix( [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2]
  ],2))



