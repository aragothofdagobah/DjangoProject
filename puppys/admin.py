from django.contrib import admin

from .models import ToyPoodle, ShihTzu


class ToyPoodleAdmin(admin.ModelAdmin):
    fields = ['Name', 'Description', 'Pic']


class ShihTzuAdmin(admin.ModelAdmin):
    fields = ['Name', 'Description', 'Pic']


admin.site.register(ToyPoodle, ToyPoodleAdmin)
admin.site.register(ShihTzu, ShihTzuAdmin)
