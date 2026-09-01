    """
    Sorterar en lista med Quick sort (dela-och-härska).
    Väljer ett pivotelement, delar upp listan i element mindre
    respektive större än pivoten, och sorterar delarna rekursivt.

    Tidskomplexitet:
        Bästa/snitt fall: O(n log n)
        Värsta fall:      O(n^2)  (t.ex. vid dåligt pivotval på
                                   redan sorterad/nästan sorterad data)
"""

def quick_sort(arr):
    a = arr[:]
    _quick_sort(a, 0, len(a) - 1)
    return a


def _quick_sort(a, low, high):
    if low < high:
        pivot_index = _partition(a, low, high)
        _quick_sort(a, low, pivot_index - 1)
        _quick_sort(a, pivot_index + 1, high)


def _partition(a, low, high):
    pivot = a[high]  # välj sista elementet som pivot
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1