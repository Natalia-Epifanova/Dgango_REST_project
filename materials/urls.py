from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonCreateApiView,
    LessonUpdateApiView,
    LessonDestroyApiView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)


urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_detail"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyApiView.as_view(),
        name="lesson_destroy",
    ),
] + router.urls
