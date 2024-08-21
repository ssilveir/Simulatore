from init import db
from sqlalchemy import Column, Integer, String

class SM_CER(db.Model):
    __tablename__='SM_CER'
    ID_CER = Column(Integer, primary_key = True, autoincrement = True)
    CR_NOME = Column(String(50), nullable = False)
    CR_PROVINCIA = Column(String(30), nullable = False)
    CR_LOCALITA = Column(String(30), nullable = False)
    CR_INDIRIZZO = Column(String(50), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name
    

class Usuarios(db.Model):
    __tablename__='SM_USER'
    ID_USER = Column(Integer, primary_key = True, autoincrement = True)
    US_NOME = Column(String(50), nullable = False)
    US_EMAIL = Column(String(50), nullable = False)
    US_PASSWORD = Column(String(50), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name