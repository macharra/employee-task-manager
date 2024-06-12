from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    department = Column(String)

Base.metadata.create_all(engine)
