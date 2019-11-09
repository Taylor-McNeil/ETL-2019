from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include
from .api import RulesViewSet
from rules import views

router = routers.DefaultRouter()
router.register('api/rules', RulesViewSet, 'rules')
#router.register(r'^admin/', admin.site.urls)
#router.register('testPost/', views.testClass, 'testClass')

urlpatterns = [
    path('', include(router.urls)),
    url('testPost/', views.testPost),    
    url('testGet/', views.testGet)
]