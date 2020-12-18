#!/usr/bin/python

import base64
import cgi

form = cgi.FieldStorage()                                   #create instance of FieldStorage

f_data = form.getvalue('e_box')                             #get submit data from form name e_box

en_data = base64.b64encode(f_data.encode('ascii'))          #encode data as ascii format, then encode with base 64

# return data in HTTP 
print ("Content-type: text/html\n")

print ('<html lang="en">\n')
print('<body>\n')

print('<p>' + en_data.decode("utf-8") + '</p>')

print('</body>\n')
print('</html>\n')