from datetime import date
from enum import Enum
from pydantic import field_validator
from sqlmodel import Field, SQLModel, Relationship

class GenreURLChoices(str, Enum):
    ROCK = "rock"
    ELECTRONIC = "electronic"
    METAL = "metal"
    HIP_HOP = "hip-hop"

class GenreChoices(str, Enum):
    ROCK = "rock"
    ELECTRONIC = "electronic"
    METAL = "metal"
    HIP_HOP = "hip-hop"

class AlbumBase(SQLModel):
    title: str
    release_date: date
    band_id: int | None = Field(default=None, foreign_key="band.id")
    
class Album(AlbumBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")

class BandBase(SQLModel):
    name: str
    genre: GenreURLChoices

class BandCreate(BandBase):
    albums: list[AlbumBase] | None = None
    @field_validator("genre", mode="before")
    def validate_case_genre(cls, value):
        return value
    
class Band(BandBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")
    
    
    
    

    