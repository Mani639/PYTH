"""Count occurance of each character in a string"""

name="testleaf"
dic={}
for i in name:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)




"""Palindrome in given range"""
num1=int(input("Enter the start range"))
num2=int(input("Enter the end range"))
for i in range (num1,num2+1):
    temp=i
    const=0
    while i>0:
        sam=i%10
        const=(const*10)+sam
        i=i//10
    if(const==temp):
        print(const)


""""Camelcase to normal case"""


name="SyncfusionSoftware"
output=""
for i in name[1:]:
    if(65<=ord(i) and 90>=ord(i)):
        output=output+" "+i
    else:
        output=output+i
print(name[0]+output)

"""Harshad number"""


r1=int(input("Enter the number"))
r2=int(input("Enter the number"))
for i in range (r1,r2+1):
    const=0
    temp=i
    while i>0:
        digit=i%10
        const=const+digit
        i=i//10
    if temp%const==0:
        print(temp)

"""Days calculation"""


month=int(input("Enter the month"))
day=int(input("Enter the day"))
sum=0
for i in range(1,month+1):
    if (i%2!=0 and i<=7) or (i%2==0 and i>=8):
        sum=sum+31
    elif i==2:
        sum=sum+28
    elif (i%2==0 and i<=7) or (i%2!=0 and i>=8):
        sum=sum+30
print(sum+day)"

