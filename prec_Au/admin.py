from django.contrib import admin
from .models import Info
# Register your models here.

@admin.register(Info)
class Au_Admin(admin.ModelAdmin):
    pass