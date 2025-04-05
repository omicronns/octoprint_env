#!/usr/bin/env python3


import requests
import sys
import os
import time

OCTOPRINT_URL = 'http://localhost:{}/api/connection'
BAUDRATE = 115200
API_KEY = os.environ['CONNECT_PRINTER_API_KEY']

printers = {
    'ender3': { 'net_port': 8000 },
    'anet-a8': { 'net_port': 8001 }
}

headers = {'X-Api-Key': API_KEY}
json = {
    "command": "connect",
    "baudrate": BAUDRATE,
}

time.sleep(10)

r = requests.post(
    OCTOPRINT_URL.format(printers[sys.argv[1]]['net_port']),
    json=json,
    headers=headers
)

if (r.status_code == 204):
    sys.exit(0)
else:
    print(r)
    sys.exit(1)
