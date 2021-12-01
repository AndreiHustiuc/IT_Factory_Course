# Assign the first element of the list to answer_1 on line 2

lst=[11, 100, 99, 1000, 999]
answer_1=lst[0]
print(answer_1)

#=====================================
#This time print the second element of the list directly on line 3. You should get 100.

lst=[11, 100, 101, 999, 1001]
print(lst[1])

#======================================
#Print the last element of the list through variable answer_1.

lst=[11, 100, 101, 999, 1001]
#Type your answer here.

answer_1=lst[-1]
print(answer_1)

#=====================================
#On line 3, add the string "pajamas" to the list with .append() method.

gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.

gift_list.append('pajamas')
print(gift_list)

#=====================================
#On line 3, this time add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list.

gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.

gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)

#======================================
#On line 3, this time insert "slippers" to index 3 of gift_list.

gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.

gift_list.insert(0, 'slippers')
print(gift_list)

#=======================================
#With .index() method you can learn the index number of an item inside your list. Assign the index no of 8679 to the variable answer_1.

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.

answer_1=lst.index(8679)
print(answer_1)

#=========================================
#Using .append() method, add a new list to the end of the list which contains strings: "Navigator" and "Suburban".

lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
#  Type your code here.

lst.append(['Navigator', 'Suburban'])
print(lst)

#=========================================
#Using .remove() method, clear the last element of the list.

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.

lst.remove(99)
print(lst)

#========================================
#Using .reverse() method, reverse the list.

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.

lst.reverse()
print(lst)

