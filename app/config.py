import os
from pydantic import BaseSettings

from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, Response
from fastapi import status


class Settings(BaseSettings):
	API_V1_STR: str = "1"
	PROJECT_NAME: str = "REST API Project"
	POSTGRES_SERVER: str
	POSTGRES_PORT: str
	POSTGRES_USER: str
	POSTGRES_PASSWORD: str
	POSTGRES_DB: str
	
	TEMPLATES_DIR: str = "app/templates"
	
	
	class Config:
		case_sensitive = True
		env_file = ".env"


def get_settings():
	config = Settings()
	for k, v in os.environ.items():
		if hasattr(config, k):
			setattr(config, k, v)
	return config


settings = get_settings()

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


class Renderer:
	
	def __init__(self, request):
		self.request = request
		self.variable_dict = {
			"request": request,
		}
		self.cookies = {}
		self.delete_cookies = []
	
	def set(self, name=None, value=None, **kwargs):
		if kwargs:
			self.variable_dict.update(kwargs)
		else:
			self.variable_dict[name] = value
		return self
	
	def cookie(self, name=None, value=None, httponly=True):
		if name and value:
			self.cookies[name] = dict(
					value=value,
					httponly=httponly
			)
		return self
	
	def delete_cookie(self, name=None):
		if name:
			self.delete_cookies.append(name)
		return self
	
	def render(self, page, context=None):
		response = templates.TemplateResponse(
				name=page,
				context=self.variable_dict
		)
		return self.respond(response)
	
	def redirect(self, url, status_code=status.HTTP_303_SEE_OTHER):
		response = RedirectResponse(url=url)
		response.status_code = status_code
		return self.respond(response)
	
	def respond(self, response: Response):
		if self.cookies:
			for key, val in self.cookies.items():
				response.set_cookie(key=key, value=val.get('value'), httponly=val.get('httponly', True))
		if self.delete_cookies:
			for del_cookie in self.delete_cookies:
				response.delete_cookie(key=del_cookie)
		
		return response
