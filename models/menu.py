# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = 'Microposts On Steroids'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Denis Lozar <dencko@gmail.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework, tukker'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Help'), False, URL('default', 'help'), []),
    (T('Login'), False, URL('default', 'user', 'login'), []),
    (T('Privacy'), False, URL('default', 'privacy'), []),
]

