#Tempo: O(nlogn), Espaço: O(1)
def nonConstructibleChange(coins):
    if(len(coins)==0):
        return 1
    coins = sorted(coins)
    sum = 0
    for coin in coins:
        if(coin>sum+1):
            return sum+1
        sum = sum + coin
    return sum + 1

nonConstructibleChange([5, 7, 1, 1, 2, 3, 22])