#!/usr/bin/env python
# sez_to_ecef.py
#
# <Insert script description here>
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Usage: python3 sez_to_ecef.py arg1 arg2
#
# Parameters:
#    param1              description
#    param2              description
#
# Output:
#    output1             description
#
# Revision history:
#    09/19/2024          Script created
#
###############################################################################

#Import relevant modules
import sys

#Define constants
const1 = 0

#User-defined functions
def user_function(param1, param2):
   return param1 + param2

#Pre-initialize input parameters
arg1 = float('nan') #Description
arg2 = 0.0 #Description

#Arguments are strings by default
if len(sys.argv) == num_args_plus_one:
   arg1 = float(sys.argv[1])
   arg2 = sys.argv[2]
else:
   print('Usage: python3 sez_to_ecef.py param1 param2')
   sys.exit()

#Main body of script

