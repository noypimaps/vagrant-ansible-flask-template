#!/bin/bash
source ./env/bin/activate
env/bin/uwsgi --ini uwsgi.flaskapp.ini && echo "Started: flaskapp"
