from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'rest', views.RestViewSet)

urlpatterns = [
    # /hr/
    url(r'^$', views.index, name='index'),
    url('rest', include(router.urls)),
]