from sqlalchemy.orm import Session
from . import models, schemas

# Administradores
def get_administrador(db: Session, admin_id: int):
    return db.query(models.Administrador).filter(models.Administrador.id == admin_id).first()

def get_administrador_by_nombre(db: Session, nombre: str):
    return db.query(models.Administrador).filter(models.Administrador.nombre == nombre).first()

def create_administrador(db: Session, admin: schemas.AdministradorCreate):
    db_admin = models.Administrador(nombre=admin.nombre, password=admin.password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_administradores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Administrador).offset(skip).limit(limit).all()

# Socios
def get_socio(db: Session, socio_id: int):
    return db.query(models.Socio).filter(models.Socio.id == socio_id).first()

def get_socio_by_email(db: Session, email: str):
    return db.query(models.Socio).filter(models.Socio.email == email).first()

def create_socio(db: Session, socio: schemas.SocioCreate):
    db_socio = models.Socio(**socio.dict())
    db.add(db_socio)
    db.commit()
    db.refresh(db_socio)
    return db_socio

def get_socios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Socio).offset(skip).limit(limit).all()

# Jugadores
def get_jugador(db: Session, jugador_id: int):
    return db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()

def create_jugador(db: Session, jugador: schemas.JugadorCreate):
    db_jugador = models.Jugador(**jugador.dict())
    db.add(db_jugador)
    db.commit()
    db.refresh(db_jugador)
    return db_jugador

def get_jugadores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Jugador).offset(skip).limit(limit).all()

# Pistas
def get_pista(db: Session, pista_id: int):
    return db.query(models.Pista).filter(models.Pista.id == pista_id).first()

def create_pista(db: Session, pista: schemas.PistaCreate):
    db_pista = models.Pista(**pista.dict())
    db.add(db_pista)
    db.commit()
    db.refresh(db_pista)
    return db_pista

def get_pistas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pista).offset(skip).limit(limit).all()

# Reservas
def get_reserva(db: Session, reserva_id: int):
    return db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()

def create_reserva(db: Session, reserva: schemas.ReservaCreate):
    db_reserva = models.Reserva(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def get_reservas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Reserva).offset(skip).limit(limit).all()