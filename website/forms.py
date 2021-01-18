from django import forms
from django.forms import fields
from quiz.models import Category, SubCategory 
from website.models import User, Role, AssignTest

class selectAssignTestForm(forms.Form):

    class Meta:
        model = AssignTest
        fields = ['category', 'role', 'candidate']


    category = forms.ChoiceField(
        label="Select the type of test you want to create",
        choices = [],
    )

    role = forms.ChoiceField(
            label="Select which role you are hiring",
            required=True,
            choices = [],
    )

    candidate = forms.CharField(
            label="Recipient's email",
            required=True,
    )

        

    def __init__(self,*args,**kwargs):
        super (selectAssignTestForm,self ).__init__(*args,**kwargs) # populates the post 
        self.fields['category'].choices= [(x['id'], x['category']) for x in Category.objects.values()] 
        self.fields['role'].choices= [(x['id'], x['name']) for x in Role.objects.values()] 
	
        
    

    # candidate_role = forms.ChoiceField(
    #     label="Candidate Role",
    #     choices = [],
    # )


    

    # #Preenche lista 
    # def __init__(self, *args, **kwargs):
    #     super(selectAssignTestForm, self).__init__(*args, **kwargs)
    #     self.fields['p_language'].choices = [(x['id'], x['category']) for x in Category.objects.values()] 
    #     self.fields['candidate_role'].choices =[(x['id'], x['name']) for x in Role.objects.values()] 