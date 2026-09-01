# manual test harness 
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.python_sorting import python_sort


sizes = [100, 1000, 10000]
content_types = ["random_0_100", "random_0_10000", "sorted"]
algorithms = {
    "bubble_sort": bubble_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
    "python_sort": python_sort
}



