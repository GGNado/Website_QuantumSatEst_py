from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from database.Database import *

router = APIRouter(
	tags=['Clienti'],
	prefix='/api/v1.0/clienti'
)

templates = Jinja2Templates(
	directory='templates',
	autoescape=False,
	auto_reload=True
)

@router.get('/')
async def getPagina(req: Request):
	return templates.TemplateResponse(
		'clienti.html', {
			'request': req,
			'clienti': getClienti()
		}
	)

@router.delete("/{id}")
async def eliminaCliente(id: int):
	deleteClienteByID(id)

@router.get("/add")
async def cambiaPag(req: Request):
	return templates.TemplateResponse(
		'clientiAdd.html', {
			'request': req,
		}
	)

@router.post("/add")
async def addCliente(c: Cliente):
	aggiungiCliente(c)

@router.get("/{id}/edit")
async def cambiaPag(req: Request, id: int):
	return templates.TemplateResponse(
		'clientiEdit.html', {
			'request': req,
			'cliente': getClienteById(id)
		}
	)

@router.put("/edit")
async def editCliente(cliente: Cliente):
	updateCliente(cliente)

@router.get("/filtro/{nome}/{cognome}/{id}/{telefono}")
async def filtraClienti(req: Request, nome: str = "", cognome: str = "", id: int = "", telefono: str = ""):
	return templates.TemplateResponse(
		'clienti.html', {
			'request': req,
			'clienti': getClientiFiltro(nome, cognome, id, telefono)
		}
	)


