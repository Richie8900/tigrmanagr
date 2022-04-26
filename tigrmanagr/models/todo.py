from sqlalchemy import Column, String, Integer, ForeignKey 
from sqlalchemy.orm import relationship
from tigrmanagr.db import Base

class Todo(Base):
    __tablename__ = 'todos'
    todo_id = Column(Integer, primary_key=True)
    todo_title = Column(String(200), nullable=False)
    todo_status = Column(Integer, nullable=False)
    board_id = Column(Integer, ForeignKey('boards.board_id'))
    
    # boards = relationship("Boards", back_populates="todo")
