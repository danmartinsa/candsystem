from  quiz.models import Question, Category, SubCategory
from multichoice.models import MCQuestion, Answer
from essay.models import Essay_Question 

n_question = 30

languages=["Python", "SAS", "SQL", "VBA"]

for lang in languages:
    lang_category = Category.objects.get(category=lang)
    lang_subcat   = SubCategory.objects.filter(category=lang_category.id)
    for i in range(1, n_question):

        if i  % 3 == 0:
            subcat = 2
        elif i % 2 == 0:
            subcat = 1
        else:
            subcat = 0
        newquestion = MCQuestion(answer_order="content", category=lang_category, sub_category=lang_subcat[subcat], content="%s %s  Objective - Q %s" % (lang, lang_subcat[subcat].sub_category, str(i)), weight=1)
        newquestion.save()

        newquestion_answer1 = Answer(question=newquestion, content="Answer1", correct=True)
        newquestion_answer1.save()
        newquestion_answer2 = Answer(question=newquestion, content="Answer2", correct=False)
        newquestion_answer2.save()
        newquestion_answer3 = Answer(question=newquestion, content="Answer3", correct=False)
        newquestion_answer3.save()
        newquestion_answer4 = Answer(question=newquestion, content="Answer4", correct=False)
        newquestion_answer4.save()

        newEssayQuestion = Essay_Question(category=lang_category, sub_category=lang_subcat[subcat], content="%s %s  Objective - Q %s")

