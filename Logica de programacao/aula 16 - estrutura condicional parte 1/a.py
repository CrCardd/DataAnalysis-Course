def quick_sort(array, start, end):

    if(end <= start):
        return

    pivot = start
    i = start+1
    j = start+1

    while(i<end+1):

        if(array[i] < array[pivot]):
            array[i],array[j] = array[j],array[i]
            j+=1

        i+=1

    array[pivot],array[j-1] = array[j-1],array[pivot]

    quick_sort(array, start, j-2)
    quick_sort(array, j, end)
    return array



arra = [5,2,1,4,10,3,0,-1,51,12,7,0,-2,1000]
print(quick_sort(arra, 0, len(arra)-1))


