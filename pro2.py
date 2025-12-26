s=[1,5,7,10,-1]
largest=0
smallest=0
for num in s:
    if num >largest:
        largest=num
        if num < smallest:
            smallest=num
print(largest,smallest)
