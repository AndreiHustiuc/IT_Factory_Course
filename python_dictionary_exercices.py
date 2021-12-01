#When was Plato born?
dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

#Type your answer below.
answer_1=dict["born"]
print(answer_1)

#========================
#Change Plato's birth year from B.C. 427 to B.C. 428.

dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

#Type your answer below.

dict["born"] = -428
print(dict["born"])

#==============================
#Try to add the key "work" to dict with values shown below.
#"work": ["Apology", "Phaedo", "Republic", "Symposium"]

dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

#Type your answer below.
dict['work'] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)

#===================================
#Add 2 inches to the son's height.

dict={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

#Type your answer below.
dict.update({"son's height": dict["son's height"] + 2})
print(dict)

#================================
#Using .items() method generate a list of tuples consisted of each key value pair.

dict={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

#Type your answer below.
ans_1=dict.items()
print(ans_1)

#==============================
#Using .get() method print the value of "son's eyes".

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Type your answer inside the print.
ans_1=dict.get("son's eye color")
print (ans_1)

#================================
#Try to look for key: "son's age" and if nothing comes up make the .get() return "2".

dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Type your answer here.
ans_1=dict.get("son's age", '2')
print(ans_1)

#==========================
#Clear method to remove everything from a dictionary

dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#clear the dictionary here then print it.
dict.clear()
print(dict)

#=========================
#Using len function, find how many keys there are in the dictionary.

dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Write your answer here.
ans_1=len(dict)
print(ans_1)

#============================
#What's the key with the highest value in the dictionary?

dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Write your answer here.
ans_1=max(dict)
print(ans_1)

#=======================
#What's the key with the lowest value in the dictionary?

dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Write your answer here.
ans_1=min(dict)
print(ans_1)

