
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('mysql://user:pass/scuole', echo
= True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()



class Dirigenti_scolastici(Base):
	__tablename__ = 'Dirigenti_scolastici'
	CF = Column(Integer, primary_key = True)
	nome = Column(String)
	cognome = Column(String)
	dirigente = relationship("Elenco_scuole", back_populates="scuola", cascade = "all, delete-orphan")


class Elenco_scuole(Base):
	__tablename__ = 'Elenco_scuole'
	nome_scuola = Column(String, primary_key = True)
	indirizzo = Column(String)
	CF_dirigente = Column(String, ForeignKey('Dirigenti_scolastici.CF'))
	scuola = relationship("Dirigenti_scolastici", back_populates="dirigente")
	docenza = relationship("Docenti", back_populates="scuola_appartenenza")
	studenti_appartenenza = relationship("Studenti", back_populates="scuola_appartenenza")
	ATA_appartenenza = relationship("Personale_ATA", back_populates="scuola_appartenenza")

class Docenti(Base):
	__tablename__ = 'Docenti'
	CF = Column(String, primary_key = True)
	insegnamento = Column(String, primary_key = True)
	nome_scuola = Column(String, ForeignKey('Elenco_scuole.nome_scuola'))
	nome = Column(String)
	cognome = Column(String)
	scuola_appartenenza = relationship("Elenco_scuole", back_populates="docenza")
	materie = relationship("Lista_materie", back_populates="elenco_docenti")
	attivita_docente = relationship("Attivita_extrascolastiche", back_populates="elenco_docenti")

class Lista_materie(Base):
	__tablename__ = 'Lista_materie'
	classe = Column(String, primary_key = True)
	nome_insegnamento = Column(String, primary_key = True, ForeignKey('Docenti.insegnamento'))
	
	elenco_docenti = relationship("Docenti", back_populates="materie")
	classi = relationship("Elenco_classi", back_populates="elenco_materie")

class Elenco_classi(Base):
	__tablename__ = 'Elenco_classi'
	classe = Column(String, primary_key = True, ForeignKey('Lista_materie.classe'))
	nome_scuola = Column(String, primary_key = True)
	ATA_classi = relationship("Personale_ATA", back_populates="elenco_classi")
	elenco_materie = relationship("Lista_materie", back_populates="classi")
	elenco_studenti = relationship("Studenti", back_populates="classi_studente")

class Attivita_extrascolastiche(Base):
	__tablename__ = 'Attivita_extrascolastiche'
	CF_docente = Column(String, primary_key = True, ForeignKey('Docenti.CF'))
	nome_corso = Column(String, primary_key = True)
	classe = Column(String, ForeignKey('Elenco_classi.classe'), ForeignKey('Studenti.classe'))
	elenco_materie = relationship("Lista_materie", back_populates="classi")
	elenco_studenti = relationship("Studenti", back_populates="attivita_studente")
	elenco_docenti = relationship("Docenti", back_populates="attivita_docente")

class Studenti(Base):
	__tablename__ = 'Studenti'
	CF = Column(String, primary_key = True)
	classe = Column(String, primary_key = True, ForeignKey('Elenco_classi.classe'))
	nome_scuola = Column(String, ForeignKey('Elenco_scuole.nome_scuola'), ForeignKey('Elenco_classi.nome_scuola'))
	nome = Column(String)
	cognome = Column(String)
	classi_studente = relationship("Elenco_classi", back_populates="elenco_studenti")
	scuola_appartenenza = relationship("Elenco_scuole", back_populates="studenti_appartenenza")
	attivita_studente = relationship("Attivita_extrascolastiche", back_populates="elenco_studenti")

class Personale_ATA(Base):
	__tablename__ = 'Personale_ATA'
	CF = Column(String, primary_key = True)
	classe = Column(String, ForeignKey('Elenco_classi.classe'))
	nome_scuola = Column(String, ForeignKey('Elenco_scuole.nome_scuola'), ForeignKey('Elenco_classi.nome_scuola'))
	nome = Column(String)
	cognome = Column(String)
	elenco_classi = relationship("Elenco_classi", back_populates="ATA_classi")
	scuola_appartenenza = relationship("Elenco_scuole", back_populates="ATA_appartenenza")
	

session.add(c1)
session.commit()
# per più elementi…


a1 = Dirigenti_scolastici(CF = 'AAA1', nome = 'Ugo', cognome = 'Sari', Elenco_scuole(nome_scuola = 'Istituto De Amicis', indirizzo = 'Viale Vittorio Veneto'))
a2 = Dirigenti_scolastici(CF = 'BBB1', nome = 'Guido', cognome = 'Celli', Elenco_scuole(nome_scuola = 'Istituto Ugo Foscolo', indirizzo = 'Corso Emanuele'))
a3 = Dirigenti_scolastici(CF = 'CCC1', nome = 'Nadia', cognome = 'Bianchi', Elenco_scuole(nome_scuola = 'Istituto Leonardo Da Vinci', indirizzo = 'Corso Gelone'))

d1 = Docenti(CF = 'DDD1', insegnamento = 'Scienze', nome = 'Mario', cognome = 'Rossi', nome_scuola = 'Istituto De Amicis')
d2 = Docenti(CF = 'EEE1', insegnamento = 'Arte', nome = 'Bruno', cognome = 'Riggi', nome_scuola = 'Istituto Ugo Foscolo')

c1 = Elenco_classi(classe = 'IIIA', nome_scuola = 'Istituto De Amicis')
c2 = Elenco_classi(classe = 'IIC', nome_scuola = 'Istituto De Amicis')

m1 = Lista_materie(classe = 'IA', nome_insegnamento = 'Scienze')
m2 = Lista_materie(classe = 'IIIA', nome_insegnamento = 'Matematica')

s1 = Studenti(CF = 'AA11', nome = 'Mario', cognome = 'Valle', nome_scuola = 'Istituto De Amicis', classe = 'IA')
s2 = Studenti(CF = 'BB11', nome = 'Diego', cognome = 'Salerno', nome_scuola = 'Istituto De Amicis', classe = 'IIC')
s3 = Studenti(CF = 'CC11', nome = 'Eleonora', cognome = 'Giacchi', nome_scuola = 'Istituto Ugo Foscolo', classe = 'IIB')
s4 = Studenti(CF = 'DD11', nome = 'Ambra', cognome = 'Ragaglia', nome_scuola = 'Istituto De Amicis', classe = 'IIIA')

p1 = Personale_ATA(CF = 'AAA2', nome = 'Danilo', cognome = 'Vanni', nome_scuola = 'Istituto De Amicis', classe = 'IA')
p2 = Personale_ATA(CF = 'BBB2', nome = 'Piero', cognome = 'Salerno', nome_scuola = 'Istituto De Amicis', classe = 'NO')

session.add_all([a1, a2, a3. d1, d2, c1, c2, m1, m2, s1, s2, s3, s4, p1, p2])
session.commit()

dirigenti_scuole = session.query(Dirigenti_scolastici).join(Elenco_scuole).all()
for el in dirigenti_scuole:
	print(el)

docenti_scuole = session.query(Docenti).join(Elenco_scuole).filter(Docenti.nome_scuola == 'Istituto De Amicis').all()
for el in docenti_scuole:
	print(el)

studenti_classi = session.query(Studenti).join(Elenco_classi).filter(Studenti.nome_scuola == 'Istituto De Amicis').all()
for el in studenti_classi:
	print(el)

ATA_classi = session.query(Personale_ATA).join(Elenco_classi).filter(Personale_ATA.classe != 'NO').all()
for el in ATA_classi:
	print(el)


xx = session.query(Dirigenti_scolastici).get(3)
session.delete(xx)
a3 = Dirigenti_scolastici(CF = 'KKK1', nome = 'Andrea', cognome = 'Bianchi', Elenco_scuole(nome_scuola = 'Istituto Leonardo Da Vinci', indirizzo = 'Corso Francia'))
session.add(a3)
session.commit()
dirigenti_scuole = session.query(Dirigenti_scolastici).join(Elenco_scuole).all()
for el in dirigenti_scuole:
	print(el)
# Inserimento dei dati in tabella Dirigenti
