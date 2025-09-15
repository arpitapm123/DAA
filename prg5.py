# Function to find minimum and maximum using Divide and Conquer
def find_min_max(arr, low, high):
    # Case 1: Only one element
    if low == high:
        return arr[low], arr[low]
    # Case 2: Two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    # Case 3: More than two elements
    else:
        mid = (low + high) // 2
        # Divide into two halves
        min1, max1 = find_min_max(arr, low, mid)
        min2, max2 = find_min_max(arr, mid + 1, high)
        # Conquer: Combine results
        return min(min1, min2), max(max1, max2)
if __name__ == "__main__":
    # Taking input from user
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    n = len(arr)


    # Call function
    minimum, maximum = find_min_max(arr, 0, n - 1)
    # Display results
    print("\nArray:", arr)
    print("Minimum element:", minimum)
    print("Maximum element:", maximum)