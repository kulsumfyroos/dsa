import java.util.Scanner;

public class LargestElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input array size
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter array elements:");

        // Input array elements
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Find the largest element
        int largest = arr[0]; // Assume the first element is the largest
        for (int i = 1; i < n; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }

        // Output the largest element
        System.out.println("The largest element is: " + largest);
    }
}


python:

Input the array from the user
arr = list(map(int, input("Enter array elements (space-separated): ").split()))

# Initialize the largest element with the first element of the array
largest = arr[0]

# Iterate through the array to find the largest element
for num in arr:
    if num > largest:
        largest = num

# Print the largest element
print("The largest element is:", largest)
