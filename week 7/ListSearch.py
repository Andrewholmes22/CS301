sortList1 = [1,2,3,4,5,6,7,8,9]
sortList2 = []
for x in range(200): #make list2
    sortList2.append(x*1.25)
# print(sortList1)
# print(sortList2[:50])

def search_sorted_list(sorted_list,item,low=0,high=None): #binary search
    if high == None:
        high = len(sorted_list)-1 #sets high point
    #print(str(high)+" "+str(low))
    mid = (low+high)//2 #finds mid-point, to check
    #print(mid)
    if low > high: #break condition, if item is Not in list
        return False
    if sorted_list[mid] == item: #if item is found
        return True
    if sorted_list[mid] < item: #Returns list, takes the right side of it to search
        return search_sorted_list(sorted_list,item,mid+1,high)
    else:                       #Returns list, takes the left side
        return search_sorted_list(sorted_list,item,low,mid-1)
        
# print(search_sorted_list(sortList1,5))
# print(search_sorted_list(sortList1,3))
# print(search_sorted_list(sortList1,1))
# print(search_sorted_list(sortList1,9))

inList = input("Input nums, comma seperated: ").split(',') #takes list to be hashed
print(inList)
itemFind = int(input("Item to find: ")) #for searching in the list
hashList = [None]*(len(inList)*3) #creates the empty list to be filled
# print(inList)
# print(len(hashList))
def hasher_maker(inList,hashList): #creates the hash-ed list
    l = len(hashList)
    for num in  inList:
        place = int(num) % l #sets the place to put the number
        while hashList[place] != None: #to not overfill
            place += 1
        hashList[place] = int(num) #actually places the number
    #return hashList
        
def hasher_finder(hashList,item): #locates items
    l = len(hashList)
    hashItem = item % l #starting search
    start = item % l #so to not iterate forever
    if hashList[hashItem] == item: #don't worry about this one
        return True
    else: #its because of the while loop's condition
        hashItem += 1
    while hashItem != start: #I needed hashItem to be one higher, or at least not equal too start
        if hashList[hashItem] == item: #Yay! found item
            return True
        else: #checks next spot
            hashItem += 1
        if hashItem == len(hashList)-1: #if we run out of hash list spots, this will go back to the start
            hashItem = 0
    return False #:( item not found

hasher_maker(inList,hashList)
#print(hashList)
print(hasher_finder(hashList,itemFind))