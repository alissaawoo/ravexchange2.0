# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    return dict(message=T('Welcome to ravExchange!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)



# @auth.requires_login()
# def add():
    # #Function to add a listing
    # grid = SQLFORM(db.checklist)
    # if grid.process().accepted:
    #     session.flash = T('added')
    #     redirect(URL('default', 'posting'))
    # export_classes = dict(csv=True, json=False, html=False,
    # tsv=False, xml=False, csv_with_hidden_cols=False,
    # tsv_with_hidden_cols=False)
    # return dict(grid=grid)

# @auth.requires_login()
# def view():
# 	# Function to view a listing
#     p = db.listing(request.args(0)) or redirect(URL('default', 'posting'))
#     grid = SQLFORM(db.listing, record = p, readonly = True)
#     button = A('return to listings', _class='btn btn-default', _href=URL('default', 'posting'))
#     export_classes = dict(csv=True, json=False, html=False,
# 	tsv=False, xml=False, csv_with_hidden_cols=False,
# 	tsv_with_hidden_cols=False)
#     return dict(p=p, button = button)


# def buy():
#     #the posting to show the grid
#     show_all = request.args(0) == 'all'
#     q = (db.listing) if show_all else (db.listing.sold == False)
#     export_classes = dict(csv=True, json=False, html=False,
#          tsv=False, xml=False, csv_with_hidden_cols=False,
#          tsv_with_hidden_cols=False)

def events():
    return dict(message=T('Welcome to ravExchange!'))

def buy():
    return dict(message=T('Welcome to ravExchange!'))

# def sell():
#     return dict(message=T('Welcome to ravExchange!'))



def sell():
    # Function to add a listing
    form = SQLFORM(db.listing)
    if form.accepted:
        session.flash = T("Checklist added.")
        redirect(URL('default', 'buy'))
    elif form.errors:
        session.flash = T('Please correct the info')
    return dict(form=form)
    # form = FORM('Your name:',
    #           INPUT(_name='name', requires=IS_NOT_EMPTY()),
    #           INPUT(_type='submit'))
    # if form.process().accepted:
    #     session.flash = 'form accepted'
    #     redirect(URL('buy'))
    # elif form.errors:
    #     response.flash = 'form has errors'
    # else:
    #     response.flash = 'please fill the form'
    # return dict(form=form)

def buy():
    return dict()