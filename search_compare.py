import random
import time


def sequential_search(a_list, item):
    start_time = time.perf_counter()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end_time = time.perf_counter()
    return found, end_time - start_time


def ordered_sequential_search(a_list, item):
    start_time = time.perf_counter()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    end_time = time.perf_counter()
    return found, end_time - start_time


def binary_search_iterative(a_list, item):
    start_time = time.perf_counter()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.perf_counter()
    return found, end_time - start_time


def binary_search_recursive(a_list, item):
    start_time = time.perf_counter()
    found = binary_search_recursive_helper(a_list, item)
    end_time = time.perf_counter()
    return found, end_time - start_time


def binary_search_recursive_helper(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2

        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive_helper(a_list[:midpoint], item)
            else:
                return binary_search_recursive_helper(a_list[midpoint + 1:], item)


def average_search_time(search_function, size, runs=100):
    total_time = 0

    for _ in range(runs):
        numbers = [random.randint(1, 100000) for _ in range(size)]

        # only sort for the algorithms that need ordered input
        if search_function in (
            ordered_sequential_search,
            binary_search_iterative,
            binary_search_recursive,
        ):
            numbers.sort()

        result, elapsed = search_function(numbers, 99999999)
        total_time += elapsed

    return total_time / runs


def main():
    sizes = [500, 1000, 5000]

    for size in sizes:
        print(f"\nList size: {size}")

        seq_time = average_search_time(sequential_search, size)
        ordered_seq_time = average_search_time(ordered_sequential_search, size)
        bin_iter_time = average_search_time(binary_search_iterative, size)
        bin_rec_time = average_search_time(binary_search_recursive, size)

        print(f"Sequential Search took {seq_time:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ordered_seq_time:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {bin_iter_time:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {bin_rec_time:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()