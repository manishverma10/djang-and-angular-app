from django.shortcuts import render
from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer

def index(request):
    employee_list = Employee.objects.order_by('id').all()
    context = {'employees': employee_list}
    return render(request, 'employee_mgmt/index.html', context)


class RestViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.order_by('id').all()
    serializer_class = EmployeeSerializer