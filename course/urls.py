from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register("stu", StudentViewSet),
router.register("uni", UniversityViewSet)

routerV2 = routers.DefaultRouter()
routerV2.register("stu", StudentViewSet),
# routerV2.register("uni", UniversityViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v2/", include(routerV2.urls))
]
