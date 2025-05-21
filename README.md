# Monster Hunter API

Uma API desenvolvida com FastAPI para gerenciar monstros do universo Monster Hunter. Permite criar, listar, buscar, atualizar e deletar monstros de um banco de dados.

## 🚀 Tecnologias
- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite (padrão)
- Uvicorn (para rodar o servidor)

## ▶️ Como Rodar

1. Instale as dependências:
- pip install -r requirements.txt

No bash:
- uvicorn main:app --reload

📌 Funcionalidades

  - GET /monsters — Lista todos os monstros

  - GET /monsters/{name} — Busca por nome

  - POST /monsters/ — Cria um novo monstro

  - PATCH /monsters/{id} — Atualiza apenas campos desejados

  - DELETE /monsters/{id} — Remove um monstro
