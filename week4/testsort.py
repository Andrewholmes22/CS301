def InsertionSort(unsorted):  #O(n^2)
    for x in range(len(unsorted)):
        for n in range(len(unsorted)):
            current_id = unsorted[x]
            next_id = unsorted[n]
            if current_id < next_id:
                unsorted[n] = current_id
                unsorted[x] = next_id
    return unsorted

def BubbleSort(unsorted):  #O(n^2)
    listLength = len(unsorted)
    for x in range(0, listLength - 1):
        found = False
        for n in range(0, listLength - 1):
            current_id = unsorted[n]
            next_id = unsorted[n + 1]
            if current_id > next_id:
                unsorted[n + 1] = current_id
                unsorted[n] = next_id
                found = True
        listLength = listLength - 1
        if not(found):
            break   
    return unsorted
def SelectionSort(unsorted):  #O(n^2)
    for x in range(len(unsorted)):
        min_index = x
        for n in range(x + 1, len(unsorted)):
            if unsorted[min_index] > unsorted[n]:
                min_index = n
        unsorted[x], unsorted[min_index] = unsorted[min_index], unsorted[x]
    return unsorted
def MergeSort(unsorted):#O(n log n)
    # base case
    if len(unsorted) > 1:
        mid = len(unsorted) // 2
        left= unsorted[:mid]
        right= unsorted[mid:]
        # recursive call sort the left then right
        MergeSort(left)
        MergeSort(right)
        i = 0
        j = 0
        k = 0
        # merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted[k] = left[i]
                i += 1
            else:
                unsorted[k] = right[j]
                j += 1
            k += 1
        # check to see if elements are left on the left side
        while i < len(left):
            unsorted[k] = left[i]
            i += 1
            k += 1
        # check to see if elements are left on the right side
        while j < len(right):
            unsorted[k] = right[j]
            j += 1
            k += 1

    return unsorted

# test
print("insertion:"+InsertionSort([5, 3, 8, 6, 1, 9, 2, 7]))
print("bubble:"+BubbleSort([5, 3, 8, 6, 1, 9, 2, 7]))
print("selection:"+SelectionSort([5, 3, 8, 6, 1, 9, 2, 7]))
print("merge:"+MergeSort([5, 3, 8, 6, 1, 9, 2, 7]))
