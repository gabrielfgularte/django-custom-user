#!/bin/bash

docker run -itd \
    -p 8000:8000 \
    -v `pwd`/django_custom_user:/home/docker \
    django-custom-user:0.1
