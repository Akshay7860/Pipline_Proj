#!/bin/sh

ssh root@13.233.151.193 <<EOF
  cd /var/www/Pipline_Proj/
  git pull
  source /var/www/cicd_env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo service apache2 restart
  exit
EOF
