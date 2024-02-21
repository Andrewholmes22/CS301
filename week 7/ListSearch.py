sortList1 = [1,2,3,4,5,6,7,8,9]
sortList2 = []
for x in range(200): #make list2
    sortList2.append(x*1.25)
# print(sortList1)
# print(sortList2)
# print(sortList3[:21])

def search_sorted_list(sorted_list,item,low=0,high=None):
    print(high)
    if high == None:
        high = len(sorted_list)
    mid = (low+high)//2
    if sorted_list[mid] == item:
        return True
    if low == high:
        return False
    elif sorted_list[mid] < item:
        search_sorted_list(sorted_list,item,low,mid)
    elif sorted_list[mid] > item:
        search_sorted_list(sorted_list,item,mid,high)
    
        
print(search_sorted_list(sortList1,5))
print(search_sorted_list(sortList1,2))
