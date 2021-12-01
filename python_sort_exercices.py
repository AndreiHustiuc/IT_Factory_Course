#Sort the list in ascending order with .sort() method.

lst=[11, 100, 99, 1000, 999]

#Type your answer here.

lst.sort()
print(lst)

#==========================
#This time sort the countries in alphabetic order.

lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]

#Type your code here.

lst.sort()
print(lst)

#=============================
#Now sort the list in descending order with .sort() method.

lst=[11, 100, 101, 999, 1001]

#Type your answer here.

lst.sort(reverse=True)
print(lst)

#===============================
#Can you sort the gift list in reverse alphabetic order?

gift_list=['socks', '4K drone', 'wine', 'jam']

# Type your answer here.

gift_list.sort(reverse=True)
print(gift_list)

#===============================
#Sort the list below in reverse alphabetic order and then assign the last element to the answer_1 variable.

NFL=["Panthers", "Bears", "Dolphins" "Patriots", "Saints", "Giants"]

# Type your code here.

NFL.sort(reverse=True)
answer_1=NFL[-1]
print(answer_1)

#=========================
#Sort the cities from z to a.

muni=["Melbourne", "Shanghai", "Delhi", "Atlanta", "Moscow", "Montreal"]

# Type your code here.

muni.sort(reverse=True)
print(muni)

#=======================
#Sort the keys of the dictionary from a to z.

dict={"tiramisu":5, "chocolate":2, "pudding":3, "cheesecake":4}
#  Type your code below.

key_list=list(dict.keys())
key_list.sort()
print(key_list)