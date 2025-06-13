def QuickSort(array):
    if len(array) <= 1:
        print(array)
        return array

    pivot = array[0]
    x = 0

    for y in range(1, len(array)):
        if(array[y] < pivot):
            x += 1  
            array[x], array[y] = array[y], array[x]

    array[0] = array[x]
    array[x] = pivot

    left = QuickSort(array[:x])
    right = QuickSort(array[x+1:])
    return left + [pivot] + right


print(QuickSort([9,19,3,1,39,5,6]))