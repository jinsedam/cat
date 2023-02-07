from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ICP_OES)
class ICP_OES_Admin(admin.ModelAdmin):
    pass

@admin.register(GC)
class GC_Admin(admin.ModelAdmin):
    pass

@admin.register(SAXS)
class SAXS_Admin(admin.ModelAdmin):
    pass

@admin.register(BET)
class BET_Admin(admin.ModelAdmin):
    pass

@admin.register(TEM)
class TEM_Admin(admin.ModelAdmin):
    pass

@admin.register(TGA)
class TGA_Admin(admin.ModelAdmin):
    pass
