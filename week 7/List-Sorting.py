import random
import time

def listMaker(length):
    unsorted = []
    for x in range(length):
        rand = random.randint(0,length*2)
        unsorted.append(rand)
    return unsorted

def Insert_Sort(): #Insert Sort
    unsorted = listMaker(10)
    sort = []
    print(unsorted[:100])
    sort.append(unsorted[0])
    for item in unsorted:
        for test in sort:
            if item > test:
                sort.insert(sort.index(test),item)
    print(sort[:100])

#Bubble Sort

#Select Sort

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

start = time.time()
Insert_Sort()
end = time.time()
total = end-start
string = "Insert sort time: {time:.2f} seconds"
print(string.format(time=total))