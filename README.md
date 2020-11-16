# Análise de perfil de usuários (Parte I)

## Introdução

Este projeto tem como objetivo definir a modelagem de uma base analítica com a finalidade de entender melhor as características dos usuários da Passei Direto.

Definindo um star chema e escrevendo o pipeline ETL, os dados baseados em arquivos json são transferidos para uma base de dados para análises futuras. 

## Data Schema and ETL Pipeline

### Data Schema


Utilizando os arquivos courses.json, sessions.json, student_follow_subject.json, students.json, subjects.json, subscription.json, universities.json foi criado um star schema como mostrado abaixo, que inclui

- Uma tabela fato: **students**, e 
- Seis tabelas dimensões: **courses**, **sessions**, **student_follow_subject**, **students**, **subjects**, **subscription**, e **universities**.

![Star Schema](images/star_schema.png)

### ETL Pipeline

O ETL pipeline extrai os dados dos arquivos e faz a inserção nas tabelas do MySQL utilizando o script `etl.py`, como você pode observar na imagem abaixo

![Pipeline ETL](images/Pipeline_ETL_PasseiDireto.png)

## Como executar

### Pré-requisitos

Se você deseja executar esse projeto em sua máquina, você deve finalizar os seguintes passos primeiro.

- Instalar `MySQL` em localhost.
- Criar usuário `root` com senha `admin`.
- Instalar as bibliotecas:
  - mysql.connector==8.0.21
  - pandas==1.0.5


### Instruções

1. Criar database/tabelas: `python create_tables.py`
2. Enviar os dados dos arquivos, armazenando na base de dados: `python etl.py`

## Arquivos do projeto

- **data/BASE_A**
  - **courses.json**
    - lista de cursos cadastrados no Passei Direto
  - **sessions.json**
    - visitas que os usuários fizeram ao longo do mês
  - **student_follow_subject.json**
    - disciplinas que cada usários está seguindo
  - **students.json**
    - amostra de usuários que acessaram o Passei Direto em Novembro de 2017
  - **subjects.json**
    - lista de disciplinas cadastradas no Passei Direto
  - **subscriptions.json**
    - assinaturas dos usuários que aderiram ao plano premium do Passei Direto
  - **universities.json**
    - lista de universidades cadastradas no Passei Direto
- **images**
  - Imagens do documento
- **create_tables.py**
  - Quando executado, esse script irá
    - `drop` database `passeidiretodb`
    - `create` database `passeidiretodb`
    - `drop` tables if exists
    - `create` tables if not exists
- **etl.py**
  - Script para implementaçao do processo de ETL.
  - Quando executado, esse script irá 
  Quando executado, esse script irá:
    - Iterar entre todos arquivos dentro de data/BASE_A para extrair os dados de cada arquivo e inseri-los em suas respectivas tabelas na base de dados do MySQL
- **README.md**
  - Descrição e instruções sobre o projeto
- **sql_queries.py**
  - Contém todas instruções DLL definidas
- **PasseiDireto.pbix**
  - Dashboard com as análises realizadas.
