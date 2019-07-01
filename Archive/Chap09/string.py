#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()
