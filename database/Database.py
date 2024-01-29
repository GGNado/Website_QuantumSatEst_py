import mysql.connector as dbms

from models.Clienti import Cliente
from models.Ricambi import Ricambio

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
                posizione=row[5]
            )
            listaRicambi.append(ricambio)
        cursore.close()
        connessione.close()
        return listaRicambi

def aggiungiRicambio(ricambio: Ricambio):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "INSERT INTO Ricambi (tipo, marca, modello, quantita, posizione) VALUES (%s, %s, %s, %s, %s)"
        dati_ricambio = (ricambio.tipo, ricambio.marca, ricambio.modello, ricambio.quantita, ricambio.posizione)
        cursore = connessione.cursor()
        cursore.execute(QUERY, dati_ricambio)
        connessione.commit()
        nuovo_ricambio_id = cursore.lastrowid
        cursore.close()
        connessione.close()
        return nuovo_ricambio_id


def modificaRicambio(id: int, ricambio: Ricambio):
    connessione = getConnection()
    if connessione.is_connected():
        QUERY = "UPDATE Ricambi SET tipo=%s, marca=%s, modello=%s, quantita=%s, posizione=%s WHERE id=%s"
        dati_ricambio = (ricambio.tipo, ricambio.marca, ricambio.modello, ricambio.quantita, ricambio.posizione, id)
        cursore = connessione.cursor()
        cursore.execute(QUERY, dati_ricambio)
        connessione.commit()
        cursore.close()
        connessione.close()

def getRicambiFiltro(tipo, marca, modello, quantita):
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

        if quantita != -1:
            QUERY += " AND quantita = %s"
            params.append(quantita)

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
                posizione=row[5]
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


