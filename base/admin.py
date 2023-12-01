from django.contrib import admin
from base.models import Drug, Purchase, History

# Register your models here.


@admin.register(Drug)
class DrugAddmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Drug._meta.fields)
    search_fields = ["name"]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Purchase._meta.fields)
    search_fields = ["drug__name"]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in History._meta.fields)
    search_fields = ["purchase__drug__name"]
