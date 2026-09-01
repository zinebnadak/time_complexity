# manual test harness 
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.python_sorting import python_sort

import csv
import os
import random
import sys
import time

sizes = [100, 1000, 10000]
content_types = ["random_0_100", "random_0_10000", "sorted"]
algorithms = {
    "bubble_sort": bubble_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
    "python_sort": python_sort
}

resultat_mapp = "results"
resultat_fil = os.path.join(resultat_mapp, "benchmark_results.csv")

sys.setrecursionlimit(10000)  # prevent recursion limit issues, Python's default recursion limit at n=10000


# Skapa lista 
def generate_lists() -> dict[tuple[int, str], list[int]]:
    lists = {}

    for size in sizes:
        lists[(size, "random_0_100")] = [
            random.randint(0, 100) for _ in range(size)
        ]
        lists[(size, "random_0_10000")] = [
            random.randint(0, 10000) for _ in range(size)
        ]
        lists[(size, "sorted")] = list(range(size))

    return lists

# Tidsmätning
def time_sort(sort_func, data):
    data_copy = data[:]  # ny kpoia inte mätad.

    start = time.perf_counter()
    sort_func(data_copy)
    end = time.perf_counter()

    return end - start

# Kör alla kombinationer av algoritmer, storlekar och innehållstyper och mät tiden
def run_benchmark():
    lists = generate_lists()
    results = []

    total_runs = len(lists) * len(algorithms)
    run_count = 0

    for (size, content_type), the_list in lists.items():
        for algorithm_name, algorithm_func in algorithms.items():
            run_count += 1
            print(f"[{run_count}/{total_runs}] Running {algorithm_name} on size={size}, type={content_type}")

            duration = time_sort(algorithm_func, the_list)

            results.append({
                "algorithm": algorithm_name,
                "size": size,
                "content_type": content_type,
                "time_seconds": duration,
            })

    return results