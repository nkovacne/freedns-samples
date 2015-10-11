#!/usr/bin/ruby

# The FreeDns.io project
# This sample updates an AAAA record to IP address FE80::0202:B3FF:FE1E:8329

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'AAAA',
    'value' => 'FE80::0202:B3FF:FE1E:8329'
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
