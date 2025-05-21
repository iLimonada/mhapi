from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.monster_controller import (
    fetch_all_monsters_controller, 
    fetch_monster_by_name_controller, 
    create_monster_controller,
    update_monster_controller,
    delete_monster_controller
)
from app.schemas.monster_schema import MonsterCreate, MonsterRead, MonsterUpdate
from app.db.connection import get_db

router = APIRouter()

@router.get("/monsters")
def read_all_monsters(db: Session = Depends(get_db)): 
    return fetch_all_monsters_controller(db)

@router.get("/monsters/{name}")
def read_monster(name: str, db: Session = Depends(get_db)):  
    return fetch_monster_by_name_controller(name, db)

@router.post("/monsters/", response_model=MonsterCreate)
async def create_monster(monster: MonsterCreate, db: Session = Depends(get_db)): 
    return create_monster_controller(monster, db)

@router.patch("/monsters/{monster_id}", response_model=MonsterRead)
def update_monster(monster_id: int, data: MonsterUpdate, db: Session = Depends(get_db)):
    return update_monster_controller(monster_id, data, db)

@router.delete("/monsters/{monster_id}")
def delete_monster_route(monster_id: int, db: Session = Depends(get_db)):
    return delete_monster_controller(monster_id, db)
