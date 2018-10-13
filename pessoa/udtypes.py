from schematics.types import IntType
from schematics.exceptions import ValidationError

class SizedNumberType(IntType):
    def validate_number(self, number):
        sized = str(number)
        if len(sized) != 2:
            raise ValidationError("This number doesn't comply with the expected format size 2")
        return number
