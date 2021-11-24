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
print(sum+day)