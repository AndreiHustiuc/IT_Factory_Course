#Pop the last item of the list below.

lst=[11, 100, 99, 1000, 999]

#Type your answer here.

popped_item=lst.pop(len(lst)-1)
 
print(popped_item)
print(lst)

#=======================
#Remove "broccoli" from the list using .pop and .index methods.

lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]

#Type your code here.

item=lst.pop(lst.index('broccoli'))
print(lst, item)

#=========================
#Save Italy's GDP in a separate variable and remove it from the dictionary.

GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}

#Type your answer here.

italy_gdp=GDP_2018.get('Italy')
GDP_2018.pop('Italy')

print(GDP_2018)
print(italy_gdp, "trillion USD")