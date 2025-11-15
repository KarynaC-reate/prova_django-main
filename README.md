## 📚 Prova Django – Sistema de Catalogação de Documentos
## 📋 Visão Geral

Este projeto é um sistema desenvolvido em Django para catalogação e classificação de documentos textuais, relacionando-os a seus respectivos gêneros textuais e tipos de gênero.
Ele foi criado como parte de uma prova/tarefa acadêmica, demonstrando modelagem de dados (MER), uso do Django ORM e construção de um sistema web funcional.

## 🧱 Estrutura do Projeto

O repositório contém as seguintes pastas principais:

catalogacao/ – App Django responsável pelos modelos, views e templates.

modelagens/ – Contém arquivos de modelagem, incluindo o MER.

setup/ – Scripts ou arquivos auxiliares de configuração.

static/ – Arquivos estáticos como CSS, JS e imagens.

db.sqlite3 – Banco de dados SQLite já utilizado no projeto.

requirements.txt – Dependências Python.

manage.py – Gerenciador padrão do Django.

## 🎯 Funcionalidades

✔ Cadastro de Gêneros Textuais
✔ Cadastro de Tipos de Gênero
✔ Cadastro de Documentos contendo título, conteúdo e gênero
✔ Interface de administração com Django Admin
✔ Página de catálogo com listagem e pesquisa dinâmica
✔ Organização clara entre documento → gênero → tipo

## 🗂 Modelo de Dados (Resumo)

A modelagem segue esta estrutura lógica:

Tipo de Gênero

nome

descrição

Gênero Textual

nome

descrição

tipo (FK para Tipo de Gênero)

Documento

título

conteúdo

gênero (FK para Gênero Textual)

data de cadastro

## 🚀 Como Executar o Projeto
- 1️⃣ Clonar o repositório
git clone https://github.com/KarynaC-reate/prova_django-main.git
cd prova_django-main

- 2️⃣ Criar ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate


Linux/macOS:

python3 -m venv venv
source venv/bin/activate

- 3️⃣ Instalar dependências
pip install -r requirements.txt

- 4️⃣ Aplicar migrações
python manage.py migrate

- 5️⃣ Criar superusuário
python manage.py createsuperuser

- 6️⃣ Rodar o servidor
python manage.py runserver

- 7️⃣ Acessar

Página pública: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## 🛠 Tecnologias Utilizadas

Python 3

Django

SQLite

HTML, CSS e JavaScript

Tailwind ou Bootstrap (dependendo da parte visual implementada)

Git e GitHub

## 🚧 Melhorias Futuras (Sugeridas)

Criar API REST com Django REST Framework

Criar página detalhada para cada documento

Implementar paginação

Melhorar os filtros de busca

Migrar banco para PostgreSQL em produção

Criar sistema de usuários autenticados para cadastro de documentos

## 📄 Licença

Este repositório faz parte de uma prova/atividade acadêmica. Para uso comercial ou extensões públicas, consulte o autor.