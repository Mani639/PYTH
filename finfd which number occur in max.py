"""Find which number number occur in max"""
num=[6,2,5,2,0,2,3,4,0,4,5,6,0,0,1,2,3,4,5]
d={}
for i in num:
    d[i]=num.count(i)
const=max(d.values())
for j in num:
    if const==num.count(j):
        print(j)
        break