from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include
from .api import RulesViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/rules', RulesViewSet, 'rules')
# router.register(r'^admin/', admin.site.urls)
# router.register('testPost/', views.testClass, 'testClass')

urlpatterns = [
    path('', include(router.urls)),
    url('submit_rule/', views.rule_submission),
    url('sync', views.sync),
    url('get_rules/', views.get_rules),
    url('get_file_history/', views.get_file_history),
    url('get_file_data/', views.get_file_data)
]
