from pydantic import BaseModel, Field
from database import Database

class Cliente(BaseModel):
	id: int
	nome: str = Field(default="Nome")
	cognome: str = Field(default="Cognome")
	telefono: str = Field(default="000-000-000")
	email: str = Field(default="nome@dominio.com")

	def getNumeroRiparazioni(self):
		return Database.getCountRiparazioniByID(self.id)




