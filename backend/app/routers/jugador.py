from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, crud
from ..database import get_db

router = APIRouter(
    prefix="/jugadores",
    tags=["jugadores"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.Jugador])
def read_jugadores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    jugadores = crud.get_jugadores(db, skip=skip, limit=limit)
    return jugadores

@router.post("/", response_model=schemas.Jugador)
def create_jugador(jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    return crud.create_jugador(db=db, jugador=jugador)

@router.get("/{jugador_id}", response_model=schemas.Jugador)
def read_jugador(jugador_id: int, db: Session = Depends(get_db)):
    db_jugador = crud.get_jugador(db, jugador_id=jugador_id)
    if db_jugador is None:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return db_jugador

@router.put("/{jugador_id}", response_model=schemas.Jugador)
def update_jugador(jugador_id: int, jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    return crud.update_jugador(db=db, jugador_id=jugador_id, jugador=jugador)

@router.delete("/{jugador_id}")
def delete_jugador(jugador_id: int, db: Session = Depends(get_db)):
    crud.delete_jugador(db=db, jugador_id=jugador_id)
    return {"message": "Jugador deleted successfully"}