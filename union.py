def union(arr1,arr2):
    return list(set(arr1)|set(arr2))
n=int(input("enter the size:"))
arr1=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr1.append(element)
n=int(input("enter the size:"))
arr2=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr2.append(element)
result=union(arr1,arr2)
print(result)