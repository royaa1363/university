from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, TeacherViewSet, Main_unitViewSet, MajorViewSet, Public_unitViewSet, SessionViewSet, \
    TermViewSet, teacher_apiview, TeacherApiView

router = routers.DefaultRouter()
router.register("maj", MajorViewSet),
router.register("main", Main_unitViewSet),
router.register("pub", Public_unitViewSet),
router.register("stu", StudentViewSet),
router.register("teach", TeacherViewSet),
router.register("sess", SessionViewSet),
router.register("term", TermViewSet)


# routerV2 = routers.DefaultRouter()
# routerV2.register("stu", StudentViewSet),
# routerV2.register("uni", UniversityViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("teach/", TeacherApiView.as_view()),
    path("teach1/", teacher_apiview)
]
