from pydantic import BaseModel


class SchoolGradeDataOutSchema(BaseModel):
	id: int
	code: str
	school_name: str
	category:  str
	year:  str
	total_enrollment:  int
	grade_k:  str
	grade_1:  str
	grade_2:  str
	grade_3:  str
	grade_4:  str
	grade_5:  str
	grade_6:  str
	grade_7:  str
	grade_8:  str
	male_count:  str
	female_count:  str
	asian_count:  str
	black_count:  str
	hispanic_count:  str
	other_count:  str
	white_count:  str
	ela_test_takers:  str
	ela_l1:  str
	ela_l2:  str
	ela_l3:  str
	ela_l4:  str
	ela_l3_l4:  str
	math_test_takers:  str
	math_l1:  str
	math_l2:  str
	math_l3:  str
	math_l4:  str
	math_l3_l4:  str
	
	
	class Config:
		orm_mode = True


