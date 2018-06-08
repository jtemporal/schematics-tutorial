from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType


class Pessoa(Model):
    nome = StringType(required=True)
    idade = IntType()
    linguagens = ListType(StringType)
