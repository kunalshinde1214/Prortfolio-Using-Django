from django.contrib import admin
from .models import home
# Register your models here.
admin.site.register(home)

#class homeAdmin(admin.ModelAdmin):
 # list_display = ("firstname", "lastname", "enroll_id",)
#admin.site.register(home, homeAdmin)