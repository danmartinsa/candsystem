from django.db.models.fields import CharField
from quiz.models import Category, Quiz, Question, Sitting, SubCategory
from essay.models import Essay_Question
from multichoice.models import MCQuestion
from true_false.models import TF_Question
from website.models import User, AssignTest, Role
from itertools import chain

from datetime import datetime


def create_quiz(user_email, plang, position, interviewer):
    '''
    Function to associate a user with a quiz
    
    '''
    
    try:
        user = User.objects.get(email=user_email)
    except:
        user = User.objects.create_user(username=user_email,
                                 email=user_email,
                                 password='evs123',
                                 is_candidate=True)
        user.save()
    
    new_quiz = select_questions(plang , position)
    if new_quiz is None:
        raise TypeError
    else:
        sitting = Sitting.objects.new_sitting(user=user, quiz=new_quiz)
        set_quiz = AssignTest.objects.create(candidate=user, quiz=new_quiz, requestor=interviewer, role=position, sitting=sitting)
        set_quiz.save()

        return new_quiz



def select_questions(plang, position):
    '''
    Function to create quiz selecting appropriate questions

    '''
    category = Category.objects.get(id=plang.id)  # selection for language
        
    new_quiz = Quiz.objects.create()
    new_quiz.title = str(datetime.now()) + category.category
    new_quiz.url = str(datetime.now()) + category.category
    new_quiz.category = category
    new_quiz.save()

    language_subset = SubCategory.objects.filter(category_id = category.id)

    MC_list = MCQuestion.objects.filter(sub_category__in=language_subset.values('id')) 
    TF_list = TF_Question.objects.filter(sub_category__in=language_subset.values('id'))
    # Essay_list = Essay_Question.objects.filter(sub_category__in=language_subset.values('id'))
            
    questions_list = list(chain(MC_list.values('id'), TF_list.values('id')))

    for item in questions_list: 
        question = Question.objects.get(id=item['id'])
        question.quiz.add(new_quiz)         
    return new_quiz


# select evaluators
def select_evaluators(x, y):
    evalutor1 = x
    evaluator2 = y
    return (evalutor1, evaluator2)
