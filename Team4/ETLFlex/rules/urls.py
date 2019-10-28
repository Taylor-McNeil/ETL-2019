from rest_framework import routers
from .api import RulesViewSet

router = routers.DefaultRouter()
router.register('api/rules', RulesViewSet, 'rules')

urlpatterns = router.urls
