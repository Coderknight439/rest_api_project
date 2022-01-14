"""
Model Class For School Grade Data
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr
from app.db.base_class import Base


class SchoolGradeData(Base):
    """
    Define Table of School Grade Data
    """
    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    school_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    year = Column(String, nullable=False)
    total_enrollment = Column(Integer, nullable=False)
    grade_k = Column(Integer, nullable=True)
    grade_1 = Column(Integer, nullable=True)
    grade_2 = Column(Integer, nullable=True)
    grade_3 = Column(Integer, nullable=True)
    grade_4 = Column(Integer, nullable=True)
    grade_5 = Column(Integer, nullable=True)
    grade_6 = Column(Integer, nullable=True)
    grade_7 = Column(Integer, nullable=True)
    grade_8 = Column(Integer, nullable=True)
    male_count = Column(Integer, nullable=True)
    female_count = Column(Integer, nullable=True)
    asian_count = Column(Integer, nullable=True)
    black_count = Column(Integer, nullable=True)
    hispanic_count = Column(Integer, nullable=True)
    other_count = Column(Integer, nullable=True)
    white_count = Column(Integer, nullable=True)
    ela_test_takers = Column(Integer, nullable=True)
    ela_l1 = Column(Integer, nullable=True)
    ela_l2 = Column(Integer, nullable=True)
    ela_l3 = Column(Integer, nullable=True)
    ela_l4 = Column(Integer, nullable=True)
    ela_l3_l4 = Column(Integer, nullable=True)
    math_test_takers = Column(Integer, nullable=True)
    math_l1 = Column(Integer, nullable=True)
    math_l2 = Column(Integer, nullable=True)
    math_l3 = Column(Integer, nullable=True)
    math_l4 = Column(Integer, nullable=True)
    math_l3_l4 = Column(Integer, nullable=True)

    @declared_attr
    def __tablename__(self) -> str:
        """
        :return: Table Name
        """
        return 'school_grade_data'
