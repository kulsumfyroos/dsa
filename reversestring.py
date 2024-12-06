def reverse(s):
    words=s.split()
    reverse=words[::-1]
    result=' '.join(reverse)
    return result
s="hello my name is kulsum"
output=reverse(s)
print(output)