s=[1,2,3,2,1]
def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return "not a palindrome"
        i+=1
        j-=1
        return "palindrome"
print(palindrome(s))
