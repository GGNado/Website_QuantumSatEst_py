from pydantic import BaseModel

class Oggetto(BaseModel):
    id: int
    nome: str
    marca: str
    modello: str
    matricola: str
    fk_riparazione: int