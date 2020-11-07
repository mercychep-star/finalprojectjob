from django.contrib import admin

# Register your models here.
from jobs.models import Job,Category


admin.site.register(Job)
admin.site.register(Category)


