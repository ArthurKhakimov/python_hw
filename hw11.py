#!/usr/bin/env python3
def letters_range(start, stop, step=1):
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return abc[abc.index(start):abc.index(stop):step]

if __name__ == "__main__":
    print(letters_range('p', 'g',-2))
