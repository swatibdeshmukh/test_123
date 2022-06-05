from django.contrib import admin
from app1.models import Emplo
# Register your models here.

class EmploAdmin(admin.ModelAdmin):
    list_display = ['sid', 'name', 'marks']

admin.site.register(Emplo, EmploAdmin)