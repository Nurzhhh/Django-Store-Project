from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "text")

# @admin.register(MassEmail)
# class MassEmailAdmin(admin.ModelAdmin):
# 	list_display = ("subject", "text")
