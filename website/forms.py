from django import forms
from quiz.models import Category, SubCategory 
from website.models import User, Role

class selectAssignTestForm(forms.Form):
    
    p_language = forms.ChoiceField(
        label="Programming Language",
        choices = [],
    )

    candidate_role = forms.ChoiceField(
        label="Candidate Role",
        choices = [],
    )


    candidate_email = forms.CharField(
            help_text="Enter Candidate Email Here", 
            label="Candidate email",
            required=True)

    #Preenche lista 
    def __init__(self, *args, **kwargs):
        super(selectAssignTestForm, self).__init__(*args, **kwargs)
        self.fields['p_language'].choices = [(x['id'], x['category']) for x in Category.objects.values()] 
        self.fields['candidate_role'].choices =[(x['id'], x['name']) for x in Role.objects.values()] 