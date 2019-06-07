from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'roles', views.RoleViewSet)
router.register(r'subjects', views.SubjectList, base_name="Subjects")
urlpatterns = router.urls
