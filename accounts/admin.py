from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.html import format_html

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['email','first_name','last_name','username','last_login','is_active','date_joined']
    list_display_links = ['email','username']
    readonly_fields = ['last_login','date_joined']
    ordering = ['-date_joined',]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    
admin.site.register(Account,AccountAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="70" height="50" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(UserProfile,UserProfileAdmin)