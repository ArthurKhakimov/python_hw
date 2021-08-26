#!/usr/bin/env python3
print([a*b*(1000-a-b) for a in range(1,1001) for b in range(a,1001) if a**2+b**2==(1000-a-b)**2][0])
