'''
Programming assignment 1

Count the number of inversions in the given array
'''


def merge_and_count(arr):
    n = len(arr)
    if n <= 1:
        return 0, arr
    mid = n >> 1
    left_cnt, left = merge_and_count(arr[:mid])
    right_cnt, right = merge_and_count(arr[mid:])
    arr = []
    cnt = left_cnt + right_cnt
    i = j = 0
    while i < mid and j < n - mid:
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            cnt += mid - i
            j += 1
    if i < mid:
        arr.extend(left[i:])
    if j < n - mid:
        arr.extend(right[j:])
    return cnt, arr


with open('IntegerArray.txt') as f:
    arr = map(int, f)
    cnt, arr = merge_and_count(arr)
    print cnt
