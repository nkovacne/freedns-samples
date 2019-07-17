#/usr/bin/env python3

"""
     The FreeDns.io project
     This sample updates a TXT record to string "foo bar"

     Please note that you shouldn't place any double-quotes
     around the value parameter's value. The server will itself
     enclose the expression with double-quotes.
"""

from urllib.parse import urlencode
from urllib import request

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'TXT',
  'value': 'foo bar'
}

data = urlencode(params)
req = request.Request(url, data.encode('utf-8'))

try:
  response = request.urlopen(req)
  content = response.read()
  print(content)
except request.URLError as e:
  print("Error: %d %s (%s)" % (e.code, e.reason, e.read()))
