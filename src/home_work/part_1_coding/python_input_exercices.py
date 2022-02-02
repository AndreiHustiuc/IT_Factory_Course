#Using input() function ask for user's name.

#Type your answer here.

ans_1=input('Enter a user name: ')
print("Hello!, " + ans_1)

#=====================
#This time ask the user a numerical question, such as, "Please enter your age." See what type of data input() returns.

#Type your code here.
ans_1=input('Please enter you age: ')

print(type(ans_1))

#===========================
#Using input() function, print() function and another function you may need; ask for the current year, then print the answer +50.

current_year = int(input('Enter please the current year: '))
answer = current_year + 50
print(answer)

#==============================
#Create a converter that will ask for amount of days and convert it to years, then print it.

days = int(input('How many days would you like to convert in a years?: '))
result = days / 365
print(f"The {days} days are {result} years")

#=================================
#Let's create the same converter this time with float() function instead of int().
days = float(input('How many days would you like to convert in a years?: '))
result = days / 365
print(f"The {days} days are {result} years")

#===============================
#Can you create a converter that converts miles to kms?

miles = int(input('How many miles do you want to convers in km?: '))
result = miles * 1.609
print(f'{miles} miles are {result} km')


