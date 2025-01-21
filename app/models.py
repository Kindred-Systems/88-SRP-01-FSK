from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime


class World(db.Model):
    __tablename__ = 'worlds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with Hex
    hexes = relationship('Hex', back_populates='world', cascade="all, delete-orphan")

    # Relationship with Principal
    principals = relationship('Principal', back_populates='world', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<World {self.name}>"


class Hex(db.Model):
    __tablename__ = 'hexes'
    id = db.Column(db.Integer, primary_key=True)
    position_x = db.Column(db.Integer, nullable=False)
    position_y = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(50), nullable=True)  # e.g., forest, mountain, plains
    resources = db.Column(db.String(255), nullable=True)  # Comma-separated resource types
    world_id = db.Column(db.Integer, ForeignKey('worlds.id'), nullable=False)

    # Relationship with World
    world = relationship('World', back_populates='hexes')

    # Relationship with Principal
    controlled_by = db.Column(db.Integer, ForeignKey('principals.id'), nullable=True)
    principal = relationship('Principal', back_populates='controlled_hexes', uselist=False)

    def __repr__(self):
        return f"<Hex ({self.position_x}, {self.position_y}) in World {self.world_id}>"


class Principal(db.Model):
    __tablename__ = 'principals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(50), nullable=False)  # e.g., Elf, Human, Dwarf
    abilities = db.Column(db.Text, nullable=True)  # JSON-like string for abilities
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    world_id = db.Column(db.Integer, ForeignKey('worlds.id'), nullable=False)

    # Relationship with World
    world = relationship('World', back_populates='principals')

    # Relationship with Hex
    controlled_hexes = relationship('Hex', back_populates='principal')

    def __repr__(self):
        return f"<Principal {self.name} ({self.race}) in World {self.world_id}>"
