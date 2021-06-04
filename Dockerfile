FROM ubuntu:20.04
RUN apt-get update

RUN apt-get install -y build-essential python3.8 python3.8-dev python3-pip python3.8-venv

# update pip
RUN python3.8 -m pip install pip --upgrade
RUN python3.8 -m pip install wheel

COPY ./ /app
WORKDIR /app/clothes_shop
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install setuptools \
    && pip install utils \
    && pip install -r /app/requirements.txt --no-cache-dir
EXPOSE 8000
CMD python3 manage.py runserver