import csv
import os
from math import sin, cos, sqrt, atan2


def file_reader(filename):
    """
    file_reader reads a file specified by the file name and returns the map with
    keys as the lat, long tuple and value as name, date as the tuple.
    Name in the value can either be city name or the image name depending on which file
    is read.

    @params:
    filename: string. Name of the file to be read.

    @returns:
    city_map: dict. Map of the city {(lat, long):(name, date)}
    """
    csv_map = {}
    with open(filename, newline='')as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        for row in filereader:
            csv_map[row[2], row[3]] = (row[1], row[4])
    return csv_map


def write_files(filename, img_name, img_coord, img_date):
    """
    write_files writes to the path specified by filename. The file is
    written in append mode, with each line representing an image in the file.
    Data written is a csv row with image name, image coordinates and image date.

    @params:
    filename: string. Name of the file to be written.
    img_name: string. Name of the image.
    img_coord: tuple. Lat, long of the image.
    img_date: string. Date of the image capture.
    """
    DOWNLOAD_LOCATION_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    DOWNLOAD_LOCATION_PATH += "/result/"

    if not os.path.exists(DOWNLOAD_LOCATION_PATH):
        print("Making result directory: ", DOWNLOAD_LOCATION_PATH)
        os.makedirs(DOWNLOAD_LOCATION_PATH)

    full_file = DOWNLOAD_LOCATION_PATH + filename
    row = [img_name, img_coord, img_date]
    with open(full_file, 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
    csvfile.close()

def calculate_haversian_distance(lat_loc_1, long_loc_1, lat_loc_2, long_loc_2):
    """
    calculate_haversian_distance calculates haversian distance between two lat long pairs.

    @params:
    lat_loc_1: float. Latitude of location 1
    long_loc_1: float. Longitude of location 1
    lat_loc_2: float. Latitude of location 2
    long_loc_2: float. Longitude of location 2

    @returns:
    distance: float. Distance between location 1 and location 2
    """
    # Radius of Earth in km
    R = 6373.0

    dlon = long_loc_2 - long_loc_1
    dlat = lat_loc_2 - lat_loc_1
    a = (sin(dlat/2))**2 + cos(lat_loc_1) * cos(lat_loc_2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance
