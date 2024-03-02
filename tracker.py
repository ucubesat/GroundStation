import math

def calculate_angles(lat_a, lon_a, alt_a, lat_b, lon_b, alt_b):
    # Convert latitude and longitude to radians
    lat_a_rad = math.radians(lat_a)
    lon_a_rad = math.radians(lon_a)
    lat_b_rad = math.radians(lat_b)
    lon_b_rad = math.radians(lon_b)

    # Calculate differences in latitude and longitude
    delta_lat = lat_b_rad - lat_a_rad
    delta_lon = lon_b_rad - lon_a_rad

    # Calculate distance between the two points
    distance = math.sqrt((delta_lat ** 2) + (delta_lon ** 2))

    # Calculate azimuth angle
    azimuth = math.atan2(delta_lon, delta_lat)

    # Calculate elevation angle
    elevation = math.atan2(alt_b - alt_a, distance)

    # Convert azimuth and elevation angles to degrees
    azimuth_deg = math.degrees(azimuth)
    elevation_deg = math.degrees(elevation)

    return azimuth_deg, elevation_deg

# Example usage
lat_a = 37.7749
lon_a = -122.4194
alt_a = 0
lat_b = 34.0522
lon_b = -118.2437
alt_b = 500

azimuth, elevation = calculate_angles(lat_a, lon_a, alt_a, lat_b, lon_b, alt_b)
print(f"Azimuth: {azimuth} degrees")
print(f"Elevation: {elevation} degrees")