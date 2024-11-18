import timeit
import random
from typing import List


def measure_execution_time(func, input_size):
    test_data = [random.randint(0, input_size) for _ in range(input_size)]
    start_time = timeit.default_timer()
    func(test_data)
    end_time = timeit.default_timer()
    return end_time - start_time


def infer_time_complexity(exec_times, input_sizes):
    ratios = []
    for i in range(1, len(exec_times)):
        time_increase = exec_times[i] / exec_times[i-1]
        size_increase = input_sizes[i] / input_sizes[i-1]
        ratio = time_increase / size_increase
        ratios.append(ratio)

    # Heuristic to determine time complexity
    if all(ratio < 2 for ratio in ratios):
        return "O(N) - Linear"
    elif all(2 <= ratio < (input_sizes[i] / input_sizes[i - 1]) ** 2 for i, ratio in enumerate(ratios, start=1)):
        return "O(N^2) - Quadratic"
    elif all(ratio < 1.5 for ratio in ratios):  # Assuming very slow increase for logarithmic
        return "O(log N) - Logarithmic"
    elif all(1 < ratio < 2 for ratio in ratios):  # Assuming moderate increase for linearithmic
        return "O(N log N) - Linearithmic"
    else:
        return "Other - Could be exponential or unknown"


# Create generic functions to measure time complexity of any function passed as argument
def calc_time_complexity(func, input_sizes: List[int] = (100, 1000, 10000, 100000)):
    exec_times = [measure_execution_time(func, size) for size in input_sizes]
    complexity = infer_time_complexity(exec_times, input_sizes)
    print(f"`{func.__name__}` has `{complexity}` Time Complexity.")
    return complexity
