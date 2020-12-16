#!/usr/bin/python3.7

import base64
import cgi

form = cgi.FieldStorage() 

f_data = form.getvalue('e_box')

en_data = base64.b64encode(f_data.encode('ascii'))

print ("Content-type: text/html\n")

print ('<html lang="en">\n')

print("""\
    
    <head>
<title>Sample CGI Script</title>
<link rel="stylesheet" href="css/main.css">
</head>

""")

print('<body>\n')

print('<p>' + en_data.decode("utf-8") + '</p>')


print('</body>\n')
print('</html>\n')