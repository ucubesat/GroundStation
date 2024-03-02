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

data1 = {
    "lat": 37.7749,
    "lon": -122.4194,
    "alt": 0
}

data2 = {
    "lat": 34.0522,
    "lon": -118.2437,
    "alt": 500,
}

def load_from_IMU(data1, data2):
    # data1 is location of the ground station (possibly constant)
    # data2 is the location of the IMU onboard satellite
    # assume data comes in as a dictionary
    lat_a = data1["lat"]
    lon_a = data1["lon"]
    alt_a = data1["alt"]
    lat_b = data2["lat"]
    lon_b = data2["lon"]
    alt_b = data2["alt"]
    return (lat_a, lon_a, alt_a, lat_b, lon_b, alt_b)
    
while (true):
    lat_a, lon_a, alt_a, lat_b, lon_b, alt_b = load_from_IMU(data1, data2)
    azimuth, elevation = calculate_angles(lat_a, lon_a, alt_a, lat_b, lon_b, alt_b)

print(f"Azimuth: {azimuth} degrees")
print(f"Elevation: {elevation} degrees")