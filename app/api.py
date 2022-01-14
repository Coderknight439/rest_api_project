from fastapi import APIRouter


home_router = APIRouter(
		tags=['Home']
)


@home_router.get("/root", name='home:root')
async def read_root():
	"""Main function of the web application

	Returns:
		Dict -- {"Hello":  "World"}
	"""
	return {"Hello": "World"}
