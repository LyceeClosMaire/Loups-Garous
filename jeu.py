from flask import Flask, render_template, request
import random   # On import Flask et la génération aléatoire

app = Flask("Loups-garous")

@app.route("/") # On définie l'index qui sera la page d'accueil du site
def index():
   # usage de base
   return render_template("index.html")

@app.route("/resultat", methods=['POST'])
def resultat():
   carte = ["loup.jpg", "voyante.jpg", "villageois.jpg"]    # On définie les différentes cartes
   random.shuffle(carte)    #On gérère une carte aléatoirement au joueur
   nom=request.form['username'] # On récupère le nom du joueur
   cartejoueur=carte[1]
   return render_template("passage.html", nom=nom, cartejoueur=cartejoueur)
