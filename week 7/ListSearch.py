# sortList1 = [1,2,3,4,5,6,7,8,9]
# sortList2 = []
# for x in range(200): #make list2
#     sortList2.append(x*1.25)
# # print(sortList1)
# # print(sortList2[:50])

# def search_sorted_list(sorted_list,item,low=0,high=None): #binary search
#     if high == None:
#         high = len(sorted_list)-1 #sets high point
#     #print(str(high)+" "+str(low))
#     mid = (low+high)//2 #finds mid-point, to check
#     #print(mid)
#     if low > high: #break condition, if item is Not in list
#         return False
#     if sorted_list[mid] == item: #if item is found
#         return True
#     if sorted_list[mid] < item: #Returns list, takes the right side of it to search
#         return search_sorted_list(sorted_list,item,mid+1,high)
#     else:                       #Returns list, takes the left side
#         return search_sorted_list(sorted_list,item,low,mid-1)
        
# # print(search_sorted_list(sortList1,5))
# # print(search_sorted_list(sortList1,3))
# # print(search_sorted_list(sortList1,1))
# # print(search_sorted_list(sortList1,9))

# # inList = input("Input nums, comma seperated: ").split(',') #takes list to be hashed
# # print(inList)
# # #hashList = [None]*(len(inList)*3)
# # print(str(len(inList))+" is the length of the input List")
# # length = int(input("Length of hashList: "))
# # itemFind = int(input("Item to find: ")) #for searching in the list
# # print(inList)
# # print(len(hashList))
# class HashList():
#     def __init__ (self,length):
#         self.length = length
#         self.hashList = [None]*length
#     def put(self,item): #creates the hash-ed list
#         if None not in self.hashList:
#             return False
#         l = len(self.hashList)
#         place = int(item) % l #sets the place to put the number
#         placeP = int(item) % l
#         if self.hashList[place] == None:
#             self.hashList[place] == int(item)
#             return
#         else:
#             place += 1
#         while self.hashList[place] != None and place != placeP:
#             place += 1
#         self.hashList[place] = int(item) #actually places the number
#     def hasher_finder(self): #locates items
#         l = len(self.hashList)
#         hashList = self.hashList
#         item = self.item
#         hashItem = item % l #starting search
#         start = item % l #so to not iterate forever
#         if hashList[hashItem] == item: #don't worry about this one
#             return True
#         else: #its because of the while loop's condition
#             hashItem += 1
#         while hashItem != start: #I needed hashItem to be one higher, or at least not equal too start
#             if hashList[hashItem] == item: #Yay! found item
#                 return True
#             else: #checks next spot
#                 hashItem += 1
#             if hashItem == len(hashList)-1: #if we run out of hash list spots, this will go back to the start
#                 hashItem = 0
#         return False #:( item not found
    
# new_hash_list = HashList(inList,length,itemFind)
# print(new_hash_list.hasher_maker())
# print(new_hash_list.hasher_finder())

class HashList():
    def __init__ (self,length):
        self.length = length
        self.hashList = [None]*length
    def put(self,item):
        self.item = item
        l = self.length
        li = self.hashList
        place = item % l
        placeP = item % l
        if li[place] != None:
            li[place] = item
        else:
            place += 1
            while li[place] != None:
                place += 1
                if li[place] == None:
                    li[place] = item
                if place == l-1:
                    place = 0
                if place == placeP:
                    return False
    def contains(self,item):
        self.item = item
        l = len(self.hashList)
        hashList = self.hashList
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
    def items(self):
        itemLi = []
        for item in self.hashList:
            if item != None:
                itemLi.append(item)
        print(itemLi)
        
new_hash = HashList(15)
new_hash.put(1)
new_hash.put(4)
new_hash.put(1)
new_hash.put(2)
new_hash.items()
new_hash.put(3)
print(new_hash.contains(3))
new_hash.put(1)
new_hash.put(7)
new_hash.put(12)
new_hash.put(1)
new_hash.items()