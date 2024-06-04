from app.core.base_model import Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Categoria(Base):
    __tablename__ = "categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # type: ignore  # noqa: F821
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="categoria")  # type: ignore  # noqa: F821
