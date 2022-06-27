from django.contrib import admin
from .models import Choice, Question, Student

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Student)


# Register your models here.
