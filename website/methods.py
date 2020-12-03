from quiz.models import Category, Quiz, Question, SubCategory
from essay.models import Essay_Question
from multichoice.models import MCQuestion
from true_false.models import TF_Question
from website.models import User, Candidate

from datetime import datetime


def bind_quiz(user_email, plang_id, position):
    '''
    Function to associate a user with a quiz
    
    '''
    user = User.objects.filter(email=user_email)
    if user is not None:
        userid = user[0].id
    else:
        return None
    
    new_quiz = create_quiz()
    set_quiz = Candidate.objects.create(userid=user, quiz_list_id=new_quiz)
    set_quiz.save()



def create_quiz(plang, position):
    '''
    Function to create quiz selecting appropriate questions

    '''
    #set of rules
    new_quiz = Quiz.objects.create()
    new_quiz.title = str(datetime.now()) + plang + position
    new_quiz.url = str(datetime.now()) + plang + position
    new_quiz.save()
    # chose question
    # Multiple Choice List
    category = Category.objects.filter(category=plang)  # selection for language
    language_subset = SubCategory.objects.filter(category_id = category[0].id)
    # MC_list = MCQuestion.objects.filter() # s
    # True/False List

    return new_quiz.id
