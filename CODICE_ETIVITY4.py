
import mysql.connector
conn = mysql.connector.connect(user='root',
password='scuole', host='127.0.0.1', database='scuoledb’)
cursor = conn.cursor()



cursor.execute("DROP database IF EXISTS scuoledb") 
sql = "CREATE database scuoledb"
cursor.execute(sql)
print(cursor.fetchall())

# Creazione delle tabelle

sql ='CREATE TABLE Dirigenti_scolastici( CF CHAR(4) PRIMARY KEY, NOME VARCHAR(100) NOT NULL, COGNOME VARCHAR(100) NOT NULL)’
cursor.execute(sql)

sql ='CREATE TABLE Elenco_scuole( CF_DIRIGENTE CHAR(4) NOT NULL, NOME_SCUOLA VARCHAR(100) PRIMARY KEY, INDIRIZZO VARCHAR(100) NOT NULL, FOREIGN KEY CF_DIRIGENTE REFERENCES Dirigenti_scolastici(CF))’
cursor.execute(sql)

sql ='CREATE TABLE Docenti( CF CHAR(4), INSEGNAMENTO VARCHAR(100), NOME_SCUOLA VARCHAR(100) NOT NULL, NOME VARCHAR(100) NOT NULL, COGNOME VARCHAR(100) NOT NULL, PRIMARY KEY (CF, INSEGNAMENTO), FOREIGN KEY NOME_SCUOLA REFERENCES Elenco_scuole(NOME_SCUOLA))’
cursor.execute(sql)

sql ='CREATE TABLE Studenti( CF CHAR(4) PRIMARY KEY, CLASSE VARCHAR(5) NOT NULL, NOME_SCUOLA VARCHAR(100) NOT NULL, NOME VARCHAR(100) NOT NULL, COGNOME VARCHAR(100) NOT NULL, FOREIGN KEY NOME_SCUOLA REFERENCES Elenco_scuole(NOME_SCUOLA))’
cursor.execute(sql)

sql ='CREATE TABLE Personale_ATA( CF CHAR(4) PRIMARY KEY, CLASSE VARCHAR(5) NOT NULL, NOME_SCUOLA VARCHAR(100) NOT NULL, NOME VARCHAR(100) NOT NULL, COGNOME VARCHAR(100) NOT NULL, FOREIGN KEY NOME_SCUOLA REFERENCES Elenco_scuole(NOME_SCUOLA))’
cursor.execute(sql)

sql ='CREATE TABLE Elenco_classi( CLASSE VARCHAR(5), NOME_SCUOLA VARCHAR(100), PRIMARY KEY (CLASSE, NOME_SCUOLA))’
cursor.execute(sql)

sql ='CREATE TABLE Lista_materie( CLASSE VARCHAR(5), NOME_INSEGNAMENTO VARCHAR(100), PRIMARY KEY (CLASSE, NOME_INSEGNAMENTO))’
cursor.execute(sql)

sql ='CREATE TABLE Attivita_extrascolastiche( NOME_CORSO VARCHAR(100), CF_DOCENTE CHAR(4), CLASSE VARCHAR(5), PRIMARY KEY (NOME_CORSO, CF_DOCENTE), FOREIGN KEY CF_DOCENTE REFERENCES Docenti(CF))’
cursor.execute(sql)


# Inserimento dei dati in tabella Dirigenti

sql = "INSERT INTO Dirigenti_scolastici( CF, NOME, COGNOME) VALUES ('AAA1', 'Ugo', 'Sari')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Dirigenti_scolastici( CF, NOME, COGNOME) VALUES ('BBB1', 'Guido', 'Celli')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Dirigenti_scolastici( CF, NOME, COGNOME) VALUES ('CCC1', 'Nadia', 'Bianchi')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Inserimento dei dati in tabella Elenco_scuole

sql = "INSERT INTO Elenco_scuole( NOME_SCUOLA, INDIRIZZO, CF_DIRIGENTE) VALUES ('Istituto De Amicis', 'Viale Vittorio Veneto', 'AAA1')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Elenco_scuole( NOME_SCUOLA, INDIRIZZO, CF_DIRIGENTE) VALUES ('Istituto Ugo Foscolo', 'Corso Emanuele', 'BBB1')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Elenco_scuole( NOME_SCUOLA, INDIRIZZO, CF_DIRIGENTE) VALUES ('Istituto Leonardo Da Vinci', 'Corso Gelone', 'CCC1')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Inserimento dei dati in tabella Docenti

sql = "INSERT INTO Docenti( CF, INSEGNAMENTO, NOME, COGNOME, NOME_SCUOLA) VALUES ('DDD1', 'Scienze', 'Mario', 'Rossi', 'Istituto De Amicis')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Docenti( CF, INSEGNAMENTO, NOME, COGNOME, NOME_SCUOLA) VALUES ('DDD1', 'Matematica', 'Mario', 'Rossi', 'Istituto De Amicis')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Docenti( CF, INSEGNAMENTO, NOME, COGNOME, NOME_SCUOLA) VALUES ('EEE1', 'Arte', 'Bruno', 'Riggi', 'Istituto Ugo Foscolo')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Docenti( CF, INSEGNAMENTO, NOME, COGNOME, NOME_SCUOLA) VALUES ('FFF1', 'Arte', 'Agata', 'Natali', 'Istituto De Amicis')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Inserimento dei dati in tabella Studenti

sql = "INSERT INTO Studenti( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('AA11', 'Mario', 'Valle', 'Istituto De Amicis', 'IA')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Studenti( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('BB11', 'Diego', 'Salerno', 'Istituto De Amicis', 'IIC')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Studenti( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('CC11', 'Eleonora', 'Giacchi', 'Istituto Ugo Foscolo', 'IIB')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Studenti( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('DD11', 'Ambra', 'Ragaglia', 'Istituto De Amicis', 'IIIA')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Studenti( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('EE11', 'Guido', 'Ambrosini', 'Istituto De Amicis', 'IIB')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Inserimento dei dati in tabella Elenco_classi

sql = "INSERT INTO Elenco_classi( CLASSE, NOME_SCUOLA) VALUES ('IA', 'Istituto De Amicis')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Elenco_classi( CLASSE, NOME_SCUOLA) VALUES ('IIIA', 'Istituto De Amicis')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Elenco_classi( CLASSE, NOME_SCUOLA) VALUES ('IIC', 'Istituto De Amicis')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Inserimento dei dati in tabella Personale_ATA

sql = "INSERT INTO Personale_ATA( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('AAA2', 'Danilo', 'Vanni', 'Istituto De Amicis', 'IA')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Personale_ATA( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('BBB2', 'Piero', 'Salerno', 'Istituto De Amicis', NULL)"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Personale_ATA( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('CCC2', 'Sandra', 'Gianni', 'Istituto Ugo Foscolo', NULL)"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Personale_ATA( CF, NOME, COGNOME, NOME_SCUOLA, CLASSE) VALUES ('DDD2', 'Valeria', 'Artale', 'Istituto De Amicis', 'IIIA')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Inserimento dei dati in tabella Lista_materie

sql = "INSERT INTO Lista_materie( CLASSE, NOME_INSEGNAMENTO) VALUES ('IA', 'Scienze')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Lista_materie( CLASSE, NOME_INSEGNAMENTO) VALUES ('IIIA', 'Matematica')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Lista_materie( CLASSE, NOME_INSEGNAMENTO) VALUES ('IIB', 'Tecnologia')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Lista_materie( CLASSE, NOME_INSEGNAMENTO) VALUES ('IIID', 'Musica')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Lista_materie( CLASSE, NOME_INSEGNAMENTO) VALUES ('IIB', 'Italiano')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
sql = "INSERT INTO Lista_materie( CLASSE, NOME_INSEGNAMENTO) VALUES ('IIB', 'Inglese')"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Esecuzione interrogazioni

# Estrazione del dirigente scolastico assegnato all'Istituto De Amicis
sql = "SELECT A.NOME AS NOME_DIRIGENTE, A.COGNOME AS COGNOME_DIRIGENTE, B.NOME_SCUOLA FROM Dirigenti_scolastici A INNER JOIN Elenco_scuole B ON A.CF = B.CF_DIRIGENTE WHERE B.NOME_SCUOLA = 'Istituto De Amicis'"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# Estrazione Nome, cognome dei docenti presenti nell’istituto De Amicis ed indirizzo della scuola
sql = "SELECT A.NOME AS NOME_DOCENTE, A.COGNOME AS COGNOME_DOCENTE, B.INDIRIZZO FROM Docenti A INNER JOIN Elenco_scuole B ON A.NOME_SCUOLA = B.NOME_SCUOLA WHERE B.NOME_SCUOLA = 'Istituto De Amicis'"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# Estrazione Nome, Cognome ed indirizzo scuola del personale ATA che svolge un impiego di carattere amministrativo all’interno della scuola Istituto De Amicis
sql = "SELECT A.NOME AS NOME_IMPIEGATO, A.COGNOME AS COGNOME_IMPIEGATO, B.INDIRIZZO FROM Personale_ATA A INNER JOIN A.NOME_SCUOLA = B.NOME_SCUOLA WHERE A.CLASSE IS NULL AND B.NOME_SCUOLA = 'Istituto De Amicis'"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# Estrazione nome, cognome, nome_scuola  ed insegnamenti e nella classe IIB
sql = "SELECT A.NOME AS NOME_STUDENTE, A.COGNOME AS COGNOME_STUDENTE, A.NOME_SCUOLA, B.INSEGNAMENTI FROM Studenti A INNER JOIN (SELECT C.CLASSE AS CLASSE, C.NOME_SCUOLA AS NOME_SCUOLA, D.INSEGNAMENTI FROM Elenco_classi C INNER JOIN Lista_materie D ON C.CLASSE = D.CLASSE WHERE D.CLASSE = 'IIB') B ON A.CLASSE = B.CLASSE AND A.NOME_SCUOLA = B.NOME_SCUOLA"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# Estrazione nome, cognome studenti e docenti con relativo insegnamento nella scuola Istituto De Amicis
sql = "SELECT A.NOME AS NOME_STUDENTE, A.COGNOME AS COGNOME_STUDENTE, B.NOME AS NOME_DOCENTE, B.COGNOME AS COGNOME_DOCENTE, B.INSEGNAMENTO FROM (SELECT C.NOME AS NOME, C.COGNOME AS COGNOME, D.CLASSE AS CLASSE, D.INSEGNAMENTO AS INSEGNAMENTO FROM Studenti C INNER JOIN (SELECT E1.CLASSE AS CLASSE, E1.NOME_SCUOLA AS NOME_SCUOLA, E2.INSEGNAMENTO AS INSEGNAMENTO FROM Elenco_classi E1 INNER JOIN Lista_materie E2 ON E1.CLASSE = E2.CLASSE) D C.NOME_SCUOLA = D.NOME_SCUOLA) A INNER JOIN (SELECT F.NOME AS NOME, F.COGNOME AS COGNOME, F.INSEGNAMENTO AS INSEGNAMENTO FROM Docenti F INNER JOIN Lista_materie G ON F.INSEGNAMENTO = G.NOME_INSEGNAMENTO WHERE F.NOME_SCUOLA = 'Istituto De Amicis') B ON A.INSEGNAMENTO = B.INSEGNAMENTO AND A.CLASSE = B.CLASSE"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# Aggiornamento della tabella Dirigenti_scolastici per una tupla
sql = "UPDATE Dirigenti_scolastici SET COGNOME = 'Nari' WHERE CF LIKE '%A%'"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

# Aggiornamento della tabella Dirigenti_scolastici per una tupla
sql = "DELETE FROM Dirigenti_scolastici WHERE CF LIKE '%B%'"
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

conn.close()