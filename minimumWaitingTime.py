# Tempo: O (nlogn) Espaço: O(1)
def minimumWaitingTime(queries):
    newArray = sorted(queries)
    sum = 0
    for index,number in enumerate(newArray):
        print(len(newArray)-1-index)
        sum = sum + number*(len(newArray)-1-index)
    return sum

minimumWaitingTime([3,2,1,2,6])