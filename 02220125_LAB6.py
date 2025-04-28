# Part 1: Quick SortImplementation by Sonam Tobgay
#Part 2: Merge SortImplementation by chesung dorji


def quick_sort(arr):
    comparisons = [0]
    swaps = [0]

    def median_of_three(low, high):
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        comparisons[0] += 3
        if (a - b) * (c - a) >= 0:
            return low
        elif (b - a) * (c - b) >= 0:
            return mid
        else:
            return high

    def partition(low, high):
        pivot_index = median_of_three(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps[0] += 1

        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    original = arr.copy()
    quick_sort_recursive(0, len(arr) - 1)

    print("Original List:", original)
    print("Sorted using Quick Sort:", arr)
    print("Number of comparisons:", comparisons[0])
    print("Number of swaps:", swaps[0])

    return arr, comparisons[0], swaps[0]

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr)

