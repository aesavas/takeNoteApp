from flask import Blueprint,render_template

views = Blueprint('views', __name__) # It is for routes

@views.route('/')
def home():
    return render_template('index.html')