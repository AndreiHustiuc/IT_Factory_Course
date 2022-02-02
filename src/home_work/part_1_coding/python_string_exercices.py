#Assign the string below to the variable in the exercise.
#Type your answer here.

str="It's always darkest before dawn."
print(str)

#==================================
#By using first, second and last characters of the string, create a new string.

str="It's always darkest before dawn."

#Type your answer here.

ans_1=str[0] + str[1] + str[-1]
print(ans_1)

#===============================
#Replace the (.) with (!)

str="It's always darkest before dawn."

#Type your code here.

str = str.replace('.', '!')
print(str)

#===============================
#Reassign str so that, all its characters are lowercase.

str="EVERY Strike Brings Me Closer to the Next Home run."
# Type your code here.

str = str.lower()
print(str)

#=========================
#Now make everything uppercase.

str="don't stop me now."
# Type your code here.

str = str.upper()
print(str)

#========================
#Make the string so that everything is properly and first letter is capital with one function.

str="there are no traffic JamS Along The extra mile."

#Type your answer here.

str = str.capitalize()
print(str)

#=======================
#Does the string start with an A?
#Assign a boolean answer to the ans_1 variable.

str="There are no traffic jams along the extra mile."
#  Type your code here.

ans_1=str[0] == 'A'
print(ans_1)

#============================
#Does it end with a fullstop (.) ?

str="There are no traffic jams along the extra mile."
#  Type your code here.

ans_1=str[-1] == '.'
print(ans_1)

#===========================
#Using .index() method, identify the index of character: (v).

str="The best revenge is massive success."

#  Type your code here.

ans_1=str.index('v')
print(ans_1)

#=========================
#Using .find() method, identify the index of character: (m).

str="The best revenge is massive success."

#  Type your code here.

ans_1=str.find('m')
print(ans_1)

#==================================
#Try to see what results you get looking for character: (X). First with .find() method and then with .index() method.

str="The best revenge is massive success."

#  Type your code here.

ans_1=str.find('e')
ans_2 = str.index('e')

print(ans_1)
print(ans_2)

#===============================
#Which character occur more often in the string? "a" or "o" ? Print both counts inside the print function.

str="People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."
#  Type your code here.

ans_1=str.count('a')
ans_2=str.count('o')

print("count of a is: ", ans_1, " count of o is: ", ans_2)

#========================
#Print the types of two given variables with the print function.

v_1="1"
v_2=1

#  Type your code on line 4:

ans_1=type(v_1)
ans_2=type(v_2)

print(ans_1)
print(ans_2)

#===========================
#What is the length of the given string?

str="1.975.000"

#  Type your code here:

ans_1=len(str)
print(ans_1)