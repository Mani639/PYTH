x=[7,5,3,6,9,2]
min=x[0]
max=x[0]
for i in range(len(x)):
    if min>x[i]:
        min=x[i]
    elif max<x[i]:
        max=x[i]
print(min)
print(max)