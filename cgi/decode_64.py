#!/usr/bin/python

import base64
import cgi

form = cgi.FieldStorage() 

d_data = form.getvalue('d_box')

dec_data = base64.b64decode(d_data + "=" * (-len(d_data) % 4))


print ("Content-type: text/html\n")

print ('<html lang="en">\n')
print("""\
    
    <head>
<title>Sample CGI Script</title>
<link rel="stylesheet" href="css/main.css">
</head>

""")
print('<body>\n')

print('<p>' + dec_data.decode("utf-8") + '</p>')

print('</body>\n')
print('</html>\n')