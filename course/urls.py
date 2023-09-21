from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register("", StudentViewSet),
router.register("", UniversityViewSet)

urlpatterns = [
    path("", include(router.urls))
]
