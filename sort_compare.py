import random
import time


def insertion_sort(a_list):
    copied_list = a_list[:]

    start_time = time.perf_counter()

    for index in range(1, len(copied_list)):
        current_value = copied_list[index]
        position = index

        while position > 0 and copied_list[position - 1] > current_value:
            copied_list[position] = copied_list[position - 1]
            position = position - 1

        copied_list[position] = current_value

    end_time = time.perf_counter()
    return copied_list, end_time - start_time


def shell_sort(a_list):
    copied_list = a_list[:]

    start_time = time.perf_counter()

    sublist_count = len(copied_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(copied_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.perf_counter()
    return copied_list, end_time - start_time


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    copied_list = a_list[:]

    start_time = time.perf_counter()
    copied_list.sort()
    end_time = time.perf_counter()

    return copied_list, end_time - start_time


def average_sort_time(sort_function, size, runs=100):
    total_time = 0

    for _ in range(runs):
        numbers = [random.randint(1, 100000) for _ in range(size)]
        sorted_list, elapsed = sort_function(numbers)
        total_time += elapsed

    return total_time / runs


def main():
    sizes = [500, 1000, 5000]

    for size in sizes:
        print(f"\nList size: {size}")

        insertion_time = average_sort_time(insertion_sort, size)
        shell_time = average_sort_time(shell_sort, size)
        python_time = average_sort_time(python_sort, size)

        print(f"Insertion Sort took {insertion_time:10.7f} seconds to run, on average")
        print(f"Shell Sort took {shell_time:10.7f} seconds to run, on average")
        print(f"Python Sort took {python_time:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()