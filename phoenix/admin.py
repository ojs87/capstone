from django.contrib import admin
from .models import TarkovItem, User, TarkovHideout, TarkovItemHideout, TarkovQuestTester, TarkovFoundInRaid, TarkovQuestStructure
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
# class TarkovItemAdmin(admin.ModelAdmin):
#
# class TarkovQuestAdmin(admin.ModelAdmin):


class TarkovItemHideoutAdmin(admin.ModelAdmin):
    list_display = ("tarkovitem", "tarkovhideout")

class TarkovQuestAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)

class TarkovItemAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name", )

class TarkovQuestTesterAdmin(admin.ModelAdmin):
    list_display = ("name", "questgiver")
    ordering = ("questgiver", "name")

class TarkovFoundInRaidAdmin(admin.ModelAdmin):
    list_display = ("name", "quest", "amount")
    ordering = ("name", )


admin.site.register(TarkovQuestStructure, DraggableMPTTAdmin, list_display=('tree_actions', 'indented_title'), list_display_links=('indented_title',),)
admin.site.register(TarkovFoundInRaid, TarkovFoundInRaidAdmin)
admin.site.register(TarkovQuestTester, TarkovQuestTesterAdmin)
admin.site.register(TarkovItem, TarkovItemAdmin)
admin.site.register(User)
admin.site.register(TarkovHideout)
admin.site.register(TarkovItemHideout, TarkovItemHideoutAdmin)
