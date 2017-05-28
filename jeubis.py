from flask import Flask, render_template, request, session
import random

app = Flask("Loups-garous")

@app.route("/")
def index():
   # usage de base
   return render_template("index.html")

@app.route("/resultat", methods=['POST'])
def resultat():
   carte = ["loup.jpg", "voyante.jpg", "villageois.jpg"]
   random.shuffle(carte)
   nom=request.form['username']
   cartejoueur=carte[1]
   return render_template("passage.html", nom=nom, cartejoueur=cartejoueur)

if 'username' in session:
        return 'Bonjour ' + session['username']

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/')

@app.route('/deconnexion')
def deconnexion():
    session.pop('username', None)
    return redirect('/')
