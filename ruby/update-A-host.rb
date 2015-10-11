#!/usr/bin/ruby

# The FreeDns.io project
# This sample updates an A record to IP address 8.8.8.8

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'A',
    'value'=> '8.8.8.8'
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
