from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import DataTableSchema
from app.models import SchoolGradeData
from app.config import Renderer


home_router = APIRouter(
		tags=['Home']
)


@home_router.get("/", name='home:root')
async def read_root(req: Request):
	"""Root function of the web application

	Returns:
		Dict -- {"Hello":  "World"}
	"""
	renderer = Renderer(req)
	return renderer.render("home.html")


@home_router.get("/get_data", name='home:home', response_model=DataTableSchema)
async def get_data(req: Request, db: Session = Depends(get_db)):
	"""function to filter the dataset on ajax request from frontend
	Returns:
		[SchoolGradeDataOutSchema]
	"""
	query_params = dict(req.query_params)  # Query Parameters for Filtering Purpose
	data = db.query(SchoolGradeData).all()
	
	return {'data': data}

