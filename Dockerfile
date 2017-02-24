FROM python

RUN apt-get update

RUN useradd -rm -G www-data docker

EXPOSE 8000

ADD ./django_custom_user /home/docker

ADD ./requirements.txt /home/docker/requirements.txt

VOLUME /home/docker

RUN pip install -r /home/docker/requirements.txt

WORKDIR /home/docker

CMD python manage.py migrate account --noinput && \
    python manage.py migrate --noinput && \
    echo "Listening on localhost:8000" && \
    python manage.py runserver 0.0.0.0:8000
