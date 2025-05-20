from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
import os

if getattr(sys, 'frozen', False):
    
    user_folder = os.path.join(os.path.expanduser("~"), "Documents")
    app_folder = os.path.join(user_folder, "BackupManager")
    os.makedirs(app_folder, exist_ok=True)
    db_path = os.path.join(app_folder, "meubanco.db")
else:
    
    db_path = os.path.abspath("meubanco.db")


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        
        user_folder = os.path.expanduser("~")
        app_folder = os.path.join(user_folder, "MeuAppBackup")
        os.makedirs(app_folder, exist_ok=True)
        return os.path.join(app_folder, relative_path)
    else:
       
        return os.path.join(os.path.abspath("."), relative_path)

db = create_engine(f"sqlite:///{db_path}")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Conta(Base):
    __tablename__ = "contas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    ultimo_bkp = Column("ultimo_backup", String)
    segundo_backup = Column("segundo_backup", String)

    def __init__(self, nome, email, ultimo_bkp="00/00/00", segundo_backup="S/segundobkp"):
        self.nome = nome
        self.email = email
        self.ultimo_bkp = ultimo_bkp
        self.segundo_backup = segundo_backup

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_user = Column("nome_user", String)
    senha_user = Column("senha_user", String)

    def __init__(self, nome_user, senha_user):
        self.nome_user = nome_user
        self.senha_user = senha_user

class Conta_dados(Base):
    __tablename__ = "contas_dados"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    ultimo_bkp = Column("ultimo_backup", String)
    obs = Column("obs", String)

    def __init__(self, nome, email, ultimo_bkp="00/00/00", obs="S/obs"):
        self.nome = nome
        self.email = email
        self.ultimo_bkp = ultimo_bkp
        self.obs = obs


Base.metadata.create_all(bind=db)


if not session.query(User).first():
    admin = User(nome_user='admin', senha_user='q')
    session.add(admin)
    session.commit()
