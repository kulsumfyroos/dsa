def sum_of_gp(a, r, n):
    """
    Calculate the sum of a G.P. series.

    Parameters:
    a (float): The first term of the G.P.
    r (float): The common ratio of the G.P.
    n (int): The number of terms in the G.P.

    Returns:
    float: The sum of the G.P. series.
    """
    if r == 1:
        # If the common ratio is 1, the G.P. becomes an A.P. where all terms are the same.
        return a * n
    else:
        # Formula for the sum of n terms of a G.P.: S = a * (1 - r^n) / (1 - r)
        return a * (1 - r ** n) / (1 - r)

# Example usage:
a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

sum_gp = sum_of_gp(a, r, n)
print(f"The sum of the G.P. series is: {sum_gp}")
