from django.db.models.fields import CharField
from quiz.models import Category, Quiz, Question, SubCategory
from essay.models import Essay_Question
from multichoice.models import MCQuestion
from true_false.models import TF_Question
from website.models import User, Candidate
from itertools import chain

from datetime import datetime


def bind_quiz(user_email, plang, position):
    '''
    Function to associate a user with a quiz
    
    '''
    user = User.objects.filter(email=user_email)
    try:
        userid = user[0].id
    except:
        return "user not found"
    else:
        new_quiz = create_quiz(plang , position)
        if new_quiz is None:
            raise TypeError
        set_quiz = Candidate.objects.create(userid=user, quiz_list_id=new_quiz)
        set_quiz.save()

        return set_quiz



def create_quiz(plang, position):
    '''
    Function to create quiz selecting appropriate questions

    '''
    
    
    category = Category.objects.filter(category=plang)  # selection for language
    if category.count() > 0:
        language_subset = SubCategory.objects.filter(category_id = category[0].id)
        new_quiz = Quiz.objects.create()
        new_quiz.title = str(datetime.now()) + plang + position
        new_quiz.url = str(datetime.now()) + plang + position
        new_quiz.save()
        MC_list = MCQuestion.objects.filter(sub_category__in=language_subset.values('id')) 
        TF_list = TF_Question.objects.filter(sub_category__in=language_subset.values('id'))

        
        for i in list(chain(MC_list.values('id'), TF_list.values('id'))):
            question = Question.objects.get(id=i['id'])
            question.quiz.add(new_quiz)         
        return new_quiz.id
    else:
        return None
