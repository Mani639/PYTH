num=int(input("enter the number"))
lst=[]
for i in range(1,num+1):
      if num%i==0:
          lst.append(i)
print(lst)
x=max(lst)
print(x)
