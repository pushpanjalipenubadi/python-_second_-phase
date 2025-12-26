s=[1,5,10,12,10]
def check_sorted(s):
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            return False
    return True
print(check_sorted(s))    
