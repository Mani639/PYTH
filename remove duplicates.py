num=[4,5,6,3,4,2,1,2]
lst=[]
for i in num:
    if i not in lst:
        lst.append(i)
print(lst)