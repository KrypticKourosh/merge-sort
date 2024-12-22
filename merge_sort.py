def merge(left_half, right_half): #helper method
    left_len = len(left_half)
    right_len = len(right_half)
    merged = []
    l, r = 0, 0

    while l < left_len and r < right_len:
        if left_half[l] < right_half[r]:
            merged.append(left_half[l])
            l += 1
        else:
            merged.append(right_half[r])
            r += 1
    merged.extend(left_half[l:])
    merged.extend(right_half[r:])

    return merged

def merge_sort(array):
    if len(array) <= 1: #base case
        return  array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)
