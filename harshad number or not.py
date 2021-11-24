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

