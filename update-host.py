#/usr/bin/env python3

"""
     The FreeDns.io project
     This sample updates a record to the IP address of the user who made the request
"""

from datetime import datetime
from urllib.parse import urlencode
from urllib import request
from config import USERNAME, PASSWORD, HOST, RECORD_TYPE

url = 'https://freedns.io/request'
params = {
  'username': USERNAME,
  'password': PASSWORD,
  'host': HOST,
  'record': RECORD_TYPE
}

data = urlencode(params)
req = request.Request(url, data.encode('utf-8'))

try:
  response = request.urlopen(req)
  content = response.read()
  print("[%s] %s" % (datetime.now(), content))
except request.URLError as e:
  print("[%s] Error: %d %s (%s)" % (datetime.now(), e.code, e.reason, e.read()))
