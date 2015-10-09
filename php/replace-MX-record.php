<?php
  /*
     The FreeDns.io project
     This sample replaces an existing MX record.
     As you can have up to 4 MX records, it's necessary to specify which to replace.
     The replaced value is 'mail.foo.bar' and will be overriden by 'mail.bar.foo'
  */

  $url = 'http://freedns.io/request';
  $data = array(
    'username' => 'foo',
    'password' => '***',
    'host' => 'myhost',
    'record' => 'MX',
    'replace' => 'mail.foo.bar',
    'preference' => 5,
    'value' => 'mail.bar.foo'
  );

  $options = array(
    'http' => array(
      'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
      'method'  => 'POST',
      'ignore_errors' => true,             // This one's important if you want to read the response status message from the server even in the case of error
      'content' => http_build_query($data),
    ),
  );

  $context = stream_context_create($options);

  $result = file_get_contents($url, false, $context);   // Will contain the response status message
  $retcode = $http_response_header[0];                  // Will contain the HTML-style response code (401 on errors, 200 on success)
?>
