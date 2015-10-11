#/usr/bin/env python

"""
     The FreeDns.io project
     This sample updates an AAAA record to IP address FE80::0202:B3FF:FE1E:8329
"""

import urllib
import urllib2

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'AAAA',
  'value': 'FE80::0202:B3FF:FE1E:8329'
}

data = urllib.urlencode(params)
req = urllib2.Request(url, data)

try:
  response = urllib2.urlopen(req)
  content = response.read()
  print content
except urllib2.URLError as e:
  print "Error: %d %s (%s)" % (e.code, e.reason, e.read())
