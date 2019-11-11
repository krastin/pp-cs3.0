import time

from sample01 import linear_search_while
from sample01 import linear_search_for
from sample01 import linear_search_sentinel
from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
    """Time how long it takes to run function search to find
    value v in list L.
    """
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

def print_times(v: Any, L: list) -> None:
    """Print the number of milliseconds it takes for linear_search(v, L)
    to run for list.index, the while loop linear search, the for loop
    linear search, and sentinel search.
    """
    # Get list.index's running time.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0
    # Get the other three running times.
    while_time = time_it(linear_search_while, L, v)
    for_time = time_it(linear_search_for, L, v)
    sentinel_time = time_it(linear_search_sentinel, L, v)
    print("{0}\t\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(
    v, while_time, for_time, sentinel_time, index_time))

L = list(range(10000001)) # A list with just over ten million values
print_times(10, L) # How fast is it to search near the beginning?
print_times(5000000, L) # How fast is it to search near the middle?
print_times(10000000, L) # How fast is it to search near the end?