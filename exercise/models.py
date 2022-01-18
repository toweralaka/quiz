# from django.conf import settings
# from django.core import serializers
from django.db import models, transaction
# from django.db.models.signals import post_save, pre_save
# from django.http import JsonResponse
# # from django.utils.text import slugify
# from django.utils import timezone
# from datetime import date, datetime, timedelta

from questions.models import Subject, Topic, Question, get_duration
from userdata.models import Subscription, Profile

# Create your models here.


def createscript(ques, script, instance):
    bulk_script = []
    for question in ques:
        new_script = script()
        new_script.question = question
        new_script.module = instance
        new_script.user = instance.user
        bulk_script.append(new_script)
    script.objects.bulk_create(bulk_script)


def updatescript_exercise(model, scripts, instance):
    bulk_script = []
    for script in scripts:
        script.exercise = instance
        bulk_script.append(script)
    model.objects.bulk_update(bulk_script, ['exercise'])




class UserExercise(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE)
    subscription = models.ForeignKey(
        Subscription, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    time_started = models.DateTimeField(blank=True, null=True)
    time_ended = models.DateTimeField(blank=True, null=True)
    score = models.PositiveIntegerField(default=0)
    is_marked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.module.user}"

    def has_started(self):
        return (time_started != Null)

    def has_ended(self):
        return (time_ended != Null)

#     def seconds_used(self):
#         if self.ended:
#             start = self.time_started.timestamp()
#             end = self.time_ended.timestamp()
#             duration = end - start
#             return duration
#         else:
#             return 0

#     def time_used(self):
#         if self.ended:
#             return get_duration(self.seconds_used())
#         else:
#             return 'NA'

#     def get_exercise_set(self):
#         return ExerciseScript.objects.filter(
#             exercise=self, module=self.module)
#     # def get_percentage_score(self):
#     #     exercises = ExerciseScript.objects.filter(exercise=self)
#     #     is_right = 0
#     #     for i in exercises:
#     #         if i.is_correct():
#     #             is_right += 1
#     #     return (is_right/exercises.count()) * 100

#     def scores(self):
#         exercises = ExerciseScript.objects.filter(exercise=self)
#         is_right = 0
#         for i in exercises:
#             if i.is_correct():
#                 is_right += 1
#         return (is_right, exercises)

#     def percentage_score(self):
#         if self.ended:
#             exercises = ExerciseScript.objects.filter(exercise=self)
#             is_right = 0
#             for i in exercises:
#                 if i.is_correct:
#                     is_right += 1
#             return (is_right / exercises.count()) * 100
#         else:
#             return 0

#     def exercise_time(self):
#         time_each = self.module.subject.exam.time_per_question
#         return self.module.question_size() * time_each

#     def time_up(self):
#         time_spent = self.time_ended - self.time_started
#         if time_spent >= self.exercise_time():
#             return True
#         else:
#             return False

#     # next module to be unlocked
#     # def next_module(self):
#     #     topic_id = self.module.topic.id
#     #     all_ids = [i.id for i in Topic.objects.filter(active=True).order_by('priority')]
#     #     next_topic_index = (all_ids.index(topic_id)) + 1
#     #     the_id = all_ids[next_topic_index]
#     #     the_module = ExerciseModule.objects.get(topic__id = the_id)
#     #     return the_module


# def get_score_receiver(sender, instance, *args, **kwargs):
#     if instance.ended:
#         if not instance.marked:
#             exercises = ExerciseScript.objects.filter(
#                 exercise=instance)
#             is_right = 0
#             for i in exercises:
#                 if i.is_correct:
#                     is_right += 1
#             d_score = (is_right / exercises.count()) * 100
#             if int(d_score) == int(instance.percentage_score()):
#                 instance.score = d_score
#                 instance.marked = True


# pre_save.connect(get_score_receiver, sender=UserExercise)


# def unlock_module_receiver(
#         sender, instance, created, *args, **kwargs):
#     if created:
#         scripts = instance.module.script_set()
#         updatescript_exercise(ExerciseScript, scripts, instance)
#     if instance.marked:
#         if instance.module.can_unlock_module():
#             module = instance.module.next_module()
#             module.locked = False
#             module.save()


# post_save.connect(unlock_module_receiver, sender=UserExercise)


# on subscription, script is created for all topic/subject/user
class ExerciseScript(models.Model):
    exercise = models.ForeignKey(
        UserExercise,
        on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT)
    selected_option = models.CharField(max_length=1, default='')

    # @property
    # def is_correct(self):
    #     if str(self.question.answer_option).lower() == str(
    #             self.selected_option).lower():
    #         return True
    #     else:
    #         return False

    # def the_choice(self):
    #     if self.choice.lower() == 'a':
    #         return self.question.option_a
    #     elif self.choice.lower() == 'b':
    #         return self.question.option_b
    #     elif self.choice.lower() == 'c':
    #         return self.question.option_c
    #     elif self.choice.lower() == 'd':
    #         return self.question.option_d
    #     elif self.choice.lower() == 'e':
    #         return self.question.option_e

    # def the_answer(self):
    #     if self.question.answer_option.lower() == 'a':
    #         return self.question.option_a
    #     elif self.question.answer_option.lower() == 'b':
    #         return self.question.option_b
    #     elif self.question.answer_option.lower() == 'c':
    #         return self.question.option_c
    #     elif self.question.answer_option.lower() == 'd':
    #         return self.question.option_d
    #     elif self.question.answer_option.lower() == 'e':
    #         return self.question.option_e


