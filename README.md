### Skycatch DevOps Challenge
## Code Organization:
1. main.py is a wrapper for running image correlation.
2. All imported code is modularized and available in modules
3. data is the download directory, where the files from s3 bucket are downloaded.
4. result is the upload directory, where the correlated image files are uploaded from.
5. libs contain utility functions that are shared across modules.

## How to run:
```
1. Set the following env vars. BUCKET_NAME, AWS_ACCESS_KEY_ID and AWS_ACCESS_SECRET_KEY
2. make build -> This will build a docker container for the application.
3. make run -> This will run the docker container
4. make upload -> This will push the docker container to the public repo supriyapremkumar/skycatch:latest
5. make tests -> Will run all the unit tests inside of the docker container.
```

## Future Work:
1. Using k-means clustering seems like an appropriate use case here instead of manually
calculating haversian distances between clusters. Here k = len(cities)
2. For scaling this up, a map reduce algorithm suits really well. Where we will have individual mappers
will emit a coordinate for all the images, and the reducers will reduce this on a per city basis.
3. We can use kinesis and lambda functions on AWS to address deployability challenges. For example, we can have a kinesis stream which accepts an image name and its coordinates and every time a new
coordinate is pushed into the stream it can be consumed by a lambda function which updates a s3 file inline after computing the nearest city.
