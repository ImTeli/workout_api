from app.core.base_model import Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CentroTreinamento(Base):
    __tablename__ = "centros_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # type: ignore  # noqa: F821
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="centro_treinamento")  # type: ignore  # noqa: F821
