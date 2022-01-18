from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.utils.html import format_html, mark_safe
# from django.utils.safestring import mark_safe
from django.utils.text import slugify


import datetime
# from datetime import timedelta
from decimal import Decimal


# Create your models here.
# import sched
# import schedule
# import time as time_module

# def myfunc(): 
#     print("Working" * 12)

# def myfunc2(): 
#     print("Working Easy " * 12)

# def myfunc3(): 
#     print("Working Easy B" * 12)
    
# # scheduler = sched.scheduler(time_module.time, time_module.sleep)
# # t = time_module.strptime('2021-04-25 09:59:00', '%Y-%m-%d %H:%M:%S')
# # t = time_module.mktime(t)
# # scheduler_e = scheduler.enterabs(t, 1, myfunc, ())
# # scheduler.run()

# job = schedule.every().day.at("09:59").do(myfunc2)
# # job = schedule.every().day.at('22:30').do(some_task)
# schedule.cancel_job(job)

# # while 1:
# #     schedule.run_pending()
# #     time_module.sleep(1)

def get_duration(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if h == 0 and d == 0 and m == 0:
        return f"{s} Secs"
    else:
        return f"{int(d)}d {int(h)}h {int(m)}m {int(s)}s"


class Examination(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    acronym = models.CharField(max_length=50)
    # year = models.CharField(max_length=4)#remove
    # start_date = models.DateField()#remove
    # end_date = models.DateField()#remove
    subjects_number = models.PositiveIntegerField()
    # exercises = models.PositiveIntegerField(default=5,
    #                 help_text="Number Of Exercises In The Period")
    # pass_mark = models.DecimalField(
    #                 max_digits=2, decimal_places=2, help_text="Between 0.1 and 1.0")
    # time_per_question = models.PositiveIntegerField(
    #                         default=0, 
    #                         help_text="In seconds. Use '0' if the exercise is not timed")
    # questions_cap = models.PositiveIntegerField(default=20)
    # benchmark_score = models.PositiveIntegerField(
    #                     default=20, help_text="Percentage")
    active = models.BooleanField(default=True)
    # unlock_modules = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Examination, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # class Meta:
    #     unique_together = [['name', 'year'], ]


class Subject(models.Model):
    exam = models.ForeignKey(Examination, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    is_compulsory = models.BooleanField()

    class Meta:
        unique_together = [['exam', 'slug'], ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.exam.name} {self.name}"

    # def user_modules(self, request):
    #     # return self.exercisemodule_set.filter(user=user)
    #     return self.exercisemodule_set.filter(user=request.user)

    # def time_spent(self, user):
    #     secs = 0
    #     for i in self.exercisemodule_set.filter(user=user):
    #         for j in i.userexercise_set.all():
    #             secs += j.seconds_used()
    #     return get_duration(secs)
    #     # for i in UserExercise.filter(module__subject=self.subject):
    #     #     secs += i.seconds_used()
    #     # return get_duration(secs)
    #     # return 3

    # def last_seen(self, user):
    #     mylist = []
    #     for i in self.exercisemodule_set.filter(user=user):
    #         for j in i.userexercise_set.all():
    #             if j.ended:
    #                 mylist.append(j.time_ended)
    #     # last = UserExercise.filter(
    #     #     module__subject=self.subject).order_by('time_ended')[0]
    #     if len(mylist) > 0:
    #         return max(mylist).date()
    #     else:
    #         return 'Never'
    #     # return timezone.now().date()

    # def progress(self, user):
    #     total = 0
    #     count = 0
    #     for module in self.exercisemodule_set.filter(user=user):
    #         total = total + module.percentage_attempted()
    #         count += 1
    #     if count > 0:
    #         return int(total / count)
    #     else:
    #         return 0

    # def performance(self):
    #     pass

    # def average_general_score(self, user):
    #     total = 0
    #     exercises = self.generalexercise_set.filter(
    #         user=user, ended=True)
    #     for exercise in exercises:
    #         total = total + exercise.score
    #     if len(exercises) > 0:
    #         return total / len(exercises)
    #     else:
    #         return 0

    



# def set_subj_slug_receiver(sender, instance, *args, **kwargs):
#     instance.name_slug = slugify(instance.name)


# pre_save.connect(set_subj_slug_receiver, sender=Subject)


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    priority = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    # class Meta:
    #     unique_together = [
    #         ['subject', 'priority'], ['subject', 'name']]
    #     ordering = ["subject", "priority"]
    #     # verbose_name_plural = "oxen"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # def question_count(self):
    #     return Question.objects.filter(topic=self).count()


# def set_topic_slug_receiver(sender, instance, *args, **kwargs):
#     instance.name_slug = slugify(instance.name)


# pre_save.connect(set_topic_slug_receiver, sender=Topic)


# class SubTopic(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     name_slug = models.CharField(max_length=250)

#     def __str__(self):
#         return self.name


# def set_sbtopic_slug_receiver(sender, instance, *args, **kwargs):
#     instance.name_slug = slugify(instance.name)


# pre_save.connect(set_sbtopic_slug_receiver, sender=SubTopic)

def get_question_code(subject_pk):
    the_subject = Subject.objects.get(pk=subject_pk)
    subject = the_subject.slug[:3]
    exam = the_subject.examination.slug[:3]
    ordered_questions = Question.objects.filter(
        subject=the_subject).order_by('question_code')
    if ordered_questions.count() <= 0:
        number = 0
    else:
        last_number = ordered_questions.last.question_code[8:]
        number = int(last_number) + 1
    return f"{exam}-{subject}-{number}"

class Question(models.Model):
    question_code = models.CharField(max_length=20, unique=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT)
    topic = models.ForeignKey(
        Topic, on_delete=models.PROTECT)
    # sub_topic = models.ForeignKey(
    #     SubTopic, on_delete=models.SET_NULL, blank=True, null=True)
    year = models.CharField(max_length=4)
    question_text = RichTextUploadingField()
    option_a = RichTextUploadingField()
    option_b = RichTextUploadingField()
    option_c = RichTextUploadingField(blank=True, null=True)
    option_d = RichTextUploadingField(blank=True, null=True)
    option_e = RichTextUploadingField(blank=True, null=True)
    answer_option = models.CharField(max_length=1)
    explanation = RichTextUploadingField(blank=True, null=True)

    # class Meta:
    #     unique_together = [['question_number', 'subject'], ]

    def save(self, *args, **kwargs):
        self.question_code = get_question_code(self.subject.pk)
        super(Subject, self).save(*args, **kwargs)

    # @property
    # def question(self):
    #     return format_html(self.question_text)

    # @property
    # def optionA(self):
    #     return mark_safe(self.option_a)

    # @property
    # def optionB(self):
    #     return mark_safe(self.option_b)

    # @property
    # def optionC(self):
    #     return mark_safe(self.option_c)

    # @property
    # def optionD(self):
    #     return mark_safe(self.option_d)

    # @property
    # def optionE(self):
    #     return mark_safe(self.option_e)

    def __str__(self):
        return "Question %s" % (self.question_code)


# class QuestionBank(models.Model):
#     file_name = models.CharField(max_length=60, unique=True)
#     question_file = models.FileField()

#     def __str__(self):
#         return self.file_name
