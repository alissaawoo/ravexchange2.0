# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

def get_user_email():
    return auth.user.email if auth.user is not None else None


db.define_table('checklist',
                Field('user_email', default=get_user_email()),
                Field('title'),
                Field('memo', 'text'),
                Field('updated_on', 'datetime', update=datetime.datetime.utcnow()),
                Field('is_public', 'boolean', default=False),


                )


db.define_table('listing',
                Field('title'),
                Field('price', 'decimal(6,2)'),
                Field('sold', 'boolean'),
                Field('image', 'upload',default='static/images/No_image.png'),
                Field('name'),
                Field('user_id', db.auth_user),
                Field('phone'),
                Field('email'),
                Field('votes', 'integer', default=0),
                Field('messeged', 'text'),
                Field('date_posted', 'datetime'),
                )


# db.define_table('person',
#     Field('name', requires=IS_NOT_EMPTY()))
# db.define_table('dog',
#     Field('owner', 'reference person'),
#     Field('name', requires=IS_NOT_EMPTY()))
# db.dog.owner.requires = IS_IN_DB(db,db.person.id,'%(name)s')


db.checklist.user_email.writable = False
db.checklist.user_email.readable = False

db.checklist.is_public.writable = False
db.checklist.is_public.readable = False

db.checklist.updated_on.writable = db.checklist.updated_on.readable = False
db.checklist.id.writable = db.checklist.id.readable = False




# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
