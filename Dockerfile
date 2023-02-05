FROM python:3.9.12

WORKDIR /sketch/
COPY ./sketch.py /sketch/
COPY ./docker.txt /sketch/

RUN pip3 install -r ./docker.txt

CMD ["python","sketch.py"] 