from django.contrib import admin

# Register
from .models import EmployeeProfile,Degree,Skill,Training,Experience,CV
admin.site.register(EmployeeProfile)
admin.site.register(Degree)
admin.site.register(Skill)
admin.site.register(Training)
admin.site.register(Experience)
admin.site.register(CV)
