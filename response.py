#! /usr/local/bin/python
from cgi import FieldStorage

print('Content-Type: text/html')
print()

form_data =FieldStorage()
fname = form_data.getfirst("firstname")
sname = form_data.getfirst("surname")
'''
firstname=&surname=&street_address"=&town=&postcode=&BIO=&EMAIL=&FAV-COLOR=%23000000&BDAY=&FILE_NAME=response.py
file:///users/csdipact2020/pw9/public_html/cgi-bin/scripts/response.py?NAME=&BIO=&EMAIL=&FAV-COLOR=%239e3333&BDAY=&FILE_NAME=to_morse.py&IMG_NAME.x=24&IMG_NAME.y=9
'''

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Response</title>
        </head>
        <body>
            <p>
                Hello, %s %s. You may go on your way.
            </p>
        </body>
    </html>""" % (fname, sname))
