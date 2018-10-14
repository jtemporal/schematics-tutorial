from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType

from udtypes import SizedNumberType


class Cachorrinho(Model):
    nome = StringType(required=True, deserialize_from="name",
                      serialized_name="name")
    cor = StringType(required=True, deserialize_from="fur",
                      serialized_name="fur")
    def validate_nome(self, data, value):
        if data['nome'].capitalize() != data['nome']:
            raise ValidationError('Pet name is not capitalized!')
        return value


class Pessoa(Model):
    def linguagens_validas(value):
        linguagens_disponiveis = ["python", "r", "go", "rum"]
        result = [a for a in value if a not in linguagens_disponiveis]
        if type(value) is list:
            return value
        if value.lower() not in linguagens_disponiveis:
            raise ValidationError(f'Language {value} not available!')

    nome = StringType(required=True, deserialize_from="name",
                      serialized_name="name")
    idade = SizedNumberType(serialize_when_none=False, deserialize_from="age",
                            serialized_name="age")
    linguagens = ListType(StringType, serialize_when_none=False,
                          deserialize_from="lang", serialized_name="blabla",
                          validators=[linguagens_validas])
    cachorrinhos = ListType(ModelType(Cachorrinho), serialize_when_none=False,
                            deserialize_from="pets", serialized_name="pets")
