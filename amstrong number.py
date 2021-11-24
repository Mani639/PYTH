x=153
temp=x
num=str(x)
y=len(num)
const=0
while x>0:
    sam=x%10
    const=const+(sam**y)
    x=x//10
if(const==temp):
    print("It is a amstrong number")
else:
    print("It is not a amstrong number")

