from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType


class Pessoa(Model):
    nome = StringType(required=True)
    idade = IntType(serialize_when_none=False)
    linguagens = ListType(StringType, serialize_when_none=False)
