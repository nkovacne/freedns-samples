#/usr/bin/env python

"""
     The FreeDns.io project
     This sample updates a TXT record to string "foo bar"

     Please note that you shouldn't place any double-quotes
     around the value parameter's value. The server will itself
     enclose the expression with double-quotes.
"""

import urllib
import urllib2

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'TXT',
  'value': 'foo bar'
}

data = urllib.urlencode(params)
req = urllib2.Request(url, data)

try:
  response = urllib2.urlopen(req)
  content = response.read()
  print content
except urllib2.URLError as e:
  print "Error: %d %s (%s)" % (e.code, e.reason, e.read())
