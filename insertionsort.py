n=int(input("enter the size:"))
arr=[]
print("enter array elements")
for i in range(n):
    element=int(input())
    arr.append(element)
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key

print(arr)





    #takes an element and place it in correct position