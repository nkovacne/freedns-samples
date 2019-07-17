#/usr/bin/env python3

"""
     The FreeDns.io project
     This sample replaces an existing MX record.
     As you can have up to 4 MX records, it's necessary to specify which to replace.
     The replaced value is 'mail.foo.bar' and will be overriden by 'mail.bar.foo'
"""

from urllib.parse import urlencode
from urllib import request

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'MX',
  'replace': 'mail.foo.bar',
  'preference': 5,
  'value': 'mail.bar.foo'
}

data = urlencode(params)
req = request.Request(url, data.encode('utf-8'))

try:
  response = request.urlopen(req)
  content = response.read()
  print(content)
except request.URLError as e:
  print("Error: %d %s (%s)" % (e.code, e.reason, e.read()))
