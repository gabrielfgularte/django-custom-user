#!/bin/bash

apt-get update
apt-get install -y python3-dev
apt-get install -y python-virtualenv
apt-get install -y ntp

echo "America/Sao_Paulo" | sudo tee /etc/timezone
sudo dpkg-reconfigure --frontend noninteractive tzdata


su vagrant << EOF
    virtualenv -p python3 ~/env
    ~/env/bin/pip install -r /vagrant/requirements.txt
    ~/env/bin/python /vagrant/django_custom_user/manage.py migrate account
    ~/env/bin/python /vagrant/django_custom_user/manage.py migrate
EOF
