from sqlalchemy import exc, insert, select, update
from tigrmanagr.models.board import Board
from tigrmanagr.models.todo import Todo
from tigrmanagr.db import session

def get_all():
    error = ''
    try: 
        statement = select(Todo)
        todos = session.execute(statement).scalars().all() # scalars is used to make sure result is formatted as a list
    except exc.NoResultFound as e:
        error = e
    return todos, error

def get_by_id(todo_id):
    error = ''
    try:
        todo = session.get(Todo, todo_id)
    except exc.NoResultFound as e:
        error = e
    return todo, error

def create(data):
    """ function to create todo from data dict passed by controller return error if no data sent from controller"""
    error = ''
    if data:
        try:
            statement = insert(Todo).values(data)
            session.execute(statement)
            session.commit()
        except exc.IntegrityError as e:
            session.rollback()
            error = e
    return None, error # returning none as a default response from server. But in controller None is ignored so unless there's error, everything is ok

def edit(data):
    """ function to update title and status """
    error = ''
    if data and data.get('todo_id') and data.get('todo_title') and data.get('todo_status'):
        try:
            update_data = data.copy()
            update_data.pop('todo_id')
            statement = update(Todo)\
                    .where(Todo.todo_id == data['todo_id'])\
                    .values(update_data)\
                    .execution_options(synchronize_session='fetch')
            session.execute(statement)
            session.commit()
        except exc.IntegrityError as e:
            session.rollback()
            error = e
                                                                            
    return None, error # returning none. But in controller, None is ignored

def delete(todo_id):
    """function to delete todo with id as the parameter"""
    error = ''
    try:
        todo = session.get(Todo, todo_id)
        session.delete(todo)
        session.commit()
    except exc.IntegrityError as e:
        session.rollback()
        error = e
    return None, error


