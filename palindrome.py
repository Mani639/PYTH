num=554
temp=num
const=0
while num>0:
    sam=num%10
    const=(const*10)+sam
    num=num//10
if const==temp:
    print("It is a Palindrome")
else:
    print("It is not a palindrome")
