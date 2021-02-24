from django.contrib import admin
from django.contrib.admin.sites import site

from .models import AssignTest, User, Role, Rules, Evaluation, EvaluationScore
from quiz.models import Category

class AssignTestAdmin(admin.ModelAdmin):
    class Meta:
        model = AssignTest

    fields = (
        'candidate', 'requestor', 
        'evaluator_1', 'evaluator_2', 'role', 'language',
        'quiz', 'sitting')
    readonly_fields = ('candidate', 'role', 'language')

class RulesAdmin(admin.ModelAdmin):
    class Meta:
        model = Rules
    
    fields = ( 
        ('n_basic_obj',  'mark_basic_obj'),
        ('n_intermediate_obj',  'mark_intermediate_obj'),
        ('n_advanced_obj',  'mark_advanced_obj'),
        ('n_basic_subj',  'mark_basic_subj'),
        ('n_intermediate_subj',  'mark_intermediate_subj'),
        ('n_advanced_subj',  'mark_advanced_subj')      
    )

class EvaluationScoreInline(admin.TabularInline):
    model = EvaluationScore
    extra = 1
    
class EvaluationAdmin(admin.ModelAdmin):
    class Meta:
        model = Evaluation
    
    inlines = [EvaluationScoreInline]

    
 
admin.site.register(AssignTest, AssignTestAdmin)
admin.site.register(Role)
admin.site.register(Rules, RulesAdmin)
admin.site.register(User)
admin.site.register(Evaluation, EvaluationAdmin)


# Register your models here.
