# Generated by Django 4.0.5 on 2022-06-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsonzambia', '0003_post_views_alter_postfeature_ft_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfeature',
            name='ft_likes',
            field=models.ManyToManyField(blank=True, related_name='feature_likes', to='whatsonzambia.ipmodel'),
        ),
    ]
