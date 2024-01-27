CREATE DATABASE Quantumsatest;
USE Quantumsatest;

CREATE TABLE Clienti(
    ID int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(40) NOT NULL,
    cognome varchar(40) NOT NULL,
    telefono varchar(20),
    email varchar(80)
);

CREATE TABLE StatoRiparazione (
    ID int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(50) NOT NULL
);

INSERT INTO StatoRiparazione (nome) VALUES ('In attesa'), ('In corso'), ('Completata');


CREATE TABLE Riparazioni (
    ID int PRIMARY KEY AUTO_INCREMENT,
    dataIngresso DATE NOT NULL,
    dataUscita DATE,
    descrizioneGuasto TEXT NOT NULL,
    descrizioneRiparazione TEXT,
    prezzo DECIMAL(10, 2) DEFAULT 0.0,
    FK_Cliente int,
    FK_StatoRiparazione int,
    FOREIGN KEY (FK_Cliente) REFERENCES Clienti(ID),
    FOREIGN KEY (FK_StatoRiparazione) REFERENCES StatoRiparazione(ID),
    INDEX idx_FK_Cliente (FK_Cliente)
);

CREATE TABLE Oggetti(
    ID int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(40) NOT NULL,
    marca varchar(40) NOT NULL,
    modello varchar(40),
    matricola varchar(40) UNIQUE,
    FK_Riparazione int,
    FOREIGN KEY (FK_Riparazione) REFERENCES Riparazioni(ID)
);
CREATE TABLE Pagamenti (
    ID int PRIMARY KEY AUTO_INCREMENT,
    dataPagamento DATE NOT NULL,
    importo DECIMAL(10, 2) NOT NULL,
    FK_Riparazione int,
    FOREIGN KEY (FK_Riparazione) REFERENCES Riparazioni(ID)
);

