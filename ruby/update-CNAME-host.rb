#!/usr/bin/ruby

# The FreeDns.io project
# This sample updates a CNAME record to host foo.google.com

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'CNAME',
    'value' => 'foo.google.com'
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
