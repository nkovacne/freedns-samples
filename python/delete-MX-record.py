#/usr/bin/env python3

"""
     The FreeDns.io project
     This sample deletes an existing MX record.
     As you can have up to 4 MX records, it's necessary to specify which to delete.
     The deleted record is 'mail.bar.foo'
"""

from urllib.parse import urlencode
from urllib import request

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'MX',
  'value': 'mail.bar.foo',
  'delete': 1 
}

data = urlencode(params)
req = request.Request(url, data.encode('utf-8'))

try:
  response = request.urlopen(req)
  content = response.read()
  print(content)
except request.URLError as e:
  print("Error: %d %s (%s)" % (e.code, e.reason, e.read()))
