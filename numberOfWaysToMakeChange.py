
#Tempo O(n*d) com d = len(denoms), Espaço: O(n)
def numberOfWaysToMakeChange(n, denoms):
    array = [0] * (n+1)
    array[0] = 1
    for index,denom in enumerate(denoms):
        for index2,value in enumerate(array):
            if(index2 < denom):
                continue
            array[index2] += array[index2-denom]
    print(array)
    return array.pop()
print(numberOfWaysToMakeChange(7,[2,4]))