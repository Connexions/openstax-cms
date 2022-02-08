from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'roles', views.RoleViewSet)
router.register(r'subjects', views.SubjectList, basename="Subjects")
router.register(r'erratacontent', views.ErrataContentViewSet, basename="ErrataContent")
router.register(r'subjectcategory', views.SubjectCategoryViewSet, basename="SubjectCategory")
urlpatterns = router.urls
