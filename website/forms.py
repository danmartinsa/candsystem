from django import forms
from django.forms import fields
from quiz.models import Category, SubCategory 
from website.models import User, Role, AssignTest
from django.forms.widgets import RadioSelect, Textarea
from crispy_forms.bootstrap import InlineRadios


from crispy_forms.helper import FormHelper, Layout

class selectAssignTestForm(forms.Form):

    class Meta:
        model = AssignTest
        fields = ['category', 'role', 'candidate']

    role = forms.ChoiceField(
            label="Select which role you are hiring",
            required=True,
            choices = [],
    )

    category = forms.ChoiceField(
        label="Select the type of test you want to create",
        choices = [],
    )

    candidate = forms.CharField(
            label="Candidate's Email",
            required=True,
    )

        

    def __init__(self,*args,**kwargs):
        super (selectAssignTestForm,self ).__init__(*args,**kwargs) # populates the post 
        self.fields['category'].choices= [(x['id'], x['category']) for x in Category.objects.values()] 
        self.fields['role'].choices= [(x['id'], x['name']) for x in Role.objects.values()] 
	

from django.utils.safestring import mark_safe


from essay.models import Essay_Question
        
class QuestionForm(forms.Form):

    def __init__(self, quiz, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        question_list = quiz.get_questions()
        for question in question_list:
            field_name = str(question.id) + "answerset"
            if question.__class__ is Essay_Question:
                self.fields[field_name] = forms.CharField(
                    label=question.content,
                    widget=Textarea(attrs={'style': 'width:100%'}),
                    required = False
                    )
            else:
                choice_list = [x for x in question.get_answers_list()]
                
                
                self.fields[field_name] = forms.ChoiceField(
                    label=question.content,
                    choices=choice_list,
                    widget=RadioSelect(attrs={"class": "questionList"}),
                    required = False
                )
                self.helper = FormHelper()
                self.helper.layout = Layout(
                    InlineRadios(str(question))
                )

class EvaluateForm(forms.Form):
    def __init__(self, sitting, evaluation, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        question_list = sitting.quiz.get_questions()
        for question in question_list:
            field_name = str(question.id) + "answerset"
            self.fields[field_name] = forms.CharField(
                        label=question.content,
                        widget=Textarea(attrs={'style': 'width:100%'}),
                        required = False
            )
            field_name = str(question.id) + "candanswer"
      

    # candidate_role = forms.ChoiceField(
    #     label="Candidate Role",
    #     choices = [],
    # )


    

    # #Preenche lista 
    # def __init__(self, *args, **kwargs):
    #     super(selectAssignTestForm, self).__init__(*args, **kwargs)
    #     self.fields['p_language'].choices = [(x['id'], x['category']) for x in Category.objects.values()] 
    #     self.fields['candidate_role'].choices =[(x['id'], x['name']) for x in Role.objects.values()] 