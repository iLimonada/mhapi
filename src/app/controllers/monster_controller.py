from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.connection import SessionLocal
from app.services.monter_service import fetch_all_monsters, fetch_monster_by_name, create_monster, update_monster, delete_monster
from app.schemas.monster_schema import MonsterCreate, MonsterUpdate

# Função para criar a sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Controladores para pegar os monstros
def fetch_all_monsters_controller(db: Session = Depends(get_db)):
    return fetch_all_monsters(db)

def fetch_monster_by_name_controller(name: str, db: Session = Depends(get_db)):
    return fetch_monster_by_name(db, name)

# Controlador para criar um monstro
def create_monster_controller(monster: MonsterCreate, db: Session = Depends(get_db)):
    return create_monster(db, monster)

# Controlador para atualizar o monstro
def update_monster_controller(monster_id: int, monster_data: MonsterUpdate, db: Session = Depends(get_db)):
    patch_monster = update_monster(db, monster_id, monster_data)
    if patch_monster is None:
        raise HTTPException(status_code=404, detail="Monster not found")
    return patch_monster

# Controlador para deletar o monstro
def delete_monster_controller(monster_id: id, db: Session = Depends(get_db)):
    monster_deleted = delete_monster(db, monster_id)
    if monster_deleted is None:
        raise HTTPException(status_code=404, detail="Monster not found")
    return {"detail": f"Monster with id {monster_id} deleted successfully"}