from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'manager_name')
    
    def to_representation(self, instance):
        rep = super(EmployeeSerializer, self).to_representation(instance)
        rep['manager_name'] = instance.manager_name_id
        return rep