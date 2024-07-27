from pydantic import BaseModel
from typing import List, Optional

# Esquemas para Administradores
class AdministradorBase(BaseModel):
    nombre: str

class AdministradorCreate(AdministradorBase):
    password: str

class Administrador(AdministradorBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Socios
class SocioBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: str
    tipo_socio: str

class SocioCreate(SocioBase):
    password: str

class Socio(SocioBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Jugadores
class JugadorBase(BaseModel):
    nombre: str
    apellido: str
    tipo_jugador: str

class JugadorCreate(JugadorBase):
    pass

class Jugador(JugadorBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Pistas
class PistaBase(BaseModel):
    nombre: str
    tipo_pista: str
    tiempo_juego: int
    individuales: bool

class PistaCreate(PistaBase):
    pass

class Pista(PistaBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Reservas
class ReservaBase(BaseModel):
    pista_id: int
    dia: str
    hora_inicio: str
    hora_fin: str
    individuales: bool
    dobles: bool
    tipo_bloqueo: str

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int
    jugadores: List[Jugador] = []

    class Config:
        from_attributes = True

# Esquemas para Autenticación
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str