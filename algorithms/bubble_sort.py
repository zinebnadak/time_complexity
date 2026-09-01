"""
AI fick användas till att ta fram implementationer av Bubble sort, Insertion sort, Quick sort, Merge sort och pythons sorted
"""

"""
    Sorterar en lista med Bubble sort.
    Jämför intilliggande element och byter plats om de står i fel ordning.
    Upprepas tills ingen byte behövs (optimering ger O(n) bästa fall).

    Tidskomplexitet:
        Bästa fall:  O(n)      (redan sorterad lista)
        Snitt/värsta: O(n^2)
"""

def bubble_sort(arr):
    a = arr[:]  
    n = len(a)
    for i in range(n):
        swapped = False
        # Efter varje varv "bubblar" det största kvarvarande elementet upp till sin rätta plats, så vi kan minska sökområdet med i.
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break 
    return a