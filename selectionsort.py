n=int(input("enter the size:"))
arr=[]
print("enter array elements")
for i in range(n):
    element=int(input())
    arr.append(element)
for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr)

#select minimum and swap