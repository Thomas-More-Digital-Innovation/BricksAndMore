from django.contrib import admin
from .models import Creation


# Register your models here.

class CreationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
        ('Creator', {'fields': ['creator']}),
        ('Image', {'fields': ['image']}),
    ]


admin.site.register(Creation, CreationAdmin)
