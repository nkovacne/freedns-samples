#!/usr/bin/ruby

# The FreeDns.io project
# This sample updates a TXT record to string "foo bar"
# Please note that you shouldn't place any double-quotes
# around the value parameter's value. The server will itself
# enclose the expression with double-quotes.

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'TXT',
    'value' => 'foo bar'
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
