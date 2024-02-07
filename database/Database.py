import mysql.connector as dbms

from models.Clienti import Cliente
from models.Ricambi import Ricambio
from models.Riparazioni import Riparazione
from models.RiparazioniOggetti import RiparazioneInput
from datetime import date


def getConnection():
    return dbms.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        database = 'Quantumsatest'
    )

def getClienti():
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT * FROM Clienti"
        listaClienti = []
        cursore = connessione.cursor()
        cursore.execute(QUERY)
        results = cursore.fetchall()
        for row in results:
            listaClienti.append(Cliente(id=int(row[0]), nome=row[1], cognome=row[2], telefono=row[3], email=row[4]))
        cursore.close()
        connessione.close()
        return listaClienti

def getClienteById(cliente_id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT * FROM Clienti WHERE ID = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (cliente_id,))
        result = cursore.fetchone()
        cursore.close()
        connessione.close()

        if result:
            return Cliente(id=int(result[0]), nome=result[1], cognome=result[2], telefono=result[3], email=result[4])
        else:
            return None


def aggiungiCliente(c: Cliente):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "INSERT INTO Clienti (nome, cognome, telefono, email) VALUES (%s, %s, %s, %s)"
        dati_cliente = (c.nome, c.cognome, c.telefono, c.email)
        cursore = connessione.cursor()
        cursore.execute(QUERY, dati_cliente)
        connessione.commit()
        nuovo_cliente_id = cursore.lastrowid
        cursore.close()
        connessione.close()
        return nuovo_cliente_id

def updateCliente(cliente: Cliente):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "UPDATE Clienti SET nome = %s, cognome = %s, telefono = %s, email = %s WHERE ID = %s"
        dati_cliente = (cliente.nome, cliente.cognome, cliente.telefono, cliente.email, cliente.id)

        cursore = connessione.cursor()
        cursore.execute(QUERY, dati_cliente)
        connessione.commit()
        cursore.close()
        connessione.close()

        # Verifica se l'update ha avuto successo
        return cursore.rowcount > 0


