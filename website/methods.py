from django.db.models.fields import CharField
from quiz.models import Category, Quiz, Question, SubCategory
from essay.models import Essay_Question
from multichoice.models import MCQuestion
from true_false.models import TF_Question
from website.models import User, AssignTest
from itertools import chain

from datetime import datetime


def create_quiz(user_email, plang, position):
    '''
    Function to associate a user with a quiz
    
    '''
    user = User.objects.filter(email=user_email)
    try:
        userid = user[0].id
    except:
        return None
    else:
        new_quiz = select_questions(plang , position)
        if new_quiz is None:
            raise TypeError
        else:
            set_quiz = Candidate.objects.create(userid=user, quiz_list_id=new_quiz)
            set_quiz.save()

            return set_quiz



def select_questions(plang, position):
    '''
    Function to create quiz selecting appropriate questions

    '''
    category = Category.objects.filter(category=plang)  # selection for language
    if category.count() > 0:
        
        new_quiz = Quiz.objects.create()
        new_quiz.title = str(datetime.now()) + plang + position
        new_quiz.url = str(datetime.now()) + plang + position
        new_quiz.save()

        language_subset = SubCategory.objects.filter(category_id = category[0].id)
        
        MC_list = MCQuestion.objects.filter(sub_category__in=language_subset.values('id')) 
        TF_list = TF_Question.objects.filter(sub_category__in=language_subset.values('id'))
        # Essay_list = Essay_Question.objects.filter(sub_category__in=language_subset.values('id'))
               
        questions_list = list(chain(MC_list.values('id'), TF_list.values('id')))

        for item in questions_list: 
            question = Question.objects.get(id=item['id'])
            question.quiz.add(new_quiz)         
        return new_quiz.id
    else:
        return None
