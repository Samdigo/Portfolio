from django.contrib import admin
from .models import Developer, Project


@admin.register(Developer)
class DevAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProAdmin(admin.ModelAdmin):
    pass