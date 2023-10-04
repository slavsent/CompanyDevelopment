from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "short_name", "post_address", "bank_account", "deleted"]
    list_per_page = 5
    list_filter = ["name", "short_name", "deleted"]

    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.Developments)
class DevelopmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "cod", "name", "parent", "levels", "deleted"]
    list_per_page = 5
    list_filter = ["cod", "parent", "levels", "deleted"]

    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["id", "firstname", "lastname", "post_address", "bank_account", "development", "deleted"]
    list_per_page = 5
    list_filter = ["firstname", "lastname", "development", "deleted"]

    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")
