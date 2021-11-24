name="WeLcome"
for i in name:
    if (ord(i)<90):
        print(chr(ord(i)+32),end="")
    elif((ord(i)>97)):
        print(chr(ord(i)-32),end="")