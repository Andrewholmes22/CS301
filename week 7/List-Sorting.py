import random
import time

def listMaker(length):
    unsorted = []
    for _ in range(length):
        rand = random.randint(1,length*100)
        unsorted.append(rand)
    return unsorted

def Insert_Sort(unsorted): #Insert Sort
    length = len(unsorted)
    if length<=1:
        return
    for i in range(1,length):
        curr = unsorted[i]
        print(curr)
        j = i-1
        while j>=0 and curr<unsorted[j]:
            unsorted[j+1]=unsorted[j]
            j -= 1
        unsorted[j+1] = curr

#Bubble Sort

#Select Sort
def SelectionSort(unsorted):  #O(n^2)
    for x in range(len(unsorted)):
        min_index = x
        for n in range(x + 1, len(unsorted)):
            if unsorted[min_index] > unsorted[n]:
                min_index = n
        unsorted[x], unsorted[min_index] = unsorted[min_index], unsorted[x]
    return unsorted
#Merge Sort

def Bogo_Sort(): #BOGO Sort
    unsorted = listMaker(10)
    sort = sorted(unsorted)
    count = 0
    while count != 1000000:
        if unsorted == sort:
            print(unsorted)
            return True
        else:

            random.shuffle(unsorted)
        count += 1
    return False

# for x in range(10):
#     start = time.time()
#     bogo = Bogo_Sort()
#     end = time.time()
#     total = end-start
#     if bogo:
#         string = "Bogo sort time: {time:.2f} seconds"
#     else:
#         string = "Bogo failed after {time:.2f} seconds"
#     print(string.format(time=total))

unsorted = listMaker(10000)

start = time.time()
Insert_Sort(unsorted)
end = time.time()
total = end-start
string = "Insert sort time: {time:.2f} seconds"
print(string.format(time=total))