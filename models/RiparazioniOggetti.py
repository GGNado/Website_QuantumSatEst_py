from pydantic import BaseModel

class RiparazioneInput(BaseModel):
    id: int = 0
    descrizioneGuasto: str
    nomeOggetto: str
    marcaOggetto: str = "Nessuna Marca"
    modelloOggetto: str = "Nessun Modello"
    matricolaOggetto: str = "Nessuna Matricola"
    prezzo: float = 0.0
    componentiExtra: str = "Nessun Componente Extra"
