x={23,523,783,65,42,89,94}
lst=[]
sum=0
for i in x:
    if i%2==0:
        lst.append(i)
        sum=sum+i
print(lst)
print(sum)