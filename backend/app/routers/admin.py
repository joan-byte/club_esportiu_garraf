from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, crud
from ..database import get_db

router = APIRouter(
    prefix="/administradores",
    tags=["administradores"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.Administrador])
def read_administradores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    administradores = crud.get_administradores(db, skip=skip, limit=limit)
    return administradores

@router.post("/", response_model=schemas.Administrador)
def create_administrador(administrador: schemas.AdministradorCreate, db: Session = Depends(get_db)):
    return crud.create_administrador(db=db, administrador=administrador)

@router.get("/{administrador_id}", response_model=schemas.Administrador)
def read_administrador(administrador_id: int, db: Session = Depends(get_db)):
    db_administrador = crud.get_administrador(db, administrador_id=administrador_id)
    if db_administrador is None:
        raise HTTPException(status_code=404, detail="Administrador not found")
    return db_administrador

@router.put("/{administrador_id}", response_model=schemas.Administrador)
def update_administrador(administrador_id: int, administrador: schemas.AdministradorCreate, db: Session = Depends(get_db)):
    return crud.update_administrador(db=db, administrador_id=administrador_id, administrador=administrador)

@router.delete("/{administrador_id}")
def delete_administrador(administrador_id: int, db: Session = Depends(get_db)):
    crud.delete_administrador(db=db, administrador_id=administrador_id)
    return {"message": "Administrador deleted successfully"}