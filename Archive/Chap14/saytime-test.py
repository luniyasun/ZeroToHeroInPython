#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import saytime

def main():
    st = saytime.saytime()
    print('\nnumbers test:')
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30, 
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000 
    )
    for l in list:
        st.number(l)
        print(l, st.numwords())

    print('\ntime test:')
    list = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list:
        st.time(*l)
        print(st.digits(), st.words())
    
    st.time_t() # set time to now
    print('\nlocal time is ' + st.words())

if __name__ == '__main__': main()
