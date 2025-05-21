from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./monsters.db"

# Criação do engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criar a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para as classes do modelo
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
