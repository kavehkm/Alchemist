# standard
from typing import List

# alchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey

# internal
from .base import Base


class Post(Base):
    """Post Model"""

    __tablename__ = "post"

    # fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    # relations
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="posts")
    tags: Mapped[List["TagPost"]] = relationship(back_populates="post")

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title})"
