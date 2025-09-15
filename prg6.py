def quick_sort(arr):
    # Base case: if array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    # Step 1: Choose a pivot (here we take the last element)
    pivot = arr[-1]
    # Step 2: Partition the array into two halves
    left = [x for x in arr[:-1] if x <= pivot]   # elements <= pivot
    right = [x for x in arr[:-1] if x > pivot]   # elements > pivot
    # Step 3: Recursively sort left and right, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)
if __name__ == "__main__":
    # Take input from user
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    print("\nOriginal Array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted Array (Ascending Order):", sorted_arr)