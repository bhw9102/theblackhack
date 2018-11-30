from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from game.models import *


class JobClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


class EquipmentClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'defence')
    list_display_links = ('id', 'name', )
    list_filter = ('price', 'defence', )


admin.site.register(JobClass, JobClassAdmin)
admin.site.register(EquipmentClass, EquipmentClassAdmin)
