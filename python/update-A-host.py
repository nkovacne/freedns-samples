#/usr/bin/env python3

"""
     The FreeDns.io project
     This sample updates an A record to IP address 8.8.8.8
"""

from urllib.parse import urlencode
from urllib import request

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'A',
  'value': '8.8.8.8'
}

data = urlencode(params)
req = request.Request(url, data.encode('utf-8'))

try:
  response = request.urlopen(req)
  content = response.read()
  print(content)
except request.URLError as e:
  print("Error: %d %s (%s)" % (e.code, e.reason, e.read()))
