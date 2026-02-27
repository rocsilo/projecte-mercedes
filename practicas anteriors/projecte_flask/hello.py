from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime
from markupsafe import escape
import sqlite3

app = Flask(__name__)
app.secret_key = 'la_teva_clau_secreta'  # Necessària per als missatges (flash)

# --- CONFIGURACIÓ DE LA BASE DE DADES ---
DB_NAME = 'usuaris.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Per poder accedir a les columnes pel nom
    return conn

def init_db():
    """Crea la taula si no existeix al iniciar l'app"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuaris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            mail TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicialitzem la BD només d'arrencar
init_db()


# --- LES TEVES RUTES ANTIGUES (NO TOCADES) ---

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/kalcul-edat', methods=['GET', 'POST'])
def kalcul_edat_form():
    if request.method == 'POST':
        nom = request.form['nom']
        try:
            edat = int(request.form['edat'])
        except ValueError:
            return "Error: L'edat ha de ser un número."

        current_year = datetime.now().year
        if edat >= 100:
            missatge = "Ja tens 100 anys o més!"
        else:
            any_resultat = current_year + (100 - edat)
            missatge = f"Compliràs 100 anys l'any {any_resultat}."

        return render_template('resultat.html', nom=nom, edat=edat, missatge=missatge)
    else:
        return render_template('form_edad.html')


# --- LES NOVES RUTES (GETMAIL i ADDMAIL) ---

@app.route('/getmail', methods=('GET', 'POST'))
def getmail():
    resultat_mail = None
    error = None
    nom_buscat = ""

    if request.method == 'POST':
        nom_buscat = request.form['nom']
        
        # Connexió a la BD per cercar
        conn = get_db_connection()
        usuari = conn.execute('SELECT mail FROM usuaris WHERE nom = ?', (nom_buscat,)).fetchone()
        conn.close()

        if usuari:
            resultat_mail = usuari['mail']
        else:
            error = "Error: Aquest usuari no existeix."

    # Renderitza usant la plantilla 'getmail.html'
    return render_template('getmail.html', mail=resultat_mail, error=error, nom_anterior=nom_buscat)


@app.route('/addmail', methods=('GET', 'POST'))
def addmail():
    if request.method == 'POST':
        nom = request.form['nom']
        mail = request.form['mail']

        if not nom or not mail:
            flash("Si us plau, omple tots els camps!")
        else:
            # Connexió a la BD per guardar
            conn = get_db_connection()
            conn.execute('INSERT INTO usuaris (nom, mail) VALUES (?, ?)', (nom, mail))
            conn.commit()
            conn.close()
            flash(f"Usuari '{nom}' afegit correctament!")

    # Renderitza usant la plantilla 'addmail.html'
    return render_template('addmail.html')


if __name__ == '__main__':
    app.run(debug=True)