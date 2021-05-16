#!/usr/bin/python

import base64
import cgi

form = cgi.FieldStorage()                                       #create instance of FieldStorage
f_data = form.getvalue('e_box')                                 #get submit data from form name e_box

if f_data is None:                                              #check for nonetype
    print ("Content-type: text/html\n")
    print ("<html>\n")
    print("<body>\n")
    print ("Please fill in value")
    print("</body>\n")
    print("</html>\n")
    exit
else:
    en_data = base64.b64encode(f_data.encode('ascii'))          #encode data as ascii format, then encode with base64
    print ("Content-type: text/html\n")                         #return data in HTTP
    print ("<html>\n")
    print("<body>\n")
    print('<p>' + en_data.decode("utf-8") + '</p>')
    print("</body>\n")
    print("</html>\n")