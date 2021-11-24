inp1="Interview2021@syncfusion.com"
sam=""
for i in inp1:
    if(ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        sam=sam+i
print(sam)