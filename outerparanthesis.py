def outer(s):
    depth=0
    result=" "

    for char in s:
        if char=='(':
            if depth>0:
                result+=char
            depth+=1
        elif char==')':
            depth-=1
            if depth>0:
                result+=char
    return result
s="(()()())"
out=outer(s)
print(out)