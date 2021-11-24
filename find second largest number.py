x=[46,89,76,32,87,238,900,211]
max1=0
max2=0
for i in x:
    if max1<i:
        max1=i
for j in x:
    if max2<j:
        if max1!=j:
            max2=j
print(max2)

