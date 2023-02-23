from application.app import app
from application import game
from flask import render_template, flash, redirect, url_for, session, request, g
from .forms import TryForm, NewGameForm


@app.route('/')
@app.route('/<session_id>')
def index(session_id=None):
    session['lang'] = 'english'
    if not session_id:
        return redirect(url_for('new_game'))
    else:
        return redirect(url_for('current_game', session_id=session_id))


@app.route('/new_game', methods=['GET', 'POST'])
@app.route('/new_game/<message>', methods=['GET', 'POST'])
def new_game(message=''):
    new_form = NewGameForm()
    session_id = 0
    if new_form.validate_on_submit() and request.method == 'POST':
        session_id = game.create_new_game()
        return redirect(url_for('current_game', session_id=session_id))
    else:
        return render_template(
            "new_game.html",
            form=new_form,
            session_id=session_id,
            message=message,
        )


@app.route('/current_game/<session_id>', methods=['GET', 'POST'])
def current_game(session_id=None):
    game_form = TryForm()
    results = dict()
    if game_form.validate_on_submit():
        try_number = game_form.try_number.data
        results = game.another_try(session_id, try_number)
        if not len(results['checker_response']):
            return redirect(url_for('new_game', message=results['message']))

    return render_template(
        "game.html",
        session_id=session_id,
        form=game_form,
        results=results,
    )
