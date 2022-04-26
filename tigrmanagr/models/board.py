from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from tigrmanagr.db import Base

class Board(Base):
    __tablename__ = 'boards'
    board_id = Column(Integer, primary_key=True)
    board_name = Column(String(200), nullable=False)


    
