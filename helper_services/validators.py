from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_card_number_input(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError(
            _('%(value) has to be 16 digits long.'))
    if len(value) != 16:
        raise ValidationError(
            _('%(value) has to be 16 digits long.'))


def validate_number_input(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError(
            _('‰(value) has to be only digits.'))


def validate_exp_date(value):
    if len(value) != 5:
        raise ValidationError(
            _('Expiration date has to be on this format MM/YY.'))
    try:
        int(value[0])
        int(value[1])
        int(value[3])
        int(value[4])
    except ValueError:
        raise ValidationError(
            _('Expiration date has to be on this format MM/YY.'))

    if value[2] != '/':
        raise ValidationError(
            _('Expiration date has to be on this format MM/YY.'))
