from flask import Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, session
from functools import wraps


import tigrmanagr.services.todo as svc_todo
import tigrmanagr.services.board as svc_board

bp = Blueprint('todo', __name__, url_prefix='/todo')


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)

        if user:
            return f(*args, **kwargs)
        return redirect('/login')
    return decorated_function

@bp.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def edit(todo_id):
    error = ''
    todo, error = svc_todo.get_by_id(todo_id)

    if request.method == 'POST':
        title_update = request.form['title_update']
        status_update = request.form['status_update']

        data = {
            'todo_id': int(todo_id),
            'todo_title': title_update,
            'todo_status': status_update,
        }
        _,error = svc_todo.edit(data)
        if not error:
            return jsonify({'status': 200, 'message': 'Success', 'redirect': '/todo'})
    if error:
        return jsonify({'status': 500, 'message': 'Error'})
    
    return render_template('todo/edit.html', todo=todo)
            
@bp.route('/delete/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def delete(todo_id):
    error = ''
    todo, error = svc_todo.get_by_id(todo_id)

    if request.method == 'POST':
        _,error = svc_todo.delete(todo_id)
        if not error:
            return redirect(url_for('board.home'))

    if error:
        flash(error)

    return jsonify({'status': 200, 'redirect': '/board'})



