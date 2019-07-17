#/usr/bin/env python3

"""
     The FreeDns.io project
     This sample updates an AAAA record to the IP address to IPv6 address FE80::0202:B3FF:FE1E:8329
"""

from urllib.parse import urlencode
from urllib import request

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'AAAA',
  'value': 'FE80::0202:B3FF:FE1E:8329'
}

data = urlencode(params)
req = request.Request(url, data.encode('utf-8'))

try:
  response = request.urlopen(req)
  content = response.read()
  print(content)
except request.URLError as e:
  print("Error: %d %s (%s)" % (e.code, e.reason, e.read()))
