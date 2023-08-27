# imports 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(7)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'

class Coreset(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    rarity = db.Column(db.String(150))
    size = db.Column(db.String(150))
    release_date = db.Column(db.String(200))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,name,rarity, size, release_date,user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.rarity = rarity
        self.size = size
        self.release_date= release_date
        self.user_token = user_token

# coreset = Coreset(name, rarity, size, release_date, user_token = user_token )

    def __repr__(self):
        return f'The following mini has been added to the coreset: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class CoresetSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name','rarity','size', 'release']

coreset_schema = CoresetSchema()
coresets_schema = CoresetSchema(many=True)


class Wish(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    rarity = db.Column(db.String(150))
    size = db.Column(db.String(150))
    release_date = db.Column(db.String(200))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,name,rarity, size, release_date,user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.rarity = rarity
        self.size = size
        self.release_date= release_date
        self.user_token = user_token

# coreset = Coreset(name, rarity, size, release_date, user_token = user_token )

    def __repr__(self):
        return f'The following mini has been added to the coreset: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class WishSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name','rarity','size', 'release']

wish_schema = WishSchema()
wishs_schema = WishSchema(many=True)

class Set(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    rarity = db.Column(db.String(150))
    size = db.Column(db.String(150))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,name,rarity, size, release_date,user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.rarity = rarity
        self.size = size
        self.user_token = user_token

# coreset = Coreset(name, rarity, size, release_date, user_token = user_token )

    def __repr__(self):
        return f'The following mini has been added to the coreset: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class SetSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name','rarity','size']

set_schema = SetSchema()
sets_schema = SetSchema(many=True)