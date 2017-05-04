# -*- coding: utf-8 -*-

import os

from flask import render_template, redirect, url_for, request, g
from flask import send_from_directory
from flask_login import login_user, logout_user, current_user, login_required

from app import app, login_manager
from .models import User, Party
from app import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def validateAndAdd(party_name):
    cur_user = User.query.filter_by(id_number=current_user.id_number).all()
    party = Party.query.filter_by(name=party_name).first()
    party.vote_count += 1
    for user in cur_user:
        user.voted = True
    db.session.commit()



@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    error = None
    if request.method == 'POST':
        validateAndAdd(request.form['party_name'])
        return redirect(url_for('login'))
    g.user = current_user #global user parameter used by flask framwork
    parties = Party.query.all()
    return render_template('index.html', title='Home', user=g.user, parties=parties, error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        ## Validate user
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        id_number = request.form['id_number']
        check_db = User.query.filter_by(id_number=id_number).all()
        if check_db == None:
            error = u'המצביע אינו מופיע בבסיס הנתונים'
        else:
            for user in check_db:
                if first_name == user.first_name and last_name == user.last_name and id_number == user.id_number:
                    if user.voted:
                        error = u'ניתן להצביע פעם אחת בלבד'
                        return render_template('login.html', error=error)

                    else:
                        #user = User.query.filter_by(id_number=id_number).first()
                        login_user(user)  ## built in 'flask login' method that creates a user session
                        return redirect(url_for('index'))

            error = u'המצביע אינו מופיע בבסיס הנתונים'

    return render_template('login.html', error=error)


## will handle the logout request
@app.route('/logout')
@login_required
def logout():
    logout_user() ## built in 'flask login' method that deletes the user session
    return redirect(url_for('index'))


## secret page that shows the user name
@app.route('/secret', methods=['GET'])
@login_required
def secret():
    return 'This is a secret page. You are logged in as {} {} {}'.format(current_user.first_name,
                                                                         current_user.last_name,
                                                                         current_user.id_number)


## will handle the site icon - bonus 2 points for creative new icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'Realfavicon.ico',
                               mimetype='image/vnd.microsoft.icon')
