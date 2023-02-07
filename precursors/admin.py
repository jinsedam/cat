from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Au)
class Au_Admin(admin.ModelAdmin):
    pass

@admin.register(PEG)
class PEG_Admin(admin.ModelAdmin):
    pass

@admin.register(Au_PEG)
class Au_PEG_Admin(admin.ModelAdmin):
    pass