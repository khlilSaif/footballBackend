from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from ..database import Base

class Actuality(Base):
    __tablename__ = 'actuality'
    
    id = Column(Integer, primary_key= True, nullable=False)
    date = Column(DateTime, nullable=True, default = datetime.utcnow())
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    type = Column(String, nullable=True)
    body = Column(String, nullable=True)
    