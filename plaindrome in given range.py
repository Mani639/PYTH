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