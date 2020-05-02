#!/bin/sh

ssh /home/ubuntu/Akshaytest.pem ubuntu@52.66.247.217 <<EOF
  cd /var/www/Pipline_Proj/
  git pull
  source /var/www/cicd_env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo service apache2 restart
  exit
EOF
