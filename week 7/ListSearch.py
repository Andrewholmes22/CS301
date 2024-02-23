sortList1 = [1,2,3,4,5,6,7,8,9]
sortList2 = []
for x in range(200): #make list2
    sortList2.append(x*1.25)
# print(sortList1)
# print(sortList2[:50])


def search_sorted_list(sorted_list,item,low=0,high=None):
    if high == None:
        high = len(sorted_list)-1
    #print(str(high)+" "+str(low))
    mid = (low+high)//2
    #print(mid)
    if low > high:
        return False
    if sorted_list[mid] == item:
        return True
    if sorted_list[mid] < item:
        return search_sorted_list(sorted_list,item,mid+1,high)
    else:
        return search_sorted_list(sorted_list,item,low,mid-1)
    
        
print(search_sorted_list(sortList1,5))
print(search_sorted_list(sortList1,3))
print(search_sorted_list(sortList1,1))
print(search_sorted_list(sortList1,9))

