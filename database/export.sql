-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Creato il: Feb 10, 2024 alle 18:28
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Quantumsatest`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `Clienti`
--

CREATE TABLE `Clienti` (
  `ID` int(11) NOT NULL,
  `nome` varchar(40) NOT NULL,
  `cognome` varchar(40) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `Oggetti`
--

CREATE TABLE `Oggetti` (
  `ID` int(11) NOT NULL,
  `nome` varchar(40) NOT NULL,
  `marca` varchar(40) NOT NULL,
  `modello` varchar(40) DEFAULT NULL,
  `matricola` varchar(40) DEFAULT NULL,
  `FK_Riparazione` int(11) DEFAULT NULL,
  `extra` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `Pagamenti`
--

CREATE TABLE `Pagamenti` (
  `ID` int(11) NOT NULL,
  `dataPagamento` date NOT NULL,
  `importo` decimal(10,2) NOT NULL,
  `FK_Riparazione` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `Ricambi`
--

CREATE TABLE `Ricambi` (
  `id` int(11) NOT NULL,
  `tipo` varchar(40) NOT NULL,
  `marca` varchar(40) DEFAULT NULL,
  `modello` varchar(40) DEFAULT NULL,
  `quantita` int(11) DEFAULT 0,
  `posizione` varchar(40) NOT NULL,
  `Guasto` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `Riparazioni`
--

CREATE TABLE `Riparazioni` (
  `ID` int(11) NOT NULL,
  `dataIngresso` date NOT NULL,
  `dataUscita` date DEFAULT NULL,
  `descrizioneGuasto` text NOT NULL,
  `descrizioneRiparazione` text DEFAULT NULL,
  `prezzo` decimal(10,2) DEFAULT 0.00,
  `FK_Cliente` int(11) DEFAULT NULL,
  `FK_StatoRiparazione` int(11) DEFAULT NULL,
  `dataCompletata` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `StatoRiparazione`
--

CREATE TABLE `StatoRiparazione` (
  `ID` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `StatoRiparazione`
--

INSERT INTO `StatoRiparazione` (`ID`, `nome`) VALUES
(1, 'In attesa'),
(2, 'In corso'),
(3, 'Completata'),
(4, 'Ritirata ma non pagata'),
(5, 'Ritirata e Pagata'),
(6, 'Non Riparabile');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `Clienti`
--
ALTER TABLE `Clienti`
  ADD PRIMARY KEY (`ID`);

--
-- Indici per le tabelle `Oggetti`
--
ALTER TABLE `Oggetti`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `oggetti_ibfk_1` (`FK_Riparazione`);

--
-- Indici per le tabelle `Pagamenti`
--
ALTER TABLE `Pagamenti`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Riparazione` (`FK_Riparazione`);

--
-- Indici per le tabelle `Ricambi`
--
ALTER TABLE `Ricambi`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `Riparazioni`
--
ALTER TABLE `Riparazioni`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_StatoRiparazione` (`FK_StatoRiparazione`),
  ADD KEY `idx_FK_Cliente` (`FK_Cliente`);

--
-- Indici per le tabelle `StatoRiparazione`
--
ALTER TABLE `StatoRiparazione`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `Clienti`
--
ALTER TABLE `Clienti`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `Oggetti`
--
ALTER TABLE `Oggetti`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `Pagamenti`
--
ALTER TABLE `Pagamenti`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `Ricambi`
--
ALTER TABLE `Ricambi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `Riparazioni`
--
ALTER TABLE `Riparazioni`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `StatoRiparazione`
--
ALTER TABLE `StatoRiparazione`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `Oggetti`
--
ALTER TABLE `Oggetti`
  ADD CONSTRAINT `oggetti_ibfk_1` FOREIGN KEY (`FK_Riparazione`) REFERENCES `Riparazioni` (`ID`) ON DELETE CASCADE;

--
-- Limiti per la tabella `Pagamenti`
--
ALTER TABLE `Pagamenti`
  ADD CONSTRAINT `pagamenti_ibfk_1` FOREIGN KEY (`FK_Riparazione`) REFERENCES `Riparazioni` (`ID`);

--
-- Limiti per la tabella `Riparazioni`
--
ALTER TABLE `Riparazioni`
  ADD CONSTRAINT `riparazioni_ibfk_1` FOREIGN KEY (`FK_Cliente`) REFERENCES `Clienti` (`ID`) ON DELETE SET NULL,
  ADD CONSTRAINT `riparazioni_ibfk_2` FOREIGN KEY (`FK_StatoRiparazione`) REFERENCES `StatoRiparazione` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
