#/usr/bin/env python

"""
     The FreeDns.io project
     This sample replaces an existing MX record.
     As you can have up to 4 MX records, it's necessary to specify which to replace.
     The replaced value is 'mail.foo.bar' and will be overriden by 'mail.bar.foo'
"""

import urllib
import urllib2

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

data = urllib.urlencode(params)
req = urllib2.Request(url, data)

try:
  response = urllib2.urlopen(req)
  content = response.read()
  print content
except urllib2.URLError as e:
  print "Error: %d %s (%s)" % (e.code, e.reason, e.read())
