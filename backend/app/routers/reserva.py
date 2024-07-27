from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, crud
from ..database import get_db

router = APIRouter(
    prefix="/reservas",
    tags=["reservas"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.Reserva])
def read_reservas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservas = crud.get_reservas(db, skip=skip, limit=limit)
    return reservas

@router.post("/", response_model=schemas.Reserva)
def create_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    return crud.create_reserva(db=db, reserva=reserva)

@router.get("/{reserva_id}", response_model=schemas.Reserva)
def read_reserva(reserva_id: int, db: Session = Depends(get_db)):
    db_reserva = crud.get_reserva(db, reserva_id=reserva_id)
    if db_reserva is None:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return db_reserva

@router.put("/{reserva_id}", response_model=schemas.Reserva)
def update_reserva(reserva_id: int, reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    return crud.update_reserva(db=db, reserva_id=reserva_id, reserva=reserva)

@router.delete("/{reserva_id}")
def delete_reserva(reserva_id: int, db: Session = Depends(get_db)):
    crud.delete_reserva(db=db, reserva_id=reserva_id)
    return {"message": "Reserva deleted successfully"}