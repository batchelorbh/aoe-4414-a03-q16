#!/usr/bin/env python
# sez_to_ecef.py
#
# Converts SEZ reference frame components to ECEF
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    o_lat_deg           description
#    o_lon_deg
#    o_hae_km
#    s_km
#    e_km
#    z_km
#
# Output:
#    Prints ECEF x, y, and z position vector components in km
#
# Revision history:
#    09/19/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
from math import pi, sqrt, sin, cos

#Define constants
DEG_TO_RAD = pi / 180.0

#Pre-initialize input parameters
o_lat_deg = float('nan') #Description
o_lon_deg = float('nan')
o_hae_km = float('nan')
s_km = float('nan')
e_km = float('nan')
z_km = float('nan')

#Arguments are strings by default
if len(sys.argv) == 7:
   o_lat_deg = float(sys.argv[1])
   o_lon_deg = float(sys.argv[2])
   o_hae_km = float(sys.argv[3])
   s_km = float(sys.argv[4])
   e_km = float(sys.argv[5])
   z_km = float(sys.argv[6])
   
else:
   print(('Usage: python3 sez_to_ecef.py o_lat_deg '
                 'o_lon_deg o_hae_km s_km e_km z_km'))
   sys.exit()

#Main body of script
o_lat_rad = o_lat_deg * DEG_TO_RAD
o_lon_rad = o_lon_deg * DEG_TO_RAD

ecef_x_km = cos(o_lon_rad) * sin(o_lat_rad) * s_km \
            + cos(o_lon_rad) * cos(o_lat_rad) * z_km \
            - sin(o_lon_rad) * e_km

ecef_y_km = sin(o_lon_rad) * sin(o_lat_rad) * s_km \
            + sin(o_lon_rad) * cos(o_lat_rad) * z_km \
            + cos(o_lon_rad) * e_km

ecef_z_km = -cos(o_lat_rad) * s_km + sin(o_lat_rad) * z_km

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
