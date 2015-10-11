#!/usr/bin/ruby

# The FreeDns.io project
# This sample replaces an existing MX record.
# As you can have up to 4 MX records, it's necessary to specify which to replace.
# The replaced value is 'mail.foo.bar' and will be overriden by 'mail.bar.foo'

require 'net/http'
require 'uri'

data = {
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'MX',
    'replace' => 'mail.foo.bar',
    'preference' => 5,
    'value'=> 'mail.bar.foo'
}

uri = URI('https://freedns.io/request')
res = Net::HTTP.post_form(uri, data)

#res.body will contain the response 
#res.code will contain the return the HTML status code
