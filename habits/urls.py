from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublishedHabitListAPIView
from django.urls import path


schema_view = get_schema_view(
    openapi.Info(
        title="Atomic habits API",
        default_version='v1',
        description="Tracking to your habits",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = HabitsConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [
    # Published habit
    path('published_habit/', PublishedHabitListAPIView.as_view(), name='published_habit_list'),
    # docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls