# Generated by Django 3.1.1 on 2022-01-18 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=13)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('picture', models.ImageField(default='company/avatar.jpg', upload_to='profile/')),
                ('guardian_email', models.EmailField(help_text='To Hold You Accountable', max_length=254)),
                ('guardian_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('receive_mails', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.examination')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.profile')),
                ('subjects', models.ManyToManyField(to='questions.Subject')),
            ],
        ),
    ]