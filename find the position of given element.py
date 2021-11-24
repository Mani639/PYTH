lst=[34,78,72,65,27,68]
x=int(input("Enter the number"))
if x in lst:
    for i in range(len(lst)):
        if lst[i]==x:
            print(f"The number {x} is available in the position {i+1}")
else:
    print("The number doesn't occur")