from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class OurBaseModel(BaseModel):
    class Config:
        from_attributes = True #Retrieving and validating data from the database using Pydantic's ORM mode
     
class OurBaseModelOut(OurBaseModel): #We want to return classes with message and status
    message: Optional[str] = None
    status: Optional[str] = None

    
class ActualityOut(OurBaseModelOut):
    id: Optional[int] = None
    date: Optional[datetime] = datetime.utcnow()  # Correct type for date field
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    body: Optional[str] = None
    
class ActualitiesResponseOut(OurBaseModelOut):
    list: Optional[List[ActualityOut]] = None