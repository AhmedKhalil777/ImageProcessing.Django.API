from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from StudentProject.AttendanceApp.serializers import GroupSerializer, UserSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all.order_by('data_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSets(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

