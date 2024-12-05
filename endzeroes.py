def move_zero(arr):
    non_zero=0
    for i in range(len(arr)):
        if arr[i]!=0:
            if non_zero!=i:
                arr[non_zero],arr[i]=arr[i],arr[non_zero]
            non_zero+=1
    return arr
n=int(input("enter the size:"))
arr1=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr1.append(element)
result=move_zero(arr1)
print(result)