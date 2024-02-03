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
			'riparazioni': getRiparazioni()
		}
	)

@router.get('/dsadsa')
async def getPagina():
	return getRiparazioni()




