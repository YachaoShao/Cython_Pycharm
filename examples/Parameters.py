#!/usr/bin/env python3
# coding=utf-8

# method 1
# from optparse import OptionParser
#
# parser = OptionParser()
# parser.add_option("-f","--file",dest="filename",help="write report to FILE",metavar="FILE")
# parser.add_option("-q","--quiet",action="store_false",dest="verbose",default="True",help="do not print status messages to stdout")
#
# (options,args)=parser.parse_args()
#
#
#
# print(args)

# method 2
# import sys
#
# print ("\n".join(sys.argv))

# method 3
# import sys
#
# print("The number of parameter is ", len(sys.argv))
# print("The parameter list is: ", str(sys.argv))
# import json
# with open('input.json') as parameter:
#     input_pa = json.load(parameter)
#
# num_cell = input_pa["cells"]
# num_syn = input_pa["synapses"]
# num_comp = input_pa["compartments"]
# time_step = input_pa["dt"]
# simu_time = input_pa["tfinal"]
# print(num_cell, num_comp)

# method4

import  sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o",["ifile=", "ofile="])
    except getopt.GetoptError:
        print("test.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("test.py -i <inputfile -o <outputfile>>")
            sys.exit()
        elif opt in ("-i","--ifile"):
            inputfile = arg
            print("the input file is: ", inputfile)
        elif opt in ("-o","--ofile"):
            outputfile = arg
            print("the output file is: ", outputfile)


if __name__ == '__main__':
    main(sys.argv[1:])




