#!/usr/bin/env python
# sez_to_ecef.py
#
# Converts SEZ reference frame components to ECEF
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: None
#
# Parameters:
#    o_lat_deg           Latitude in degrees
#    o_lon_deg           Longitude in degrees
#    o_hae_km            Height above ellipsoid in km
#    s_km                S component of SEZ coordinate frame in km
#    e_km                E component of SEZ coordinate frame in km
#    z_km                Z component of SEZ coordinate frame in km
#
# Output:
#    Prints ECEF x, y, and z position vector components in km
#
# Revision history:
#    09/19/2024          Script created
#    09/23/2024          Added origin calculation
#
###############################################################################

#Import relevant modules
import sys
from math import pi, sqrt, sin, cos

#Define constants
R_E_KM = 6378.137 #km
E_E = 0.081819221456
DEG_TO_RAD = pi / 180.0

#Calculate denominator for SE and CE equations
def calc_denom(ecc, lat_rad):
   return sqrt(1 - ecc**2 * sin(lat_rad)**2)

#Pre-initialize input parameters
o_lat_deg = float('nan') #Latitude in degrees
o_lon_deg = float('nan') #Longitude in degrees
o_hae_km = float('nan') #Height above reference ellipsoid in km
s_km = float('nan') #S axis component in SEZ coordinate frame [km]
e_km = float('nan') #E axis component in SEZ coordinate frame [km]
z_km = float('nan') #Z axis component in SEZ coordinate frame [km]

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

#Convert lat and lon to radians
o_lat_rad = o_lat_deg * DEG_TO_RAD
o_lon_rad = o_lon_deg * DEG_TO_RAD

#Calculate ECEF components using rotation matrices
ecef_x_km = cos(o_lon_rad) * sin(o_lat_rad) * s_km \
            + cos(o_lon_rad) * cos(o_lat_rad) * z_km \
            - sin(o_lon_rad) * e_km

ecef_y_km = sin(o_lon_rad) * sin(o_lat_rad) * s_km \
            + sin(o_lon_rad) * cos(o_lat_rad) * z_km \
            + cos(o_lon_rad) * e_km

ecef_z_km = -cos(o_lat_rad) * s_km + sin(o_lat_rad) * z_km

'''
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
'''

#Calculate denominator for C_E and S_E equations
denom = calc_denom(E_E, o_lat_rad)

C_E = R_E_KM / denom
S_E = R_E_KM * (1 - E_E**2) / denom

#Find ECEF vector components
ecef2_x_km = (C_E + o_hae_km) * cos(o_lat_rad) * cos(o_lon_rad)
ecef2_y_km = (C_E + o_hae_km) * cos(o_lat_rad) * sin(o_lon_rad)
ecef2_z_km = (S_E + o_hae_km) * sin(o_lat_rad)

'''
print(ecef2_x_km)
print(ecef2_y_km)
print(ecef2_z_km)
'''

#Add ECEF vector and origin vector to get true ECEF components
r_x_km = ecef_x_km + ecef2_x_km
r_y_km = ecef_y_km + ecef2_y_km
r_z_km = ecef_z_km + ecef2_z_km

print(r_x_km)
print(r_y_km)
print(r_z_km)
