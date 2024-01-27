from datetime import date

from pydantic import BaseModel, Field

class Riparazione(BaseModel):
    id: int
    dataIngresso: date
    dataUscita: date = Field(default=date.min)
    descrizioneGuasto: str
    descrizioneRiparazione: str
    prezzo: float = Field(default=0.0, ge=0)
    fk_cliente: int
    fk_stato_riparazione: int = Field(default=0)
