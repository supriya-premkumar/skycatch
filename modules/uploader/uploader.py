#!/usr/bin/env python

import boto
import boto3
import sys
import os
from boto.s3.key import Key
from boto.exception import S3ResponseError

UPLOAD_LOCATION_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
UPLOAD_LOCATION_PATH += "/result/"


def upload():
    """
    upload uploads all the files from a directory called results to the s3 bucket specified in an env var  BUCKET_NAME.
    It also needs AWS_ACCESS_KEY_ID and AWS_ACCESS_SECRET_KEY specified in the env to access the
        s3 bucket.
    """
    print("Uploading Results")
    BUCKET_NAME = os.getenv("BUCKET_NAME")
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_ACCESS_SECRET_KEY"),
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)

    for subdir, dirs, files in os.walk(UPLOAD_LOCATION_PATH):
        for file in files:
            result_file = os.path.join(subdir, file)
            print(file)
            with open(result_file, 'rb') as data:
                bucket.put_object(Key=file, Body=data)
