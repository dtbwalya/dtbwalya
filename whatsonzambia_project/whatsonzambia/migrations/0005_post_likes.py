# Generated by Django 4.0.5 on 2022-06-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsonzambia', '0004_postfeature_ft_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to='whatsonzambia.ipmodel'),
        ),
    ]
