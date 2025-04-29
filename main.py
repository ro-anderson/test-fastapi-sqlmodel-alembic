from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreURLChoices, BandCreate, Band, Album
from typing import Annotated
from db import init_db, get_session
from sqlmodel import Session, select



app = FastAPI()

@app.post("/bands")
async def create_band(
    band_data: BandCreate,
    session: Session = Depends(get_session)
)-> Band:
    band = Band(name=band_data.name, genre=band_data.genre)
    session.add(band)

    if band_data.albums:
        for album in band_data.albums:
            album_obj = Album(title=album.title,
                          release_date=album.release_date,
                          band=band)
            session.add(album_obj)
            session.commit()
            session.refresh(album_obj)
            band.albums.append(album_obj)

    session.add(band)
    session.commit()
    session.refresh(band)
    return band
    
@app.get("/bands/{band_id}", response_model=Band)
async def band(
    band_id: Annotated[int, Path(title="The ID of the band", gt=0)],
    session: Session = Depends(get_session)
)-> Band:
    band = session.get(Band, band_id)
    if not band:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get("/bands", response_model=list[Band])
async def bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,
    session: Session = Depends(get_session), 
)-> list[Band]:
    
    band_list = session.exec(select(Band)).all()
    if genre:
        band_list = [band for band in band_list if band.genre.value.lower() == genre.value]
    if q:
        band_list = [band for band in band_list if q.lower() in band.name.lower()]
    return band_list

