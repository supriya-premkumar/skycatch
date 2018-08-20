HOST = 127.0.0.1

run:
	docker run --rm -e "BUCKET_NAME=${BUCKET_NAME}" -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" -e "AWS_ACCESS_SECRET_KEY=${AWS_ACCESS_SECRET_KEY}"  supriyapremkumar/skycatch

build:
	docker build -t supriyapremkumar/skycatch .

upload:
	docker push supriyapremkumar/skycatch

test:
	docker run --rm -e "BUCKET_NAME=${BUCKET_NAME}" -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" -e "AWS_ACCESS_SECRET_KEY=${AWS_ACCESS_SECRET_KEY}"  supriyapremkumar/skycatch bash -c "cd tests && python test_correlator.py"
