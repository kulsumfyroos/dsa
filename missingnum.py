def missing(arr1):
    n=len(arr1)+1
    sum_exp=n*(n+1)//2
    sum_act=sum(arr1)
    return sum_exp-sum_act
n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
result=missing(arr)
print(result)