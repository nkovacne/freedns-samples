#!/usr/bin/ruby

# The FreeDns.io project
# This sample deletes an existing MX record.
# As you can have up to 4 MX records, it's necessary to specify which to delete.
# The deleted record is 'mail.bar.foo'

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'MX',
    'value' => 'mail.bar.foo',
    'delete' => 1
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
