#!/usr/bin/env python3
import functools as f;print(f.reduce(lambda x,y:x*y,[int(("".join([str(i) for i in range(1,200000)]))[j]) for j in range(1000000) if j in (0,9,99,999,9999,99999,999999)]))
