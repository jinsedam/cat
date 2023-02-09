from django.contrib import admin
from .models import Data, Photo
# Register your models here.

@admin.register(Data, Photo)
class TEMAdmin(admin.ModelAdmin):
    pass