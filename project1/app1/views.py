from django.shortcuts import render
from app1.models import Emplo
from app1.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny#pre-defined permissions
from app1.permissions import IsReadonly, IsGetOrPostOrPut, RolePermission, SubUserPermission
# Create your views here.

class EmploInfo(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Emplo.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [SubUserPermission]