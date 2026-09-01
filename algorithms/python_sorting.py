"""
    Sorterar en lista med Pythons inbyggda sorted().
    (används av algoritmen Timsort, hybrid mellan Merge sort och
    Insertion sort.) Den identifierar redan sorterade delsekvenser
    ("runs") i indatan.

    Tidskomplexitet:
        Bästa fall:  O(n)        (redan sorterad lista)
        Snitt/värsta: O(n log n)
    """

def python_sort(arr):
    return sorted(arr)