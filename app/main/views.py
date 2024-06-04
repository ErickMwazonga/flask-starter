from datetime import datetime
from flask import flash, render_template, request, session, redirect, url_for
 
from . import main
from app import db
from .forms import NameForm
from ..models import User

@main.route('/', methods=['GET', 'POST']) 
def index():
    form = NameForm()
    
    if form.validate_on_submit():
        name = form.name.data

        user = User.query.filter_by(name=name).first()
        if user:
            flash('User already exists!', 'error')
        else:
            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()

            session['name'] = form.name.data
            flash('New user created!', 'success')
            return redirect(url_for('main.index')) 
    
    users = User.query.order_by(User.created_at.desc()).all()
    context_data = {
        'form': form,
        'name': session.get('name'),
        'current_time': datetime.now(),
        'users': users
    }
    return render_template('index.html', **context_data)


@main.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form['user_id']
    user = User.query.get(user_id)

    if not user:
        flash('User not found!', 'error')
    else:
        db.session.delete(user)
        db.session.commit()
        session.pop('name')
        flash('User deleted successfully!', 'success')
        
    return redirect(url_for('main.index'))