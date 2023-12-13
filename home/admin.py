from django.contrib import admin
from .models import Honor


@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    pass
