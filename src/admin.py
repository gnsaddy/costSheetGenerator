from django.contrib import admin
from .models import UserProfile, CostSheetName, Embroidery, Fabric
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin


class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')


admin.site.register(UserProfile)
admin.site.register(CostSheetName)
admin.site.register(Embroidery)
admin.site.register(Fabric)
admin.site.unregister(Group)
