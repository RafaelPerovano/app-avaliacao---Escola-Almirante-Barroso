from flask import Flask, request, render_template, redirect, session, url_for
import psycopg2
from db import cursor, conn
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'secreta'  # chave secreta para sessões
# app.permanent_session_lifetime = timedelta(minutes=1)

# classe para o modelo de usuário
class User:
    def __init__(self, id, tipo_usuario, usuario, ultima_avaliacao):
        self.id = id
        self.tipo_usuario = tipo_usuario
        self.usuario = usuario
        self.ultima_avaliacao = ultima_avaliacao
    
    def is_active(self):
        return True

    def get_id(self):
        return self.id
    
    def get_usuario(self):
        return self.usuario
    
    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def get_ultima_avaliacao(self):
        return self.ultima_avaliacao

# função para carregar o usuário na sessão
def load_user(user_id):
    cursor.execute("SELECT tipo_usuario, usuario, ultima_avaliacao FROM usuarios WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        return User(user_id, user_data[0], user_data[1], user_data[2])
    return None

# página inicial
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

# página de login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tipo_usuario = request.form.get('tipo_usuario')
        usuario = request.form.get('usuario')

        cursor.execute("SELECT u.id, u.usuario, tu.nome AS tipo_usuario, u.ultima_avaliacao FROM usuarios u JOIN tipo_usuario tu ON u.tipo_usuario_id = tu.id WHERE u.usuario = %s", (usuario,))
        user_data = cursor.fetchone()

        # faz o login do usuario
        if user_data:
            user = User(user_data[0], user_data[1], user_data[2], user_data[3])
            
            # armazena as informações do usuário na sessão
            session['user_id'] = user.id
            session['tipo_usuario'] = user.tipo_usuario
            session['usuario'] = user.usuario
            session['ultima_avaliacao'] = user.ultima_avaliacao
            
            avaliou = ja_avaliou()

            if tipo_usuario == 'Admin':
                return redirect('avaliacao') ###
            
            if avaliou == False:
                return redirect('avaliacao')
            else:
                return redirect('login')
            
        # caso o usuário não esteja no bd
        return redirect('login')
    
    return render_template("login.html")

# página da avaliação
@app.route("/avaliacao", methods=['GET', 'POST'])
def avaliacao():
    tipo_usuario = session.get('tipo_usuario')

    if request.method == 'POST':
        dados = request.form

        satisfacao = dados.get("emogi")
        comentarios = dados.get("comentarios")
        data = datetime.now()
        turno = verificar_turno(data.hour)
        data = datetime.now().strftime('%Y-%m-%d')

        cursor.execute("INSERT INTO avaliacoes (tipo_usuario, satisfacao, comentarios, turno, data) VALUES (%s, %s, %s, %s, %s)", (tipo_usuario, satisfacao, comentarios, turno, data))
        cursor.execute("UPDATE usuarios SET ultima_avaliacao = %s WHERE usuario = %s", (data, session.get('usuario')))

        return render_template("termino_avaliacao.html")

    return render_template("avaliacao.html")

@app.route("/painel", methods=['GET', 'POST'])
def painel():
    return render_template("painel.html")

# logout da pagina
@app.route("/logout")
def logout():
    session.clear()  # Limpa a sessão
    return redirect('login')

def ja_avaliou():
    hoje = datetime.now().strftime('%Y-%m-%d')
    ultima_avaliacao = session.get('ultima_avaliacao')
    
    if ultima_avaliacao and hoje == ultima_avaliacao.strftime('%Y-%m-%d'):
        return True
    else:
        return False

def verificar_turno(hora):
    if 6 <= hora < 12:
        return "Manha"
    elif 12 <= hora < 19:
        return "Tarde"
    elif 19 <= hora <= 23:
        return "Noite"
    else:
        return "fora do horario"

if __name__ == "__main__":
    app.run(debug=True)
