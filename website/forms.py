from django import forms
from quiz.models import Category, SubCategory 

class selectCandidateForm(forms.Form):
    candidate_email = forms.CharField(
            help_text="Enter Candidate Email Here", 
            label="Candidate email",
            required=True)
    p_language = forms.ChoiceField(
        choices = [],
    )

    #Preenche lista 
    def __init__(self, *args, **kwargs):
        super(selectCandidateForm, self).__init__(*args, **kwargs)
        self.fields['p_language'].choices = [(x.id, x.category()) for x in Category.objects.all()]