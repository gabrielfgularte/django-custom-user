# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(help_text='Required. 15 characters or fewer. Letters,                     numbers and @/./+/-/_ characters', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active.                     Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('is_trusty', models.BooleanField(verbose_name='trusty', default=False, help_text='Designates whether this user has confirmed his account.')),
                ('groups', models.ManyToManyField(to='auth.Group', blank=True, verbose_name='groups', related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', blank=True, verbose_name='user permissions', related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
        ),
    ]
