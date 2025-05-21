from fastapi import FastAPI
from app.routes.monster_routes import router as monster_router
from app.db.connection import Base, engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Monster Hunter API!"}

# Cria as tabelas no banco de dados ao iniciar a aplicação
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Inclui as rotas
app.include_router(monster_router)