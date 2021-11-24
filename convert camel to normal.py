name="SyncfusionSoftware"
output=""
for i in name[1:]:
    if(65<=ord(i) and 90>=ord(i)):
        output=output+" "+i
    else:
        output=output+i
print(name[0]+output)
