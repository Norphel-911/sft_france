#we will store all the standard views here 
from flask import Blueprint, render_template
#it will have bunch of roots in it

views = Blueprint('views', __name__)

@views.route('/') #homepage
def index():
    return render_template('index.html') 




