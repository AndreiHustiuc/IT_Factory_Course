#Slice the word until first "a". (Tosc)

wrd="Toscana"
#Type your answer here.

ans_1=wrd[0:wrd.index('a')]
print(ans_1)

#=========================
#Slice the word so that you get "cana".

wrd="Toscana"
#Type your answer here.

ans_1=wrd[wrd.index('c'): wrd.index('a')+3]
print(ans_1)

#=========================
#Now try to get "can" only.

wrd="Toscana"
#Type your answer here.

ans_1=wrd[3:-1]
print(ans_1)