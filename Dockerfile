FROM python:3
COPY main.py /main.py
COPY modules /modules
COPY data /data
COPY tests /tests
RUN pip install boto boto3
RUN chmod +x /main.py
CMD python /main.py
