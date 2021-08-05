from django.contrib import admin

# Register your models here.
from .models import Home

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Home, HomeAdmin)