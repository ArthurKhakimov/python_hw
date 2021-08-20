#!/usr/bin/env python3
def letters_range(start, stop, step=1):
    abc=list(map(chr, range(97, 123)))
    return abc[abc.index(start):abc.index(stop):step]

if __name__ == "__main__":
    print(letters_range('p', 'g',-2))
