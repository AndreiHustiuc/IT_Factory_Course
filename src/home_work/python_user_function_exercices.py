#Define a function named f_1 which will print "Hello World!"

def f_1():
    print('Hello World!')
    
#=================
#Now define the same function f_1 and assign it to variable ans_1. See what happens.

def f_1():
    print("Hello World!")

ans_1=f_1()
print(ans_1)

#============================
#Now define the same f_1 function this time so that it returns a value instead of just printing it..

def f_1():
    return True

ans_1=f_1()
print(ans_1)

#=========================
#Now create a function named f_1 which both prints and returns "Hello World!"

def f_1():
    print('Hello World!')
    return "Hello World!"

ans_1=f_1()
print(ans_1)

#=========================
#Create a function named f_1 which always returns the number: 100 .

def f_1(m):
    return 100

print(f_1(999))

#==========================
#Create a function named f_1 which takes an integer as input and then returns it.

def f_1(num):
    return num

print(f_1(44))

#=========================
#Can you define a function that takes a list as input and returns the reverse of that list?

def reverse_list(array):
    array.sort(reverse=True)
    return array

lst=[100,200,300,400,500]
print(reverse_list(lst))

#==============================
#Write a function named f_1 which will ask user for their name and print Hello!, Name


def f_1():
    name = input('Enter your name: ')
    print('Hello! ', name)
    
f_1()

#===========================================
#Write 2 functions named f_1 and f_2. First one takes a number as input and returns that number +5, second function takes a number as input and returns first function's result multiplied by 2.

def f_1(num):
    return num + 5

def f_2(num):
    return f_1(num) * 2

print(f_2(4))

