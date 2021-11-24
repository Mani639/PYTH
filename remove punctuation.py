
punct=""".!,@#$%^&*()*"""
x="Hellow!,Mani@#"
no_punct=""
for i in x:
    if i not in punct:
        no_punct=no_punct+i
print(no_punct)


