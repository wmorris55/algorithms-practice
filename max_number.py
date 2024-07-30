def find_largest_number(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


find_largest_number([4, 6, 3, -5, 300])
