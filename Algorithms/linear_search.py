# Linear Search Algorithm


def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target element.

    Parameters:
    - arr (list): The list to search through.
    - target: The element to search for.

    Returns:
    - int: The index of the target element if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage:
arr = [4, 2, 7, 1, 9, 5]
target = 1
result_index = linear_search(arr, target)
if result_index != -1:
    print(f"Element {target} found at index {result_index}.")
else:
    print(f"Element {target} not found in the array.")
