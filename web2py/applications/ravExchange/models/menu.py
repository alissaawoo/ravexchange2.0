# # -*- coding: utf-8 -*-
# # this file is released under public domain and you can use without limitations
#
# # ----------------------------------------------------------------------------------------------------------------------
# # this is the main application menu add/remove items as required
# # ----------------------------------------------------------------------------------------------------------------------
#
# response.menu = [
#     (T('Home'), False, URL('default', 'index'), [])
# ]
#
# # ----------------------------------------------------------------------------------------------------------------------
# # provide shortcuts for development. you can remove everything below in production
# # ----------------------------------------------------------------------------------------------------------------------
#
# if not configuration.get('app.production'):
#     _app = request.application
#     response.menu += [
#         (T('My Sites'), False, URL('admin', 'default', 'site')),
#         (T('This App'), False, '#', [
#             (T('Design'), False, URL('admin', 'default', 'design/%s' % _app)),
#             (T('Controller'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/controllers/%s.py' % (_app, request.controller))),
#             (T('View'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/views/%s' % (_app, response.view))),
#             (T('DB Model'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/models/db.py' % _app)),
#             (T('Menu Model'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/models/menu.py' % _app)),
#             (T('Config.ini'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/private/appconfig.ini' % _app)),
#             (T('Layout'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/views/layout.html' % _app)),
#             (T('Stylesheet'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % _app)),
#             (T('Database'), False, URL(_app, 'appadmin', 'index')),
#             (T('Errors'), False, URL(
#                 'admin', 'default', 'errors/' + _app)),
#             (T('About'), False, URL(
#                 'admin', 'default', 'about/' + _app)),
#         ]),
#     ]
#

# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(IMG(_src='https://i.imgur.com/A2LRvVK.png',_alt="My Logo",_style= "margin:20px 10px"), _href=URL('default','index'))
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''
# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

#response.menu = [
#    (T('Home'), False, URL('default', 'index'), [])
#]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # Buttons and redirection for our navigation bar
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('Home'), False, '/ravexchange/default/'),
        (T('Events'), False, '/ravexchange/default/events'),
        (T('Buy'), False, '/ravexchange/default/buy'),
        (T('Sell'), False, '/ravexchange/default/sell')

    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()

