from sqlalchemy.orm import Session
from app.models.monster_model import Monster
from app.schemas.monster_schema import MonsterCreate, MonsterUpdate

API_URL = "https://mhw-db.com/monsters"


def fetch_all_monsters(db: Session):
    return db.query(Monster).all()

def fetch_monster_by_name(db: Session, name: str):
    return db.query(Monster).filter(Monster.name.ilike(f"%{name}")).all()

def create_monster(db: Session, monster: MonsterCreate):
    db_monster = Monster(**monster.model_dump())
    db.add(db_monster)
    db.commit()
    db.refresh(db_monster)
    return db_monster

def update_monster(db: Session, monster_id: int, monster_data: MonsterUpdate):
    monster = db.query(Monster).filter(Monster.id == monster_id).first()
    if not monster:
        None
    
    update_data = monster_data.model_dump(exclude_unset=True)

    for monster_field, update_value in update_data.items():
        setattr(monster, monster_field, update_value)

    db.commit()
    db.refresh(monster)

    return monster

def delete_monster(db: Session, monster_id: int):
    monster = db.query(Monster).filter(Monster.id == monster_id).first()
    if not monster:
        return None
    db.delete(monster)
    db.commit()
    return monster