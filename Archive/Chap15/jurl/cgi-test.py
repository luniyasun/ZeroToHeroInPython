#!/usr/bin/env python3
# cgi-test.py by Bill Weinman [http://bw.org/]
# Python versoin of CGI testing script
# Copyright 1995-2010 The BearHeart Group, LLC

import sys, os, cgi
version = "5.3.1py cgi/{}".format(cgi.__version__)

for s in (
    "Content-type: text/plain", '',
    "BW Test version: {}".format(version),
    "Copyright 1995-2010 The BearHeart Group, LLC",
    "\nVersions:\n=================",
    "Python: {}".format(sys.version.split(' ')[0])
) :
    print(s)

form = cgi.FieldStorage()
if form :
    print("\nQuery Variables:\n=================")
    for k in sorted(form):
        v = ']['.join(form.getlist(k))  # multiple items as [a][b][c]...
        print("{} [{}]".format(k, v))

print("\nEnvironment Variables:\n=================")
for k in sorted(os.environ.keys()):
    v = os.environ[k]
    print("{} [{}]".format(k, v))

