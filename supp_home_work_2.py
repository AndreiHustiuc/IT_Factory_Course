"""
Find the longest word in a string, if there are more than one with same size, return the first one.
"""

sample_string = 'Find the longest word in a string, if there are more than one with same size, return the first one'

lst_string = sample_string.split(' ')
len_words = []

for item in lst_string:
    len_words.append(len(item))

print(lst_string[len_words.index(max(len_words))])

#using dictionary
dict_string = {}
for item in lst_string:
    dict_string.update({item: len(item)})
    
def get_key(val):
    for key, value in dict_string.items():
        if val == value:
            return key
        
print(get_key(max(dict_string.values())))