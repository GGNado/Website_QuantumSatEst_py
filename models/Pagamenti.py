from pydantic import BaseModel
from datetime import date

class Pagamento(BaseModel):
    id: int
    dataPagamento: date
    importo: float
    fk_riparazione: int
