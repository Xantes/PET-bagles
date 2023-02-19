from application.app import app
from application import game
from flask import render_template, flash, redirect, url_for, session, request, g
from .forms import TryForm, NewGameForm


@app.route('/')
@app.route('/index')
def index():
    if request.args.get('session_id'):
        return redirect(url_for('new_game'))
    else:
        return redirect(url_for('current_game'))


@ app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    new_form = NewGameForm()
    session_id = 0
    if new_form.validate_on_submit() and request.method == 'POST':
        session_id = game.create_new_game()
        return redirect(url_for('current_game'))
    else:
        return render_template(
            "new_game.html",
            form=new_form,
            session_id=session_id,
        )


@ app.route('/current_game', methods=['GET', 'POST'])
def current_game():
    session_id = session['session_id']
    game_form = TryForm()
    if game_form.validate_on_submit():
        return redirect('/index')
    else:
        return render_template(
            "game.html",
            session=session_id,
            form=game_form,
        )
