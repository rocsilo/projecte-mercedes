from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clau_secreta_viatges_2025'

# Configuració de la Base de Dades
def init_db():
    conn = sqlite3.connect('viatges.db')
    cursor = conn.cursor()
    # Taula d'usuaris
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuaris 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT UNIQUE, password TEXT)''')
    # Taula de viatges (Més complexa: Destí, País, Valoració, Comentari)
    cursor.execute('''CREATE TABLE IF NOT EXISTS viatges 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, desti TEXT, pais TEXT, 
                       valoracio INTEGER, comentari TEXT, usuari_id INTEGER)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registre', methods=['GET', 'POST'])
def registre():
    if request.method == 'POST':
        nom = request.form['nom']
        pwd = generate_password_hash(request.form['password'])
        conn = sqlite3.connect('viatges.db')
        try:
            conn.execute("INSERT INTO usuaris (nom, password) VALUES (?, ?)", (nom, pwd))
            conn.commit()
            return redirect(url_for('login'))
        except:
            return "Error: L'usuari ja existeix."
        finally:
            conn.close()
    return render_template('registre.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nom = request.form['nom']
        pwd = request.form['password']
        conn = sqlite3.connect('viatges.db')
        user = conn.execute("SELECT * FROM usuaris WHERE nom = ?", (nom,)).fetchone()
        conn.close()
        if user and check_password_hash(user[2], pwd):
            session['usuari_id'] = user[0]
            session['usuari_nom'] = user[1]
            return redirect(url_for('privat'))
    return render_template('login.html', error="Dades incorrectes")

@app.route('/privat')
def privat():
    if 'usuari_id' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('viatges.db')
    # Només mostrem els viatges de l'usuari connectat
    meus_viatges = conn.execute("SELECT * FROM viatges WHERE usuari_id = ?", (session['usuari_id'],)).fetchall()
    conn.close()
    return render_template('privat.html', viatges=meus_viatges)

@app.route('/afegir_viatge', methods=['GET', 'POST'])
def afegir():
    if 'usuari_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        desti = request.form['desti']
        pais = request.form['pais']
        valoracio = request.form['valoracio']
        comentari = request.form['comentari']
        conn = sqlite3.connect('viatges.db')
        conn.execute("INSERT INTO viatges (desti, pais, valoracio, comentari, usuari_id) VALUES (?, ?, ?, ?, ?)",
                     (desti, pais, valoracio, comentari, session['usuari_id']))
        conn.commit()
        conn.close()
        return redirect(url_for('privat'))
    return render_template('formulari_viatges.html')

@app.route('/about')
def about():
    # Complint el requisit del portfoli passant dades de GitHub des de Python 
    github_url = "https://github.com/rocsilo/projecte-mercedes/tree/main/practicas%20anteriors"
    return render_template('about_me.html', github=github_url)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Aquest bloc SEMPRE ha de ser l'últim del fitxer
if __name__ == '__main__':
    app.run(debug=True)