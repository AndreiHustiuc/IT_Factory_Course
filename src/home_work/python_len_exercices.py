#Using len() function find out how many items are in the list.

lst=[11, 10, 12, 101, 99, 1000, 999]

answer_1=len(lst)
print(answer_1)

#======================
#Find out the length of the string given below.

msg="Be yourself, everyone else is taken."
#Type your code here.

msg_length=len(msg)
print(msg_length)

#=========================
#How many keys are there in the dictionary?

dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
#Type your answer here.

ans_1=len(dict)
print(ans_1)

#==============================
#Call the last element of the list by using the len() function.

gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.

index_no=len(gift_list) - 1
ans_1=gift_list[index_no]
print(ans_1)

#=================================
#Below is a nested data. Find out the length of the item: 'raincoat'. You can use reverse indexing.

gift_list=['4K drone', 'wine', 'jam', ['socks', 'pajamas', 'raincoat']]
# Type your code here.

ans_1=gift_list[-1][-1]
print(ans_1)