from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, CharField
from habits.models import Habit
from habits.validators import validate_period_value
from django.utils.timezone import timedelta
from rest_framework import serializers


class HabitSerializer(ModelSerializer):
    period = CharField(validators=[validate_period_value])
    reward = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Habit
        fields = [
            'id', 'place', 'time', 'action',
            'is_pleasant', 'connection_habit', 'period',
            'reward', 'time_to_action', 'is_published'
        ]

    def validate(self, attrs):
        is_pleasant = attrs.get('is_pleasant')
        connection_habit = attrs.get('connection_habit')
        reward = attrs.get('reward')
        time_to_action = attrs.get('time_to_action')

        if reward == "":
            reward = None

        if connection_habit and reward:
            raise ValidationError("Одновременный выбор вознаграждения и связанной привычки")

        if time_to_action and time_to_action > timedelta(minutes=2):
            raise ValidationError({
                'time_to_action': ["Время выполнения больше 120 секунд"]
            })

        if connection_habit:
            connected_habit = Habit.objects.get(pk=connection_habit)
            if not connected_habit.is_pleasant:
                raise ValidationError({
                    'connection_habit': ["Связанная привычка должна быть приятной."]
                })

        if is_pleasant and (connection_habit or reward):
            raise ValidationError({
                'non_field_errors': [
                    "У приятной привычки не может быть вознаграждения или связанной привычки."
                ]
            })

        attrs['reward'] = reward

        return attrs
