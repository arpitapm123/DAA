def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Step 1: Divide - Find the middle index
    mid = len(arr) // 2
    # Step 2: Recursively sort left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # Step 3: Merge sorted halves
    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i = j = 0
    # Compare elements from left and right, append smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
if __name__ == "__main__":
    print("Program 7: Merge Sort using Divide and Conquer\n")
    # Take input from user
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    print("\nOriginal Array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted Array (Ascending Order):", sorted_arr)