def ap(a,d,n):
    sum=(n/2)*(2*a+(n-1)*d)
    return sum

a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

sum_ap = ap(a, d, n)
print(f"The sum of the A.P. series is: {sum}")