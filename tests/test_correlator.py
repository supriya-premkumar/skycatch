import unittest
import sys
import os
from os import environ
import shutil
MODULE_PATH = [os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/modules/correlator',
               os.path.dirname(os.path.dirname(
                   os.path.realpath(__file__))) + '/modules/downloader',
               os.path.dirname(os.path.dirname(
                   os.path.realpath(__file__))) + '/modules/uploader',
               os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/modules/libs']
sys.path.extend(MODULE_PATH)
from correlator import correlate, get_closest_match
from downloader import download
from uploader import upload


class CorrelatorTestCase(unittest.TestCase):
    """ Tests for correlator.py """

    def test_closest_match(self):
        img_coord = ('38.0103956', '-119.0308747')
        img_date = "2018-06-14"
        city_map = {(37.9914638, -119.0024967): ('Mono Lake', '2018-06-14')}
        city = get_closest_match(img_coord, img_date, city_map)
        self.assertEqual(city, ('Mono Lake', '2018-06-14'),
                         msg="Expected city to match Mono Lake")

    def test_closest_match_false_values(self):
        img_coord = ('45.3991447', '-121.669157')
        img_date = "2018-03-22"
        city_map = {(45.3956221, -121.6622495): ('Mount Hood', '2018-06-14'),
                    (37.9914638, -119.0024967): ('Mono Lake', '2018-06-14')}
        city = get_closest_match(img_coord, img_date, city_map)
        self.assertEqual(
            city, None, msg="Expected city to not match due to different dates")

    def test_correlate(self):
        results_dir = os.path.abspath("../result")
        correlate()
        self.assertEqual(len(os.listdir(results_dir)), 2,
                         msg="Expected correlate to generate two city files")

    def test_download(self):
        download_dir = os.path.abspath("../data")
        download()
        self.assertGreater(len(os.listdir(download_dir)), 2,
                           msg="Expected the downloaded bucket to have atleast 2 files")

    def test_upload(self):
        upload_dir = os.path.abspath("../result")
        download_dir = os.path.abspath("../data")
        upload()
        # Test by downloading the files
        download()
        self.assertEqual(len(os.listdir(download_dir)), 4,
                         msg="Expected the downloaded bucket to have atleast 4 files")

def init():
    if ("BUCKET_NAME" not in environ or "AWS_ACCESS_KEY_ID" not in environ or "AWS_ACCESS_SECRET_KEY" not in environ):
        print("Please ensure that the following environment variables are set.\nBUCKET_NAME\nAWS_ACCESS_KEY_ID\nAWS_ACCESS_SECRET_KEY")
        sys.exit(1)

if __name__ == '__main__':
    init()
    unittest.main()
