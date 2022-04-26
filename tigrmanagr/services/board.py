from sqlalchemy import exc, insert, select, update
from tigrmanagr.models.board import Board
from tigrmanagr.models.todo import Todo
from tigrmanagr.db import session

#Code for todo

def get_all():
    error = ''
    try: 
        statement = select(Board)
        board = session.execute(statement).scalars().all() # scalars is used to make sure result is formatted as a list
    except exc.NoResultFound as e:
        error = e
    return board, error

def get_by_id(board_id):
    error = ''
    try:
        board = session.get(Board, board_id)
    except exc.NoResultFound as e:
        error = e
    return board, error

def create(data):
    """ function to create todo from data dict passed by controller return error if no data sent from controller"""
    error = ''
    if data:
        try:
            statement = insert(Board).values(data)
            session.execute(statement)
            session.commit()
        except exc.IntegrityError as e:
            session.rollback()
            error = e
    return None, error # returning none as a default response from server. But in controller None is ignored so unless there's error, everything is ok

def edit(data):
    """ function to update title and status """
    error = ''
    if data and data.get('board_id') and data.get('board_name'):
        try:
            update_data = data.copy()
            update_data.pop('board_id')
            statement = update(Board)\
                    .where(Board.board_id == data['board_id'])\
                    .values(update_data)\
                    .execution_options(synchronize_session='fetch')
            session.execute(statement)
            session.commit()
        except exc.IntegrityError as e:
            session.rollback()
            error = e
                                                                            
    return None, error # returning none. But in controller, None is ignored

def delete(board_id):
    """function to delete todo with id as the parameter"""
    error = ''
    try:
        board = session.get(Board, board_id)
        session.delete(board)
        session.commit()
    except exc.IntegrityError as e:
        session.rollback()
        error = e
    return None, error

#If there's some errror when getting the todo, this may be the case

def get_todo(board_id):
    error = ''
    try:
        statement = select(Todo, Todo.todo_id, Todo.todo_title, Todo.board_id)\
                    .where(Todo.board_id == board_id)\
                    .join(Board, Board.board_id == Todo.board_id)\
                    .where(Board.board_id == board_id)
        todos = session.execute(statement).scalars().all() # scalars is used to make sure result is formatted as a list
    except exc.IntegrityError as e:
        session.rollback()
        error = e
    return todos, error

