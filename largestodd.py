def largestodd(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
    return ""
        
s="489278"
result=largestodd(s)
print(result)

