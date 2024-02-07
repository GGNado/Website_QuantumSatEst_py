from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from database.Database import *

router = APIRouter(
	tags=['Riparazioni'],
	prefix='/api/v1.0/riparazioni'
)

templates = Jinja2Templates(
	directory='templates',
	autoescape=False,
	auto_reload=True
)


@router.get('/')
async def getPagina(req: Request):
	return templates.TemplateResponse(
		'riparazioni.html', {
			'request': req,
			'riparazioni': getRiparazioni(),
			'cliente': None
		}
	)

@router.get('/{id}')
async def getPagina(req: Request, id: int):
	return templates.TemplateResponse(
		'riparazioni.html', {
			'request': req,
			'riparazioni': getRiparazioniByFK_Cliente(id),
			'cliente': getClienteById(id)
		}
	)

@router.get("/{id}/add")
async def getPagina(id: int, req: Request):
	return templates.TemplateResponse(
		'riparazioniAdd.html', {
			'request': req,
			'cliente': getClienteById(id)
		}
	)

@router.post("/add")
async def aggiungiRiparazione(rip: RiparazioneInput):
	addRiparazioni(rip)

@router.delete("/{id}")
async def eliminaRiparazione(id: int):
	deleteRiparazione(id)

@router.put("/edit")
async def modificaRiparazione(rip: RiparazioneInput):
	updateRiparazioni(rip)

@router.get("/{id}/edit")
async def cambiaPag(req: Request, id: int):
	return templates.TemplateResponse(
		'RiparazioniEdit.html', {
			'request': req,
			'rip': getRiparazioniById(id)
		}
	)