def getCountRiparazioniByID(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        query = "SELECT COUNT(*) FROM Riparazioni WHERE FK_Cliente = %s"
        cursore = connessione.cursor()
        cursore.execute(query, (id,))
        count_riparazioni = cursore.fetchone()[0]
        cursore.close()
        connessione.close()
        return count_riparazioni

def deleteClienteByID(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        try:
            # Inizia una transazione
            connessione.start_transaction()
            # Elimina il cliente
            query_cliente = "DELETE FROM Clienti WHERE ID = %s"
            cursore = connessione.cursor()
            cursore.execute(query_cliente, (id,))
            connessione.commit()
            cursore.close()
            connessione.close()
            return True  # Ritorna True se l'eliminazione ha avuto successo
        except Exception as e:
            # Rollback in caso di errore
            connessione.rollback()
            print(f"Errore durante l'eliminazione del cliente: {e}")
            return False  # Ritorna False in caso di errore
    return False  # Ritorna False se la connessione non è riuscita

def getClientiFiltro(nome, cognome, id, telefono):
    connessione = getConnection()
    if connessione.is_connected():
        # Costruisci la query in base ai valori forniti
        QUERY = "SELECT * FROM Clienti WHERE 1=1"
        params = []

        if nome != "nullo":
            QUERY += " AND nome LIKE %s"
            params.append(f"%{nome}%")

        if cognome != "nullo":
            QUERY += " AND cognome LIKE %s"
            params.append(f"%{cognome}%")

        if id != -1:
            QUERY += " AND id = %s"
            params.append(id)

        if telefono != "nullo":
            QUERY += " AND telefono LIKE %s"
            params.append(f"%{telefono}%")

        listaClienti = []
        cursore = connessione.cursor()
        cursore.execute(QUERY, tuple(params))
        results = cursore.fetchall()
        for row in results:
            listaClienti.append(Cliente(id=int(row[0]), nome=row[1], cognome=row[2], telefono=row[3], email=row[4]))
        cursore.close()
        connessione.close()
        return listaClienti

def getRicambi():
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT * FROM Ricambi"
        listaRicambi = []
        cursore = connessione.cursor()
        cursore.execute(QUERY)
        results = cursore.fetchall()
        for row in results:
            ricambio = Ricambio(
                id=int(row[0]),
                tipo=row[1],
                marca=row[2],
                modello=row[3],
                quantita=int(row[4]),
                posizione=row[5],
                guasto=int(row[6])
            )
            listaRicambi.append(ricambio)
        cursore.close()
        connessione.close()
        return listaRicambi

def aggiungiRicambio(ricambio: Ricambio):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "INSERT INTO Ricambi (tipo, marca, modello, quantita, posizione, guasto) VALUES (%s, %s, %s, %s, %s, %s)"
        dati_ricambio = (ricambio.tipo, ricambio.marca, ricambio.modello, ricambio.quantita, ricambio.posizione, ricambio.guasto)
        cursore = connessione.cursor()
        cursore.execute(QUERY, dati_ricambio)
        connessione.commit()
        nuovo_ricambio_id = cursore.lastrowid
        cursore.close()
        connessione.close()
        return nuovo_ricambio_id

def updateRicambio(ricambio: Ricambio):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "UPDATE Ricambi SET tipo = %s, marca = %s, modello = %s, quantita = %s, posizione = %s, guasto = %s WHERE ID = %s"
        dati_cliente = (ricambio.tipo, ricambio.marca, ricambio.modello, ricambio.quantita, ricambio.posizione, ricambio.guasto, ricambio.id)

        cursore = connessione.cursor()
        cursore.execute(QUERY, dati_cliente)
        connessione.commit()
        cursore.close()
        connessione.close()

        # Verifica se l'update ha avuto successo
        return cursore.rowcount > 0

def getRicambiFiltro(tipo, marca, modello, quantita, posizione, guasto):
    connessione = getConnection()
    if connessione.is_connected():
        # Costruisci la query in base ai valori forniti
        QUERY = "SELECT * FROM Ricambi WHERE 1=1"
        params = []

        if tipo != "nullo":
            QUERY += " AND tipo LIKE %s"
            params.append(f"%{tipo}%")

        if marca != "nullo":
            QUERY += " AND marca LIKE %s"
            params.append(f"%{marca}%")

        if modello != "nullo":
            QUERY += " AND modello LIKE %s"
            params.append(f"%{modello}%")

        if posizione != "nullo":
            QUERY += " AND posizione LIKE %s"
            params.append(f"%{posizione}%")

        if quantita != -1:
            QUERY += " AND quantita = %s"
            params.append(quantita)

        if guasto != -1:
            QUERY += " AND guasto = %s"
            params.append(guasto)

        listaRicambi = []
        cursore = connessione.cursor()
        cursore.execute(QUERY, tuple(params))
        results = cursore.fetchall()
        for row in results:
            ricambio = Ricambio(
                id=int(row[0]),
                tipo=row[1],
                marca=row[2],
                modello=row[3],
                quantita=int(row[4]),
                posizione=row[5],
                guasto=int(row[6])
            )
            listaRicambi.append(ricambio)
        cursore.close()
        connessione.close()
        return listaRicambi


def deleteRicambioByID(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        try:
            # Inizia una transazione
            connessione.start_transaction()

            # Elimina il ricambio
            query_ricambio = "DELETE FROM Ricambi WHERE ID = %s"
            cursore = connessione.cursor()
            cursore.execute(query_ricambio, (id,))

            # Esegui il commit della transazione
            connessione.commit()

            # Chiudi il cursore
            cursore.close()

            # Chiudi la connessione
            connessione.close()

            return True  # Ritorna True se l'eliminazione ha avuto successo
        except Exception as e:
            # Rollback in caso di errore
            connessione.rollback()
            print(f"Errore durante l'eliminazione del ricambio: {e}")
            return False  # Ritorna False in caso di errore
    return False  # Ritorna False se la connessione non è riuscita

def getRicambioById(id):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT * FROM Ricambi WHERE ID = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (id,))
        result = cursore.fetchone()
        cursore.close()
        connessione.close()

        if result:
            return Ricambio(
                id=int(result[0]),
                tipo=result[1],
                marca=result[2],
                modello=result[3],
                quantita=int(result[4]),
                posizione=result[5],
                guasto=int(result[6])
            )
        else:
            return None

def getRiparazioni():
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT * From Riparazioni"
        listaRiparazione = []
        cursore = connessione.cursor()
        cursore.execute(QUERY)
        results = cursore.fetchall()
        for row in results:
            listaRiparazione.append(Riparazione(
                id=int(row[0]),
                dataIngresso=row[1],
                dataUscita=row[2] if row[2] else date.min,  # Assicurati che la data di uscita sia disponibile nel risultato della query
                descrizioneGuasto=str(row[3]),
                descrizioneRiparazione=str(row[4]),
                prezzo=float(row[5]),
                fk_cliente=int(row[6] if row[6] else -1),
                fk_stato_riparazione=int(row[7])
            ))
        cursore.close()
        connessione.close()
        return listaRiparazione

def getRiparazioniByFK_Cliente(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT * From Riparazioni WHERE FK_Cliente = %s"
        listaRiparazione = []
        cursore = connessione.cursor()
        cursore.execute(QUERY, (id, ))
        results = cursore.fetchall()
        for row in results:
            listaRiparazione.append(Riparazione(
                id=int(row[0]),
                dataIngresso=row[1],
                dataUscita=row[2] if row[2] else date.min,  # Assicurati che la data di uscita sia disponibile nel risultato della query
                descrizioneGuasto=str(row[3]),
                descrizioneRiparazione=str(row[4]),
                prezzo=float(row[5]),
                fk_cliente=int(row[6]),
                fk_stato_riparazione=int(row[7])
            ))
        cursore.close()
        connessione.close()
        return listaRiparazione


def addRiparazioni(rip: RiparazioneInput):
    connessione = getConnection()
    if connessione.is_connected():
        # Prima query per inserire dati nella tabella Riparazioni
        QUERY = "INSERT INTO Riparazioni (dataIngresso, descrizioneGuasto, prezzo, FK_Cliente, FK_StatoRiparazione) VALUES (%s, %s, %s, %s, %s)"
        datiRiparazione = (date.today(), rip.descrizioneGuasto, rip.prezzo, rip.id, 1)
        cursore = connessione.cursor()
        cursore.execute(QUERY, datiRiparazione)
        connessione.commit()

        # Ottieni l'ID dell'ultima riga inserita nella tabella Riparazioni
        nuovo_ricambio_id = cursore.lastrowid

        # Seconda query per inserire dati nella tabella corretta
        QUERYSec = "INSERT INTO Oggetti (nome, marca, modello, matricola, fk_riparazione, extra) VALUES (%s, %s, %s, %s, %s, %s)"
        datiOgg = (rip.nomeOggetto, rip.marcaOggetto, rip.modelloOggetto, rip.matricolaOggetto, nuovo_ricambio_id,
                   rip.componentiExtra)
        cursore.execute(QUERYSec, datiOgg)
        connessione.commit()

        cursore.close()
        connessione.close()

        return nuovo_ricambio_id

def getNomeCognomeClienteByRiparazioneId(riparazione_id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT C.nome, C.cognome FROM Clienti C INNER JOIN Riparazioni R ON C.ID = R.FK_Cliente WHERE R.ID = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (riparazione_id,))
        result = cursore.fetchone()
        cursore.close()
        connessione.close()

        if result:
            return str(result[0]) + " " +  str(result[1])  # Ritorna il nome e il cognome del cliente
        else:
            return None, None  # Ritorna None se non è stato trovato nessun cliente associato alla riparazione

def deleteRiparazione(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        try:
            # Inizia una transazione
            connessione.start_transaction()

            # Elimina il ricambio
            query_ricambio = "DELETE FROM Riparazioni WHERE ID = %s"
            cursore = connessione.cursor()
            cursore.execute(query_ricambio, (id,))

            # Esegui il commit della transazione
            connessione.commit()

            # Chiudi il cursore
            cursore.close()

            # Chiudi la connessione
            connessione.close()

            return True  # Ritorna True se l'eliminazione ha avuto successo
        except Exception as e:
            # Rollback in caso di errore
            connessione.rollback()
            print(f"Errore durante l'eliminazione della riparazione: {e}")
            return False  # Ritorna False in caso di errore
    return False  # Ritorna False se la connessione non è riuscita

def updateRiparazioni(rip: RiparazioneInput):
    connessione = getConnection()
    if connessione.is_connected():
        # Prima query per inserire dati nella tabella Riparazioni
        QUERY = "UPDATE Riparazioni SET descrizioneGuasto = %s, prezzo = %s WHERE ID = %s"
        datiRiparazione = (rip.descrizioneGuasto, rip.prezzo, rip.id)
        cursore = connessione.cursor()
        cursore.execute(QUERY, datiRiparazione)
        connessione.commit()

        # Seconda query per inserire dati nella tabella corretta
        QUERYSec = "UPDATE Oggetti SET nome = %s, marca = %s, modello = %s, matricola = %s, extra = %s WHERE FK_Riparazione = %s"
        datiOgg = (rip.nomeOggetto, rip.marcaOggetto, rip.modelloOggetto, rip.matricolaOggetto, rip.componentiExtra, rip.id)
        cursore.execute(QUERYSec, datiOgg)
        connessione.commit()

        cursore.close()
        connessione.close()

        return rip.id

def getRiparazioniById(id: int):
    con = getConnection()
    if con.is_connected():
        QUERY = "SELECT Riparazioni.ID, descrizioneGuasto, o.nome, o.marca, o.modello, o.matricola, prezzo, o.extra FROM Riparazioni JOIN Oggetti o on Riparazioni.ID = o.FK_Riparazione WHERE FK_Riparazione = %s"
        cursore = con.cursor()
        cursore.execute(QUERY, (id,))
        results = cursore.fetchall()
        cursore.close()
        con.close()

        for row in results:
            rip = RiparazioneInput(
                id=int(row[0]),
                descrizioneGuasto=row[1],
                nomeOggetto=row[2],
                marcaOggetto=row[3],
                modelloOggetto=row[4],
                matricolaOggetto=row[5],
                prezzo=float(row[6]),
                componentiExtra=row[7]
            )
            return rip
        else:
            return None

def getNameObject(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT nome from Oggetti WHERE FK_Riparazione = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (id,))
        results = cursore.fetchall()
        cursore.close()
        connessione.close()
        return results[0][0]

def getMarcaObject(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT marca from Oggetti WHERE FK_Riparazione = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (id,))
        results = cursore.fetchall()
        cursore.close()
        connessione.close()
        return results[0][0]

def getModelloObject(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT modello from Oggetti WHERE FK_Riparazione = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (id,))
        results = cursore.fetchall()
        cursore.close()
        connessione.close()
        return results[0][0]

def getMatricolaObject(id: int):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "SELECT matricola from Oggetti WHERE FK_Riparazione = %s"
        cursore = connessione.cursor()
        cursore.execute(QUERY, (id,))
        results = cursore.fetchall()
        cursore.close()
        connessione.close()
        return results[0][0]






