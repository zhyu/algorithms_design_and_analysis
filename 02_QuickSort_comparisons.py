'''
Programming assignment 2

Count the number of comparisons in QuickSort algorithm
using strategis of picking the pivot below:
    1. first element
    2. last element
    3. median of first, middle and last elements
'''
PIVOT_FIRST = 0
PIVOT_LAST = 1
PIVOT_MEDIAN = 2


def qsort(arr, st, ed, pos):
    if st >= ed:
        return 0

    res = ed - st - 1

    if pos == 'FIRST':
        pass
    elif pos == 'LAST':
        arr[st], arr[ed-1] = arr[ed-1], arr[st]
    elif pos == 'MEDIAN':
        mid = st + res / 2
        if arr[st] < arr[mid] < arr[ed-1] or arr[ed-1] < arr[mid] < arr[st]:
            arr[st], arr[mid] = arr[mid], arr[st]
        elif arr[st] < arr[ed-1] < arr[mid] or arr[mid] < arr[ed-1] < arr[st]:
            arr[st], arr[ed-1] = arr[ed-1], arr[st]
    pivot = arr[st]

    i = st+1
    for j in xrange(st+1, ed):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[st], arr[i-1] = arr[i-1], arr[st]
    res += qsort(arr, st, i-1, pos)
    res += qsort(arr, i, ed, pos)
    return res


with open('QuickSort.txt') as f:
    raw_arr = map(int, (line for line in f))
    for pos in ('FIRST', 'LAST', 'MEDIAN'):
        arr = raw_arr[:]
        print pos, qsort(arr, 0, len(arr), pos)
