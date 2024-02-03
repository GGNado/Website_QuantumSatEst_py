from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from database.Database import *

router = APIRouter(
	tags=['Magazzino'],
	prefix='/api/v1.0/magazzino'
)

templates = Jinja2Templates(
	directory='templates',
	autoescape=False,
	auto_reload=True
)


@router.get('/')
async def getPagina(req: Request):
	return templates.TemplateResponse(
		'magazzino.html', {
			'request': req,
			'oggetti': getRicambi()
		}
	)

@router.delete("/{id}")
async def eliminaRicambio(id: int):
	deleteRicambioByID(id)

@router.get("/add")
async def cambiaPag(req: Request):
	return templates.TemplateResponse(
		'magazzinoAdd.html', {
			'request': req,
		}
	)
@router.post("/add")
async def addCliente(r: Ricambio):
	aggiungiRicambio(r)

@router.get("/{id}/edit")
async def cambiaPag(req: Request, id: int):
	return templates.TemplateResponse(
		'magazzinoEdit.html', {
			'request': req,
			'oggetto': getRicambioById(id)
		}
	)

@router.put("/edit")
async def editMagazzino(oggetto: Ricambio):
	updateRicambio(oggetto)

@router.get("/filtro/{tipo}/{marca}/{modello}/{quantita}/{posizione}")
async def filtraMagazzino(req: Request, tipo: str = "", marca: str = "", modello: str = "", quantita: int = 0, posizione: str = ""):
	return templates.TemplateResponse(
		'magazzino.html', {
			'request': req,
			'oggetti': getRicambiFiltro(tipo, marca, modello, quantita, posizione)
		}
	)

