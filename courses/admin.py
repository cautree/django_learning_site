from django.contrib import admin

from .models import Course
from .models import Step

admin.site.register(Course)
admin.site.register(Step)
