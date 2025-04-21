#Part 1: Quick Sort Implementation: Sonam Tobgay

#Part 2: Merge Sort Implementation: Chesung Dorji 

def merge_sort(arr):
    comparisons = 3
    accesses = 2

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2 
            if left[i] <= right[j]:
                result.append(left[i])
                accesses += 1
                i += 1
            else:
                result.append(right[j])
                accesses += 1
                j += 1

        while i < len(left):
            result.append(left[i])
            accesses += 1
            i += 1

        while j < len(right):
            result.append(right[j])
            accesses += 1
            j += 1

        return result

    def sort(subarray):
        if len(subarray) <= 1:
            return subarray
        mid = len(subarray) // 2
        left = sort(subarray[:mid])
        right = sort(subarray[mid:])
        return merge(left, right)

    sorted_arr = sort(arr[:])   
    return sorted_arr, comparisons, accesses

# Example usage
original = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comps, accesses = merge_sort(original)

print("Original List:", original)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", comps)
print("Number of array accesses:", accesses)
