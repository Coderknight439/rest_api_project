"""
This File Contains SQLAlchemy Base Model.
"""

from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """
    Base Class to Create All SqlAlchemy Models
    """
    id: Any
    __name__: str
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        """
        :return: Returns DB Table name as Plural
        """
        return self.__name__.lower() + 's'
