from django.conf import settings
from django.db import models
from uuid import uuid4

from questions.models import Examination, Subject

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    profile_ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(
        max_length=250)
    phone_number = models.CharField(max_length=13)
    email_address = models.EmailField(blank=True, null=True)
    picture = models.ImageField(default='company/avatar.jpg', upload_to='profile/')
    guardian_email = models.EmailField(help_text="To Hold You Accountable")
    guardian_phone = models.CharField(
        max_length=13, blank=True, null=True)
    receive_mails = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id}'



class Subscription(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)
    examination = models.ForeignKey(
        Examination, on_delete=models.PROTECT)
    subjects = models.ManyToManyField(Subject)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile.user_id}'

    def is_active(self):
        return False



# class SubscriptionPayment(models.Model):
#     subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
#     customer_id = models.CharField(max_length=150)
#     payment_id = models.CharField(max_length=150)
#     payment_status = models.CharField(max_length=50)
#     start_period = models.DateField(blank=True, null=True) #check_period
#     end_period = models.DateField(blank=True, null=True)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     invoice_url = models.URLField(blank=True, null=True)
#     is_active = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.subscription.profile.user_id}'

#     def is_active(self):
#         return False



# def set_subscription_state_receiver(sender, instance, *args, **kwargs):
#     # if instance.end_period == None:
#     #     if instance.subscription_type == 'monthly':
#     #         instance.end_period = timezone.now() + relativedelta(months=1)
#     if instance.payment_status == 'paid':
#         # and instance.end_period > timezone.now():
#         instance.is_active = True


# pre_save.connect(set_subscription_state_receiver, sender=Subscription)

# def set_end_date_receiver(sender, instance, *args, **kwargs):
#     if instance.end_period == None:
#         if instance.subscription_type == 'monthly':
#             instance.end_period = instance.date + relativedelta(months=1)

# post_save.connect(set_end_date_receiver, sender=Subscription)


# class Team(models.Model):
#     name = models.CharField(max_length=50)
#     creator = models.ForeignKey(Profile)
#     created_at = models.DateTimeField(auto_now_add=True)
#     members = models.ManyToManyField(Profile)
#     scores = models.PositiveIntegerField(default=0)

#     def ranking(self):
#         ordered_team = Team.objects.all().order_by('scores')
#         return ordered_team.index(self) + 1