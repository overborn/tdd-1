# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
