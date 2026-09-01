"""
    Sorterar en lista med Insertion sort.
    Bygger upp en sorterad del av listan ett element i taget genom
    att sätta in varje nytt element på rätt plats bland de redan sorterade.

    Tidskomplexitet:
        Bästa fall:  O(n)      (redan sorterad lista)
        Snitt/värsta: O(n^2)
"""

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # Flytta element som är större än key ett steg åt höger
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a