n=int(input("enter the size:"))
arr=[]
print("enter array elements")
for i in range(n):
    element=int(input())
    arr.append(element)
for i in range(n-1,0,-1):
    for j in range(0,i,1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
#compare 2 elements and swap