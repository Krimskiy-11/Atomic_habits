from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner
from rest_framework.generics import ListAPIView


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    pagination_class = CustomPagination
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "retrieve", "destroy"]:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class PublishedHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
