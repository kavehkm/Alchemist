# standard
from typing import List

# alchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

# internal
from .base import Base


class Category(Base):
    """Category Model"""

    __tablename__ = "category"

    # fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    # relations
    posts: Mapped[List["Post"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}"
