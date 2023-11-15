def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid].id == target:
            return arr[mid]
        elif arr[mid].id < target:
            low = mid + 1
        else:
            high = mid - 1  

    return None  
