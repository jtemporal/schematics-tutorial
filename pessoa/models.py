from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType

from udtypes import SizedNumberType


class Cachorrinho(Model):
    nome = StringType(required=True, deserialize_from="name",
                      serialized_name="name")
    cor = StringType(required=True, deserialize_from="fur",
                      serialized_name="fur")


class Pessoa(Model):
    nome = StringType(required=True, deserialize_from="name",
                      serialized_name="name")
    idade = SizedNumberType(serialize_when_none=False, deserialize_from="age",
                            serialized_name="age")
    linguagens = ListType(StringType, serialize_when_none=False,
                          deserialize_from="lang", serialized_name="blabla")
    cachorrinhos = ListType(ModelType(Cachorrinho), serialize_when_none=False,
                            deserialize_from="pets", serialized_name="pets")
