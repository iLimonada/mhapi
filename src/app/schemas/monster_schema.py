from pydantic import BaseModel
from typing import Optional

# Criacao de classe base usada para criar, ler, atualizar os monstros

class MonsterBase(BaseModel):
    name: str
    type: str | None = None
    element: str | None = None
    species: str | None = None
    ailment: str | None = None
    is_large: bool


# Schema utilizando para criacao de um monstrro
class MonsterCreate(MonsterBase):
    pass

# Schema utilizado para um monstro na API
class MonsterRead(MonsterBase):
    id: int

    class Config:
        from_attributes = True

# Schema utilizado para atualizações parciais
class MonsterUpdate(MonsterBase):
    name: Optional[str] = None
    type: Optional[str] = None
    element: Optional[str] = None
    species: Optional[str] = None
    ailment: Optional[str] = None
    is_large: Optional[bool] = None