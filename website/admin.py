from django.contrib import admin

from .models import Candidate, User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'password', 
        'is_candidate', 'is_evaluator', 'is_interviwer',
        'is_active',)


admin.site.register(Candidate)
admin.site.register(User, UserAdmin)

# Register your models here.
