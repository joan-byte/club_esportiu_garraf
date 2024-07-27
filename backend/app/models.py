# backend/app/models.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Tabla de asociación para Reserva y Jugador
reserva_jugador = Table(
    'reserva_jugador',
    Base.metadata,
    Column('reserva_id', Integer, ForeignKey('reservas.id'), primary_key=True),
    Column('jugador_id', Integer, ForeignKey('jugadores.id'), primary_key=True)
)

class Administrador(Base):
    __tablename__ = "administradores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    password = Column(String)

class Socio(Base):
    __tablename__ = "socios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String)
    tipo_socio = Column(String)
    password = Column(String)

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    tipo_jugador = Column(String)

    reservas = relationship('Reserva', secondary=reserva_jugador, back_populates='jugadores')

class Pista(Base):
    __tablename__ = "pistas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo_pista = Column(String)
    tiempo_juego = Column(Integer)
    individuales = Column(Boolean)

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    pista_id = Column(Integer, ForeignKey('pistas.id'))
    dia = Column(String)
    hora_inicio = Column(String)
    hora_fin = Column(String)
    individuales = Column(Boolean)
    dobles = Column(Boolean)
    tipo_bloqueo = Column(String)

    jugadores = relationship('Jugador', secondary=reserva_jugador, back_populates='reservas')