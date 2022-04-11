

def aux(array,hash,indiceNext):
    print(array)
    if(len(array) == 1 or len(array) == 2):
        return array[0]
    sum = 0
    for i in range(0,len(array)):  
        if((indiceNext+i+2) in hash):
            sumAux = array[0] + hash[indiceNext+i+2]
        else:
            sumAux = array[0] + aux(array[i+2:],hash,indiceNext+i+2)
        if(sumAux>sum):
            sum = sumAux
    hash[indiceNext] = sum
    return sum

def maxSubsetSumNoAdjacent(array):
    hash = {}
    return max(aux(array,hash,0),aux(array[1:],hash,1))  

print(maxSubsetSumNoAdjacent([1,15]))
