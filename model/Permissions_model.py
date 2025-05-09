from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.conn import Base

class Permissions_Roll(Base): 
    __tablename__ = 'Permissions_Roll'

    IDRoll = Column(Integer, primary_key=True, autoincrement=True)
    Name_Roll = Column(String(100),  nullable=False)
    Status = Column(Integer, nullable=False, default=1)
    #Relación: Mi tabla user ocupa el id de IDRoll
    Users = relationship("Permissions_Users", back_populates="Roll")
    Access= relationship("Permissions_Access",back_populates='Roll')

class Permissions_Screen(Base):
    __tablename__ = 'Permissions_Screen'

    IDScreen = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100),  nullable=False)
    Url = Column(String(100),  nullable=False)
    Status = Column(Integer, nullable=False, default=1)
    #Relación:
    Access= relationship("Permissions_Access",back_populates='Screen')

class Permissions_Users(Base):
    __tablename__ = 'Permissions_Users'

    IDUsers = Column(Integer, primary_key=True, autoincrement=True)
    IDRoll = Column(Integer, ForeignKey('Permissions_Roll.IDRoll'), nullable=False)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    Password = Column(String(100), nullable=False)
    Status = Column(Integer, nullable=False, default=1)
    #El nullable=false es como decir NOT NULL en sql que el cambio es obligatorio llenarlo
    #Relación: Mi tabla Roll ocupa el id de Users
    Roll = relationship("Permissions_Roll", back_populates="Users")
    Access= relationship("Permissions_Access",back_populates='Users')

class Permissions_Access(Base):
    __tablename__ = 'Permissions_Access'

    IDAccess = Column(Integer, primary_key=True, autoincrement=True)
    IDUsers = Column(Integer, ForeignKey('Permissions_Users.IDUsers'), nullable=False)
    IDRoll = Column(Integer, ForeignKey('Permissions_Roll.IDRoll'), nullable=False)
    IDScreen= Column(Integer,ForeignKey('Permissions_Screen.IDScreen'), nullable=False)
    Status = Column(Integer, nullable=False, default=1)

    #Relación: 
    #back_populates:establece la relacion que ambas son de la misma conexion
    Users = relationship("Permissions_Users", back_populates="Access")
    Roll = relationship("Permissions_Roll", back_populates="Access")
    Screen = relationship("Permissions_Screen",back_populates="Access")

    