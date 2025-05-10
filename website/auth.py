from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/actualites')
def actualites():
    return render_template("actualité.html", page_description="Découvrez les dernières nouvelles, événements et initiatives de notre organisation.") 

@auth.route('/evenement')
def evenement():
    return render_template("evenement.html", page_description="Découvrez les dernières nouvelles, événements et initiatives de notre organisation 2.")

@auth.route('/rejoignez_nous')
def rejoignez_nous():
    return render_template("rejoignez.html", page_description="Découvrez les dernières nouvelles, événements et initiatives de notre organisation 3.")

@auth.route('/A_propos')
def A_propos():
    return render_template("A_propos.html", page_description="Découvrez les dernières nouvelles, événements et initiatives de notre organisation 4.")

@auth.route('/boutique')
def boutique():
    return render_template("sft_boutique.html")

