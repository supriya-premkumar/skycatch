import sys
sys.path.extend(
    ['modules/downloader', 'modules/correlator', 'modules/uploader'])
from downloader import download
from correlator import correlate
from uploader import upload
from os import environ


def main():
    init()
    download()
    correlate()
    upload()

def init():
    if ("BUCKET_NAME" not in environ or "AWS_ACCESS_KEY_ID" not in environ or "AWS_ACCESS_SECRET_KEY" not in environ):
        print("Please ensure that the following environment variables are set.\nBUCKET_NAME\nAWS_ACCESS_KEY_ID\nAWS_ACCESS_SECRET_KEY")
        sys.exit(1)
if __name__ == '__main__':
    main()
