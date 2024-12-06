def rotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    s2_concat=s2+s2
    return s1 in s2_concat

s1="hello"
s2="olleh"
print(rotation(s1,s2))