#!/usr/bin/python

import ast
import json
from sys import argv
from os import path

def pj_get():

    if path.exists(argv[1]) : # checking if the "intel" is solid

        jsonf = json.load( open( argv[1] ) )

        struct_buffer = jsonf
        
        if len(argv) == 4 :

            for next in argv[3][1:].split(argv[3][0]):

                struct_buffer = struct_buffer[next]

        if argv[2].isdigit():

            argv[2] = int(argv[2])

        exit(struct_buffer[argv[2]])

pj_get()