import random
from matplotlib import pyplot as pl
from sorting_algorithms import SortingAlgorithms

def main():
    sorter = SortingAlgorithms()
    
    array_list = [[random.randint(1,100) for _ in range(100)] for _ in range(10)]

    bubble_times = []
    bubble_times.append(calculate_sort_time(bubble_times, sorter.bubble_sort, sorter.get_time, array_list))

    selection_times = []
    selection_times.append(calculate_sort_time(selection_times, sorter.selection_sort, sorter.get_time, array_list))

    insertion_times = []
    insertion_times.append(calculate_sort_time(insertion_times, sorter.insertion_sort, sorter.get_time, array_list))

    merge_times = []
    merge_times.append(calculate_sort_time(merge_times, sorter.merge_sort, sorter.get_time, array_list))

    quick_times = []
    quick_times.append(calculate_sort_time(quick_times, sorter.quick_sort, sorter.get_time, array_list))






def calculate_sort_time(time_arr, sort_func, get_time_func, arrays_list):
    for i in range(len(arrays_list)):
        curr_arr = arrays_list[i]
        sort_func(curr_arr)
        time_arr.append(get_time_func())
    
    return time_arr

if __name__ == "__main__":
    main()



