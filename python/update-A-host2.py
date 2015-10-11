#/usr/bin/env python

"""
     The FreeDns.io project
     This sample updates an A record to the IP address of the user who made the reques
"""

import urllib
import urllib2

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'A'
}

data = urllib.urlencode(params)
req = urllib2.Request(url, data)

try:
  response = urllib2.urlopen(req)
  content = response.read()
  print content
except urllib2.URLError as e:
  print "Error: %d %s (%s)" % (e.code, e.reason, e.read())
