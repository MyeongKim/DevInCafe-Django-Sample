#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
python $SCRIPTPATH/../manage.py startapp $1