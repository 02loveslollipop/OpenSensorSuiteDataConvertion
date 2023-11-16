FROM python:3.11.3
RUN apt-get update
WORKDIR .
COPY main.py .
COPY config.yaml .
COPY config.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD [ "python","main.py" ]