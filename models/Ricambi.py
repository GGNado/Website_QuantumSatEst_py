from pydantic import BaseModel, Field
class Ricambio(BaseModel):
	id: int
	tipo: str
	marca: str = Field(default="Nessuna Marca")
	modello: str = Field(default="Nessun Modello")
	quantita: int = Field(default=0)
	posizione: str = Field(default="Nessuna Posizione")
	guasto: int = Field(default=0)

	def isGausto(self):
		if self.guasto == 0:
			return "No"
		else:
			return "Si"
