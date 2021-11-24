"""num=int(input("Enter the number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)"""

num=int(input("Enter the number"))
if(num<0):
    print("Please enter positive numbers")
else:
    sum=0
    while(num>0):
        sum=sum+num
        num=num-1
    print(sum)