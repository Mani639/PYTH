name="Manigandan"
vowels=["a","e","i","o","u"]
new=""
for i in name:
    if i not in vowels:
        new=new+i
print(new)