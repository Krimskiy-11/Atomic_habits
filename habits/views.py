from rest_framework.viewsets import ModelViewSet
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    # pagination_class = CustomPagination
    serializer_class = HabitSerializer
