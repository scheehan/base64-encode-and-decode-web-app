#!/usr/bin/python3.7

import base64
import cgi


# form = cgi.FieldStorage() 

# d_data = form.getvalue('d_box')

d_data = 'null'

#print(d_data)

dec_data = base64.b64decode(d_data + "=" * (-len(d_data) % 4))

print ("Content-type: text/html\n")

print ('<html lang="en">\n')
print("""\
    
    <head>
<title>Sample CGI Script</title>
<link rel="stylesheet" href="../css/main.css">
</head>

""")
print('<body>\n')

print(dec_data)


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