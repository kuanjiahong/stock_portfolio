from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positive_number(value: float) -> None:
    """
    Raise ValidationError if value is negative

    :param value: the numeric value to check
    :return: ValidationError if value is negative
    """
    if value < 0:
        raise ValidationError(_('%(value)s is a negative number'), params={'value': value})
