import uvicorn
import jinja2
import httptools
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import database.Database
from controller.ClientiRotte import router as ClientiRotte
from controller.MagazzinoRotte import router as MagazzinoRotte
from controller.RiparazioniRotte import router as RiparazioniRotte
# from controller.SchedeRotte import router as schedaRotte

webapp = FastAPI(
	title='Palestra Programmazioni',
	decription='Tener traccia delle programmazioni'
)

templates = Jinja2Templates(
	directory='templates',
	autoescape=False,
	auto_reload=True
)

webapp.mount(
	'/static',
	app=StaticFiles(directory='static'),
	name='static'
)


@webapp.get('/', response_class=HTMLResponse)
async def root(req: Request):
	marca, numero = database.Database.numeroRiparazioniPerMarca()
	return templates.TemplateResponse(
		'root.html', {
			'request': req,
			'completate': database.Database.getAllStatoRiparazioni(3),
			'inAttesa': database.Database.getAllStatoRiparazioni(1),
			'effettivo': database.Database.getGuadagnoEffettivo(),
			'possibile': database.Database.getGuadagnoPossibile(),
			"marche": marca,
			"numero_riparazioni": numero
		}
	)

webapp.include_router(ClientiRotte)
webapp.include_router(MagazzinoRotte)
# webapp.include_router(ClientiRotte)
webapp.include_router(RiparazioniRotte)

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host='0.0.0.0',
		port=3000,
		# use_colors = False,
		http='httptools',
		reload=True
	)
