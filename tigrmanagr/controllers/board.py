from flask import Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, session
from functools import wraps


import tigrmanagr.services.todo as svc_todo
import tigrmanagr.services.board as svc_board

bp = Blueprint('board', __name__, url_prefix='/board')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)

        if user:
            return f(*args, **kwargs)
        return redirect('/login')
    return decorated_function

@bp.route('/')
@login_required
def home():
    boards, error = svc_board.get_all()
    if error:
        flash(error)
    email = dict(session)['profile']['email']
    return render_template('board/index.html', email=email, boards=boards)

@bp.route('/<int:board_id>')
@login_required
def boardSpace(board_id):
   todos, error = svc_board.get_todo(board_id)
   boards, error = svc_board.get_all()
   board, error = svc_board.get_by_id(board_id)
   if error:
       flash(error)
   email = dict(session)['profile']['email']
   return render_template('board/read.html', todos=todos, email=email, boards=boards, board=board)

@bp.route('/<int:board_id>/create', methods=['GET', 'POST'])
@login_required
def createTodo(board_id):
    error = ''
    board, error = svc_board.get_by_id(board_id)
    if request.method == 'POST':
        data = request.get_json() or {}
        
        if data.get('todo_title') and data.get('board_id'):
            todo_title = data.get('todo_title', '')
            board_id = data.get('board_id', '')

            todo_title = todo_title.strip()

            data = {
                'todo_title': todo_title,
                'board_id': int(board_id)
            }
            _,error = svc_todo.create(data)
            if not error:
                return jsonify({'status': 200, 'message': 'Success', 'redirect': '/board'})

    if error:
        return jsonify({'status': 500, 'message': 'Error'})
    return render_template('todo/create.html', board=board)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def createBoard():
    error = ''
    if request.method == 'POST':
        data = request.get_json() or {}
        
        if data.get('board_name'):
            board_name = data.get('board_name', '')

            board_name = board_name.strip()

            data = {
                'board_name': board_name,
            }
            _,error = svc_board.create(data)
            if not error:
                return jsonify({'status': 200, 'message': 'Success', 'redirect': '/board'})

    if error:
        return jsonify({'status': 500, 'message': 'Error'})
    return render_template('board/create.html')

@bp.route('/edit/<int:board_id>', methods=['GET', 'POST'])
@login_required
def edit(board_id):
    error = ''
    board, error = svc_board.get_by_id(board_id)

    if request.method == 'POST':

        data = request.get_json() or {}

        if data.get('board_id') and data.get('name_update'):
            board_id = data.get('board_id', '')
            name_update = data.get('name_update', '')
                                                    
            name_update = name_update.strip()


            data = {
                'board_id': int(board_id),
                'board_name': name_update,
            }
            _,error = svc_board.edit(data)
        if not error:
            return jsonify({'status': 200, 'message': 'Success', 'redirect': '/board'})
    if error:
        return jsonify({'status': 500, 'message': 'Error'})
    
    return render_template('board/edit.html', board=board)
            
@bp.route('/delete/<int:board_id>', methods=['GET', 'POST'])
@login_required
def delete(board_id):
    error = ''
    todo, error = svc_board.get_by_id(board_id)

    if request.method == 'POST':
        _,error = svc_board.delete(board_id)
        if not error:
            return redirect(url_for('board.home'))

    if error:
        flash(error)

    return jsonify({'status': 200, 'redirect': '/'})



