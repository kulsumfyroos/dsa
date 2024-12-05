def linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

n=int(input("enter the size:"))
arr1=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr1.append(element)
target=int(input("enter target"))
result=linear(arr1,target)
if result!=-1:
    print("found")
else:
    print("not found")