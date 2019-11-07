import time
from exercise05 import bubble_sort
from sorts import insertion_sort, insert, selection_sort
from typing import Callable, List, Any

def sorts(find_func: Callable[[List[float]], Any],
    lst: List[float]) -> float:
    """Return how many seconds find_func(lst) took to execute.
    """
    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

if __name__ == '__main__':
    # Gather the sea level pressures
    sea_levels = []
    sea_levels_file = open('../chapter-12/sea_levels.txt', 'r')
    for line in sea_levels_file:
        sea_levels.append(float(line))
    sea_levels_file.close()
    # Time each of the approaches
    bubble_sort_time = sorts(bubble_sort, sea_levels)
    selection_sort_time = sorts(selection_sort, sea_levels)
    insertion_sort_time = sorts(insertion_sort, sea_levels)
    print('"Bubble sort" took {:.2f}ms.'.format(bubble_sort_time))
    print('"Selection sort" took {:.2f}ms.'.format(selection_sort_time))
    print('"Insertion sort" took {:.2f}ms.'.format(insertion_sort_time))

    '''
    "Bubble sort" took 647.20ms.
    "Selection sort" took 193.79ms.
    "Insertion sort" took 3.56ms.
    '''