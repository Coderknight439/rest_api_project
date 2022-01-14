from pydantic import BaseModel, validator
from typing import List


class SchoolGradeDataOutSchema(BaseModel):
	id: int
	code: str
	school_name: str
	category:  str
	year:  str
	total_enrollment:  int
	grade_k:  int
	grade_1:  int
	grade_2:  int
	grade_3:  int
	grade_4:  int
	grade_5:  int
	grade_6:  int
	grade_7:  int
	grade_8:  int
	male_count:  int
	female_count:  int
	asian_count:  int
	black_count:  int
	hispanic_count:  int
	other_count:  int
	white_count:  int
	ela_test_takers:  int
	ela_l1:  int
	ela_l2:  int
	ela_l3:  int
	ela_l4:  int
	ela_l3_l4:  int
	math_test_takers:  int
	math_l1:  int
	math_l2:  int
	math_l3:  int
	math_l4:  int
	math_l3_l4:  int
	
	
	class Config:
		orm_mode = True
	

class DataTableSchema(BaseModel):
	data: List[SchoolGradeDataOutSchema]

