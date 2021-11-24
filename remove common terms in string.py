wrd1="Hai how good are u?"
wrd2="Hai I'm Good"
a=set(wrd1.split())
b=set(wrd2.split())
samewrd=a.intersection(b)
def remove(x):
     lst=[]
     for i in x.split():
         if i not in samewrd:
             lst.append(i)
     return (" ".join(lst))
print(remove(wrd1))
print(remove(wrd2))

#find common word

wrd1="Hai how good are u?"
wrd2="Hai I'm Good"
lst=[]
for i in wrd1.split():
    if i in wrd2.split():
        lst.append(i)
print(" ".join(lst))


