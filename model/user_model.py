from pydantic import BaseModel
import json

from json import JSONEncoder
class user_post(BaseModel):
	first_name: str
	last_name: str
	email: str


class user_get(BaseModel):
	first_name: str
	last_name: str
	email: str
