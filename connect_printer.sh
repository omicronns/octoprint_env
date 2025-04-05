#!/bin/bash

source /home/kad/docker/octoprint/.api_key
echo "/home/kad/docker/octoprint/connect_printer.py $1" | /usr/bin/at -M now

