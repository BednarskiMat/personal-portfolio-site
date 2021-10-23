from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Skill
from .models import Project

admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Project)