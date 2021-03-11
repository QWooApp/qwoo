# Generated by Django 3.1.7 on 2021-03-10 13:18

import cloudinary.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        error_messages={
                            'unique': 'A user with that username already exists.'
                        },
                        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name='username',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True, max_length=150, verbose_name='first name'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True, max_length=150, verbose_name='last name'
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        blank=True, max_length=254, verbose_name='email address'
                    ),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True,
                        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                        verbose_name='active',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name='date joined'
                    ),
                ),
                ('bio', models.CharField(default='', max_length=250)),
                ('secret_key', models.CharField(blank=True, max_length=32)),
                (
                    'avatar',
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True
                    ),
                ),
                (
                    'phone_number',
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'ordering': ('-date_joined',),
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(
                fields=['is_active'], name='user_user_is_acti_829fed_idx'
            ),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(
                fields=['is_active', 'username'], name='user_user_is_acti_3b6bbb_idx'
            ),
        ),
    ]
