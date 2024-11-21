from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Mark(Base):
    __tablename__ = "marks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[str] = mapped_column(String(10))
    

class Review(Base):
    __tablename__ = "reviews"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String)
    owner: Mapped[str] = mapped_column(String(69))
    marks_id: Mapped[int] = mapped_column(ForeignKey(Mark.id))
    mark: Mapped[Mark] = relationship()
    