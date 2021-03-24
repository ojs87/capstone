from django.contrib import admin
from .models import TarkovItem, TarkovQuest, TarkovItemQuest, User, TarkovHideout, TarkovItemHideout
# Register your models here.
# class TarkovItemAdmin(admin.ModelAdmin):
#
# class TarkovQuestAdmin(admin.ModelAdmin):

class TarkovItemQuestAdmin(admin.ModelAdmin):
    list_display = ("tarkovitem", "tarkovquest")

class TarkovItemHideoutAdmin(admin.ModelAdmin):
    list_display = ("tarkovitem", "tarkovhideout")

class TarkovQuestAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)

class TarkovItemAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name", )

admin.site.register(TarkovItem, TarkovItemAdmin)
admin.site.register(TarkovQuest, TarkovQuestAdmin)
admin.site.register(TarkovItemQuest, TarkovItemQuestAdmin)
admin.site.register(User)
admin.site.register(TarkovHideout)
admin.site.register(TarkovItemHideout, TarkovItemHideoutAdmin)
