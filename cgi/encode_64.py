#!/usr/bin/python

import base64
import cgi

form = cgi.FieldStorage()       #create instance of FieldStorage

f_data = form.getvalue('e_box')

en_data = base64.b64encode(f_data.encode('ascii'))

print ("Content-type: text/html\n")

print ('<html lang="en">\n')
print('<body>\n')

print('<p>' + en_data.decode("utf-8") + '</p>')

print('</body>\n')
print('</html>\n')