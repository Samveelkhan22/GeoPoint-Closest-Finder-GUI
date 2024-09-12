# geo_lib.py

import math

class GeoPoint:
    """Class to represent a geographical point with latitude, longitude, and description."""
    def __init__(self, lat, lon, description):
        self.lat = float(lat)
        self.lon = float(lon)
        self.description = description
    
    def distance_to(self, other):
        """Calculate the Euclidean distance between this point and another point."""
        return math.sqrt((self.lat - other.lat)**2 + (self.lon - other.lon)**2)

def read_points_from_file(filename):
    """Read points from a file and return a list of GeoPoint objects."""
    point_list = []
    with open(filename, 'r') as file:
        for line in file:
            lat, lon, description = line.strip().split(', ')
            point_list.append(GeoPoint(lat, lon, description))
    return point_list

def find_closest_point(user_point, point_list):
    """Find the closest point in the list to the user's point."""
    closest_point = None
    min_distance = float('inf')
    for point in point_list:
        distance = user_point.distance_to(point)
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point
