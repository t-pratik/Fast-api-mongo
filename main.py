from typing import Optional
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db import documents
from model import user_model
import json
from fastapi.encoders import jsonable_encoder
import sys
from fastapi.testclient import TestClient


app = FastAPI()

@app.post("/db/documents")
def user(body: user_model.user_post):
	user = documents.User.objects.create(
		first_name=body.first_name,
		last_name=body.last_name,
		email=body.email,
	)

	user.save()

	return JSONResponse(content='Successfully Created', status_code=status.HTTP_200_OK)

@app.get(
	"/db/user_details",
	response_model=user_model.user_get)
async def user(email: str):
	# user = documents.User()
	 user_detail=documents.User.objects(email=email).first()

	 if not user_detail:
			return JSONResponse(content="Not Found", status_code=status.HTTP_404_NOT_FOUND)

	 # json_detail = jsonable_encoder(documents.User)
	 # return email
	 # resturn user
	 response = user_model.user_get(
	 	first_name=user_detail.first_name,
	 	last_name=user_detail.last_name,
	 	email=user_detail.email,
 	).dict()
	 return JSONResponse(content=response)
	









# try a correct one
# try string@test.com in get 
	
	


	


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
    