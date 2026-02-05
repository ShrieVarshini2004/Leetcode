def min_balanced_subarrays(arr):
    if not arr:
        return 0

    count = 1
    current_min = arr[-1]

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < current_min:
            count += 1
            current_min = arr[i]

    return count
print(min_balanced_subarrays([4,3,2,5,1])) #1
print(min_balanced_subarrays([1,2,3,4]))  # → 4
print(min_balanced_subarrays([5,4,3,2]))  # → 1
print(min_balanced_subarrays([6,2,5,1,4,3]))  # → 2