name="The Indian Standard Time(IST)"
up=0
lo=0
for i in name:
    if i.isupper():
        up=up+1
    if i.islower():
        lo=lo+1
print(f"The number of UpperCase is {up} ")
print(f"The number of LowerCase is {lo} ")

