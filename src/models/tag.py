# standard
from typing import List

# alchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

# internal
from .base import Base


class TagPost(Base):
    """Tag-Post Association Model"""

    __tablename__ = "tag_post"

    # relations
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
    tag: Mapped["Tag"] = relationship(back_populates="posts")
    post: Mapped["Post"] = relationship(back_populates="tags")

    def __repr__(self):
        return f"TagPost(tag={self.tag_id}, post={self.post_id})"


class Tag(Base):
    """Tag Model"""

    __tablename__ = "tag"

    # fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    # relations
    posts: Mapped[List["TagPost"]] = relationship(back_populates="tag")
