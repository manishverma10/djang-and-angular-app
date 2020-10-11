from django.db import models

class Employee(models.Model):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    CEO = 'CEO'

    EMPLOYEE_TYPES = (
        (STANDARD, 'employee'),
        (MANAGER, 'manager'),
        (CEO, 'CEO')
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    employee_name = models.CharField(max_length=100)
    manager_name = models.ForeignKey('self', null= True, related_name= 'employee', on_delete = models.CASCADE,)

    def __str__(self):
        return self.employee_name

    def __repr__(self):
        return self.__str__()