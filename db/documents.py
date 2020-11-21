from mongoengine import Document
from mongoengine import fields

class User(Document):
	first_name = fields.StringField()
	last_name = fields.StringField()
	email = fields.EmailField(unique=True, required=True)