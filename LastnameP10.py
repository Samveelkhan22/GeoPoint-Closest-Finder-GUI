# SoberanesP10
# Programmer: Cali Soberanes
# Email: csoberanes@cnm.edu
# Purpose: demonstrate how to define a class and find the closest point from a list of points

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

def main():
    point_list = read_points_from_file('points.txt')
    
    while True:
        try:
            user_lat = float(input("Enter your latitude: "))
            user_lon = float(input("Enter your longitude: "))
        except ValueError:
            print("Please enter valid numbers for latitude and longitude.")
            continue

        user_point = GeoPoint(user_lat, user_lon, "Your Location")

        closest_point = find_closest_point(user_point, point_list)

        print(f"You are closest to {closest_point.description} which is located at ({closest_point.lat}, {closest_point.lon})")

        another = input("Do another (y/n)? ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
