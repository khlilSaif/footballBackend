from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import Depends
from .. import schemas
from .. import models

router = APIRouter(
    prefix="/actuality"
)

@router.get('/', response_model = schemas.ActualitiesResponseOut) 
async def get_actualities(db: Session = Depends(get_db)):
    actualities =  db.query(models.Actuality).all()
    return schemas.ActualitiesResponseOut( list= actualities,
        message = "good job habibi",
        status = status.HTTP_200_OK
    )
