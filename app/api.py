from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SchoolGradeDataOutSchema
from app.models import SchoolGradeData
from typing import List
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


@home_router.get("/get_data", name='home:home')
async def get_data(req: Request, db: Session = Depends(get_db)):
	"""function to filter the dataset on ajax request from frontend
	Returns:
		[SchoolGradeDataOutSchema]
	"""
	# query_params = dict(req.query_params)  # Query Parameters for Filtering Purpose
	# data = db.query(SchoolGradeData).all()
	data = {
		"draw": 1,
		"recordsTotal": 6,
		"recordsFiltered": 6,
		'data': [
			{
				"code": "01M015",
				"school_name": "P.S. 015 Roberto Clemente",
				"year": "2015-2016",
				"category": "All Students",
				"total_enrollment": "10",
				"male_count": "5",
				"female_count": "5",
				"asian_count": "5",
				"other_count": "5",
				"ela_test_takers": "10",
				"math_test_takers": "10"
			},
			{
				"code": "01M015",
				"school_name": "P.S. 015 Roberto Clemente",
				"year": "2015-2016",
				"category": "All Students",
				"total_enrollment": "10",
				"male_count": "5",
				"female_count": "5",
				"asian_count": "5",
				"other_count": "5",
				"ela_test_takers": "10",
				"math_test_takers": "10"
			},
			{
				"code": "01M015",
				"school_name": "P.S. 015 Roberto Clemente",
				"year": "2015-2016",
				"category": "All Students",
				"total_enrollment": "10",
				"male_count": "5",
				"female_count": "5",
				"asian_count": "5",
				"other_count": "5",
				"ela_test_takers": "10",
				"math_test_takers": "10"
			},
			{
				"code": "01M015",
				"school_name": "P.S. 015 Roberto Clemente",
				"year": "2015-2016",
				"category": "All Students",
				"total_enrollment": "10",
				"male_count": "5",
				"female_count": "5",
				"asian_count": "5",
				"other_count": "5",
				"ela_test_takers": "10",
				"math_test_takers": "10"
			},
			{
				"code": "01M015",
				"school_name": "P.S. 015 Roberto Clemente",
				"year": "2015-2016",
				"category": "All Students",
				"total_enrollment": "10",
				"male_count": "5",
				"female_count": "5",
				"asian_count": "5",
				"other_count": "5",
				"ela_test_takers": "10",
				"math_test_takers": "10"
			},
			{
				"code": "01M015",
				"school_name": "P.S. 015 Roberto Clemente",
				"year": "2015-2016",
				"category": "All Students",
				"total_enrollment": "10",
				"male_count": "5",
				"female_count": "5",
				"asian_count": "5",
				"other_count": "5",
				"ela_test_takers": "10",
				"math_test_takers": "10"
			}
		]}
	return data
