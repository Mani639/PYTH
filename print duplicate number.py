num=[2,4,3,5,1,2]
for i in range (len(num)):
    for j in range(i+1,len(num)):
        if(num[i]==num[j]):
            print(num[i])
