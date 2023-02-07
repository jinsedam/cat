from django.contrib import admin
from .models import Catalyst
# Register your models here.

@admin.register(Catalyst)
class Catalyst_Admin(admin.ModelAdmin):
    pass
