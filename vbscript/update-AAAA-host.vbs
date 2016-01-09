	'The FreeDns.io project
	'This sample updates an AAAA record to IP address FE80::0202:B3FF:FE1E:8329

vUsername = "foo"
vPassword = "***"
vHost = "myhost"
vRecord = "AAAA"
vValue = "FE80::0202:B3FF:FE1E:8329"

	sRequest = "username=" & vUsername & "&password=" & vPassword &"&host=" & vHost & "&record=" & vRecord & "&value=" & vValue
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