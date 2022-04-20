#Tempo: O(nlogn) Espaço: O(n)
def classPhotos(redShirtHeights, blueShirtHeights):
    aux = []
    redShirtHeights = sorted(redShirtHeights)
    blueShirtHeights = sorted(blueShirtHeights)
    for i in range(0,len(redShirtHeights)):
        if(redShirtHeights[i] > blueShirtHeights[i]):
            aux.append(1)
            continue
        if(redShirtHeights[i] < blueShirtHeights[i]):
            aux.append(0)
            continue
        if(redShirtHeights[i] == blueShirtHeights[i]):
            return False
    for i in range(1,len(aux)):
        if(aux[i] != aux[i-1]):
            return False
    return True

print(classPhotos([2,4,7,5,1],[3,5,6,8,2]))