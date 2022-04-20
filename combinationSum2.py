#Tempo O(n^n) Espaço O(n^(n+1))

def combinationSum2(array,n):
    hash={}
    result = []
    if(sum(array)<n):
        return []
    primeiro = array[0]
    sumAux = 0
    repeat = True
    if(len(array) == 1 and array[0] == n):
        return [array]
    oldIndex = 0
    if(len(array)>10):
        for index,number in enumerate(array):
            sumAux = sumAux + number
            if(sumAux == n):
                result.append(array[oldIndex:index+1])
                oldIndex = index
                sumAux = 0
            if(number !=primeiro):
                repeat = False
                break
            
    if(repeat):  
        return list(filter(lambda x: len(x) != 0,result))
    initialLen = len(array)
    array = sorted(array)
    
    for j in range(0,initialLen):
        if(array[j]>n):
            break
        if(array[j] == n):
            result.append(array[j])
            break 
        print('[%d%%]\r'%((j+1)/(initialLen+1)), end="")
        actualLen = len(array)
        for i in range(j+1,actualLen):
            if((array[j]+array[i])>n):
                continue    
            if(i < initialLen):
                hash[len(array)] = [j,i]
                array.append(array[j]+array[i])    
                continue
            if(j not in hash[i]):
                hash[len(array)] = hash[i][:]
                hash[len(array)].append(j)
                array.append(array[j]+array[i])
                continue
    for index,number in enumerate(array):
        if(number == n and index>initialLen-1):
            resultAux = []
            for index2 in hash[index]:
                resultAux.append(array[index2])
            auxResultSorted = sorted(resultAux)
            if(len(resultAux) != 0 and auxResultSorted not in result):
                result.append(auxResultSorted)
    print(array)
    return result



print(combinationSum([1,1],2))

