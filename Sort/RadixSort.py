def bucketSortID(arr, digit):
    count = [0] * 10 
    output = [None] * len(arr)

    for obj in arr: 
        index = (obj.id // digit) % 10
        count[index] += 1

    for i in range(1, 10): 
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0: 
        index = (arr[i].id // digit) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)): 
        arr[i] = output[i]


def radixSortID(arr):
    maxElement = max(obj.id for obj in arr)
    digit = 1

    while maxElement // digit > 0: 
        bucketSortID(arr, digit)
        digit *= 10
    


