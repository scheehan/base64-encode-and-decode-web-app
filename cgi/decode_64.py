#!/usr/bin/python

import base64
import cgi

form = cgi.FieldStorage()                                                       #create instance of FieldStorage
d_data = form.getvalue('d_box')                                                 #get submit data from form name d_box

if d_data is None:                                                              #check for nonetype
    print ("Content-type: text/html\n")
    print ("<html>\n")
    print("<body>\n")
    print ("Please fill in value")
    print("</body>\n")
    print("</html>\n")
    exit
else:
    dec_data = base64.b64decode(d_data + "=" * (-len(d_data) % 4))              #add padding to bytes before decode
    print ("Content-type: text/html\n")
    print ('<html>\n')
    print('<body>\n')
    print('<p>' + dec_data.decode("utf-8") + '</p>')
    print('</body>\n')
    print('</html>\n')