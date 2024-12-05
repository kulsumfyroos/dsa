def consecutive(arr1):
    max_count=0
    current=0
    for num in arr1:
        if num==1:
            current+=1
            max_count=max(max_count,current)
        else:
            current=0
    return max_count
n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
result=consecutive(arr)
print(result)
