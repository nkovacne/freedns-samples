#/usr/bin/env python

"""
     The FreeDns.io project
     This sample adds a new MX record. You may have up to 4 MX records.
"""

import urllib
import urllib2

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'MX',
  'preference' => 10,
  'value': '8.8.8.8'
}

data = urllib.urlencode(params)
req = urllib2.Request(url, data)

try:
  response = urllib2.urlopen(req)
  content = response.read()
  print content
except urllib2.URLError as e:
  print "Error: %d %s (%s)" % (e.code, e.reason, e.read())
