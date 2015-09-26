#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision, syntax, overflow, \n")
    sys.stderr.write("\tattribute, indentation   \n ")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assert 1==2
elif error_type == "io":
    stuff = open('launchcodes.txt')
    print(stuff)
elif error_type == "import":
    from folder import skynet
elif error_type == "index":
    aaa = [10, 20]
    
    aaa = [1]
    aaa = [3]
elif error_type == "key":
    d = {} 
    
    d['key1']
elif error_type == "name":
    print(h4xx)
elif error_type == "os":
    import os
    os.ttyname(3)
elif error_type == "type":
    a1=7
    a2="10"
    a1+a2
elif error_type == "value":
    stuffv = [2,5,9]
    a, b = stuffv
elif error_type == "zerodivision":
    print(9000/0)
elif error_type == "syntax":
    None 
    type(None)
    <type 'NoneType'>
    None=1
elif error_type == "overflow":
    import math 
    1-math.exp(-1*9999999999*-0.3983230239232)
elif error_type == "attribute":
    l = [1,2]
    1.append(3)
    l = None
    l.append(4)
elif error_type == "indentatation":
a=1
if a==1;
print a

else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
