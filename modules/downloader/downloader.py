#!/usr/bin/env python

import boto
import sys
import os
from boto.s3.key import Key
from boto.exception import S3ResponseError

DOWNLOAD_LOCATION_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
DOWNLOAD_LOCATION_PATH += "/data/"

if not os.path.exists(DOWNLOAD_LOCATION_PATH):
    print("Making download directory")
    os.mkdir(DOWNLOAD_LOCATION_PATH)


def download():
    """
    download downloads all the files from a s3 bucket specified in an env var  BUCKET_NAME.
    It downloads the files into a directory called data. It also needs
    AWS_ACCESS_KEY_ID and AWS_ACCESS_SECRET_KEY specified in the env to access the
    s3 bucket.
    """
    BUCKET_NAME = os.getenv("BUCKET_NAME")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_ACCESS_SECRET_KEY = os.getenv("AWS_ACCESS_SECRET_KEY")
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_ACCESS_SECRET_KEY)
    bucket = conn.get_bucket(BUCKET_NAME)

    # go through the list of files
    bucket_list = bucket.list()
    print(bucket_list)
    #
    for l in bucket_list:
        key_string = str(l.key)
        s3_path = DOWNLOAD_LOCATION_PATH + key_string
        try:
            print("Current File is ", s3_path)
            l.get_contents_to_filename(s3_path)
        except (OSError, S3ResponseError) as e:
            pass
            # check if the file has been downloaded locally
            if not os.path.exists(s3_path):
                try:
                    os.makedirs(s3_path)
                except OSError as exc:
                    # let guard againts race conditions
                    import errno
                    if exc.errno != errno.EEXIST:
                        raise
    conn.close()
