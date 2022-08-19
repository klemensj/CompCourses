# Functions for calculating volume and surface area of a box

def volume_calc(a,b,c):
    volume = a*b*c
    return volume

def surface_area_calc(a,b,c):
    surface_area = 2*a*b + 2*b*c + 2*a*c
    return surface_area