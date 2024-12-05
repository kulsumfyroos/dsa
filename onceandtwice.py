def find(arr1):
    xor_result=0
    for num in arr1:
        xor_result^=num
    set_bit=xor_result & -xor_result
    num1=0
    num2=0
    for num in arr1:
        if num & set_bit:
            num1^=num
        else:
            num2^=num
    return num1,num2
n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
num1,num2=find(arr)
print(num1,num2)