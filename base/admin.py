from django.contrib import admin
from .models import Task,Products,News,FilesUpload,Sts,TueForm

admin.site.site_header = "BHS Admin"
admin.site.index_title = "Welcome to the BHS Anti-doping and TUE Website"
admin.site.site_title = "Anti-Doping and TUE"
# from .models import *

admin.site.register(Task)
admin.site.register(Products)
admin.site.register(News)
admin.site.register(FilesUpload)
admin.site.register(Sts)
admin.site.register(TueForm)

# class News(admin.ModelAdmin):
#     list_display = ("title")