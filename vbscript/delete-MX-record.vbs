	'The FreeDns.io project
	'This sample deletes an existing MX record.
	'As you can have up to 4 MX records, it's necessary to specify which to delete.
	'The deleted record is 'mail.bar.foo'

vUsername = "foo"
vPassword = "***"
vHost = "myhost"
vRecord = "MX"
vValue = "mail.bar.foo"
vDelete = 1

	sRequest = "username=" & vUsername & "&password=" & vPassword &"&host=" & vHost & "&record=" & vRecord & "&value=" & vValue & "&delete=" & vDelete
	Set objxmlHTTP = CreateObject("Microsoft.XMLHTTP")
	objxmlHTTP.open "POST", "https://freedns.io/request",false
	objxmlHTTP.setRequestHeader "Content-Type", "application/x-www-form-urlencoded"
	objxmlHTTP.setRequestHeader "Content-Length", Len(sRequest)
	objxmlHTTP.send sRequest

'Uncomment following lines if you would like to receive a response message
'	If objxmlHTTP.Status >= 400 And objxmlHTTP.Status <= 599 Then
'	 	WScript.echo "Error Occurred : " & objxmlHTTP.Status & " - " & objxmlHTTP.statusText
'	Else
'	 	WScript.echo objxmlHTTP.ResponseText
'	End If