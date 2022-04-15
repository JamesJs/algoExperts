#Tempo: O(logn) melhor caso, O(n) pior caso(Árvore com um ramo somente), Espaço O(1).
#Se implementado recursivamente o espaço é O(logn) para o melhor caso e O(n) para o pior caso
#pois a stack fica preenchida com código de chamadas recursivas.
def findClosestValueInBst(tree, target):
    if(tree.value == target):
		return tree.value 
	
	if(target > tree.value):
		aux = tree.right
	else:
		aux = tree.left
	auxValue = tree.value
	while(aux is not None):
		if(abs(aux.value-target)<abs(auxValue-target)):
			auxValue = aux.value
		if(aux.value == target):
			break
		if(aux.value>target):
			aux = aux.left
			continue
		if(aux.value<target):
			aux = aux.right
			continue
	return auxValue
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

