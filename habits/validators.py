from rest_framework.serializers import ValidationError


def validate_period_value(value):
    if not (1 <= int(value) <= 7):
        raise ValidationError(
            "Нельзя выполнять привычку реже чем 1 раз в неделю, больше чем 7 раз в неделю."
        )
    return int(value)
