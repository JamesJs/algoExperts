
def createMatrix(r,c):
    m = [0] * r
    for i in range(0,len(m)):
        m[i] = [0] * c
    return m
    
def aux(x,y,m):
    if(m[y][x] != 0):
        return m[y][x]
    if(x ==0 and y ==0):
        return 1
    if(x-1 >= 0 and y-1 >= 0):
        m[y][x] = aux(x-1,y,m) + aux(x,y-1,m)
        return m[y][x]
    if(y-1 >= 0):
        m[y][x] = aux(x,y-1,m)
        return m[y][x]
    if(x-1 >= 0):
        m[y][x] = aux(x-1,y,m)
        return m[y][x]



def numberOfWaysToTraverseGraph(width, height):
    if(width ==1 and height == 1):
        return 1
    m = createMatrix(height,width)
    aux(width-1,height-1,m)
    return m[-1][-1]
print(numberOfWaysToTraverseGraph(7,3))
