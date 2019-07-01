#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
