def minNumberOfJumps(array):
    size = len(array)
    if(len(array) == 1):
        print(1)
        return 1
    j = array[0]
    last = 0
    count = 0
    maybe = 1
    for i in range(0,size+1):
        if(i > last + j):
            print(maybe)
            count = count + 1
            last = maybe
            j = array[maybe]
            if(last+array[last] >= size-1):
                count = count + 1
                break
        if(i >= size):
            if(maybe != size - 1):
                count = count+1
            break
        if(array[i] + i > array[maybe] + maybe):
            maybe = i
    print(maybe)
    return count
minNumberOfJumps([2, 1, 2, 3, 1])
