#Part 1: Sequential Search Implementation: Sonam Tobgay
#Part 2: Binary Search Implementation : Chesung Dorji
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Example usage
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)
print(f"Searching for {target} using Binary Search")

# Iterative
index_iter, comps_iter = binary_search_iterative(arr, target)
print(f"Found at index {index_iter}" if index_iter != -1 else "Not found")
print(f"Number of comparisons: {comps_iter}")
 

