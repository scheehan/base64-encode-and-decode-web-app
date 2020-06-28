#!/usr/bin/python3.7

import base64
import cgi

form = cgi.FieldStorage() 

f_data = form.getvalue('e_box')

en_data = base64.b64encode(b'f_data)

print ("Content-type: text/html\n")

print ('<html lang="en">\n')
print("""\
    
    <head>
<title>Sample CGI Script</title>
<link rel="stylesheet" href="../css/main.css">
</head>

""")
print('<body>\n')

print("""\
    
<form name="e_box" action="cgi-bin/encode_64.py" method="POST">
<input type="text" id="e_box" name="e_box"><br>
<input type="submit" id="e_box" value="Submit">
</form>')

<form name="d_box" action="cgi-bin/decode_64.py" method="POST">
<input type="text" id="d_box" name="d_box"><br>
<input type="submit" id="d_box" value="Submit">
</form>

""")
  
print('</body>\n')
print('</html>\n')