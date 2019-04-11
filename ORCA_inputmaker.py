#! /usr/bin/env python
# script for making input files from an xyz file
#

import re
import os
import sys
import argparse

data = []
m = []
simple_block = []
xyz_header = []

xyz_string = re.compile("([a-zA-z]+)\s*(\d*.\d*)\s*(\d*.\d*)\s*(\d*.\d*)")
xyz_file = sys.argv[1]                 #any file containing one set of xyz coordinates (regex will search for pattern)
inp_name = xyz_file.split('.xyz')
inp_file = str(inp_name[0]) + '.inp'
block_file = sys.argv[2] #optional file containing block information, useful if creating multiple input files with the same block parameters

##############################################
#read xyz
#make new file, name it the xyz name + .inp
# add * xyz to beginning and *  to end
# multiplicity and spin
# block options
# option to yank from another file the block/top
################################################

#user inputs
total_charge = input('What is the charge of your model? (example: -1, 0, or +1) \n')

spin_mult = input('What is the spin multiplicity of your model? \n')

xyz_header.append('* xyz ' + str(total_charge) + ' ' + str(spin_mult) + '\n')

# read block input from another input file, reads until * is found in the line before the xyz coordinates
with open(block_file, 'r') as reader, open(inp_file,'w+') as writer:        # read from arg2 block file and write to new input
    simple_block = []
    read_blocks = reader.readlines()
    for block in read_blocks:
        if '*' not in block:                                                 # reads until * is found in line
            simple_block.append(block)
            continue
        else:                                                                # if * is found, break from loop
            break

#read xyz file
#def open_write():
with open(xyz_file, 'r') as reader, open(inp_file,'w+') as writer:     #reading lines of arg1 xyz coordinate file and writing to new input
    coords = reader.readlines()
    print(coords)
    coords.pop(0)                                                       # removing the first two lines of the input file, comment and name usually. ** maybe add regex match? instead **
    coords.pop(0)
    print(coords)
    writer.writelines(simple_block)              # write block input from arg2
    writer.writelines(xyz_header)                # write xyz head line with charge and multiplicity
    writer.writelines(coords)                    # write coordinates from arg1
    writer.writelines('*')                       # add a * to the end of the file

######################################################################################################
######################################################################################################
#Parse Arguments (need to add) Useful for making an input from scratch (without an arg2 block input)

#parser = argparse.ArgumentParser(description='Make an input file',
#                                 formatter_class=argparse.RawTextHelpFormatter)

#parser.add_argument(xyz_file,
#                    action = 'append',
#                    help = 'xyz coordinate file')

# parser.add_argument('-scf',
#                     default = 'none',
#                     action = 'append',
#                     help = 'add the %scf block to input\n')
#
# parser.add_argument('--keyword',
#                     default = 'none',
#                     action = 'append',
#                     help='input the functional, basis set, and any other keywords needed in the ! line')
#
#
# args = parser.parse_args()
#
#
# if args.scf != 'none':
#     scf_block = '%scf \n' + 'block_inp \n' + 'end \n'
#     simple_block = simple_block.append(scf_block)
# else:
#     pass
#
#
# if args.keyword == True:
#     keyword_line = '!' + 'keyword_inp'
#     simple_block = simple_block.apppend(keyword_line)
# elif args.keyword == False:
#     keyword_line = '!' + 'BP86 def2-SVP'
#     simple_block = simple_block.append(keyword_line)
# else:
#     pass


#inp_line = input('Input all in ! line (basis set, opt, functional) \n')
#simple_block.append(inp_line)
#np = input('number of processes \n')

