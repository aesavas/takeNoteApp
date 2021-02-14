from flask import Blueprint,render_template, request, flash
from flask.json import jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User,Note
from . import db
import json

views = Blueprint('views', __name__) # It is for routes

@views.route('/', methods=["GET","POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', 'warning')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.!', 'success')
    return render_template('index.html', user=current_user)

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})
