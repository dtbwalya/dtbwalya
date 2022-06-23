# Generated by Django 3.2.13 on 2022-06-14 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('fullname', models.CharField(max_length=100)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ft_title', models.CharField(max_length=100, verbose_name='Event Name')),
                ('ft_content', models.TextField(max_length=250, verbose_name='More Information')),
                ('ft_date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ft_charge', models.CharField(max_length=100, verbose_name='Charges')),
                ('ft_venue', models.CharField(max_length=100, verbose_name='Venue')),
                ('ft_event_day', models.CharField(max_length=100, verbose_name='Event Day')),
                ('ft_event_date', models.CharField(max_length=50, verbose_name='Event Date')),
                ('ft_town', models.CharField(max_length=100, verbose_name='Town/City')),
                ('ft_event_time', models.TimeField(verbose_name='Event Time')),
                ('ft_post_image', models.ImageField(blank=True, null=True, upload_to='feat_img', verbose_name='Upload Advert Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Event Name')),
                ('content', models.TextField(max_length=250, verbose_name='More Information')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('charge', models.CharField(max_length=100, verbose_name='Charges')),
                ('venue', models.CharField(max_length=100, verbose_name='Event Venue')),
                ('event_day', models.CharField(max_length=100, verbose_name='Event Day')),
                ('event_date', models.CharField(max_length=50, verbose_name='Event Date')),
                ('town', models.CharField(max_length=100, verbose_name='Town/City')),
                ('event_time', models.TimeField(verbose_name='Event Time')),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='post_img', verbose_name='Uploadadvert Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
