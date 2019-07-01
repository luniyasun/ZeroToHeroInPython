#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
