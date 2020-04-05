from rest_framework import routers
from StudentProject.AttendanceApp import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSets)
router.register(r'groups', views.GroupViewSets)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
