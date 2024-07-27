from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, crud
from ..database import get_db

router = APIRouter(
    prefix="/socios",
    tags=["socios"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.Socio])
def read_socios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    socios = crud.get_socios(db, skip=skip, limit=limit)
    return socios

@router.post("/", response_model=schemas.Socio)
def create_socio(socio: schemas.SocioCreate, db: Session = Depends(get_db)):
    return crud.create_socio(db=db, socio=socio)

@router.get("/{socio_id}", response_model=schemas.Socio)
def read_socio(socio_id: int, db: Session = Depends(get_db)):
    db_socio = crud.get_socio(db, socio_id=socio_id)
    if db_socio is None:
        raise HTTPException(status_code=404, detail="Socio not found")
    return db_socio

@router.put("/{socio_id}", response_model=schemas.Socio)
def update_socio(socio_id: int, socio: schemas.SocioCreate, db: Session = Depends(get_db)):
    return crud.update_socio(db=db, socio_id=socio_id, socio=socio)

@router.delete("/{socio_id}")
def delete_socio(socio_id: int, db: Session = Depends(get_db)):
    crud.delete_socio(db=db, socio_id=socio_id)
    return {"message": "Socio deleted successfully"}