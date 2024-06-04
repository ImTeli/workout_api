from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from app.core.base_schema import BaseSchema, OutMixin
from app.entities.categorias.schema import CategoriaIn
from app.entities.centros_treinamento.schema import CentroTreinamentoAtleta


class SchemaAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples=['Joao', 'Gabriel'], max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples=['12345678900', '98765432100'], max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=[25,36])]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=[75.5, 83.3])]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=[1.70, 1.84])]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples=['M','F'], max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(SchemaAtleta):
    pass


class AtletaOut(SchemaAtleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', examples=['Joao'], max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', examples=[25])]