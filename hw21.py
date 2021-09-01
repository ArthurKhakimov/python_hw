#!/usr/bin/env python3
def merge(a, b):
    def stop_iteration_trap(i):
        try:
            result = next(i)
        except StopIteration:
            result = "Stop"
        return result

    iter_a = stop_iteration_trap(a)
    iter_b = stop_iteration_trap(b)
    while iter_a != "Stop" or iter_b != "Stop":
        if iter_a != "Stop" and iter_b != "Stop":
            if iter_a >= iter_b:
                yield iter_b
                iter_b = stop_iteration_trap(b)
            elif iter_a < iter_b:
                yield iter_a
                iter_a = stop_iteration_trap(a)
        elif iter_a != "Stop" and iter_b == "Stop":
            while iter_a != "Stop":
                yield iter_a
                iter_a = stop_iteration_trap(a)
        elif iter_b != "Stop" and iter_a == "Stop":
            while iter_b != "Stop":
                yield iter_b
                iter_b = stop_iteration_trap(b)

#print(list(x for x in range(1,4)), list(x for x in range(1,10)))
#print(list(merge((x for x in range(-1,4)),(x for x in range(1,10)))))
