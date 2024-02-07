-- Modifica della tabella Oggetti per l'eliminazione in cascata
alter table Oggetti
    drop foreign key oggetti_ibfk_1;

alter table Oggetti
    add constraint oggetti_ibfk_1
        foreign key (FK_Riparazione) references quantumsatest.Riparazioni (ID)
        on delete cascade;

-- Modifica della tabella Riparazioni per l'impostazione a null
alter table Riparazioni
    drop foreign key riparazioni_ibfk_1;

alter table Riparazioni
    add constraint riparazioni_ibfk_1
        foreign key (FK_Cliente) references quantumsatest.Clienti (ID)
        on delete set null;
