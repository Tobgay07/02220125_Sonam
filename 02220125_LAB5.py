#Part 1: Sequential Search Implementation By Sonam Tobgay
#Part 2: Binary Search Implementation by Choesung Dorji


def sequential_search(arr, target):
    comparisons = 0  
    
    for index, value in enumerate(arr):
        comparisons += 1  
        if value == target:
            return index, comparisons  # Return the index and number of comparisons if found
    
    return -1, comparisons  # Return -1 and the number of comparisons if not found

# Example usage
if __name__ == "__main__":
    my_list = [23, 45, 12, 67, 89, 34, 56]
    target_value = 67
    
    print(f"List: {my_list}")
    print(f"Searching for {target_value} using Sequential Search")
    
    index, num_comparisons = sequential_search(my_list, target_value)
    
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")
    
    print(f"Number of comparisons: {num_comparisons}")