# list trick
#Adding Lists Together

items = ['cake', 'cookie', 'bread']
total_items = items + ['1', '1']
print(total_items)
'''output : ['cake', 'cookie', 'bread', 'biscuit', 'tartttttttttt']'''
#List Method .append()

total_items.append("new item")
print(total_items)
'''['cake', 'cookie', 'bread', 'biscuit', 'zartttttttttt', 'new item']'''
#index(): To get the index of the particular item
#count(): To count the no. of occurence of a element
#max(): To get the max of the list
#min(): To get the min of the list
print("Min " + min(total_items))
print("Max " + max(total_items))
print("Count " + str(total_items.count("1")))
print("Index " + str(total_items.index("1")))
if "cooke" in total_items:
    print("It has cookie")

#custom method
def index_in_list(a_list, index):
    print(index < len(a_list))
a_list = [0, 1, 2]
index_in_list(a_list, 1)

#sort
#sorted
#reverse

total_items.sort()
print(total_items)
total_items.reverse()
print(total_items)
lst = sorted(total_items)
print(lst)
print(total_items.reverse())

#for deletion two method is there
#del , remove
