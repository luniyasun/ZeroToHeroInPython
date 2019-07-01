#!/usr/bin/env python3
#
# jurl.py by Bill Weinman <http://bw.org/contact/>
# Jump to URL (a private short URL service)
# Copyright (c) 2010-2017 The BearHeart Group, LLC
# created 2017-03-10
# updated 2017-09-29
#

from bwCGI import bwCGI
from bwDB import bwDB
from bwConfig import configFile
import random
import os, sys

g = dict(
    config_file = 'db.conf',
    table_name = 'jurl'
)

default_url = 'https://bw.org/error'

def main():
    init()
    db = g['db']
    v = g['vars']

    if 'u' in v:
        key = v.getfirst('u')
    elif 'PATH_INFO' in os.environ:
        key = os.environ['PATH_INFO']
    elif len(sys.argv) > 1:
        key = sys.argv[1]
    else:
        redirect(default_url)
        return 0

    if key.startswith('/'): key = key[1:]
    try:
        target = db.sql_query_value("SELECT targetURL FROM jurl WHERE shortURL = ?", [ key ]);
    except TypeError as e:
        redirect(default_url)
    else:
        redirect(target)

def redirect(u):
    # print("content-type: text/plain", end = '\r\n\r\n')   # uncomment for debugging
    print("Status: 302 Found", end = '\r\n')
    print("Location: {}".format(u), end = '\r\n\r\n')

def init():
    g['cgi'] = bwCGI()
    g['vars'] = g['cgi'].vars()
    g['config'] = configFile(g['config_file']).recs()
    g['db'] = bwDB(filename = g['config']['db'], table = g['table_name'])

def error(e):
    print(e)
    exit(0)

if __name__ == "__main__": main()

