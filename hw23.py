#!/usr/bin/env python3
import copy

def n_arr(sizes_lst):
    result_lst = ["" for i in range(sizes_lst[0])]
    sizes_lst.pop(0)
    while len(sizes_lst):
        result_lst = [copy.deepcopy(result_lst) for i in range(sizes_lst[0])]
        sizes_lst.pop(0)
    return result_lst

print(n_arr([2,2,2,2]))
