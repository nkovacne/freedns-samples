#!/usr/bin/ruby

# The FreeDns.io project
# This sample adds a new MX record. You may have up to 4 MX records.

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'MX',
    'preference' => 10,
    'value'=> '8.8.8.8'
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
