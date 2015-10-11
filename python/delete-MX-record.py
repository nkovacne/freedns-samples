#/usr/bin/env python

"""
     The FreeDns.io project
     This sample deletes an existing MX record.
     As you can have up to 4 MX records, it's necessary to specify which to delete.
     The deleted record is 'mail.bar.foo'
"""

import urllib
import urllib2

url = 'https://freedns.io/request'
params = {
  'username': 'foo',
  'password': '***',
  'host': 'myhost',
  'record': 'MX',
  'value': 'mail.bar.foo',
  'delete': 1 
}

data = urllib.urlencode(params)
req = urllib2.Request(url, data)

try:
  response = urllib2.urlopen(req)
  content = response.read()
  print content
except urllib2.URLError as e:
  print "Error: %d %s (%s)" % (e.code, e.reason, e.read())
