from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column, String, Integer,create_engine, DateTime,text


Base = declarative_base()

connect_pg = "postgresql://postgres:1122@localhost:5432/postgres"

engine = create_engine(connect_pg,echo=True)
 
Session = sessionmaker()

class ScholarShips(Base):
     __tablename__ = 'scholarshipData'
     id = Column(Integer(), primary_key=True, nullable=False)
     name = Column(String(500))
     degrees = Column(String(100))
     funds = Column(String(90))
     date = Column(String(90))
     location = Column(String(70))


     def __repr__(self):
         return f"<Student Id={self.id} Name={self.name} degrees={self.degrees} funds={self.funds} date = {self.date} location = {self.location}>"


