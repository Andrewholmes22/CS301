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
        j = i-1
        while j>=0 and curr<unsorted[j]:
            unsorted[j+1]=unsorted[j]
            j -= 1
        unsorted[j+1] = curr

def Bubble_Sort(unsorted): #Bubble Sort
    l = len(unsorted)
    for i in range(l):
        sort = False
        for j in range(0,l-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]
                sort = True
        if (sort == False):
            break

#Select Sort
def Selection_Sort(unsorted):  #O(n^2)
    for x in range(len(unsorted)):
        min_index = x
        for n in range(x + 1, len(unsorted)):
            if unsorted[min_index] > unsorted[n]:
                min_index = n
        unsorted[x], unsorted[min_index] = unsorted[min_index], unsorted[x]
    return unsorted

def List_Merger(list1,list2):
    sort = []
    l1 = len(list1)
    l2 = len(list2)
    print(list1,list2)
    done = False
    while not done:
        if len(list1) < 1:
            sort.extend(list2)
            break
        if len(list2) < 1:
            sort.extend(list1)
            break
        if list1[0] < list2[0]:
            inp = list1.pop(0)
        else:
            inp = list2.pop(0)
        sort.append(inp)
    return sort

def Merge_Sort(unsorted): #Merge Sort
    if len(unsorted) > 1:
        mid = len(unsorted)//2
        l1 = unsorted[:mid]
        l2 = unsorted[mid:]
        Merge_Sort(l1)
        Merge_Sort(l2)
        i=0
        j=0
        k=0
        while i<len(l1) and j<len(l2):
            if l1[i] < l2[j]:
                unsorted[k] = l1[i]
                i+=1
            else:
                unsorted[k] = l2[j]
                j+=1
            k+=1
        while i < len(l1):
            unsorted[k] = l1[i]
            i+=1
            k+=1
        while j < len(l2):
            unsorted[k] = l2[j]
            j+=1
            k += 1
        return unsorted
    
def Bogo_Sort(): #BOGO Sort O(Very High)
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

unsorted = listMaker(10000)
start = time.time()
Bubble_Sort(unsorted)
end = time.time()
total = end-start
string = "Bubble sort time: {time:.2f} seconds"
print(string.format(time=total))

# list1 = [1,3,5,7,9]
# list2 = [2,4,6,8,10]
# List_Merger(list1,list2)

unsorted = listMaker(1000000)
start = time.time()
Merge_Sort(unsorted)
end = time.time()
total = end-start
string = "Merge sort time: {time:.2f} seconds"
print(string.format(time=total))