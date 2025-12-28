#remove duplicate characters
s="pushpa"
res=""
for char in s:
    if char not in res:
        res=res+char
        print(res)
