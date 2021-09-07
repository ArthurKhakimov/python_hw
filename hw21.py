#!/usr/bin/env python3
# Понял свою ошибку, теперь по окончании генератора функция проверки будет возвращать None.

def merge(a, b):
    def stop_iteration_trap(i):
        try:
            result = next(i)
        except StopIteration:
            result = None
        return result

    iter_a = stop_iteration_trap(a)
    iter_b = stop_iteration_trap(b)
    while iter_a != None or iter_b != None:
        if iter_a != None and iter_b != None:
            if iter_a >= iter_b:
                yield iter_b
                iter_b = stop_iteration_trap(b)
            elif iter_a < iter_b:
                yield iter_a
                iter_a = stop_iteration_trap(a)
        elif iter_a != None and iter_b == None:
            while iter_a != None:
                yield iter_a
                iter_a = stop_iteration_trap(a)
        elif iter_b != None and iter_a == None:
            while iter_b != None:
                yield iter_b
                iter_b = stop_iteration_trap(b)

#print(list(x for x in range(1,4)), list(x for x in range(1,10)))
#print(list(merge((x for x in range(1,4)),(x for x in range(1,10)))))
