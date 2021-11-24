num=int(input("Enter the number"))
const=0
while num>0:
    sam=num%10
    const=(const*10)+sam
    num=num//10
print(const)