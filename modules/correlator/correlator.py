import sys
import os
import csv
sys.path.append('modules/libs')
import utils

sites_file = '../data/sites.csv'
images_file = '../data/images.csv'

def correlate():
    """
    correlate reads the predownloaded sites.csv and images.csv files and correlates
    the images to the nearest city. It will also write all the images that are correlated to
    a city as <city_name>_challenge.csv in result directory.
    """
    city_map = utils.file_reader(sites_file)
    image_map = utils.file_reader(images_file)
    for img_coord, img_name in image_map.items():
        city = get_closest_match(img_coord, img_name[1], city_map)
        file_name = str(city[0]) + "_challenge.csv"
        utils.write_files(file_name, img_name[0], img_coord, img_name[1])
        print("RESULT: ", img_coord, "IMAGE_NAME: ",
              img_name[0], " ", "IMAGE_DATE: ", img_name[1], "CITY: ", city)


def get_closest_match(img_coord, img_date, city_map):
    """
        get_closest_match finds the closest city for an image based on its coordinates on a given date.
        @params
        img_coord: tuple, coordinates where the image was captured.
        img_date: string, date of the image capture.
        city_map: dict. Map of all the cities. Key: city_coord. tuple. Value: city_name, date, tuple

        @returns:
        city_name: string. Closest city to the image coordinates
    """
    min_distance = sys.maxsize
    city_match = ()
    for city_coord, city_name in city_map.items():
        city_date = city_name[1]
        if(city_date == img_date):
            distance = utils.calculate_haversian_distance(float(img_coord[0]), float(
                img_coord[1]), float(city_coord[0]), float(city_coord[1]))
            if distance < min_distance:
                min_distance = distance
                city_match = city_coord
    if city_match in city_map:
        return city_map[city_match]
    else:
        return None
