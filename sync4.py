x=int(input("Enter the number"))
y=int(input("Enter the number"))

if(x%2==0 and y%2==0):
    print(f"{x,y}both are even numbers")
elif(x%2!=0 and y%2!=0):
    print(f"{x,y}both are odd numbers")
else:
    print(f"{x,y}one is odd another one is even")
