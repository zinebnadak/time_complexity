"""
    Sorterar en lista med Merge sort (dela-och-härska).
    Listan delas rekursivt i halvor tills varje del har 1 element,
    varefter delarna slås ihop (merge) i sorterad ordning.

    Tidskomplexitet:
        Bästa/snitt/värsta fall: O(n log n)
"""

def merge_sort(arr):
    a = arr[:]
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Lägg till det som eventuellt blir kvar
    result.extend(left[i:])
    result.extend(right[j:])
    return result