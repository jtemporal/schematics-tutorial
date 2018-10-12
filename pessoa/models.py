from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType


class Pessoa(Model):
    nome = StringType(required=True, serialize_when_none=False,
                      deserialize_from="name")
    idade = IntType(serialize_when_none=False, deserialize_from="age")
    linguagens = ListType(StringType, serialize_when_none=False,
                          deserialize_from="lang")

