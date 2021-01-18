from django.contrib import admin
from django.contrib.admin.sites import site

from .models import AssignTest, User, Role 

# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         'username', 'password', 
#         'is_candidate', 'is_evaluator', 'is_interviwer',
#         'is_active',)


admin.site.register(AssignTest)
admin.site.register(Role)
admin.site.register(User)


# Register your models here.
