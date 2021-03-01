from django.db.models.fields import CharField
from quiz.models import Category, Quiz, Question, Sitting, SubCategory
from essay.models import Essay_Question
from multichoice.models import MCQuestion
from true_false.models import TF_Question
from website.models import User, AssignTest, Role, Rules
from itertools import chain
import random

from datetime import datetime
import string


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
        sitting = Sitting.objects.new_sitting(user=user, quiz=new_quiz, time=200)
        set_quiz = AssignTest.objects.create(candidate=user, quiz=new_quiz, requestor=interviewer, role=position, sitting=sitting)
        set_quiz.save()

        return new_quiz

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

def select_questions(plang, position):
    '''
    Function to create quiz selecting appropriate questions

    '''
    category = Category.objects.get(id=plang.id)  # selection for language
    
    new_quiz = Quiz.objects.create()
    new_quiz.title = str(datetime.now()) + position.name  +category.category
    new_quiz.category = category

    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(16))

    new_quiz.url = str(str(to_integer(datetime.now())) +  result_str)
    new_quiz.save()

    ruleset = Rules.objects.get(role=position)
    language_subset = SubCategory.objects.filter(category_id = category.id)

    basic_q = []
    interm_q = []
    adv_q =[]
    for item in language_subset:
        level = item.sub_category
        print(level)
        if level == "Basic" and ruleset.n_basic > 0:
            basic_q = random.sample([i for i in MCQuestion.objects.filter(sub_category=item.id)], k= ruleset.n_basic)
            print(len(basic_q), basic_q)
        elif level == "Intermediate" and ruleset.n_intermediate > 0:
            interm_q = random.sample([i for i in MCQuestion.objects.filter(sub_category=item.id)], k= ruleset.n_intermediate)
            print(len(interm_q), interm_q)
        elif level == "Advanced" and ruleset.n_advanced > 0:
            adv_q = random.sample([i for i in MCQuestion.objects.filter(sub_category=item.id)], k= ruleset.n_advanced)
            print(len(adv_q), adv_q)
  


    questions_list = list(chain(basic_q, interm_q, adv_q))
    print(len(questions_list))

    for item in questions_list: 
        question = Question.objects.get(id=item.id)
        question.quiz.add(new_quiz)         
    return new_quiz


# select evaluators
def select_evaluators(Sitting):
    """
        For a Sitting (relational between Quiz and Candidate)
        Select 2 evaluators
    """
    evaluators  = random.sample([i for i in User.objects.filter(is_evaluator=True)], k = 2)
    
    return (evaluators[0], evaluators[1])

def evaluate(User, Sitting):
    return 0 #Subjective Score for a 


def calculateScore(scoreEval1, scoreEval2):
    """
        scoreEval1 = score 1st evaluator
        scoreEval2 = score 2nd evaluator
        Return average bettween final score
    """
   
    return -0 #SubjectiveScore

def subjectiveEval(Sitting):
    return 0 #email Message to requestor with final score 



