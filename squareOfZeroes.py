def createMatrix(c,d):
    m = [] 
    for i in range(0,c):
        m.append([0] * d)
    return m
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(str(m[i][j]) + ' ')
        print("\n")

def squareOfZeroes(matrix):
    n = len(matrix)
    d = len(matrix[0])
    print(n)
    m = createMatrix(n,d) 
    print(len(m[0]))
    for i in range(0,n):
        for j in range(0,d):
            if(m[i][j] == 0):
                m[i][j] = {"left":0,"top":0,"right":0,"bottom":0}
            if(matrix[i][j] == 0):
                if(j > 0 and matrix[i][j-1] == 0):
                    m[i][j]["left"] = m[i][j-1]["left"] + 1
                if(i > 0 and matrix[i-1][j] == 0):
                    m[i][j]["top"] = m[i-1][j]["top"] + 1
    for i in range(n-1,-1,-1):
        for j in range(d-1,-1,-1):
            if(matrix[i][j] == 0):
                if(j+1 < d and matrix[i][j+1] == 0):
                    m[i][j]["right"] = m[i][j+1]["right"] + 1
                if(i+1 < n and matrix[i+1][j] == 0):
                    m[i][j]["bottom"] = m[i+1][j]["bottom"] + 1
    for i in range(0,n):
        for j in range(0,d):
            if(m[i][j]["right"] != 0 and i+m[i][j]["right"]<n and j+m[i][j]["right"]<d  and m[i][j]["right"] <= m[abs(i+m[i][j]["right"])][j]["right"] and m[i][j]["bottom"] >= m[i][j]["right"] and m[i][j+m[i][j]["right"]]["bottom"] >= m[i][j]["right"]):
                return True
            if(m[i][j]["right"] != 0 and i-m[i][j]["right"]>=0 and j+m[i][j]["right"]<d  and m[i][j]["right"] < m[i-m[i][j]["right"]][j]["right"] and m[i][j]["top"] >= m[i][j]["right"] and m[i][j+m[i][j]["right"]]["top"] >= m[i][j]["right"]):
                return True       
    return False
# print(squareOfZeroes([
#             [1, 1, 1, 0, 1, 0],
#             [0, 0, 0, 0, 0, 1],
#             [0, 1, 1, 1, 0, 1],
#             [0, 0, 0, 1, 0, 1],
#             [0, 1, 1, 1, 0, 1],
#             [0, 0, 0, 0, 0, 1],
#         ]))
print(squareOfZeroes([["1","0","1","0","0","1","1","1","0"],
["1","1","1","0","0","0","0","0","1"],
["0","0","1","1","0","0","0","1","1"],
["0","1","1","0","0","1","0","0","1"],
["1","1","0","1","1","0","0","1","0"],
["0","1","1","1","1","1","1","0","1"],
["1","0","1","1","1","0","0","1","0"],
["1","1","1","0","1","0","0","0","1"],
["0","1","1","1","1","0","0","1","0"],
["1","0","0","1","1","1","0","0","0"]]))

[["1","0","1","0","0","1","1","1","0"],
["1","1","1","0","0","0","0","0","1"],
["0","0","1","1","0","0","0","1","1"],
["0","1","1","0","0","1","0","0","1"],
["1","1","0","1","1","0","0","1","0"],
["0","1","1","1","1","1","1","0","1"],
["1","0","1","1","1","0","0","1","0"],
["1","1","1","0","1","0","0","0","1"],
["0","1","1","1","1","0","0","1","0"],
["1","0","0","1","1","1","0","0","0"]]
