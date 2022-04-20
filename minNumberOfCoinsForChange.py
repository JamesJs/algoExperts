# Tempo: O(nd) Espaço: O(n)
def minNumberOfCoinsForChange(n, denoms):
    array = [0] * (n + 1)
    if(n == 0):
        return 0
    for i in range(0,n+1):
        if(i in denoms):
            array[i] = [i]
            continue
        array[i] = []
    for index,denom in enumerate(denoms):
        if(denom > n):
            continue
        for i in range(denom+1,n+1):
            if(len(array[i-denom])==0):
                continue
            newCoins = array[i-denom][0:]
            newCoins.append(denom)
            if(array[i] and len(array[i]) >= len(newCoins) or len(array[i]) == 0):
                array[i] = newCoins
    if(len(array[n]) == 0):
        return -1
    return len(array[n])

print(minNumberOfCoinsForChange(7,[5,10]))