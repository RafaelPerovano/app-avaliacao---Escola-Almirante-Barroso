# Projeto de Sistema de Avaliacao Escolar

Este é um projeto simples de sistema de avaliação escolar feito com Flask e PostgreSQL. A ideia é permitir que diferentes tipos de usuários (como professores, alunos, etc.) façam login e deixem uma avaliação de satisfação sobre a escola ou serviços. O projeto foi desenvolvido com a finalidade de ser aplicado em uma tela touch screen que está instalada na escola para todos e com o intuito de praticar meus conhecimentos sobre as tecnologias utilizadas.

## Tecnologias Utilizadas
- **Backend**: Flask (Python)
- **Banco de Dados**: PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap

## Funcionalidades
- Sistema de login com Flask
- Avaliação com emojis e comentários
- Controle de sessão por tipo de usuário
- Tela de admin (protótipo)

## Como Rodar o Projeto
1. Clone o repositório:
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```
3. Instale as dependências:
   ```pip install -r requirements.txt```
4. Configure o banco de dados PostgreSQL:
   ```Crie um arquivo .env para armazenar a url do banco de dados ==>
   DATABASE_URL="sua_url"```
6. Execute o Flask:

## Estrutura do Projeto
```
/
|-- app.py
|-- db.py
|-- static/
|   |-- style.css
|      |--imagens/
|-- templates/
|   |-- index.html
|   |-- login.html
|   |-- avaliacao.html
|-- README.md
```

## Melhorias Futuras
- Criar relatórios de avaliações para admins
- Implementar a interface do painel
- Implementar o Flask-login
