 -> Crypto Market Tracker

Projeto backend desenvolvido em Python para coleta, persistência e visualização de dados do mercado de criptomoedas.

## Objetivo ##

Consumir dados de criptomoedas em tempo real através da API da CoinGecko, armazenar historicamente em PostgreSQL e futuramente disponibilizar dashboards interativos.

## Tecnologias ##

- Python
- Requests
- PostgreSQL
- Docker
- DBeaver
- Streamlit (em desenvolvimento)

## Arquitetura ##

O projeto segue princípios de Clean Architecture:

```text
src/
├── main/         # orquestração da aplicação
├── domain/       # entidades e regras de negócio
├── use_cases/    # casos de uso
├── infra/        # banco de dados e APIs externas
├── interfaces/   # interfaces futuras (API/Dashboard)
