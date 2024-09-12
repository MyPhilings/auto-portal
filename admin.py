from django.contrib import admin
from .models import User, Customer, Employee, Vehicle, RepairJob, Schedule

# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Vehicle)
admin.site.register(RepairJob)
admin.site.register(Schedule)