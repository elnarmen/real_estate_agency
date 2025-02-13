from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    ]
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'pure_phone',
    ]
    raw_id_fields = ['flats']


